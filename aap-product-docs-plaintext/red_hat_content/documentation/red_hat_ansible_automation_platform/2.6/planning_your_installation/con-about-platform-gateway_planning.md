# 2. Red Hat Ansible Automation Platform components
## 2.1. Platform gateway




Platform gateway is the service that handles authentication and authorization for the Ansible Automation Platform. It provides a single entry into the Ansible Automation Platform and serves the platform user interface so you can authenticate and access all of the Ansible Automation Platform services from a single location. For more information about the services available in the Ansible Automation Platform, refer to [Key functionality and concepts](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/getting_started_with_ansible_automation_platform/index#assembly-gs-key-functionality) in _Getting started with Ansible Automation Platform_ .

The platform gateway includes an activity stream that captures changes to gateway resources, such as the creation or modification of organizations, users, and service clusters, among others. For each change, the activity stream collects information about the time of the change, the user that initiated the change, the action performed, and the actual changes made to the object, when possible. The information gathered varies depending on the type of change.

You can access the details captured by the activity stream from the API:

```
/api/gateway/v1/activitystream/
```

