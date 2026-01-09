# 10. Upgrading Red Hat Ansible Automation Platform Operator on Red Hat OpenShift Container Platform
## 10.6. Creating Ansible Automation Platform custom resources




After upgrading to the latest version of Ansible Automation Platform Operator on OpenShift Container Platform, you can create an Ansible Automation Platform custom resource (CR) that specifies the names of your existing deployments, in the same namespace.

The following example outlines the steps to deploy a new Event-Driven Ansible setup after upgrading to the latest version, with existing automation controller and automation hub deployments already in place.

The [Appendix](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/installing_on_openshift_container_platform/index#appendix-operator-crs_performance-considerations) contains more examples of Ansible Automation Platform CRs for different deployments.

**Procedure**

1. Log in to Red Hat OpenShift Container Platform.
1. Navigate toOperators→Installed Operators.
1. Select your Ansible Automation Platform Operator deployment.
1. Select the **Details** tab.
1. On the **Ansible Automation Platform** tile clickCreate instance.
1. From the **Create Ansible Automation Platform** page enter a name for your instance in the **Name** field.
1. ClickYAML viewand paste the following YAML ( [aap-existing-controller-and-hub-new-eda.yml](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/installing_on_openshift_container_platform/index#appendix-operator-crs_performance-considerations) ):


```
---    apiVersion: aap.ansible.com/v1alpha1    kind: AnsibleAutomationPlatform    metadata:      name: myaap    spec:      # Development purposes only      no_log: false          controller:        name: existing-controller #obtain name from controller CR        disabled: false          eda:        disabled: false          hub:        name: existing-hub        disabled: false
```


1. ClickCreate.

Note
You can override the operator’s default image for automation controller, automation hub, or platform-resource app images by specifying the preferred image on the YAML spec. This enables upgrading a specific deployment, like a controller, without updating the operator.

The recommended approach however, is to upgrade the operator and use the default image values.



**Verification**

Navigate to your Ansible Automation Platform Operator deployment and clickAll instancesto verify whether all instances have deployed correctly. You should see the **Ansible Automation Platform** instance and the deployed **AutomationController** , **EDA** , and **AutomationHub** instances here.





Alternatively, you can verify whether all instances deployed correctly by running `oc get route` in the command line.

