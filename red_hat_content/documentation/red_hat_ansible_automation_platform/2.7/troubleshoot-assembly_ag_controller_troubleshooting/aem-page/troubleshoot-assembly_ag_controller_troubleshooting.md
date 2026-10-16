+++
template = "docs/aem-title.html"
title = "Troubleshoot automation controller - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/troubleshoot-assembly_ag_controller_troubleshooting"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/troubleshoot-assembly_ag_controller_troubleshooting/", "Troubleshoot automation controller"]]
category = "Troubleshoot"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/troubleshoot-assembly_ag_controller_troubleshooting/aem-page/troubleshoot-assembly_ag_controller_troubleshooting.html"
last_crumb = "Troubleshoot automation controller"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Troubleshoot automation controller"
oversized = "false"
page_slug = "troubleshoot-assembly_ag_controller_troubleshooting"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/troubleshoot-assembly_ag_controller_troubleshooting"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/troubleshoot-assembly_ag_controller_troubleshooting/toc/toc.json"
type = "aem-page"
+++

# Troubleshoot automation controller

Useful troubleshooting information for automation controller.

## Unable to login to automation controller through HTTP

Access to automation controller is intentionally restricted through a secure protocol (HTTPS).

In cases where your configuration is set up to run an automation controller node behind a load balancer or proxy as "HTTP only", and you only want to access it without SSL/TLS (for troubleshooting, for example), you must add the following settings in the `custom.py` file located at `/etc/tower/conf.d` of your automation controller instance:

```
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
```

If you change these settings to `false` it enables automation controller to manage cookies and login sessions when using the HTTP protocol.
You must do this on every node of a cluster installation.

To apply the changes, run:

```
automation-controller-service restart
```

## Unable to run a job

If you are unable to run a job from a playbook, review the playbook YAML file. When importing a playbook, either manually or by a source control mechanism, remember that the host definition is controlled by automation controller and should be set to `hosts:all`.

## External system interference and job failures

Resolve intermittent Ansible Automation Platform job failures, node instability, and performance issues by configuring external security tools, path exclusions, and audit logging settings on infrastructure nodes.

If you experience intermittent job failures or delays, particularly with the following symptoms:

- The running ansible process received a shutdown signal
- Worker did not produce events or streaming was aborted
- Job reaped due to instance shutdown
- Nodes toggling between **Available** and **Unavailable** states
- 503 Service Unavailable or 403 Forbidden errors
- Database connection failures (`psycopg.OperationalError`)
- Kernel messages: `audit: backlog limit exceeded`
- Unexplained CPU load spikes or system freezes lasting 60+ seconds

Investigate external security and monitoring tools on your Ansible Automation Platform infrastructure nodes. Consult your security team to whitelist Ansible Automation Platform execution paths and consider reducing the verbosity of audit logging on those systems.

### Diagnostic checklist

- Review antivirus/EDR logs for Ansible Automation Platform process quarantine or termination events
- Check monitoring agent CPU and memory overhead on Ansible Automation Platform nodes
- Examine `auditd` logs for excessive system call logging during job failures
- Verify Ansible Automation Platform paths are excluded from real-time security scanning
- Monitor disk I/O during job execution for bottlenecks caused by audit logging
- Consult Red Hat Solution [Red Hat Solution 7144721](https://access.redhat.com/solutions/7144721) if issues persist

## External system interference and job failures: mitigation

To prevent resource contention and performance issues, configure security scanning exclusions, monitoring agent settings, and audit logging rules on Ansible Automation Platform control and execution nodes.

### Procedure

1. Add the following paths to antivirus and EDR scanning exclusions:

  - `/var/lib/awx/`
  - `/var/lib/receptor/`
  - `/var/run/receptor/`
  - `/var/log/tower/`
  - `/tmp` (and any other temporary directories configured for Ansible Automation Platform)

2. Configure monitoring agents to exclude Ansible Automation Platform process monitoring or reduce sampling frequency on Ansible Automation Platform nodes.
3. Review `auditd` rules on AAP nodes and disable overly granular system call auditing that may create disk I/O contention.
  
  Note:
  `auditd` is configured on RHEL by default. If it is configured on your systems, this step is applicable.

## Playbooks do not show up in the Job Template list

If your playbooks are not showing up in the **Job Template** list, check the following:

- Ensure that the playbook is valid YML and can be parsed by Ansible.
- Ensure that the permissions and ownership of the project path (`/var/lib/awx/projects`) is set up so that the "awx" system user can view the files.
Run the following command to change the ownership:

```
chown awx -R /var/lib/awx/projects/
```

## Playbook stays in pending

If you are attempting to run a playbook job and it stays in the `Pending` state indefinitely, try the following actions:

- Ensure that all supervisor services are running through `supervisorctl status`.
- Ensure that the `/var/ partition` has more than 1 GB of space available.
Jobs do not complete with insufficient space on the `/var/` partition.
- Run `automation-controller-service restart` on the automation controller server.

If you continue to have issues, run `sosreport` as root on the automation controller server, then file a [support request](http://support.ansible.com/) with the result.

## Prevent installation failures when reusing an external database

When reusing an external database for clustered installations, you must manually clear the database before performing subsequent installations.

Instances have been reported where reusing the external database during subsequent installation of nodes causes installation failures.

**Example**

You perform a clustered installation.
Then, you need to do this again and perform a second clustered installation reusing the same external database, only this subsequent installation failed.

When setting up an external database that has been used in a prior installation, you must manually clear the database used for the clustered node before any additional installations can succeed.

## View private EC2 VPC instances in the automation controller inventory

By default, automation controller only shows instances in a VPC that have an Elastic IP (EIP) associated with them.

### Procedure

1. From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Inventories.
2. Select the inventory that has the **Source** set to **Amazon EC2**, and click the **Source** tab. In the **Source Variables** field, enter:

```
vpc_destination_variable: private_ip_address
```

3. Click Save and trigger an update of the group.

### Results

Once you complete these steps, you can see your VPC instances.

Note:

Automation controller must be running inside the VPC with access to those instances if you want to configure them.
