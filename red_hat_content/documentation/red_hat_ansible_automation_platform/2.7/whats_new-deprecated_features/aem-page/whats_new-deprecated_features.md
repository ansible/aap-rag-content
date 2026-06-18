+++
template = "docs/aem-title.html"
title = "Deprecated features - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-deprecated_features"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-overview_of_redhat_ansible_intro/", "Ansible Automation Platform release notes"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-deprecated_features/aem-page/whats_new-deprecated_features.html"
last_crumb = "Deprecated features"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Deprecated features"
oversized = "false"
page_slug = "whats_new-deprecated_features"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/whats_new-deprecated_features"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-deprecated_features/toc/toc.json"
type = "aem-page"
+++

# Deprecated features

Deprecated features are still included in Ansible Automation Platform 2.7 and continue to be supported during this version's support cycle. However, the feature will be removed in a future release of Ansible Automation Platform and is not recommended for new deployments.

- The `ee-cloud`-services execution environment in Managed Application on Azure
- Python 3.11 and earlier versions are deprecated.


The `ee-cloud-services` execution environment in Managed Application on Azure.

Starting with the release of Ansible Automation Platform (AAP) 2.7, the `ee-cloud-services` execution environment will not be available in new deployments of Ansible Automation Platform on Microsoft Azure. Existing Ansible Automation Platform on Microsoft Azure customers are encouraged to transition their automation workflows to the ee-supported or build a new execution environment; the execution environment will remain until you choose to remove it.

Recommended migration steps

To ensure your automation continues to run smoothly on version 2.7, follow these best practices:

1. Audit Current Job Templates: Identify which Job Templates currently use `ee-cloud-services`.
2. Test with ee-supported: Switch the Execution Environment on a test Job Template to `ee-supported`.
3. Identify Missing Dependencies: If your playbooks fail due to missing Python libraries (e.g., boto3, azure-mgmt-compute) or specific Ansible collections, you will need to create a custom execution environment.
4. Build Custom execution envirnments using Ansible Builder: Use the `ee-supported` or `ee-minimal` image as your base in your execution-environment `.yml` file.


Note:

For Managed Cloud customers, ensure your private automation hub is configured to sync the latest images from the Red Hat ecosystem to maintain access to the supported `ee-supported` images.

Summary of support

- Existing Installs: Upgraded environments may retain `ee-cloud-services` for a limited grace period, but it is considered "End of Life."
- Fresh Installs: `ee-supported & ee-minimal` are the only cloud-focused EE provided out of the box.
- Event-Driven Ansible `ansible.eda.noop` is deprecated and there will not be a replacement.


Python 3.11 and earlier versions are deprecated

Support for Python 3.11 and all earlier versions is being phased out across all Supported Execution Environments and Minimal Execution Environments. To ensure security compliance and access to the latest performance optimizations, users must migrate to Python 3.12 or higher.

Affected environments
Supported Execution Environments

These environments typically include the full standard library and common pre-installed dependencies.

Minimal Execution Environments

These are stripped-down, security-hardened environments used for Custom EE’s.

Action required

Audit custom-built binaries. Python 3.11 minimal layers will no longer receive security vulnerability (CVE) patches.

**Recommendation**: Move to the python:3.12+ or equivalent Minimal EE instance.

Why this is happening

Python 3.12+ offers significant improvements that older environments cannot support, specifically:

- Improved Error Messages: More precise tracebacks for faster debugging.
- Performance: Advancements in the Faster CPython project.


 **Security**: Removal of deprecated APIs and older TLS versions that are increasingly vulnerable.

Automation intelligent assistant
Ansible Lightspeed Intelligent Assistant (ALIA) deprecated in AAP 2.5

- Ansible Lightspeed Intelligent Assistant (ALIA), included as a Technology Preview in Red Hat Ansible Automation Platform 2.5, is deprecated. ALIA in AAP 2.5 is no longer receiving new builds or ongoing security remediation. If you require supported intelligent assistant functionality, upgrade to Red Hat Ansible Automation Platform 2.6 or later. For more information about the support scope of Technology Preview features, see Technology preview in the Red Hat Ansible Automation Platform documentation.(AAP-70906)


Tarball plug-in delivery method for Ansible automation portal and Ansible plug-ins for Red Hat Developer Hub

- The HTTP plug-in registry (tarball) delivery method for Ansible plug-ins for Red Hat Developer Hub and automation portal is deprecated. Use OCI container delivery instead. The tarball delivery method will be removed in a future release of Ansible Automation Platform.
