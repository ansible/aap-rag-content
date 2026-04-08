# 5. Configuring Red Hat Ansible Automation Platform components on Red Hat Ansible Automation Platform Operator
## 5.1. Configuring platform gateway on Red Hat OpenShift Container Platform web console
### 5.1.8. Increase the OpenShift Container Platform Route timeout




During high-volume API operations, such as Configuration as Code (CasC) restores, the OpenShift Route might time out if the operation exceeds the default 30-second window.

You must increase the `client_request_timeout` in the `AnsibleAutomationPlatform` Custom Resource (CR) to resolve HTTP 504 (Gateway Timeout) or HTTP 503 (Service Unavailable) errors.

**Prerequisites**

- Access to the OpenShift Container Platform web console with administrator privileges.
- Update the Ansible Automation Platform 2.6 operator to the latest version.


**Procedure**

1. Log in to the OpenShift web console.
1. Navigate to **Installed Operators** > **Ansible Automation Platform** > **All Instances** .
1. Select your **AnsibleAutomationPlatform** instance.
1. Click the **YAML** tab.
1. In the `    spec:` section, add the `    route_annotations` to extend the timeout:


```
spec:      route_annotations: |        haproxy.router.openshift.io/timeout: 180s
```


1. Click **Save** .


**Verification**

1. Navigate to **Networking** > **Routes** in the OpenShift console.
1. Select the route for your Ansible Automation Platform instance.
1. Verify the **Annotations** section contains the updated timeout value.


