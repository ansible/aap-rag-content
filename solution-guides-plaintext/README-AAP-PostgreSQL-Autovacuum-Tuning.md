## Overview

<div class="guide-outcome">
Three <code>postgresql.conf</code> changes, applied in order, keep high-churn AAP tables continuously clean.
</div>

AAP at enterprise scale writes incessantly to large tables in its PostgreSQL database, continuously keeping track of job execution records, authorization tokens, and host health checks. PostgreSQL's default autovacuum settings were designed for smaller, less write-intensive databases and do not keep pace with this workload.

Every UPDATE and DELETE in PostgreSQL leaves behind a "dead tuple" - the old row - rather than modifying the row in place. On large, frequently-written tables these accumulate quickly: at production AAP scale, a single high-churn table can generate approximately 27,000 dead tuples per hour. With default autovacuum settings, these dead tuples have been observed waiting around for more than 6 hours before autovacuum clears them. While they wait, queries must still scan over them even though the dead tuples are invisible to the queries, degrading performance and, at scale, producing user-visible slowdowns.



<p class="guide-image-caption">Decision diagram: use this to pick your starting rung, then follow the <a href="#tuning-path">tuning path</a> below.</p>

> **Tip:** Parameter glossary
>
> See [Key Terms](#key-terms) at the end for definitions of metrics, settings, and failure modes used throughout this guide.

## Background

This guide was developed and validated in summer 2026 on a Red Hat Scale Lab cluster running AAP 2.6 (Controller 4.7.15) on OpenShift 4.21.19 with a two-node CloudNativePG PostgreSQL 15.10 database. Sized to represent a large enterprise deployment, the environment included approximately 37,000 managed hosts, 40,000 job templates, and a sustained workload of more than 3,000 jobs per hour (~75,000 per day). Database memory configuration matched a tuned production cluster with `shared_buffers=16 GB` and `effective_cache_size=48 GB`.

To simulate what a customer environment looks like without autovacuum tuning, the two highest-churn tables (`main_unifiedjob` and `main_job`) had autovacuum deliberately disabled for four days before measurement began, driving `main_unifiedjob` to 39% dead tuples at the start of the baseline rung. Each of the three tuning rungs ran for approximately 10 hours with bloat state carried forward. Since there were no table resets between rungs, each set of parameters had to recover from real accumulated bloat rather than a freshly vacuumed starting point. Measurements were taken at T=0, 2 hr, 5 hr, 8 hr, and 10 hr within each rung.

## Prerequisites
- Superuser access to the AAP PostgreSQL instance
- Ability to edit `postgresql.conf` and run `SELECT pg_reload_conf()`
- Operational impact: **Low** as all changes are reversible; `scale_factor` and `naptime`
  take effect on reload with no restart required

> **OpenShift / CNPG deployments:**
>
> Instead of editing `postgresql.conf` directly, add global parameters to the `Cluster` YAML under
> `.spec.postgresql.parameters`, then apply with `oc apply`. CNPG reloads PostgreSQL automatically so `pg_reload_conf()` is
> not needed. Per-table `ALTER TABLE` commands (Rung 3) are still run directly via `psql`, unchanged from the steps below.

---

## Baseline at scale

In a large AAP deployment, the database receives a continuous stream of writes: every executed job creates and updates records in `main_unifiedjob`; every API call touches the OAuth2 token table; every automation run updates host metrics. Tables grow to hundreds of thousands of rows and are updated thousands of times per hour. In this environment, PostgreSQL's default setting `scale_factor=0.2` falls short.

The chart in Rung 1 (left panel) shows `main_unifiedjob` under default settings:

- Dead rows stood at 39.3% at the start—reflecting accumulated bloat from high write volume prior to tuning.
- Despite the bloat, autovacuum fired **only 2 times** in 10 hours. While vacuuming cleared the table each time,
  it could not keep up with the accumulation rate.
- `dead_pct` climbed back to 10.3% by the end of the rung and was continuing to rise.

The root cause: `scale_factor=0.2` means that, at this scale, autovacuum waits for 160,000 dead
tuples on an 800K-row table before acting. At approximately 27,000 dead tuples/hour, that
threshold is crossed every ~6 hours. *The table never stays clean.*

**Ready to tune?** See the [tuning path](#tuning-path) below, then [Rung 1](#rung-1-lower-the-trigger).

---

## Tuning path

| | Apply | When |
|---|---|---|
| **Start here** | [Rung 1](#rung-1-lower-the-trigger) — `scale_factor`, `max_workers` | Every large AAP deployment. |
| **Add next** | [Rung 2](#rung-2-increase-check-frequency) — `naptime` | When the `hot_ratio` query confirms that HOT is disabled on high-churn tables. |
| **Add if needed** | [Rung 3](#rung-3-ensure-each-pass-completes) — per-table `cost_limit` | Only after the Rung 3 diagnostic tests confirm incomplete vacuuming. |

---

## Rung 1: Lower the trigger



**Apply this if:** Your large, frequently-updated tables show autovacuum firing only a few
times per day, or `dead_pct` stays above 10% for hours. If you're running AAP with
thousands of jobs per day, assume you need this.

> **Tip:** Enterprise scale factor impact
>
> In an enterprise AAP environment managing ~70,000 hosts and running ~40,000 jobs per day,
> decreasing `scale_factor` from its default setting of 0.2 to 0.02 reduced total database execution time by 96.7%.

**The change** using `postgresql.conf`:

<p class="code-lead">Apply in postgresql.conf:</p>

```
autovacuum_vacuum_scale_factor = 0.02
autovacuum_max_workers = 6
```

<p class="code-lead">Run this:</p>

```sql
SELECT pg_reload_conf();
```

**Why 0.02:** For AAP's write-intensive tables (`main_unifiedjob`, `main_job`, and `gateway.dab_oauth2`), the validated target is a 2% ceiling on dead tuples, which translates to `scale_factor = 0.02`. Dead tuples impose wasted I/O proportional to their share of tables. For example, a sequential scan at 20% `dead_pct` (PostgreSQL's default trigger) traverses 20% more pages than needed.

`scale_factor` ≈ `dead_pct` ÷ 100 for large tables so `scale_factor = 0.02` keeps the ceiling at 2%. In this study, `dead_pct` stayed below 0.8%: autovacuum fired and cleared the tables before the ceiling was ever reached.

For non-standard deployments with tables outside of this set, identify which ones are most likely impacted: in `pg_stat_user_tables`, look for tables where both `n_dead_tup` and `seq_scan` are elevated. A global `scale_factor` change applies to all tables automatically so you can monitor these tables during validation to confirm the improvement is landing. For small tables where absolute dead tuple counts stay low regardless of percentage, the `vacuum_threshold` setting in Rung 2 is the better lever.

With `scale_factor = 0.02` applied, estimate the expected fire rate:

<p class="code-lead code-lead--reference">Reference formula:</p>

```
estimated fires/hr ≈ dead_tuple_rate_per_hr ÷ (scale_factor × n_live_rows)
```

A high autovacuum fire rate (roughly more than 100 fires per hour on a single table) is not itself a problem as
autovacuum is designed to run frequently. But it signals that each vacuum pass may have a hard time
finishing and, therefore, keeping pace. If this scenario is a concern, run the Rung 3 diagnostic to
confirm passes are completing. Raising `scale_factor` back up would lower the fire rate but allow more
dead tuples to accumulate between passes, which would be the incorrect fix.

**How to compute `max_workers`:** In a large AAP deployment, the four highest-churn tables
are `main_unifiedjob`, `main_jobhostmetric`, `main_hostmetric`, and `gateway.dab_oauth2`.
Count the tables in this group that apply to your deployment and add 2 for background
maintenance headroom. For a full AAP stack, `max_workers=6` covers all four plus headroom.
Setting it higher than needed is not harmful; autovacuum only spawns workers when tables
require it.

**Result:** Autovacuum ran 22 times vs. 2 during the prior rung; `dead_pct` on `main_unifiedjob` never exceeded 0.8% for the remainder of the study.

---

## Rung 2: Increase check frequency



**Apply this if:** You have a table where a frequently-updated column is also indexed. If
this is the case, HOT (Heap Only Tuple) optimization is disabled on that table. HOT allows
PostgreSQL to handle an UPDATE entirely within the same page without creating a dead tuple. However, when a column is indexed and, therefore, HOT is disabled, PostgreSQL must
update the index, too, so every UPDATE produces a dead tuple that autovacuum must clean.
The following query returns the percentage of updates handled by HOT, `hot_ratio`, for
each table, ordered by update volume:

<p class="code-lead">Run this diagnostic:</p>

```sql
SELECT relname,
       n_tup_upd,
       n_tup_hot_upd,
       round(100.0 * n_tup_hot_upd / nullif(n_tup_upd, 0), 1) AS hot_ratio
FROM pg_stat_user_tables
WHERE n_tup_upd > 0
ORDER BY n_tup_upd DESC;
```

Any table showing `hot_ratio` well below 100% has HOT disabled and is generating a dead tuple on every UPDATE.

**Default settings and why they fall short:** With the default naptime at 60 seconds, autovacuum wakes up to inspect each table once per minute. The default absolute minimum dead-tuple count required before autovacuum considers vacuuming is 50, regardless of `scale_factor.`

At 60-second intervals, a HOT-disabled table receiving 82 dead tuples per second accumulates nearly 5,000 dead tuples between inspections.
Even when the trigger threshold is crossed within seconds of a cleanup, autovacuum doesn't notice for up to another 60 seconds. On small
tables, the `vacuum_threshold` of 50 compounds this: when `scale_factor` × `n_live_rows` is small, the absolute threshold dominates and can
block autovacuum entirely.

> **Tip:** Why naptime matters for OAuth2 tables
>
> OAuth2 and session tables receive an update on every API request. At 82 dead tuples per second, a 60-second check interval allows nearly 5,000 dead tuples to accumulate between inspections. naptime=10s reduces the backlog to about 820 dead tuples and produces a 6× increase in vacuuming.


**The change** with `postgresql.conf`:

<p class="code-lead">Apply in postgresql.conf:</p>

```
autovacuum_naptime = 10s           # default: 60s
autovacuum_vacuum_threshold = 20   # default: 50
```

<p class="code-lead">Run this:</p>

```sql
SELECT pg_reload_conf();
```

Lowering `vacuum_threshold` from 50 to 20 dead tuples ensures small, high-churn tables are not ignored. A table with only a few thousand rows may never accumulate 50 dead tuples between checks, but at high update rates, 20 is crossed almost immediately.

<p class="code-lead code-lead--reference">Reference formula:</p>

```
naptime ≈ (vacuum_threshold + scale_factor × n_live_rows ) ÷ (dead_tuple_rate_per_second)
```
For `gateway.dab_oauth2` in this study: (20 + 0.02 × ~50,000) ÷ 82 ≈ 13s — rounded to 10s for a tighter response window. For most HOT-disabled tables in an active AAP deployment, 10–15s is appropriate.

**Result:** On `gateway.dab_oauth2`, vacuuming fires averaged 530 per 10-hour rung before
naptime changed (461 fires in rung 0; 600 in rung 1) and 3,571 after (3,574 in rung 2;
3,568 in rung 3); a 6× increase. At naptime=10s, the table is re-inspected every 10
seconds instead of every 60s, allowing autovacuum to respond before the dead-tuple backlog
grows to problematic levels.

If HOT is already disabled in your environment, naptime=10s is the sole driver of this
improvement. In this study, an index on `last_used` was added at the same time naptime
changed, which disabled HOT updates on `gateway.dab_oauth2` simultaneously and amplified
the effect. If that index already existed in your environment, the full 6× gain would be from
naptime alone.

---

## Rung 3: Ensure each pass completes



**Apply this if:** Autovacuum runs frequently on a specific table but dead tuples persist anyway. The sign to look for: `autovacuum_count` is increasing fast AND `n_dead_tup` stays elevated at the same time. To find affected tables:

<p class="code-lead">Run this diagnostic:</p>

```sql
SELECT relname,
       n_dead_tup,
       n_live_tup,
       round(100.0 * n_dead_tup / nullif(n_dead_tup + n_live_tup, 0), 1) AS dead_pct,
       autovacuum_count
FROM pg_stat_user_tables
WHERE n_dead_tup > 100
  AND autovacuum_count > 500
ORDER BY autovacuum_count DESC;
```

Confirm the bottleneck by catching a live pass in progress:

<p class="code-lead">Run this diagnostic:</p>

```sql
SELECT p.relid::regclass                                          AS table,
       p.heap_blks_total                                          AS total_pages,
       p.heap_blks_vacuumed                                       AS pages_cleaned,
       round(100.0 * p.heap_blks_vacuumed
             / nullif(p.heap_blks_total, 0), 1)                   AS pct_done
FROM pg_stat_progress_vacuum p
WHERE p.phase != 'initializing';
```

If `pct_done` is consistently below 100% when passes end, the I/O throttle is cutting each
pass short before the table is fully cleaned.

> **Tip:** High fire rate with persistent dead tuples
>
> Autovacuum running 300+ times per hour while dead tuples persist is not a trigger problem. Rather, each pass is being cut short before the table is fully vacuumed. This diagnostic confirms whether the I/O throttle is actually the bottleneck before you apply the change.

**Estimate a starting `cost_limit`:** Run this diagnostic step when `n_dead_tup` is elevated on the target table. Dead tuples drop to near zero right after a pass fires so wait a few minutes after the `last_autovacuum` timestamp to catch a representative reading:

<p class="code-lead code-lead--reference">Adapt table name:</p>

```sql
SELECT relname,
       ceil(pg_relation_size(schemaname||'.'||relname) / 8192.0)      AS pages,
       ceil(pg_relation_size(schemaname||'.'||relname) / 8192.0) * 21 AS cost_limit_cached,
       ceil(pg_relation_size(schemaname||'.'||relname) / 8192.0) * 30 AS cost_limit_uncached
FROM pg_stat_user_tables
WHERE relname = 'your_table_name';
```

`cost_limit_cached` (pages × 21) and `cost_limit_uncached` (pages × 30) estimate the budget needed to process every heap page once without interruption — 21 and 30 being the cost per page when the table is in memory vs. read from disk. For `main_hostmetric` at peak, the query returned 47 pages; therefore, `cost_limit_cached` = 47 pages × 21 = 987, rounded to **1,000.**

Small tables (a few thousand rows or fewer) are almost always in memory so use `cost_limit_cached` as your starting value. For larger tables that may not be reliably cached, use `cost_limit_uncached`. For both cases, round up to a clean number. The cost limits estimate the I/O budget needed to scan all heap pages in a single pass.

The formula covers heap pages only; index cleanup and the visibility map mean real behavior may differ, which is why the empirical check follows.

**Apply per-table:** This does not touch global settings.

<p class="code-lead code-lead--reference">Adapt schema and table name:</p>

```sql
ALTER TABLE schema.tablename
  SET (autovacuum_vacuum_cost_limit = <computed_value>);
```


**Three possible outcomes — all informative:**

| Outcome | Signal | Interpretation |
|---------|---------------------------------------|-----------------|
| **Positive** | Same fire rate; dead_pct → 0 | cost_limit was the bottleneck; keep the setting |
| **Flat** | Fire rate and dead_pct unchanged | cost_limit is not the issue; look elsewhere |
| **Warning** | CPU spike without improvement | cost_limit too aggressive for available I/O headroom; dial back |

This is a per-table override. It does not change the global `cost_limit` so the effect is isolated to the single table you're targeting.

In this study, the query returned 47 pages for `main_hostmetric`, giving `cost_limit` = 47 × 21 = 987, rounded to 1,000. Applied with `ALTER TABLE`, the table reached 0.0% dead during Rung 3 at T=8hr, the first complete cleanup of this table in 40 study hours; a **positive** outcome. The other high-churn tables (`main_unifiedjob`, `gateway.dab_oauth2`) did not require a `cost_limit` override as Rungs 1 and 2 were already keeping them clean.


---

## Validation

Allow at least 2 hours of steady-state operation after each rung before evaluating.

**Rung 1** — confirm `scale_factor` is working:

<p class="code-lead">Run this validation query:</p>

```sql
SELECT relname,
       autovacuum_count,
       n_dead_tup,
       round(100.0 * n_dead_tup / nullif(n_dead_tup + n_live_tup, 0), 1) AS dead_pct,
       last_autovacuum
FROM pg_stat_user_tables
WHERE relname IN ('main_unifiedjob', 'main_jobhostmetric')
ORDER BY relname;
```

Expected: `dead_pct` consistently below 2%; `autovacuum_count` incrementing multiple times
per hour. Take two snapshots 30 minutes apart and compare `autovacuum_count`.

A healthy snapshot with Rung 1 applied (from the study environment):

<p class="code-lead code-lead--reference">Expected output:</p>

```
      relname       | autovacuum_count | n_dead_tup | dead_pct |      last_autovacuum
--------------------+------------------+------------+----------+----------------------------
 main_jobhostmetric |              214 |        480 |      0.1 | 2026-08-15 14:22:14+00
 main_unifiedjob    |              381 |          0 |      0.0 | 2026-08-15 14:23:17+00
(2 rows)
```

`dead_pct` near zero; `last_autovacuum` within the past few minutes on both tables.

**Rung 2** — confirm `naptime` is working:

Run the same query against your HOT-disabled tables. Expected: `autovacuum_count`
incrementing far faster than Rung 1 tables. Two snapshots 10 minutes apart should show
a meaningful delta.

If your environment has Prometheus instrumentation, `db_cpu_throttle` should remain flat after applying all three rungs. In the study it stayed in the 0.02–0.05 range throughout. UI job latency (p75) should show no increase; the study measured 754–762ms across all rungs with no degradation.

**Rung 3** — confirm `cost_limit` is working:

Watch `pg_stat_progress_vacuum` during a live pass on the target table. `pct_done` should
reach 100% before the pass ends. If it does not, increase `cost_limit` and re-check.

---

## Troubleshooting

Same rung mapping as the [tuning path](#tuning-path) table. Use this section when you see the symptom in production.

| Symptom | Likely Cause | Fix |
|---|---|---|
| `dead_pct` climbs for hours; autovacuum fires only a few times per day | Trigger-limited: `scale_factor` too high; threshold rarely crossed | Lower `scale_factor` → [Rung 1](#rung-1-lower-the-trigger) |
| `autovacuum_count` rising fast but `n_dead_tup` stays elevated after each fire | Throttle-limited: each pass cut short by `cost_limit` before the table is fully cleaned | Set per-table `cost_limit` → [Rung 3](#rung-3-ensure-each-pass-completes) |
| `autovacuum_count` rising very fast; `dead_pct` spikes sharply between fires | HOT disabled on a high-churn table: every UPDATE creates a dead tuple | Lower `naptime` → [Rung 2](#rung-2-increase-check-frequency) |

---

## Key Terms

Quick reference for metrics, settings, and diagnostic views. Settings show the short name used in this guide, followed by the `postgresql.conf` parameter in parentheses.

<nav class="key-terms-nav" aria-label="Key Terms categories">
  <a href="#key-terms-core">Core concepts</a>
  <a href="#key-terms-metrics">Metrics and views</a>
  <a href="#key-terms-settings">Settings</a>
  <a href="#key-terms-failure-modes">Failure modes</a>
</nav>

<div class="key-terms-group">

<h3 id="key-terms-core">Core concepts</h3>

<dl class="key-terms-glossary">
<dt>autovacuum</dt>
<dd>PostgreSQL background process that removes dead tuples when configurable thresholds are met; it does not run continuously.
<span class="key-terms-detail">Tuned via multiple <code>autovacuum_*</code> settings in <code>postgresql.conf</code>. See <a href="#key-terms-settings">Settings</a> below.</span></dd>

<dt>dead tuple</dt>
<dd>Old row copy left behind after an UPDATE or DELETE; vacuum removes it and reclaims space.
<span class="key-terms-detail">PostgreSQL writes a new row rather than modifying in place. Queries must scan past dead tuples even though they are invisible to them.</span></dd>

<dt>HOT (Heap Only Tuple)</dt>
<dd>In-page update optimization: when the changed column is not indexed, PostgreSQL can update the row without creating a dead tuple visible to autovacuum.
<span class="key-terms-detail">Disabled when the updated column is indexed -- every UPDATE then produces a dead tuple. Diagnose with the <code>hot_ratio</code> query in <a href="#rung-2-increase-check-frequency">Rung 2</a>.</span></dd>
</dl>

</div>

<div class="key-terms-group">

<h3 id="key-terms-metrics">Metrics and views</h3>

<dl class="key-terms-glossary">
<dt>autovacuum_count</dt>
<dd>Running total of completed vacuum passes on a table (column in <code>pg_stat_user_tables</code>); subtract two snapshots to get passes in an interval.
<span class="key-terms-detail">Unlike <code>n_dead_tup</code>, this counter never resets -- a low reading always means vacuum has not run, not that you checked right after a cleanup. Used in <a href="#validation">Validation</a> for all three rungs.</span></dd>

<dt>dead_pct</dt>
<dd>Dead rows as a percentage of total rows (live + dead). At 30%+, queries scan significant dead data on every read.
<span class="key-terms-detail">From <code>pg_stat_user_tables</code>:</span>
<pre class="key-terms-formula"><code>dead_pct = 100.0 * n_dead_tup / (n_live_tup + n_dead_tup)</code></pre>
</dd>

<dt>n_dead_tup</dt>
<dd>Raw dead-tuple count on a table (column in <code>pg_stat_user_tables</code>).
<span class="key-terms-detail">Useful for spotting throttle-limited tables, but can read zero right after a pass fires on high-churn tables. Prefer <code>autovacuum_count</code> delta as the primary signal.</span></dd>

<dt>n_tup_hot_upd / n_tup_upd</dt>
<dd>Update counters in <code>pg_stat_user_tables</code>; <code>hot_ratio = n_tup_hot_upd / n_tup_upd</code>.
<span class="key-terms-detail">A ratio well below 100% on a high-write table means HOT is disabled -- typically because the updated column is indexed. See <a href="#rung-2-increase-check-frequency">Rung 2</a>.</span></dd>

<dt>pg_stat_user_tables</dt>
<dd>Per-table vacuum statistics view: <code>autovacuum_count</code>, <code>n_dead_tup</code>, <code>n_live_tup</code>, <code>n_tup_upd</code>, <code>n_tup_hot_upd</code>, <code>last_autovacuum</code>.
<span class="key-terms-detail">Primary diagnostic source for all three rungs and the <a href="#validation">Validation</a> queries.</span></dd>

<dt>pg_stat_progress_vacuum</dt>
<dd>Real-time view of active vacuum passes; key columns are <code>heap_blks_total</code> and <code>heap_blks_vacuumed</code>.
<span class="key-terms-detail">Confirm <code>pct_done</code> reaches 100% before a pass ends. Used in <a href="#rung-3-ensure-each-pass-completes">Rung 3</a> and <a href="#validation">Validation</a>.</span></dd>
</dl>

</div>

<div class="key-terms-group">

<h3 id="key-terms-settings">Settings (<code>postgresql.conf</code>)</h3>

<dl class="key-terms-glossary">
<dt>scale_factor (<code>autovacuum_vacuum_scale_factor</code>)</dt>
<dd>Fraction of live rows that must be dead before autovacuum fires; default 0.2 (20%).
<span class="key-terms-detail">On an 800K-row table, 0.2 waits for 160,000 dead tuples; 0.02 fires at 16,000. At large tables, target <code>dead_pct</code> ≈ <code>scale_factor</code> × 100. Apply in <a href="#rung-1-lower-the-trigger">Rung 1</a>.</span></dd>

<dt>max_workers (<code>autovacuum_max_workers</code>)</dt>
<dd>Maximum tables vacuumed simultaneously; default 3.
<span class="key-terms-detail">Increase when multiple high-churn tables compete for vacuum attention. Set alongside <code>scale_factor</code> in <a href="#rung-1-lower-the-trigger">Rung 1</a>.</span></dd>

<dt>naptime (<code>autovacuum_naptime</code>)</dt>
<dd>Interval between autovacuum wake-ups to check each table; default 60 seconds.
<span class="key-terms-detail">At 60s on a table receiving thousands of updates per minute, nearly 5,000 dead tuples can accumulate between checks. Lower to 10s in <a href="#rung-2-increase-check-frequency">Rung 2</a>.</span></dd>

<dt>vacuum_threshold (<code>autovacuum_vacuum_threshold</code>)</dt>
<dd>Minimum absolute dead-tuple count before autovacuum considers a table, regardless of <code>scale_factor</code>; default 50.
<span class="key-terms-detail">Lowering to 20 ensures small, high-churn tables are not ignored. Set in <a href="#rung-2-increase-check-frequency">Rung 2</a>.</span></dd>

<dt>cost_limit (<code>autovacuum_vacuum_cost_limit</code>)</dt>
<dd>I/O budget for a single autovacuum pass before pausing; default 200 (~9 pages per pass).
<span class="key-terms-detail">At 1,000, autovacuum cleans ~47 pages per pass. Set per-table with <code>ALTER TABLE ... SET (autovacuum_vacuum_cost_limit = N)</code> in <a href="#rung-3-ensure-each-pass-completes">Rung 3</a> without changing the global default.</span></dd>
</dl>

</div>

<div class="key-terms-group">

<h3 id="key-terms-failure-modes">Failure modes</h3>

<p class="key-terms-table-note"><strong>trigger-limited</strong> and <strong>throttle-limited</strong> describe why autovacuum falls behind despite different symptoms. See the <a href="#tuning-path">tuning path</a> for which rung to apply and <a href="#troubleshooting">Troubleshooting</a> for symptom-to-fix mapping in production.</p>

</div>

---

## Related Guides

- [AAP HA/DR on OpenShift with CloudNativePG](https://ansible-tmm.github.io/solution-guides/README-AAP-HA-DR-OpenShift) — the deployment topology this autovacuum tuning applies to
- [High-Availability AAP with EDB PostgreSQL DR](https://ansible-tmm.github.io/solution-guides/README-EDB) — the EDB variant of the same HA/DR problem

---

## Next Steps

<div class="key-terms-closing">

<ul>
<li><a href="#overview">Review the decision diagram in Overview</a></li>
<li><a href="#tuning-path">Follow the tuning path</a> for rung order</li>
<li><a href="#key-terms">Jump to Key Terms</a> for a parameter lookup</li>
<li><a href="/">Back to AAP Guides</a></li>
</ul>

</div>
