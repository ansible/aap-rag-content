# 5. Configuring Red Hat Ansible Automation Platform components on Red Hat Ansible Automation Platform Operator
## 5.1. Configuring platform gateway on Red Hat OpenShift Container Platform web console
### 5.1.4. Configuring your CSRF settings for your platform gateway Operator ingress




The Red Hat Ansible Automation Platform Operator creates Openshift Routes and configures your Cross-site request forgery (CSRF) settings automatically. When using external ingress, you must configure your CSRF on the ingress to allow for cross-site requests. You can configure your platform gateway operator ingress under **Advanced configuration** .

**Procedure**

1. Log in to Red Hat OpenShift Container Platform.
1. Navigate toOperators→Installed Operators.
1. Select your Ansible Automation Platform Operator deployment.
1. Select the **Ansible Automation Platform** tab.
1. For new instances, clickCreate AnsibleAutomationPlatform.


1. For existing instances, you can edit the YAML view by clicking the ⋮ icon and thenEdit AnsibleAutomationPlatform.

1. ClickAdvanced Configuration.
1. Under **Ingres annotations** , enter any annotations to add to the ingress.
1. Under **Ingress TLS secret** , click the drop-down list and select a secret from the list.
1. Under **YAML view** paste in the following code:


```
spec:      extra_settings:        - setting: CSRF_TRUSTED_ORIGINS          value:            - https://my-aap-domain.com
```


1. After you have configured your platform gateway, clickCreateat the bottom of the form view (OrSavein the case of editing existing instances).


**Verification**

Red Hat OpenShift Container Platform creates the pods. This may take a few minutes. You can view the progress by navigating toWorkloads→Podsand locating the newly created instance. Verify that the following operator pods provided by the Red Hat Ansible Automation Platform Operator installation from platform gateway are running:


| Operator manager controllers pods | Automation controller pods | Automation hub pods | Event-Driven Ansible (EDA) pods | platform gateway pods |
| --- | --- | --- | --- | --- |
| The operator manager controllers for each of the four operators, include the following:

- automation-controller-operator-controller-manager
- automation-hub-operator-controller-manager
- resource-operator-controller-manager
- aap-gateway-operator-controller-manager
- ansible-lightspeed-operator-controller-manager
- eda-server-operator-controller-manager | After deploying automation controller, you can see the addition of the following pods:

- Automation controller web
- Automation controller task
- Mesh ingress
- Automation controller postgres | After deploying automation hub, you can see the addition of the following pods:

- Automation hub web
- Automation hub task
- Automation hub API
- Automation hub worker | After deploying EDA, you can see the addition of the following pods:

- EDA API
- EDA Activation
- EDA worker
- EDA stream
- EDA Scheduler | After deploying platform gateway, you can see the addition of the following pods:

- platform gateway
- platform gateway redis |


Note
A missing pod can indicate the need for a pull secret. Pull secrets are required for protected or private image registries. See [Using image pull secrets](https://docs.openshift.com/container-platform/4.11/openshift_images/managing_images/using-image-pull-secrets.html) for more information. You can diagnose this issue further by running `oc describe pod &lt;pod-name&gt;` to see if there is an ImagePullBackOff error on that pod.



