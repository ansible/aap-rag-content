# 3. Getting started as an automation developer
## 3.8. Build and use an execution environment
### 3.8.2. Adding an execution environment to a job template

After you have built an execution environment, use it to run jobs. To do so, first associate the execution environment with a job template.

Use the following procedure to add an execution environment to a job template.

**Prerequisites**

- An execution environment created using `ansible-builder` as described in [Using Ansible Builder](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/creating_and_using_execution_environments/assembly-using-builder).
- Organization administrator privileges (if the execution environment is associated with an organization).
- A credential with a username, host, and password (if assigned to the execution environment).

**Procedure**

1. From the navigation panel, select Automation Execution → Infrastructure → Execution Environments.

2. Click Create execution environment to create an execution environment.

3. Enter the appropriate details into the following fields:


1. **Name** (required): Enter a name for the execution environment.

2. **Image** (required): Enter the image name. The image name requires its full location (repository), the registry, image name, and version tag, as in the following example: `quay.io/ansible/awx-ee:latestrepo/project/image-name:tag`

3. Optional: **Pull**: Choose the type of pull when running jobs:


1. **Always pull container before running**: Pulls the latest image file for the container.

2. **Only pull the image if not present before running**: Only pulls the latest image if none are specified.

3. **Never pull container before running**: Never pull the latest version of the container image.


Note
If you do not set a type for pull, the value defaults to **Only pull the image if not present before running**.

4. Optional: **Description**: Enter an optional description.

5. Optional: **Organization**: Assign the organization to specifically use this execution environment. To make the execution environment available for use across multiple organizations, leave this field blank.

6. **Registry credential**: If the image has a protected container registry, provide the credential to access it.

4. Click Create execution environment. Your newly added execution environment is ready to be used in a job template.

5. To add an execution environment to a job template, navigate to Automation Execution → Templates and select your template.


1. Click Edit template and specify your execution environment in the field labeled **execution environment**.

**Verification**

After you add an execution environment to a job template, the template is listed in the **Templates** tab in your execution environment details.

