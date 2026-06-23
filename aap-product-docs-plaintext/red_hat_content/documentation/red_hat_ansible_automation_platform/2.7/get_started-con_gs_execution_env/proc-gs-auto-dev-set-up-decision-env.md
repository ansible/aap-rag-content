# Create automation runtimes with execution and decision environments
## Set up a new decision environment

The following steps describe how to import a decision environment into the platform.

### Before you begin

- You have set up any necessary credentials. For more information, see [Setting up credentials](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-proc_eda_set_up_credential#eda-set-up-credential "Create a credential to securely store sensitive data (like tokens and passwords) required for rulebook activations to connect to source plugins or private registries.").
- You have pushed a decision environment image to an image repository or you chose to use the image `de-supported` provided at [registry.redhat.io](http://registry.redhat.io/).

### About this task

### Procedure

1.  Navigate to Automation Decisions> (and then)Decision Environments.
2.  Click Create decision environment.
3.  Enter the following:


Name
Insert the name.

Description
This field is optional.

Image
This is the full image location, including the container registry, image name, and version tag.

Credential
This field is optional. This is the token needed to use the decision environment image.

4.  Select Create decision environment.

### Results

Your decision environment is now created and can be managed on the **Decision Environments** page.

After saving the new decision environment, the decision environment’s details page is displayed. From there or the **Decision Environments** list view, you can edit or delete it.
