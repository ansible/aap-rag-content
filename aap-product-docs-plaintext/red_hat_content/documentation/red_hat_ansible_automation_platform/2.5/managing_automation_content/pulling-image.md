# 3. Manage containers in private automation hub
## 3.5. Pulling images from a container repository
### 3.5.1. Pulling an image




You can pull automation execution environments from the automation hub remote registry to make a copy to your local machine.

**Prerequisites**

- You must have permission to view and pull from a private container repository.


**Procedure**

1. If you are pulling automation execution environments from a password or token-protected registry, [create a credential](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/managing_automation_content/index#proc-create-credential) before pulling the automation execution environments.
1. From the navigation panel, selectAutomation Content→Execution Environments.
1. Select your automation execution environments.
1. In the **Pull this image** entry, clickCopy to clipboard.
1. Paste and run the command in your terminal.


**Verification**

- Run `    podman images` to view images on your local machine.


