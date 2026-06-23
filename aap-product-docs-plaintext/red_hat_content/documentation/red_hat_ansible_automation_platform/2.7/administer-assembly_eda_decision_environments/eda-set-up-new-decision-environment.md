# Create runtime environments for event-driven automation
## Set up a new decision environment

Set up a new decision environment to define the dedicated, containerized runtime (including collections and dependencies) necessary to execute your rulebook activations.

### Before you begin

- You have set up a credential, if necessary. For more information, see the [Setting up credentials](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-proc_eda_set_up_credential#eda-set-up-credential "Create a credential to securely store sensitive data (like tokens and passwords) required for rulebook activations to connect to source plugins or private registries.") section.
- You have pushed a decision environment image to an image repository or you chose to use the `de-minimal`[image](https://catalog.redhat.com/en/software/containers/ansible-automation-platform-26/de-minimal-rhel9/66fed7ad6ae4c44aa5de8c72) located in [registry.redhat.io](http://registry.redhat.io/).

### Procedure

1.  Log in to Ansible Automation Platform.
2.  Navigate to Automation Decisions> (and then)Decision Environments.
3.  Click Create decision environment.
4.  Insert the following:


Name
Insert the name.

Description
This field is optional.

Organization
Select an organization to associate with the decision environment.

Image
This is the full image location, including the container registry, image name, and version tag.

Pull
This optional field defines when the Event-Driven Ansible controller attempts to download (pull) the specified container image from the registry before running an automation rulebook. This setting is crucial for ensuring security, consistency, and efficient use of system resources by controlling when the local image cache is updated or reused.

- **Always pull container before running** - checks the registry for a new version of the image before every use, even if a local copy exists. This ensures that the freshest content is always used, which is critical for security patches, content updates, and staging environments.
- **Only pull the image if not present before running** - checks the local cache of Event-Driven Ansible controller first. If the image is found locally, it is used immediately. A pull from the registry only happens if the image is not found locally. This optimizes performance by avoiding unnecessary downloads and is best for production environments where the content image is stable and faster startup is required.
- **Never pull container before running** - never attempts to pull the image from the registry. It only uses an image that has been previously pulled and is present in the local cache. This option guarantees consistency by preventing unintended content changes. It requires the image to be manually pulled to Event-Driven Ansible controller beforehand. If the image isn’t present, the activation fails.

Credential
This field is optional. This is the credential needed to use the decision environment image.

5.  Select Create decision environment.

### Results

Your decision environment is now created and can be managed on the **Decision Environments** page.

After saving the new decision environment, the decision environment’s details page is displayed. From there or the **Decision Environments** list view, you can edit or delete it.
