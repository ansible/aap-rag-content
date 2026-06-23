# Optimize request timeouts
## Increase the OpenShift Route timeout
### Before you begin

- Access to the Red Hat OpenShift Container Platform (RHOCP) web console.
- Update the Ansible Automation Platform 2.6 operator to the latest version to ensure configuration changes propagate correctly to the OpenShift Route.

### Procedure

1.  Log in to the OpenShift web console.
2.  Navigate to **Installed Operators → Ansible Automation Platform → All Instances**.
3.  Click your `AnsibleAutomationPlatform` instance.
4.  Select the **YAML** tab. Under the spec: section, add the `route_annotations` to extend the timeout:


```
spec:
route_annotations: |
haproxy.router.openshift.io/timeout: 180s

```

5.  Save the changes.

