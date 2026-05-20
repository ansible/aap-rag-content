# 3. Manage containers in private automation hub
## 3.5. Pulling images from a container repository
### 3.5.1. Pulling an image

You can pull an execution environment from your private automation hub remote registry to make a copy to your local machine.

**Prerequisites**

- You must have permission to view and pull from a private container repository.
- If you are pulling automation execution environments from a password or token-protected registry, [create a credential](#proc-create-credential "3.4.4.&nbsp;Creating a credential") first.

**Procedure**

1. From the navigation panel, select Automation Content → Execution Environments.
2. Select your automation execution environments.
3. In the **Pull this image** entry, click Copy to clipboard.
4. Paste and run the command in your terminal.

**Verification**

- Run `podman images` to view images on your local machine.

