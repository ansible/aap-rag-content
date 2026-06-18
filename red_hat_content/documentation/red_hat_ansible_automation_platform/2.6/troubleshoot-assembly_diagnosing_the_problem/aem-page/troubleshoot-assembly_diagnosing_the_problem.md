+++
title = "Collect configuration and diagnostic information - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/troubleshoot-assembly_diagnosing_the_problem"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/troubleshoot-assembly_diagnosing_the_problem/", "Collect configuration and diagnostic information"]]
category = "Troubleshoot"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/troubleshoot-assembly_diagnosing_the_problem/aem-page/troubleshoot-assembly_diagnosing_the_problem.html"
last_crumb = "Collect configuration and diagnostic information"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Collect configuration and diagnostic information"
oversized = "false"
page_slug = "troubleshoot-assembly_diagnosing_the_problem"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/troubleshoot-assembly_diagnosing_the_problem"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/troubleshoot-assembly_diagnosing_the_problem/toc/toc.json"
type = "aem-page"
+++

# Collect configuration and diagnostic information

To start troubleshooting Ansible Automation Platform, use the `must-gather` command on OpenShift Container Platform or the `sos` utility on a VM-based installation to collect configuration and diagnostic information. You can attach the output of these utilities to your support case.

## Troubleshoot Ansible Automation Platform on OpenShift Container Platform by using the must-gather command

The `oc adm must-gather` command line interface (CLI) command collects information from your Ansible Automation Platform installation deployed on OpenShift Container Platform. It gathers information that is often needed for debugging issues, including resource definitions and service logs.

### Before you begin

- The OpenShift CLI (`oc`) is installed.

### About this task

Running the `oc adm must-gather` CLI command creates a new directory containing the collected data that you can use to troubleshoot or attach to your support case.

If your OpenShift environment does not have access to `registry.redhat.io` and you cannot run the `must-gather` command, then run the `oc adm inspect` command instead.

### Procedure

1.  Log in to your cluster:
  

```
oc login <openshift_url>
```

2.  Run one of the following commands based on your level of access in the cluster:

  - Run `must-gather` across the entire cluster:

```
oc adm must-gather --image=registry.redhat.io/ansible-automation-platform-26/aap-must-gather-rhel9 --dest-dir <dest_dir>
```
    * `--image` specifies the image that gathers data
    * `--dest-dir` specifies the directory for the output

  - Run `must-gather` for a specific namespace in the cluster:

```
oc adm must-gather --image=registry.redhat.io/ansible-automation-platform-26/aap-must-gather-rhel9 --dest-dir <dest_dir> -- /usr/bin/ns-gather <namespace>
```
    * `-- /usr/bin/ns-gather` limits the `must-gather` data collection to a specified namespace

3.  To attach the `must-gather` archive to your support case, create a compressed file from the `must-gather` directory created before and attach it to your support case.   - For example, on a computer that uses a Linux operating system, run the following command, replacing `<must-gather-local.5421342344627712289/>` with the `must-gather` directory name:

```
$ tar cvaf must-gather.tar.gz <must-gather.local.5421342344627712289/>
```

## Troubleshoot Ansible Automation Platform on VM-based installations by generating an sos report

The `sos` utility collects configuration, diagnostic, and troubleshooting data from your Ansible Automation Platform on a VM-based installation.

For more information about installing and using the `sos` utility, see [Generating an sos report for technical support](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/getting_the_most_from_your_support_experience/index#generating-an-sos-report-for-technical-support_getting-the-most-from-your-support-experience).
