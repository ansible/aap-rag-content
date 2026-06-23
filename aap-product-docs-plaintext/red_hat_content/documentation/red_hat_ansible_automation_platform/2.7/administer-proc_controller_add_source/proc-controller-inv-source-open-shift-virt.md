# Add a source to an inventory
## Source an inventory from OpenShift Virtualization

Learn how to add an OpenShift Virtualization inventory source to an existing inventory.

### Before you begin

- You need a virtual machine deployed in a specific namespace and an OpenShift or Kubernetes API Bearer Token credential.

### About this task

This inventory source uses a cluster that is able to deploy Red Hat OpenShift Container Platform Virtualization.

### Procedure

1.  From the navigational panel, select Automation Execution> (and then)Infrastructure> (and then)Inventories.
2.  Select the inventory that you want to add a source to.
3.  In the **Sources** tab, click Add source.
4.  From the Source menu, select **OpenShift Virtualization**.   - The **Add new source** window expands with the required **Credential** field. Choose from an existing Kubernetes API Bearer Token credential. For more information, see [OpenShift or Kubernetes API Bearer Token credential type](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-ref_controller_credential_openshift#ref-controller-credential-openShift "Select this credential type to create instance groups that point to a Kubernetes or OpenShift container."). In this example, the `cmv2.engineering.redhat.com` credential is used.

5.  You can optionally specify the **Verbosity**, **Host Filter**, **Enabled Variable/Value**, and **Update options** as described in the [Adding a source](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-proc_controller_add_source#proc-controller-add-source "Use the following procedure to add a source to an inventory. When you add a source to an inventory, the system creates a new group for that source.") steps.
6.  Use the **Source Variables** field to override variables used by the `kubernetes` inventory plugin. Enter variables by using either JSON or YAML syntax. Use the radio button to toggle between the two. For more information about these variables, see the [kubevirt.core.kubevirt inventory source](https://kubevirt.io/kubevirt.core/main/plugins/kubevirt.html#parameters) documentation. In the following example, the connections variable is used to specify access to a particular namespace in a cluster:

```
---
connections:
- namespaces:
- hao-test
```

7.  Click Save and then click Sync to sync the inventory.

