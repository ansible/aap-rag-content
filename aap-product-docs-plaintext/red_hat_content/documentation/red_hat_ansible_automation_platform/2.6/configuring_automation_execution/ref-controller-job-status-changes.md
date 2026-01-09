# 9. Logging and Aggregation
## 9.1. Loggers
### 9.1.4. Job status changes




The job status changes logger captures changes in the status of jobs as they occur.

This is a lower-volume source of information about changes in job states compared to job events, and captures changes to types of unified jobs other than job template based jobs.

This logger also includes the common fields in [Log message schema](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/configuring_automation_execution/assembly-controller-logging-aggregation#ref-controller-log-message-schema) and fields present on the job model.

