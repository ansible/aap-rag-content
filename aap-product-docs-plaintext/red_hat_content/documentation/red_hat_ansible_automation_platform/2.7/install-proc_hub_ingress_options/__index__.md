# Configure ingress options for automation hub

The Ansible Automation Platform Operator installation form allows you to further configure your automation hub operator ingress under **Advanced configuration**.

## About this task

## Procedure

1.  Log in to Red Hat OpenShift Container Platform.
2.  Navigate to Operators> (and then)Installed Operators.
3.  Select your Ansible Automation Platform Operator deployment.
4.  Select the **Ansible Automation Platform** tab.
5.  Click the ⋮ icon next to your Ansible Automation Platform instance and select **Edit AnsibleAutomationPlatform** .
6.  Click **YAML view** and locate the `spec.hub:` section..
7.  Configure the route options under the `hub:` section:


```
spec:
hub:
ingress_type: Ingress
ingress_annotations: |
nginx.ingress.kubernetes.io/proxy-body-size: "0"
nginx.ingress.kubernetes.io/proxy-connect-timeout: "600"
ingress_tls_secret: hub-ingress-tls-secret
```

8.  Click **Save**.

Note:
These settings apply to the automation hub component managed by this Ansible Automation Platform instance. The operator automatically updates the ingress configuration for the hub.

For more examples of Ansible Automation Platform custom resources, see [Red Hat Ansible Automation Platform custom resources](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_appendix_operator_crs#appendix-operator-crs_appendix-operator-crs "This appendix provides a reference for the Ansible Automation Platform custom resources for various deployment scenarios.")

9.

## Results

After you have configured your automation hub ingress settings, OpenShift Container Platform updates the pods. This may take a few minutes.

You can view the progress by navigating to Workloads> (and then)Pods and locating the newly created instance.

Verify that the following operator pods provided by the Ansible Automation Platform Operator installation from automation hub are running:

| Operator manager controllers                                                                                                                                                                                                | Automation controller                                                                                                | Automation hub                                                                                                                    |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| <br>The operator manager controllers for each of the 3 operators, include the following:<br>automation-controller-operator-controller-managerautomation-hub-operator-controller-managerresource-operator-controller-manager | <br>After deploying automation controller, you will see the addition of these pods:<br>controllercontroller-postgres | <br>After deploying automation hub, you will see the addition of these pods:<br>hub-apihub-contenthub-postgreshub-redishub-worker |


Note:

A missing pod can indicate the need for a pull secret. Pull secrets are required for protected or private image registries. See [Using image pull secrets](https://docs.openshift.com/container-platform/4.11/openshift_images/managing_images/using-image-pull-secrets.html) for more information. You can diagnose this issue further by running `oc describe pod <pod-name>` to see if there is an ImagePullBackOff error on that pod.
