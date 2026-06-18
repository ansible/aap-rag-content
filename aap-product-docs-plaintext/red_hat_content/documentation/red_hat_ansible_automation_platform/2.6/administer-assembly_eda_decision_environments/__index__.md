# Create runtime environments for event-driven automation

Decision environments are container images that run Ansible rulebooks. They create a common language for communicating automation dependencies, and give a standard way to build and distribute the automation environment.

You can find the default decision environment in the *Ansible Rulebook*.

To create your own decision environment, see *Install Ansible Builder to create or edit execution environments* and *Build a custom decision environment for Event-Driven Ansible*. Refer to the Related Links section for more details.

## Supported event sources and filters

The capabilities of your decision environment are largely defined by the event sources and filters included in your container image. Event sources serve as the foundation for {EDAcontroller}, determining where your rulebooks receive incoming signals.

Selecting compatible sources is critical for successful deployment, as availability can vary—some sources are exclusive to the web-based Event-Driven Ansible controller, while others are optimized for the `ansible-rulebook` command-line interface (CLI).

When building your decision environments, the `de-minimal` image provides a curated set of supported plugins designed to ensure stability and compatibility. However, as the ecosystem evolves, plugin namespaces have been updated to reflect their specific collection origins (for example, migrating from `ansible.eda` to specific cloud collections). To ensure your rulebooks remain functional, verify that your definitions align with the latest plugin naming conventions.

The following table lists the supported plugins in the `de-minimal` image, including their plugin type and any associated deprecated names:

*Table 1. Supported event sources and filters*

| <br>Plugin name                     | <br>Event filter | <br>Deprecated name                 |
| ----------------------------------- | ---------------- | ----------------------------------- |
| `eda.builtin.dashes_to_underscores` | <br>Event filter | `ansible.eda.dashes_to_underscores` |
| `eda.builtin.event_splitter`        | <br>Event filter |                                     |
| `eda.builtin.generic`               | <br>Event source | `ansible.eda.generic`               |
| `eda.builtin.insert_hosts_to_meta`  | <br>Event filter | `ansible.eda.insert_hosts_to_meta`  |
| `eda.builtin.insert_meta_info`      | <br>Event filter |                                     |
| `eda.builtin.json_filter`           | <br>Event filter | `ansible.eda.json_filter`           |
| `eda.builtin.normalize_keys`        | <br>Event filter | `ansible.eda.normalize_keys`        |
| `eda.builtin.pg_listener`           | <br>Event source | `ansible.eda.pg_listener`           |
| `eda.builtin.range`                 | <br>Event source | `ansible.eda.range`                 |
| `eda.builtin.webhook`               | <br>Event source | `ansible.eda.webhook`               |


The following event sources have been made available in dedicated collections. The original `ansible.eda` names are currently supported as deprecated plugins in `de-minimal`, but you must transition to the new `de-supported` versions to ensure long-term compatibility and overall improvements:

*Table 2. `de\-supported` event sources*

| <br>Event source (in `de-supported`)   | <br>Deprecated name (in `de-minimal`) |
| -------------------------------------- | ------------------------------------- |
| `amazon.aws.aws_cloudtrail`            | `ansible.eda.aws_cloudtrail`          |
| `amazon.aws.aws_sqs_queue`             | `ansible.eda.aws_sqs_queue`           |
| `azure.azcollection.azure_service_bus` | `ansible.eda.azure_service_bus`       |


In addition, the `de-minimal` image currently provides event sources that are not supported, and will be removed in a future release:

- `ansible.eda.file`
- `ansible.eda.file_watch`
- `ansible.eda.journald`
- `ansible.eda.tick`
- `ansible.eda.url_check`

## Build a custom decision environment for Event-Driven Ansible

Customize a decision environment container image to ensure your rulebook activations run with the precise, custom-maintained collections and dependencies they require.

### Before you begin

- Ansible Automation Platform > = 2.5
- Event-Driven Ansible
- Ansible Builder > = 3.0


Important:

- Use the correct Event-Driven Ansible controller decision environment in Ansible Automation Platform to prevent rulebook activation failure.   * If you want to connect Event-Driven Ansible controller to Ansible Automation Platform 2.4, you must use `registry.redhat.io/ansible-automation-platform-24/de-minimal-rhel9:latest` (recommended) or `registry.redhat.io/ansible-automation-platform-24/de-minimal-rhel8:latest`
* If you want to connect Event-Driven Ansible controller to Ansible Automation Platform 2.5, you must use `registry.redhat.io/ansible-automation-platform-25/de-minimal-rhel9:latest` (recommended) or `registry.redhat.io/ansible-automation-platform-25/de-minimal-rhel8:latest`
* If you want to connect Event-Driven Ansible controller to Ansible Automation Platform 2.6, you must use `registry.redhat.io/ansible-automation-platform-26/de-minimal-rhel9:latest`

### Procedure

1.  Use `de-minimal` as the base image with Ansible Builder to build your custom decision environments. This image is built from a base image provided by Red Hat at [Ansible Automation Platform minimal decision environment](https://catalog.redhat.com/software/containers/ansible-automation-platform-25/de-minimal-rhel9/650a5672a370728c710acaab). Important:
The `ansible.eda` collection is already installed in the `de-minimal `base image. To prevent Ansible Builder from attempting to reinstall it, add `ansible.eda` to the `exclude.all_from_collections` list as shown in the following examples.

The following is an example of the Ansible Builder definition file that uses `de-minimal` as a base image to build a custom decision environment with the ansible.eda collection:

```
version: 3

images:
base_image:
name: 'registry.redhat.io/ansible-automation-platform-25/de-minimal-rhel9:latest'

dependencies:
galaxy:
collections:
- name: servicenow.itsm
python_interpreter:
package_system: "python3.12"
exclude:
all_from_collections:
# ansible.eda is already installed in de-minimal
- ansible.eda

options:
package_manager_path: /usr/bin/microdnf
```

2.  Optional: If you need other Python packages or RPMs, add the following to a single definition file:


```
version: 3

images:
base_image:
name: 'registry.redhat.io/ansible-automation-platform-25/de-minimal-rhel9:latest'

dependencies:
galaxy:
collections:
- name: servicenow.itsm
python:
- six
- psutil
python_interpreter:
package_system: "python3.12"
exclude:
all_from_collections:
# ansible.eda is already installed in de-minimal
- ansible.eda

options:
package_manager_path: /usr/bin/microdnf
```

## Set up a new decision environment

Set up a new decision environment to define the dedicated, containerized runtime (including collections and dependencies) necessary to execute your rulebook activations.

### Before you begin

- You have set up a credential, if necessary. For more information, see the [Setting up credentials](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-proc_eda_set_up_credential#eda-set-up-credential "Create a credential to securely store sensitive data (like tokens and passwords) required for rulebook activations to connect to source plugins or private registries.") section.
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
