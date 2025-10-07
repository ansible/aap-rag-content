# 3. Getting started as an automation developer
## 3.7. Build and use an execution environment
### 3.7.2. Adding an execution environment to a job template




**Prerequisites**

- An execution environment must have been created using ansible-builder as described in [Using Ansible Builder](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/creating_and_using_execution_environments/assembly-using-builder) . When an execution environment has been created, you can use it to run jobs. Use the automation controller UI to specify the execution environment to use in your job templates.
- Depending on whether an execution environment is made available for global use or tied to an organization, you must have the appropriate level of administrator privileges to use an execution environment in a job. Execution environments tied to an organization require Organization administrators to be able to run jobs with those execution environment.
- Before running a job or job template that uses an execution environment that has a credential assigned to it, ensure that the credential has a username, host, and password.


**Procedure**

1. From the navigation panel, selectAutomation Execution→Infrastructure→Execution Environments.
1. ClickCreate execution environmentto create an execution environment.
1. Enter the appropriate details into the following fields:


1.  **Name** (required): Enter a name for the execution environment.
1.  **Image** (required): Enter the image name. The image name requires its full location (repository), the registry, image name, and version tag, as in the following example: `        quay.io/ansible/awx-ee:latestrepo/project/image-name:tag`
1. Optional: **Pull** : Choose the type of pull when running jobs:


1.  **Always pull container before running** : Pulls the latest image file for the container.
1.  **Only pull the image if not present before running** : Only pulls the latest image if none are specified.
1.  **Never pull container before running** : Never pull the latest version of the container image.

Note
If you do not set a type for pull, the value defaults to **Only pull the image if not present before running** .





1. Optional: **Description** : Enter an optional description.
1. Optional: **Organization** : Assign the organization to specifically use this execution environment. To make the execution environment available for use across multiple organizations, leave this field blank.
1.  **Registry credential** : If the image has a protected container registry, provide the credential to access it.

1. ClickCreate execution environment. Your newly added execution environment is ready to be used in a job template.
1. To add an execution environment to a job template, navigate toAutomation Execution→Templatesand select your template. ..ClickEdit templateand specify your execution environment in the field labeled **execution environment** .


**Verification**

After you add an execution environment to a job template, the template is listed in the **Templates** tab in your execution environment details.


