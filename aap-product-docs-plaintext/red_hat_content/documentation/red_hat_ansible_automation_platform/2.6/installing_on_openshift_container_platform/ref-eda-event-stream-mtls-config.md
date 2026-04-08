# 5. Configuring Red Hat Ansible Automation Platform components on Red Hat Ansible Automation Platform Operator
## 5.1. Configuring platform gateway on Red Hat OpenShift Container Platform web console
### 5.1.6. Event-Driven Ansible event stream mTLS configuration variables




You can configure Mutual Transport Layer Security (mTLS) for the Event-Driven Ansible event stream by setting parameters in the `AnsibleAutomationPlatform` custom resource.

You can configure the following parameters nested under `spec.eda.event_stream:` .

| Variable | Description | Default Value | Notes |
| --- | --- | --- | --- |
|  `mtls` | Controls whether mTLS is enabled for the event stream endpoint. |  `true` | Set the value to `false` to disable event stream mTLS during installation. |
|  `mtls_prefix` | Customizes the mTLS endpoint prefix for the event stream. You must provide a valid URL prefix. |  `/mtls/eda-event-streams` | The value you provide is used as a prefix for the full endpoint URL. Customizing the full URL path is out of scope. |


**Custom resource example**

The following example shows how to configure the event stream parameters in the `AnsibleAutomationPlatform` custom resource:

```
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
name: myaap
namespace: ansible-automation-platform
spec:
eda:
disabled: false
event_stream:
mtls: true
mtls_prefix: /custom/path/mtls
```

