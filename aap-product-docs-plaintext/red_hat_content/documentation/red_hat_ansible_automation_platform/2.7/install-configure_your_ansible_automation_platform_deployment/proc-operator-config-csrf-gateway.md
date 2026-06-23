# Configure your Ansible Automation Platform deployment
## Configure your CSRF settings

The Red Hat Ansible Automation Platform Operator creates Openshift Routes and configures your Cross-site request forgery (CSRF) settings automatically. .

### About this task

When using external ingress, you must configure your CSRF on the ingress to allow for cross-site requests. You can configure your platform gateway operator ingress under **Advanced configuration**

### Procedure

1.  Log in to Red Hat OpenShift Container Platform.
2.  Navigate to Operators> (and then)Installed Operators.
3.  Select your Ansible Automation Platform Operator deployment.
4.  Select the **Ansible Automation Platform** tab.
5.  For new instances, click Create AnsibleAutomationPlatform.   1.  For existing instances, you can edit the YAML view by clicking the ⋮ icon and then Edit AnsibleAutomationPlatform.
6.  Click Advanced Configuration.
7.  Under **Ingres annotations**, enter any annotations to add to the ingress.
8.  Under **Ingress TLS secret**, click the drop-down list and select a secret from the list.
9.  Under **YAML view** paste in the following code:


```
spec:
extra_settings:
- setting: CSRF_TRUSTED_ORIGINS
value:
- https://my-aap-domain.com
```

10.  After you have configured your platform gateway, click Create at the bottom of the form view (Or Save in the case of editing existing instances).

### Results

Red Hat OpenShift Container Platform creates the pods. This may take a few minutes. You can view the progress by navigating to Workloads> (and then)Pods and locating the newly created instance. Verify that the following operator pods provided by the Red Hat Ansible Automation Platform Operator installation from platform gateway are running:

| Operator manager controllers pods                                                                                                                                                                                                                                                                                                                         | Automation controller pods                                                                                                                                                                  | Automation hub pods                                                                                                                                                 | Event-Driven Ansible pods                                                                                                          | Platform gateway pods                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| <br>The operator manager controllers for each of the four operators, include the following:<br>automation-controller-operator-controller-managerautomation-hub-operator-controller-managerresource-operator-controller-manageraap-gateway-operator-controller-manageransible-lightspeed-operator-controller-managereda-server-operator-controller-manager | <br>After deploying automation controller, you can see the addition of the following pods:<br>Automation controller webAutomation controller taskMesh ingressAutomation controller postgres | <br>After deploying automation hub, you can see the addition of the following pods:<br>Automation hub webAutomation hub taskAutomation hub APIAutomation hub worker | <br>After deploying EDA, you can see the addition of the following pods:<br>EDA APIEDA ActivationEDA workerEDA streamEDA Scheduler | <br>After deploying platform gateway, you can see the addition of the following pods:<br>platform gatewayplatform gateway redis |


Note:

A missing pod can indicate the need for a pull secret. Pull secrets are required for protected or private image registries. See [Using image pull secrets](https://docs.openshift.com/container-platform/4.11/openshift_images/managing_images/using-image-pull-secrets.html) for more information. You can diagnose this issue further by running `oc describe pod <pod-name>` to see if there is an ImagePullBackOff error on that pod.

