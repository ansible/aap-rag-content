# 1. Types of workloads
## 1.8. Reference workloads for enterprise topologies

The following table provides reference data for typical workloads, performance metrics, and capacity planning for the tested Ansible Automation Platform enterprise topologies.

**Table 1.2. Reference workloads for enterprise topologies**

| Component / Feature | Metric |
| --- | --- |
| <br>  REST API | <br>  16 requests per second (RPS) |
| <br>  REST API 50 percentile latency at 16 RPS | <br>  500 milliseconds |
| <br>  REST API 99 percentile latency at 16 RPS | <br>  1.5 seconds |
| <br>  Hosts in automation controller inventory | <br>  10,000 hosts |
| <br>  Job start rate in automation controller | <br>  80 jobs started per second |
| <br>  Concurrent jobs in automation controller | <br>  40 with default forks (5 forks is default) + 400 with forks=1 |
| <br>  Callback receiver event rate | <br>  40,000 events per second at peak |
| <br>  Job History with 7 days retention | <br>  2kb event; 500 events per playbook run; 2000 jobs a day + Less than 60Gb (as specified as minimum required disk on Database node) |
| <br>  (Certified) Sync time | <br>  Less than 30 minutes |
| <br>  (Validated) Sync time | <br>  Less than 5 minutes |
| <br>  Processing events with skip audit events enabled (6 activations) with events incoming via Event Stream and execution strategy set to sequential (default) in the rulebook | <br>  3 actionable event/minute with minimal payload with job template action on local automation controller where each job completes in 1 minute |

