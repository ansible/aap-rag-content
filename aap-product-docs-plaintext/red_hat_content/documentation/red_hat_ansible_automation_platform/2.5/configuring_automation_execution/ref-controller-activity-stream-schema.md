# 9. Logging and Aggregation
## 9.1. Loggers
### 9.1.2. Activity stream schema




This uses the fields common to all loggers listed in [Log message schema](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#ref-controller-log-message-schema) .

It has the following additional fields:

-  `    actor` : Username of the user who took the action documented in the log.
-  `    changes` : JSON summary of what fields changed, and their old or new values.
-  `    operation` : The basic category of the changes logged in the activity stream, for instance, "associate".
-  `    object1` : Information about the primary object being operated on, consistent with what is shown in the activity stream.
-  `    object2` : If applicable, the second object involved in the action.



<span id="ref-controller-job-event-schema"></span>
This logger reflects the data being saved into job events, except when they would otherwise conflict with expected standard fields from the logger, in which case the fields are nested. Notably, the field host on the `job_event` model is given as `event_host` . There is also a sub-dictionary field, `event_data` within the payload, which contains different fields depending on the specifics of the Ansible event.


This logger also includes the common fields in [Log message schema](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#ref-controller-log-message-schema) .

