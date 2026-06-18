# Host execution environment wizard templates in a private Git repository

Copy the EE Builder wizard templates from the public Ansible GitHub repository to a private repository for use in private or air-gapped environments.

## Before you begin

- You have access to a system that can reach `github.com` to download template files (or you have already obtained the files).
- You have a private Git repository accessible from your deployment environment.
- For dynamic plugins in air-gapped environments: you have access to an internal container registry for mirroring GitHub Container Registry images.

## About this task

The EE Builder wizard uses templates to guide users through creating execution environment definitions. By default, these templates are loaded from the public `ansible/ansible-rhdh-templates` repository on GitHub. If your deployment cannot reach GitHub — or you want to host templates in a private repository — copy the template files and update the catalog locations to point to your internal source.

After updating the catalog locations, import the templates into automation portal. See [Import an existing EE definition](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_create_ee_definition#proc-import-ee-template "Import a previously generated execution environment template to make it available for other users to create definitions with the same defaults.") for the import procedure.

## Procedure

1.  From a connected system, download the template YAML files:

- [ee-start-from-scratch.yaml](https://github.com/ansible/ansible-rhdh-templates/blob/v2.0.0/templates/ee-start-from-scratch.yaml)
- [ee-cloud-automation.yaml](https://github.com/ansible/ansible-rhdh-templates/blob/v2.0.0/templates/ee-cloud-automation.yaml)
- [ee-network-automation.yaml](https://github.com/ansible/ansible-rhdh-templates/blob/v2.0.0/templates/ee-network-automation.yaml)

2.  Push the template files to a private Git repository accessible from your deployment environment.
3.  In your Helm chart configuration, replace the public GitHub URLs with your private repository URLs:


```
catalog:
locations:
- type: url
target: https://git.internal.example.com/ansible-templates/ee-start-from-scratch.yaml
rules:
- allow: [Template]
- type: url
target: https://git.internal.example.com/ansible-templates/ee-cloud-automation.yaml
rules:
- allow: [Template]
- type: url
target: https://git.internal.example.com/ansible-templates/ee-network-automation.yaml
rules:
- allow: [Template]
```

4.  For Networking Automation and Cloud Automation templates: ensure the domain-specific collections they reference are available from a configured content source (private automation hub or internal Git repository).
5.  Apply the configuration. See [Apply configuration changes](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_apply_configuration_changes "Apply configuration changes after modifying your Helm chart values or RHEL appliance configuration file for execution environment builder.").
6.  Import the templates into automation portal:
1.  Navigate to **Execution Environments > Create**.
2.  Open the kebab menu and select **Import Template**.
3.  Paste the URL to the template file in your private Git repository.
4.  Click **Analyze**, then **Import**.
Alternatively, templates added to `catalog.locations` in the Helm chart load automatically without manual import.

## Results

1. Log in to automation portal and navigate to **Execution Environments > Create**.
2. Verify that the templates loaded from your private repository appear.

## What to do next

**Additional considerations for private or air-gapped environments**

- **EE image destination:** Private automation hub is the target registry for pushing built EE images. Configure the build registry in the execution environment builder wizard or template defaults to point to your private automation hub instance.

- **Dynamic plugins:** Automation portal dynamic plugins are installed from GitHub Container Registry. In air-gapped environments, mirror the required plugin images to an internal container registry. See [Install in an air-gapped environment](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_deploy_rhel_appliance_disconnected "Deploy the Ansible automation portal RHEL appliance in a disconnected or air-gapped environment where the appliance has no access to external registries or the internet.") in the Installing Ansible automation portal on OpenShift Container Platform guide.

- Mirror content sources (private automation hub, internal Git) for collection discovery.

- Configure proxy settings and CA certificates if your environment requires them for outbound connections. See Configuring proxy settings and Adding custom CA certificates in the Installing Ansible automation portal on OpenShift Container Platform guide.

- If your internal Git hosts or registries use self-signed certificates, two separate settings apply:
* `checkSSL: false` — applies to `ansibleGitContents` content discovery providers (see [Configure collection discovery sources](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_configure_collection_discovery "Configure Git content discovery and private automation hub collection discovery so that Ansible collections are available in execution environment builder and the collection catalog.")). Controls TLS verification when crawling Git repositories for `galaxy.yml` files.
* `skipTlsVerifyForHosts` — applies to the CI activities page and other catalog interactions with Git hosts. Controls TLS verification when fetching workflow run data and repository metadata.

These settings serve different purposes. You may need to configure both if your internal hosts use self-signed certificates:



```
catalog:
ansible:
skipTlsVerifyForHosts:
- git.internal.example.com
- registry.internal.example.com
```
