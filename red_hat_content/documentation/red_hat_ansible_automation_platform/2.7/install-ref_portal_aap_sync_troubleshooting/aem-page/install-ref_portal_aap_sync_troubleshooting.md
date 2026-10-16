+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-ref_portal_aap_sync_troubleshooting"
title = "Troubleshoot Ansible Automation Platform synchronization - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-install_automation_portal_on_openshift_container_platform/", "Install automation portal on OpenShift Container Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-ref_portal_aap_sync_troubleshooting/aem-page/install-ref_portal_aap_sync_troubleshooting.html"
last_crumb = "Troubleshoot Ansible Automation Platform synchronization"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Troubleshoot Ansible Automation Platform synchronization"
oversized = "false"
page_slug = "install-ref_portal_aap_sync_troubleshooting"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-ref_portal_aap_sync_troubleshooting"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-ref_portal_aap_sync_troubleshooting/toc/toc.json"
type = "aem-page"
+++

# Troubleshoot Ansible Automation Platform synchronization

Review common issues, symptoms, and solutions if synchronization between Ansible Automation Platform and Ansible automation portal does not function as expected.

## No Job Templates appearing in portal

**Issue:** Expected Job Templates are missing from the portal interface.

**Solutions:**

- Verify the `surveyEnabled` setting in your Helm values file matches the status of your Job Templates.
- Confirm the `labels` filter includes the correct, approved Ansible Automation Platform Label names.
- Try temporarily removing filters to confirm if the Job Templates appear without restrictions.
- Verify the Ansible Automation Platform Organization name spelling is exact (it is case-sensitive).
- Check Ansible Automation Platform connectivity and the configured token permissions.

## No Users or Teams appearing in portal

**Issue:** Expected users or teams are missing from the portal interface.

**Solutions:**

- Check Ansible Automation Platform connectivity and the configured token permissions.
- Verify the Ansible Automation Platform Organization name matches exactly.
- Review the configured synchronization schedule and check system logs.
- Ensure users have the proper organization or team memberships within Ansible Automation Platform.

## Slow synchronization

**Issue:** Synchronization takes too long to complete or times out.

**Symptoms:**

- Timeouts during synchronization.
- Timeout errors appear in the logs.

**Solutions:**

- Increase the `timeout` value in the synchronization schedule.
- Reduce the synchronization `frequency` (sync less often).
- Add more specific filters to the Job Templates configuration to reduce the overall count of entities processed.
- For large organizations, increase the `timeout` specifically for the identity sync (`orgsUsersTeams`).

## Wrong Ansible Automation Platform organization name

**Issue:** The portal displays unexpected Job Templates, users, or teams.

**Symptoms:**

- Expected Job Templates do not appear.
- Incorrect templates appear.
- Users or teams are missing, or the wrong ones are present.

**Solutions:**

- Verify the Ansible Automation Platform Organization name spelling is exact (it is case-sensitive).
- Check the organization names in Ansible Automation Platform itself.
- Ensure the configured organization exists in Ansible Automation Platform.
