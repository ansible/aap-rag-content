# Set up your container repository

When you set up your container repository, you can add a description, include a README, add teams that can access the repository, and tag automation execution environments.

Your container repository for Private Automation Hub is where execution environments are stored, signed, and retrieved by automation controllers.

## Add a README to your container repository

Add a README to your container repository to provide instructions to your users on how to work with the container. Automation hub container repositories support Markdown for creating a README. By default, the README is empty.

### Before you begin

- You have permissions to change containers.

### Procedure

1.  Log in to Ansible Automation Platform.
2.  From the navigation panel, select Automation Content> (and then)Execution Environments.
3.  Select your execution environment.
4.  On the **Detail** tab, click Add.
5.  In the **Raw Markdown** text field, enter your README text in Markdown.
6.  Click Save when you are finished.

### What to do next

After you add a README, you can edit it at any time by clicking Edit and repeating steps 4 and 5.

## Provide access to your automation execution environments

Provide users with access to your automation execution environments by adding them to a team. Then, modify the permissions the team can have to a particular execution environment.

### Before you begin

- You have **change container namespace** permissions.

### Procedure

1.  Log in to Ansible Automation Platform.
2.  From the navigation panel, select Automation Content> (and then)Execution Environments.
3.  Select your automation execution environment.
4.  From the **Team Access** tab, click Add roles.
5.  Select the team or teams to which you want to grant access and click Next.
6.  Select the roles that you want to add to this execution environment and click Next.
7.  Click Finish.

## Tag container images

Tag automation execution environments to add an additional name to automation execution environments stored in your automation hub container repository. If no tag is added to an automation execution environment, automation hub defaults to `latest` for the name.

### Before you begin

- You have **change automation execution environment tags** permissions.

### Procedure

1.  From the navigation panel, select Automation Content> (and then)Execution Environments.
2.  Select your automation execution environments.
3.  Click the **Images** tab.
4.  Click the More Actions icon **⋮**, and click Manage tags.
5.  Add a new tag in the text field and click Add.
6.  Optional: Remove **current tags** by clicking x on any of the tags for that image.

### Results

- Click the **Activity** tab and review the latest changes.

## Create a credential

To pull automation execution environments images from a password or token-protected registry, you must create a credential.

### About this task

In earlier versions of Ansible Automation Platform, you were required to deploy a registry to store execution environment images. On Ansible Automation Platform 2.0 and later, the system operates as if you already have a remote registry up and running. To store execution environment images, add the credentials of only your selected remote registries.

### Procedure

1.  Log in to Ansible Automation Platform.
2.  From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Credentials.
3.  Click Create credential to create a new credential.
4.  Enter an authorization **Name**, **Description**, and **Organization**.
5.  In the **Credential Type** drop-down, select **Container Registry**.
6.  Enter the **Authentication URL**. This is the remote registry address.
7.  Enter the **Username** and **Password or Token** required to log in to the remote registry.
8.  Optional: To enable SSL verification, select **Verify SSL**.
9.  Click Create credential.
