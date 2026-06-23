# Configure options in the RENEWAL_GUIDANCE report
## Generate reports to show ephemeral usage

The `metrics-utility` command-line tool can generate reports showing ephemeral usage of managed nodes.

The `RENEWAL_GUIDANCE` report has the capability to list additional sheets with ephemeral usage if the `-ephemeral` parameter is provided. Using the parameter `--ephemeral=1month`, you can define ephemeral nodes as any managed node that has been automated for a maximum of one month, then never automated again. Using this parameter, the total ephemeral usage of the 12-month period is computed as maximum ephemeral nodes used over all 1-month rolling date windows. This sheet is also added into the report.

```
# Will generate report for 12 months back with ephemeral nodes being nodes
# automated for less than 1 month.
metrics-utility build_report --since=12months --ephemeral=1month
```

## Select a date range for your `RENEWAL_GUIDANCE` report

The default behavior of the `RENEWAL_GUIDANCE` report is to build a report for the current date. The following examples describe how to override this default behavior to select a specific date range for your report:

The `RENEWAL_GUIDANCE` report requires a `since` parameter as the parameter is not supported due to the nature of the `HostMetric` data and is always set to `now`. To override a report date range that is already built, use parameter `-force` with the command. For more information, see the following examples:

```
# Build report for a specific date range, including the provided days
metrics-utility build_report --since=2025-03-01

# Build report for a last 12 months from a current date
metrics-utility build_report --since=12months

# Build report for a last 12 months from a current date overwriting an existing report
metrics-utility build_report --since=12months --force
```
