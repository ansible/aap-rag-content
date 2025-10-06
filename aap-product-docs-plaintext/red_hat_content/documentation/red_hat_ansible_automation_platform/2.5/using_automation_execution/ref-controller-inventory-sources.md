# 14. Inventories
## 14.4. Add a new inventory
### 14.4.7. Inventory sources




Choose a source which matches the inventory type against which a host can be entered:

-  [Sourcing from a Project](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#proc-controller-sourced-from-project)
-  [Amazon Web Services EC2](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#proc-controller-amazon-ec2)
-  [Google Compute Engine](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#proc-controller-inv-source-gce)
-  [Microsoft Azure Resource Manager](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#proc-controller-azure-resource-manager)
-  [VMware vCenter](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#proc-controller-inv-source-vm-vcenter)
-  [VMware ESXi](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#proc-controller-inv-source-vm-esxi)
-  [Red Hat Satellite 6](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#proc-controller-inv-source-satellite)
-  [Red Hat Insights](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#proc-controller-inv-source-insights)
-  [OpenStack](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#proc-controller-inv-source-openstack)
-  [Red Hat Virtualization](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#proc-controller-inv-source-rh-virt)
-  [Red Hat Ansible Automation Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#proc-controller-inv-source-aap)
-  [Terraform State](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#proc-controller-inv-source-terraform)


#### 14.4.7.1. Sourcing from a Project




An inventory that is sourced from a project means that it uses the SCM type from the project it is tied to. For example, if the project’s source is from GitHub, then the inventory uses the same source.

Use the following procedure to configure a project-sourced inventory:

**Procedure**

1. From the navigation panel, selectAutomation Execution→Infrastructure→Inventories.
1. Select the inventory name you want a source to and click the **Sources** tab.
1. ClickCreate source.
1. In the **Create source** page, select **Sourced from a Project** from the **Source** list.
1. Enter the following details in the additional fields:


- Optional: **Source control branch/tag/commit** : Enter the SCM branch, tags, commit hashes, arbitrary refs, or revision number (if applicable) from the source control (Git or Subversion) to checkout.

This field only displays if the sourced project has the **Allow branch override** option checked. For further information, see [SSCM Types - Configuring playbooks to use Git and Subversion](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#proc-scm-git-subversion) .

![Allow branch override](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/21802af7817107c37c3bafeaff0b1f75/projects-create-scm-project-branch-override-checked.png)


Some commit hashes and refs might not be available unless you also give a custom refspec in the next field. If left blank, the default is HEAD which is the last checked out Branch/Tag/Commit for this project.


- Optional: **Credential** : Specify the credential to use for this source.
-  **Project** (required): Pre-populates with a default project, otherwise, specify the project this inventory is using as its source. Click the![Search](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/74841a45a98b4160b7576724a8f4c038/search.png)
icon to choose from a list of projects. If the list is extensive, use the search to narrow the options.
-  **Inventory file** (required): Select an inventory file associated with the sourced project. If not already populated, you can type it into the text field within the menu to filter extraneous file types. In addition to a flat file inventory, you can point to a directory or an inventory script.

![image](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/a6ddcfbe4ad6f6ca69426b66f8af29ae/inventories-create-source-sourced-from-project-filter.png)




1. Optional: You can specify the verbosity, host filter, enabled variable/value, and update options as described in [Adding a source](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#proc-controller-add-source) .
1. Optional: To pass to the custom inventory script, you can set environment variables in the **Source variables** field. You can also place inventory scripts in source control and then run it from a project. For more information, see [Inventory File Importing](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/configuring_automation_execution/assembly-inventory-file-importing) in _Configuring automation execution_ .


**Troubleshooting**

If you are executing a custom inventory script from SCM, ensure that you set the execution bit ( `chmod +x` ) for the script in your upstream source control.


If you do not, automation controller throws a `[Error 13] Permission denied` error on execution.

#### 14.4.7.2. Amazon Web Services EC2




Use the following procedure to configure an AWS EC2-sourced inventory.

**Procedure**

1. From the navigation panel, selectAutomation Execution→Infrastructure→Inventories.
1. Select the inventory name you want a source to and click the **Sources** tab.
1. ClickCreate source.
1. In the **Create source** page, select **Amazon EC2** from the **Source** list.
1. The **Create source** window expands with additional fields. Enter the following details:


- Optional: **Credential** : Choose from an existing AWS credential. For more information, see [Managing user credentials](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-credentials) .

If automation controller is running on an EC2 instance with an assigned IAM Role, the credential can be omitted, and the security credentials from the instance metadata are used instead. For more information about using IAM Roles, see [IAM roles for Amazon EC2_documentation_at_Amazon](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html) documentation at Amazon.



1. Optional: You can specify the verbosity, host filter, enabled variables or values, and update options as described in [Adding a source](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#proc-controller-add-source) .
1. Use the **Source variables** field to override variables used by the `    aws_ec2` inventory plugin. Enter variables by using either JSON or YAML syntax. Use the radio button to toggle between the two. For more information about these variables, see the [aws inventory plugin documentation](https://console.redhat.com/ansible/automation-hub/repo/published/amazon/aws/content/inventory/aws_ec2) .


**Troubleshooting**

If you only use `include_filters` , the AWS plugin always returns all the hosts. To use this correctly, the first condition on the `or` must be on `filters` and then build the rest of the `OR` conditions on a list of `include_filters` .


#### 14.4.7.3. Google Compute Engine




Use the following procedure to configure a Google-sourced inventory:

**Procedure**

1. From the navigation panel, selectAutomation Execution→Infrastructure→Inventories.
1. Select the inventory name you want a source to and click the **Sources** tab.
1. ClickCreate source.
1. In the **Add new source** page, select **Google Compute Engine** from the **Source** list.
1. The **Create source** window expands with the required **Credential** field. Choose from an existing GCE Credential. For more information, see [Managing user credentials](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-credentials) .
1. Optional: You can specify the verbosity, host filter, enabled variables or values, and update options as described in [Adding a source](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#proc-controller-add-source) .
1. Use the **Source Variables** field to override variables used by the `    gcp_compute` inventory plugin. Enter variables by using either JSON or YAML syntax. Use the radio button to toggle between the two. For more information about these variables, see the [gcp_compute inventory plugin documentation](https://console.redhat.com/ansible/automation-hub/repo/published/google/cloud/content/inventory/gcp_compute) .


#### 14.4.7.4. Microsoft Azure resource manager




Use the following procedure to configure an Microsoft Azure Resource Manager-sourced inventory.

**Procedure**

1. From the navigation panel, selectAutomation Execution→Infrastructure→Inventories.
1. Select the inventory name you want a source to and click the **Sources** tab.
1. ClickCreate source.
1. In the **Create source** page, select **Microsoft Azure Resource Manager** from the **Source** list.
1. Enter the following details in the additional fields:
1. Optional: **Credential** : Choose from an existing Azure Credential. For more information, see [Managing user credentials](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-credentials) .
1. Optional: You can specify the verbosity, host filter, enabled variables or values, and update options as described in [Adding a source](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#proc-controller-add-source) .
1. Use the **Source variables** field to override variables used by the `    azure_rm` inventory plugin. Enter variables by using either JSON or YAML syntax. Use the radio button to toggle between the two. For more information about these variables, see the [azure_rm inventory plugin documentation](https://console.redhat.com/ansible/automation-hub/repo/published/azure/azcollection/content/inventory/azure_rm) .


#### 14.4.7.5. VMware vCenter




Use the following procedure to configure a VMWare-sourced inventory.

**Procedure**

1. From the navigation panel, selectAutomation Execution→Infrastructure→Inventories.
1. Select the inventory name you want a source to and click the **Sources** tab.
1. ClickCreate source.
1. In the **Create source** page, select **VMware vCenter** from the **Source** list.
1. The **Create source** window expands with additional fields. Enter the following details:


- Optional: **Credential** : Choose from an existing VMware credential. For more information, see [Managing user credentials](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-credentials) .

1. Optional: You can specify the verbosity, host filter, enabled variables or values, and update options as described in [Adding a source](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#proc-controller-add-source) .
1. Use the **Source Variables** field to override variables used by the `    vmware_inventory` inventory plugin. Enter variables by using either JSON or YAML syntax. Use the radio button to toggle between the two. For more information about these variables, see the [vmware_inventory inventory plugin](https://github.com/ansible-collections/community.vmware/blob/main/plugins/inventory/vmware_vm_inventory.py) .


**Troubleshooting**

VMWare properties have changed from lower case to camel case. Automation controller provides aliases for the top-level keys, but lower case keys in nested properties have been discontinued. For a list of valid and supported properties, see [Using Virtual machine attributes in VMware dynamic inventory plugin](https://docs.ansible.com/ansible/4/scenario_guides/vmware_scenarios/vmware_inventory_vm_attributes.html) .


#### 14.4.7.6. VMware ESXi




Use the following procedure to configure a VMWare-ESXI sourced inventory.

**Procedure**

1. From the navigation panel, selectAutomation Execution→Infrastructure→Inventories.
1. Select the inventory name you want to add a source to, and click the **Sources** tab.
1. ClickCreate source.
1. Enter a **Name** for the source (required).
1. In the **Create source** page, select **VMware ESXi** from the **Source** list.
1. The **Create source** window expands with additional fields. Enter the following details:


-  **Credential** : Choose from an existing VMware credential. For more information, see [Managing user credentials](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-credentials) .

1. Use the **Verbosity** menu to select the level of output on any inventory source’s update jobs.
1. Optional: You can specify the host filter, enabled variables or values, and update options as described in [Adding a source](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#proc-controller-add-source) .
1. Use the **Source Variables** field to override variables used by the `    vmware_inventory` inventory plugin. Enter variables by using either JSON or YAML syntax. Use the radio button to toggle between the two.


**Troubleshooting**

VMWare properties have changed from lower case to camel case. Automation controller provides aliases for the top-level keys, but lower case keys in nested properties have been discontinued. For a list of valid and supported properties, see [Using Virtual machine attributes in VMware dynamic inventory plugin](https://docs.ansible.com/ansible/4/scenario_guides/vmware_scenarios/vmware_inventory_vm_attributes.html) .


**Additional resources**

-  [VMware ESxi plugin](https://github.com/ansible-collections/vmware.vmware/blob/main/plugins/inventory/esxi_hosts.py)


#### 14.4.7.7. Red Hat Satellite 6




Use the following procedure to configure a Red Hat Satellite-sourced inventory.

**Procedure**

1. From the navigation panel, selectAutomation Execution→Infrastructure→Inventories.
1. Select the inventory name you want a source to and click the **Sources** tab.
1. ClickCreate source.
1. In the **Create source** page,, select **Red Hat Satellite 6** from the **Source** list.
1. The **Create source** window expands with additional fields. Enter the following details:


- Optional: **Credential** : Choose from an existing Satellite Credential. For more information, see [Managing user credentials](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-credentials) .

1. Optional: You can specify the verbosity, host filter, enabled variables or values, and update options as described in [Adding a source](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#proc-controller-add-source) .
1. Use the **Source Variables** field to specify parameters used by the `    foreman` inventory source. Enter variables by using either JSON or YAML syntax. Use the radio button to toggle between the two. For more information about these variables, see the [Foreman inventory source](https://docs.ansible.com/ansible/latest/collections/theforeman/foreman/foreman_inventory.html) in the Ansible documentation.


**Troubleshooting**

If you meet an issue with the automation controller inventory not having the "related groups" from Satellite, you might need to define these variables in the inventory source. For more information, see [Red Hat Satellite 6](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-rh-satellite) .


If you see the message, `"no foreman.id" variable(s) when syncing the inventory` , see the solution on the Red Hat Customer Portal at: [https://access.redhat.com/solutions/5826451](https://access.redhat.com/solutions/5826451) . Be sure to login with your customer credentials to access the full article.

#### 14.4.7.8. Red Hat Insights




Use the following procedure to configure a Red Hat Insights-sourced inventory.

**Procedure**

1. From the navigation panel, selectAutomation Execution→Infrastructure→Inventories.
1. Select the inventory name you want a source to and click the **Sources** tab.
1. ClickCreate source.
1. In the **Create source** page, select **Red Hat Insights** from the **Source** list.
1. The **Create source** window expands with additional fields. Enter the following details:


- Optional: **Credential** : Choose from an existing Red Hat Insights Credential. For more information, see [Managing user credentials](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-credentials) .

1. Optional: You can specify the verbosity, host filter, enabled variables or values, and update options as described in [Adding a source](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#proc-controller-add-source) .
1. Use the **Source Variables** field to override variables used by the `    insights` inventory plugin. Enter variables by using either JSON or YAML syntax. Use the radio button to toggle between the two. For more information about these variables, see [insights inventory plugin](https://console.redhat.com/ansible/automation-hub/repo/published/redhat/insights/content/inventory/insights) .


#### 14.4.7.9. OpenStack




Use the following procedure to configure an OpenStack-sourced inventory.

**Procedure**

1. From the navigation panel, selectAutomation Execution→Infrastructure→Inventories.
1. Select the inventory name you want a source to and click the **Sources** tab.
1. ClickCreate source.
1. In the **Create source** page, select **OpenStack** from the **Source** list.
1. The **Create source** window expands with additional fields. Enter the following details:


- Optional: **Credential** : Choose from an existing OpenStack Credential. For more information, see [Managing user credentials](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-credentials) .

1. Optional: You can specify the verbosity, host filter, enabled variables or values, and update options as described in [Adding a source](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#proc-controller-add-source) .
1. Use the **Source Variables** field to override variables used by the `    openstack` inventory plugin. Enter variables by using either JSON or YAML syntax. Use the radio button to toggle between the two. For more information about these variables, see [openstack inventory plugin](https://docs.ansible.com/ansible/latest/collections/openstack/cloud/openstack_inventory.html) .


#### 14.4.7.10. Red Hat Virtualization




Use the following procedure to configure a Red Hat virtualization-sourced inventory.

**Procedure**

1. From the navigation panel, selectAutomation Execution→Infrastructure→Inventories.
1. Select the inventory name you want a source to and click the **Sources** tab.
1. ClickCreate source.
1. In the **Create source** page, select **Red Hat Virtualization** from the **Source** list.
1. The **Create source** window expands with additional fields. Enter the following details:


- Optional: **Credential** : Choose from an existing Red Hat Virtualization Credential. For more information, see [Managing user credentials](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-credentials) .

1. Optional: You can specify the verbosity, host filter, enabled variables or values, and update options as described in [Adding a source](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#proc-controller-add-source) .
1. Use the **Source Variables** field to override variables used by the `    ovirt` inventory plugin. Enter variables by using either JSON or YAML syntax. Use the radio button to toggle between the two. For more information about these variables, see [ovirt inventory plugin](https://console.redhat.com/ansible/automation-hub/repo/published/redhat/rhv/content/inventory/ovirt)


Note
Red Hat Virtualization (ovirt) inventory source requests are secure by default. To change this default setting, set the key `ovirt_insecure` to **true** in `source_variables` , which is only available from the API details of the inventory source at the `/api/v2/inventory_sources/N/` endpoint.



#### 14.4.7.11. Red Hat Ansible Automation Platform




Use the following procedure to configure an automation controller-sourced inventory.

**Procedure**

1. From the navigation panel, selectAutomation Execution→Infrastructure→Inventories.
1. Select the inventory name you want a source to and click the **Sources** tab.
1. ClickCreate source.
1. In the **Create source** page, select **Red Hat Ansible Automation Platform** from the **Source** list.
1. The **Create source** window expands with additional fields. Enter the following details:


- Optional: **Credential** : Choose from an existing Red Hat Ansible Automation Platform Credential. For more information, see [Managing user credentials](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-credentials) .

1. Optional: You can specify the verbosity, host filter, enabled variables or values, and update options as described in [Adding a source](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#proc-controller-add-source) .
1. Use the **Source Variables** field to override variables used by the `    controller` inventory plugin. Enter variables by using either JSON or YAML syntax. Use the radio button to toggle between the two. For more information about these variables, see [Controller inventory plugin](https://console.redhat.com/ansible/automation-hub/repo/published/ansible/controller/content/inventory/controller) . This requires your Red Hat Customer login.


#### 14.4.7.12. Terraform State




This inventory source uses the terraform_state inventory plugin from the [cloud.terraform](https://console.redhat.com/ansible/automation-hub/repo/published/cloud/terraform/content/inventory/terraform_state/) collection. The plugin parses a terraform state file and add hosts for AWS EC2, GCE, and Microsoft Azure instances.

**Procedure**

1. From the navigation panel, selectAutomation Execution→Projects.
1. On the **Projects** page, clickCreate projectto start the **Create project** window.


- Enter the appropriate details according to the steps in [Adding a new project](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#proc-controller-adding-a-project) .

1. From the navigational panel, selectAutomation Execution→Infrastructure→Inventories.
1. Select the inventory that you want to add a source to.
1. In the **Sources** tab, clickCreate source.
1. From theSourcemenu, select **Terraform State** .


- The **Create source** window expands with the optional **Credential** field.

Choose an existing Terraform backend configuration credential. For more information, see [Terraform backend configuration](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#ref-controller-credential-terraform) .



1. Enable the options to **Overwrite** and **Update on launch** .
1. Use the **Source variables** field to override variables used by the `    terraform_state` inventory plugin. Enter variables by using either JSON or YAML syntax. Use the radio button to toggle between the two. For more information about these variables, see the [terraform_state](https://console.redhat.com/ansible/automation-hub/repo/published/cloud/terraform/content/inventory/terraform_state/) file.

The `    backend_type` variable is required by the Terraform State inventory plugin. This should match the remote backend configured in the **Terraform backend credential** . The following is an example Amazon S3 backend:


```
backend_type: s3
```


1. Select an **Execution environment** that has a Terraform binary. This is required for the inventory plugin to run the Terraform commands that read inventory data from the Terraform state file.


Important
Terraform provider for Ansible Automation Platform inventories are managed by Terraform and you must not edit them in Ansible Automation Platform as it can introduce drift to the Terraform deployment.



**Additional resources**

-  [Terraform EE](https://github.com/ansible-cloud/terraform_ee)
-  [Red Hat Ansible Automation Platform provider](https://registry.terraform.io/providers/ansible/aap/latest/docs)


#### 14.4.7.13. OpenShift Virtualization




This inventory source uses a cluster that is able to deploy Red Hat OpenShift Container Platform Virtualization. To configure a Red Hat OpenShift Container Platform Virtualization, you need a virtual machine deployed in a specific namespace and an OpenShift or Kubernetes API Bearer Token credential.

**Procedure**

1. From the navigational panel, selectAutomation Execution→Infrastructure→Inventories.
1. Select the inventory that you want to add a source to.
1. In the **Sources** tab, clickAdd source.
1. From theSourcemenu, select **OpenShift Virtualization** .


- The **Add new source** window expands with the required **Credential** field.

Choose from an existing Kubernetes API Bearer Token credential. For more information, see [OpenShift or Kubernetes API Bearer Token credential type](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#ref-controller-credential-openShift) . In this example, the `        cmv2.engineering.redhat.com` credential is used.



1. You can optionally specify the **Verbosity** , **Host Filter** , **Enabled Variable/Value** , and **Update options** as described in the [Adding a source](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#proc-controller-add-source) steps.
1. Use the **Source Variables** field to override variables used by the `    kubernetes` inventory plugin. Enter variables by using either JSON or YAML syntax. Use the radio button to toggle between the two. For more information about these variables, see the [kubevirt.core.kubevirt inventory source](https://kubevirt.io/kubevirt.core/main/plugins/kubevirt.html#parameters) documentation.

In the following example, the connections variable is used to specify access to a particular namespace in a cluster:


```
---    connections:    - namespaces:      - hao-test
```


1. ClickSaveand then clickSyncto sync the inventory.


#### 14.4.7.14. Using a custom inventory plugin




This describes how to use the `servicenow.itsm` collection inventory plugin to sync inventory on Ansible Automation Platform.

**Procedure**

1. Create and sync a project using a Source Control Git repository that includes the following files:


```
&gt;&gt; requirements.yml    ---    collections: - name: servicenow.itsm            &gt;&gt; inventories/myinventory.now.yml    # Create a file following the example below. It must have a configuration file extension ending in either "now.yml" or "now.yaml".    plugin: servicenow.itsm.now    query:    - os: = Linux Red Hat    - os: = Windows XP    keyed_groups:    - key: os      prefix: os
```

Note
Refer to the official [Ansible documentation](https://console.redhat.com/ansible/automation-hub/repo/published/servicenow/itsm/content/inventory/now/) for detailed guidance on using and configuring the `    servicenow.itsm.now` plugin.




1. Create an inventory by setting the source to **Sourced from a Project** , selecting the new project, and choose `    /(project root)` in the inventory file section.
1. Synchronize the source in the inventory.


#### 14.4.7.15. Export old inventory scripts




Despite the removal of the custom inventory scripts API, the scripts are still saved in the database. Use the following commands to recover the scripts from the database in a format that is suitable for you to subsequently check into source control.

Use the following commands:

```
$ awx-manage export_custom_scripts --filename=my_scripts.tar

Dump of old custom inventory scripts at my_scripts.tar
```

Making use of the output:

```
$ mkdir my_scripts
$ tar -xf my_scripts.tar -C my_scripts
```

The name of the scripts has the form: `<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">&lt;pk&gt;_</span></em></span>&lt;name&gt;` . This is the naming scheme used for project folders.

```
$ ls my_scripts<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">10<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">inventory_script_rawhook _19</span></em></span>_30<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">inventory_script_listenhospital _11</span></em></span>inventory_script_upperorder _1<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">inventory_script_commercialinternet45 _4</span></em></span>inventory_script_whitestring _12<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">inventory_script_eastplant _22</span></em></span>inventory_script_pinexchange _5<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">inventory_script_literaturepossession _13</span></em></span>inventory_script_governmentculture _23<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">inventory_script_brainluck _6</span></em></span>inventory_script_opportunitytelephone _14<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">inventory_script_bottomguess _25</span></em></span>inventory_script_buyerleague _7<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">inventory_script_letjury _15</span></em></span>inventory_script_wallisland _26<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">inventory_script_lifesport _8</span></em></span>random_inventory_script</span></em></span><span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">16<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">inventory_script_wallisland _27</span></em></span>inventory_script_exchangesomewhere _9<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">random_inventory_script</span></em></span>_17</span></em></span>inventory_script_bidstory            _28<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">inventory_script_boxchild _18</span></em></span>p                                    _29__inventory_script_wearstress
```

Each file contains a script. Scripts can be `bash/python/ruby/more` , so the extension is not included. They are all directly executable. Executing the script dumps the inventory data.

```
$ ./my_scripts/<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">11__inventory_script_upperorder {"group</span></em></span>\ud801\udcb0\uc20e\u7b0e\ud81c\udfeb\ub12b\ub4d0\u9ac6\ud81e\udf07\u6ff9\uc17b": {"hosts":
["host_\ud821\udcad\u68b6\u7a51\u93b4\u69cf\uc3c2\ud81f\uddbe\ud820\udc92\u3143\u62c7",
"host_\u6057\u3985\u1f60\ufefb\u1b22\ubd2d\ua90c\ud81a\udc69\u1344\u9d15",
"host_\u78a0\ud820\udef3\u925e\u69da\ua549\ud80c\ude7e\ud81e\udc91\ud808\uddd1\u57d6\ud801\ude57",
"host_\ud83a\udc2d\ud7f7\ua18a\u779a\ud800\udf8b\u7903\ud820\udead\u4154\ud808\ude15\u9711",
"host_\u18a1\u9d6f\u08ac\u74c2\u54e2\u740e\u5f02\ud81d\uddee\ufbd6\u4506"], "vars": {"ansible_host": "127.0.0.1", "ansible_connection":
"local"}}}
```

You can verify functionality with `ansible-inventory` . This gives the same data, but reformatted.

```
$ ansible-inventory -i ./my_scripts/_11__inventory_script_upperorder --list --export
```

In the preceding example, you can `cd` into `my_scripts` and then issue a `git init` command, add the scripts you want, push it to source control, and then create an SCM inventory source in the user interface.

For more information about syncing or using custom inventory scripts, see [Inventory file importing](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/configuring_automation_execution/assembly-inventory-file-importing) in _Configuring automation execution_ .

