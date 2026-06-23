# Package and distribute automation content with collections
## Understand collections for distributing roles
### Publish your collection in private automation hub

Publish your collection by packaging it into a tarball and uploading it to a namespace in private automation hub. This makes the collection available for internal use in Ansible Automation Platform projects.

#### Before you begin

- Package your collection into a tarball.
- Format your collection file name as follows `<my_namespace-my_collection-x.y.z.tar.gz>`.For example, `company_namespace-myapp_network-2.0.0.tar.gz`

#### Procedure

1.  Create a namespace for your collection in private automation hub. See [Creating a namespace](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_working_with_namespaces#proc-create-namespace "Create a namespace to organize collections that your content developers upload to automation hub.") .
2.  Optional: Add information to your namespace. See [Adding additional information and resources to a namespace](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_working_with_namespaces#proc-edit-namespace "Edit the information associated with the namespace and provide resources for your users to accompany collections included in the namespace.") in *Managing automation content* .
3.  Upload your roles collections tarballs to your namespace. See [Uploading collections to your namespaces](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_working_with_namespaces#proc-uploading-collections "Upload internally-developed collections in tar.gz file format to your private automation hub namespace for review and approval by an automation hub administrator.") in *Managing automation content* .
4.  Approve your collection for internal publication. See [Uploading collections to your namespaces](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_managing_private_collections#proc-approve-collection "You can approve collections uploaded to individual namespaces for internal publication and use.") in *Managing automation content*.

#### Use your collection in projects in Red Hat Ansible Automation Platform

To use your collection in automation controller projects, add the collection to a custom execution environment. Then tag the new image and push it to private automation hub.

##### About this task

The following procedure describes the workflow to add a collection to an execution environment. Refer to [Customizing an existing automation executions environment image](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/creating_and_using_execution_environments/assembly-publishing-exec-env#proc-customize-ee-image) for the commands to execute these steps.

##### Procedure

1.  You can pull an execution environment base image from automation hub, or you can add your collection to your own custom execution environment.
2.  Add the collections that you want to include in the execution environment.
3.  Build the new execution environment.
4.  Verify that the collections are in the execution environment.
5.  Tag the image and push it to private automation hub.
6.  Pull your new image into your automation controller instance.
7.  The playbooks that use the roles in your collection must use the fully qualified domain name (FQDN) for the roles.
