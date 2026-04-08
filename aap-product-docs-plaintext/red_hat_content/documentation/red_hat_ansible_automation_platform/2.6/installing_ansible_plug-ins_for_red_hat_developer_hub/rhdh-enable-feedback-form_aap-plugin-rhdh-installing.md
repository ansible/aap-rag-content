# 8. Red Hat Developer Hub data telemetry capturing
## 8.1. Enable the Ansible plug-ins feedback form




The Ansible plug-ins feedback form is disabled by default. When enabled, you can submit a star rating and feedback text from the Ansible plug-ins interface. The feedback data is sent to Red Hat as part of the telemetry data collected by your Red Hat Developer Hub instance.

To enable the feedback form, set the `ansible.feedback.enabled` option to `true` in your Red Hat Developer Hub configuration.

**Helm installation**

If you installed Red Hat Developer Hub by using the Helm chart, add or update the following YAML in the `app-config-rhdh.yaml` data section of the ConfigMap:

```
kind: ConfigMap
apiVersion: v1
metadata:
name: app-config-rhdh
data:
app-config-rhdh.yaml: |
ansible:
feedback:
enabled: true
```

After updating the ConfigMap:

1. In the OpenShift Developer UI, select the `    Red Hat Developer Hub` pod.
1. Open **Actions** .
1. ClickRestart rollout.


**Operator installation**

If you installed Red Hat Developer Hub by using the Operator, update the `app-config-rhdh` ConfigMap referenced by your `Backstage` custom resource.

Add or update the following YAML in the `app-config-rhdh.yaml` data section of the ConfigMap:

```
kind: ConfigMap
apiVersion: v1
metadata:
name: app-config-rhdh
data:
app-config-rhdh.yaml: |
ansible:
feedback:
enabled: true
```

The Operator detects the ConfigMap change and automatically restarts the Red Hat Developer Hub deployment.


<span id="idm139713678801024"></span>
