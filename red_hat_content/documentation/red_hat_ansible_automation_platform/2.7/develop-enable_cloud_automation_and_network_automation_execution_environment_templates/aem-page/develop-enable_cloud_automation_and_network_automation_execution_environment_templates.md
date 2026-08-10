+++
title = "Enable cloud automation and network automation execution environment templates - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-enable_cloud_automation_and_network_automation_execution_environment_templates"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-build_execution_environments_with_the_automation_portal/", "Build execution environments with automation portal"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-enable_cloud_automation_and_network_automation_execution_environment_templates/aem-page/develop-enable_cloud_automation_and_network_automation_execution_environment_templates.html"
last_crumb = "Enable cloud automation and network automation execution environment templates"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Enable cloud automation and network automation execution environment templates"
oversized = "false"
page_slug = "develop-enable_cloud_automation_and_network_automation_execution_environment_templates"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-enable_cloud_automation_and_network_automation_execution_environment_templates"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-enable_cloud_automation_and_network_automation_execution_environment_templates/toc/toc.json"
type = "aem-page"
+++

# Enable cloud automation and network automation execution environment templates

Enable the Cloud Automation and Network Automation wizard templates so that users can create execution environment definitions with preconfigured collections for common automation domains.

## Before you begin

- The collections referenced by the Cloud Automation and Network Automation templates are available in the Collections catalog. These templates do not work unless their preconfigured collections are discoverable and installable by execution environment builder. See [Configure collection discovery sources](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_configure_collection_discovery "Configure Git content discovery and private automation hub collection discovery so that Ansible collections are available in execution environment builder and the collection catalog.").
- Execution environment builder feature is available and the Start from Scratch template is working.
- Your deployment can reach `github.com` to load the template files, or you have hosted copies in a private Git repository. See [Host execution environment wizard templates in a private Git repository](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_host_templates_private_repo "Copy the EE Builder wizard templates from the public Ansible GitHub repository to a private repository for use in private or air-gapped environments.").

## About this task

Execution environment builder includes three wizard templates for creating execution environment definitions. The **Start from Scratch** template is enabled by default. Two additional templates provide preconfigured starting points for common automation domains:

| Template           | File                         | Preconfigured collections                                               |
| ------------------ | ---------------------------- | ----------------------------------------------------------------------- |
| Cloud Automation   | `ee-cloud-automation.yaml`   | `amazon.aws`,`amazon.ai`,`azure.azcollection`,`google.cloud`            |
| Network Automation | `ee-network-automation.yaml` | `cisco.ios`,`cisco.nxos`,`cisco.iosxr`,`arista.eos`,`community.general` |

On current installations, all three templates are enabled by default. On older installations, the Cloud Automation and Network Automation entries may be commented out in the configuration. Use this procedure to verify the templates are enabled and collection discovery is configured.

## Procedure

1.  Open your configuration file for editing.
      **OpenShift — CLI:**

```
$ helm get values <release_name> -n <namespace> -o yaml > current-values.yaml
  $ vi current-values.yaml
```

    **OpenShift — web console:**

    Navigate to **Helm > Installed Helm Charts**. Select your automation portal release and click **Upgrade** to open the values editor.

    **RHEL appliance:**

```
$ sudo vi /etc/portal/configs/app-config/app-config.production.yaml
```

2.  Locate the `catalog.locations` section and verify that the Cloud Automation and Network Automation template entries are present and uncommented.
      All three templates should appear as active entries:

```
catalog:
    locations:
      - type: url
        target: https://github.com/ansible/ansible-rhdh-templates/blob/v2.0.1/templates/ee-start-from-scratch.yaml
        rules:
          - allow: [Template]
      - type: url
        target: https://github.com/ansible/ansible-rhdh-templates/blob/v2.0.1/templates/ee-cloud-automation.yaml
        rules:
          - allow: [Template]
      - type: url
        target: https://github.com/ansible/ansible-rhdh-templates/blob/v2.0.1/templates/ee-network-automation.yaml
        rules:
          - allow: [Template]
```

    If the Cloud Automation or Network Automation entries are commented out (prefixed with `#`), remove the comment markers to enable them. You can enable one or both templates depending on your requirements.

3.  Verify that collection discovery is configured so that the domain-specific collections referenced by these templates are available to users.
      The Cloud Automation and Network Automation templates reference collections from community and certified repositories. Without collection discovery enabled, users must manually specify collection sources when building execution environments.

    To configure collection discovery, see [Configure collection discovery sources](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_configure_collection_discovery "Configure Git content discovery and private automation hub collection discovery so that Ansible collections are available in execution environment builder and the collection catalog.").

4.  Apply the configuration changes. See [Apply configuration changes](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_apply_configuration_changes "Apply configuration changes after modifying your Helm chart values or RHEL appliance configuration file for execution environment builder.").

## Results

After the configuration is applied, the Cloud Automation and Network Automation templates appear alongside the Start from Scratch template when users navigate to **Execution Environments > Create**.

## What to do next

**Verification**

1. Log in to automation portal and navigate to **Execution Environments > Create**.
2. Verify that the newly enabled templates appear alongside the Start from Scratch template.
3. Select a template and confirm that the preconfigured collections are listed in the definition.

**Additional resources**

- [Configure collection discovery sources](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_configure_collection_discovery "Configure Git content discovery and private automation hub collection discovery so that Ansible collections are available in execution environment builder and the collection catalog.")
- [Host execution environment wizard templates in a private Git repository](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_host_templates_private_repo "Copy the EE Builder wizard templates from the public Ansible GitHub repository to a private repository for use in private or air-gapped environments.")
- [Apply configuration changes](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_apply_configuration_changes "Apply configuration changes after modifying your Helm chart values or RHEL appliance configuration file for execution environment builder.")
