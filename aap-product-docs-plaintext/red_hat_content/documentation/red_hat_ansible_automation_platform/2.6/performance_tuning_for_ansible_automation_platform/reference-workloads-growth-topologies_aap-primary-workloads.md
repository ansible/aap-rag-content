# 1. Types of workloads
## 1.7. Reference workloads for growth topologies




The following table provides reference data for typical workloads, performance metrics, and capacity planning for the tested Ansible Automation Platform growth topologies.


<span id="idm139687045633696"></span>
**Table 1.1. Reference workloads for growth topologies**

| Component / Feature | Metric |
| --- | --- |
| REST API | 8 requests per second (RPS) |
| REST API 50 percentile latency at 8 RPS | 500 milliseconds |
| REST API 99 percentile latency at 8 RPS | 1.5 seconds |
| Hosts in automation controller inventory | 1,000 hosts |
| Job start rate in automation controller (max burst rate with standard launch) | 20 jobs started per second |
| Concurrent jobs in automation controller | 10 concurrent jobs with default forks (5 forks is default) + 100 with forks=1 |
| Callback receiver event processing rate | 10,000 job events per second at peak |
| Job History with 30 days retention | 2kb event; 500 events per playbook run; 500 jobs a day + Less than 60Gb (as specified as minimum required disk on Database node) |
| (Certified) Sync time | Less than 30 minutes |
| (Validated) Sync time | Less than 5 minutes |
| Activation processing events with skip audit events enabled (6 activation) with events incoming via Event Stream and execution strategy set to sequential (default) in the rulebook | 1 actionable event/minute with minimal payload with job template action on local automation controller where each job completes in 1 minute |




