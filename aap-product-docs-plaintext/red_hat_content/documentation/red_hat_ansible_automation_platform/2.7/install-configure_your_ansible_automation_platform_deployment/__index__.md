# Configure your Ansible Automation Platform deployment

Configuring your Ansible Automation Platform deployment after installation customizes the platform to match your organizational requirements. Apply configuration settings to secure connections and manage storage resources.

Configuring your deployment helps you to:

- **Secure authentication flows**: Enable HTTPS redirect for single sign-on to ensure secure authentication through platform gateway.
- **Protect against security threads**: Configure CSRF protection settings to prevent cross-site request forgery attacks.
- **Manage storage resources**: Find and delete persistent volume claims to reclaim storage space and manage platform resources efficiently.

## Enable HTTPS redirect for single sign-on

HTTPS redirect for SAML, allows you to log in once and access all of the platform gateway without needing to reauthenticate.

### Before you begin

- You have successfully configured SAML in the gateway from the Ansible Automation Platform Operator. Refer to [Configuring SAML authentication](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-proc_controller_set_up_saml#controller-set-up-SAML "SAML allows the exchange of authentication and authorization data between an Identity Provider (IdP) and a Service Provider (SP). Ansible Automation Platform is a SAML SP that you can configure to talk with one or more SAML IdPs to authenticate users.") for help with this.

### About this task

### Procedure

1.  Log in to Red Hat OpenShift Container Platform.
2.  Go to Operators> (and then)Installed Operators.
3.  Select your Ansible Automation Platform Operator deployment.
4.  Select **All Instances** and go to your **AnsibleAutomationPlatform** instance.
5.  Click the ⋮ icon and then select Edit AnsibleAutomationPlatform.
6.  In the **YAML view** paste the following YAML code under the `spec:` section:


```
spec:
extra_settings:
- setting: REDIRECT_IS_HTTPS
value: '"True"'
```

7.  Click Save.

### Results

After you have added the `REDIRECT_IS_HTTPS` setting, wait for the pod to redeploy automatically. You can verify this setting makes it into the pod by running:

```
oc exec -it <gateway-pod-name> -- grep REDIRECT /etc/ansible-automation-platform/gateway/settings.py
```

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

## Find and delete PVCs

A persistent volume claim (PVC) is a storage volume used to store data that automation hub and automation controller applications use.

### About this task

This persistence is a key feature of static provisioning. If you redeploy an instance using the same name, the Operator must bind to these existing PVCs, allowing for data continuity across deployments. If you are confident that you no longer need a PVC, or have backed it up elsewhere, you can manually delete them.

### Procedure

1.  List the existing PVCs in your deployment namespace:


```
oc get pvc -n <namespace>
```

2.  Identify the PVC associated with your previous deployment by comparing the old deployment name and the PVC name.
3.  Delete the old PVC:


```
oc delete pvc -n <namespace> <pvc-name>
```

## Enable feature flags in your CR

Feature flags control access to Technology Preview and Developer Preview features in Ansible Automation Platform. You can set feature flags at install time by adding them to the `AnsibleAutomationPlatform` custom resource (CR).

### About this task

To make feature flag information visible in the web UI to superusers and auditors, enable the `RUNTIME_FEATURE_FLAGS` setting. To lock specific feature flags to a fixed value, add them to the `feature_flags` field. Flags set in the CR are read-only and cannot be changed at runtime.

### Procedure

1.  Edit the `AnsibleAutomationPlatform` custom resource:


```
apiVersion:aap.ansible.com/v1alpha1
kind:AnsibleAutomationPlatform
metadata:
name:myaap
namespace:aap
spec:
extra_settings:
- setting:RUNTIME_FEATURE_FLAGS
value:'@bool True'
feature_flags:
FEATURE_EDA_ANALYTICS_ENABLED:True
FEATURE_POLICY_AS_CODE_ENABLED:True
```

2.  Save the custom resource. The operator applies the changes automatically.

### What to do next

If you rerun the Operator or update the CR, install-time feature flag values are reapplied and override any runtime changes made through the UI or API. If you remove a flag from the `feature_flags` field, that flag reverts to allowing runtime changes.

## Review platform gateway FAQs

Manage your Ansible Automation Platform deployment and troubleshoot common issues with these frequently asked questions. Learn about resource management, logging, and error recovery for your components.

If I delete my Ansible Automation Platform deployment will I still have access to automation controller?
No, automation controller, automation hub, and Event-Driven Ansible are nested within the deployment and are also deleted.

How must I manage parameters when adding or removing them in the Ansible Automation Platform custom resource (CR) hierarchy?
When *adding* parameters, you can add it to the Ansible Automation Platform custom resource (CR) only and those parameters will work their way down to the nested CRs.

When *removing* parameters, you have to remove them both from the Ansible Automation Platform CR *and* the nested CR, for example, the **Automation Controller** CR.

Something went wrong with my deployment but I’m not sure what, how can I find out?
You can follow along in the command line while the operator is reconciling, this can be helpful for debugging. Alternatively you can click into the deployment instance to see the status conditions being updated as the deployment goes on.

Is it still possible to view individual component logs?
When troubleshooting you should examine the **Ansible Automation Platform** instance for the main logs and then each individual component (**EDA**, **AutomationHub**, **AutomationController**) for more specific information.

Where can I view the condition of an instance?
To display status conditions click into the instance, and look under the **Details** or **Events** tab. Alternatively, to display the status conditions you can run the get command: `oc get automationcontroller <instance-name> -o jsonpath=Pipe "| jq"`

Can I track my migration in real time?
To help track the status of the migration or to understand why migration might have failed you can look at the migration logs as they are running. Use the logs command: `oc logs fresh-install-controller-migration-4.6.0-jwfm6 -f`

I have configured my SAML but authentication fails with this error: "Unable to complete social auth login" What can I do?
You must update your Ansible Automation Platform instance to include the `REDIRECT_IS_HTTPS` extra setting. See [Enabling single sign-on (SSO) for platform gateway on OpenShift Container Platform](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-configure_your_ansible_automation_platform_deployment#proc-operator-enable-https-redirect "HTTPS redirect for SAML, allows you to log in once and access all of the platform gateway without needing to reauthenticate.") for help with this.
