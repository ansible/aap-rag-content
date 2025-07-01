# 9. Ansible Automation Platform Resource Operator
## 9.5. Creating custom resources for Resource Operator
### 9.5.4. Creating an automation controller schedule custom resource




**Procedure**

- Create a schedule on automation controller by creating an automation controller schedule custom resource:


```
apiVersion: tower.ansible.com/v1alpha1
kind: AnsibleSchedule
metadata:
name: schedule
spec:
connection_secret: controller-access
runner_pull_policy: IfNotPresent
name: "Demo Schedule"
rrule: "DTSTART:20210101T000000Z RRULE:FREQ=DAILY;INTERVAL=1;COUNT=1"
unified_job_template: "Demo Job Template"
```

