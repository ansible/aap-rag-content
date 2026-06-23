# Custom credential types
## Content sourcing from collections

automation controller supports sourcing content for projects from Ansible collections defined in `requirements.yml` files. This is done by configuring Ansible Galaxy credentials at the organization level to define content sources for collection installations.

A "managed" credential type of `kind=galaxy` represents a content source for fetching collections defined in `requirements.yml` when project updates are run. Examples of content sources are galaxy.ansible.com, console.redhat.com, or on-premise automation hub. This new credential type represents a URL and (optional) authentication details necessary to construct the environment variables when a project update runs `ansible-galaxy collection install` as described in the Ansible documentation, [Configuring the ansible-galaxy client](https://docs.ansible.com/projects/ansible/latest/collections_guide/collections_installing.html#configuring-the-ansible-galaxy-client). It has fields that map directly to the configuration options exposed to the Ansible Galaxy CLI, for example, per-server.

An endpoint in the API reflects an ordered list of these credentials at the Organization level:

```
/api/v2/organizations/N/galaxy_credentials/
```
When installations of automation controller migrate existing Galaxy-oriented setting values, post-upgrade proper credentials are created and attached to every Organization. After upgrading to the latest version, every organization that existed before upgrade now has a list of one or more "Galaxy" credentials associated with it.

Additionally, post-upgrade, these settings are not visible (or editable) from the `/api/v2/settings/jobs/` endpoint.

Automation controller continues to fetch roles directly from public Galaxy even if `galaxy.ansible.com` is not the first credential in the list for the organization. The global Galaxy settings are no longer configured at the jobs level, but at the organization level in the user interface.

The organization’s **Create organization** and **Edit organization** windows have an optional **Galaxy credentials** lookup field for credentials of `kind=galaxy`.

![Create organization](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/organizations-galaxy-credentials.png)

It is important to specify the order of these credentials as order sets precedence for the sync and lookup of the content. For more information, see [Creating an organization](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-proc_controller_create_organization#proc-controller-create-organization "Ansible Automation Platform automatically creates a default organization. If you have a self-support level license, you have only the default organization available and cannot delete it.").

For more information about how to set up a project by using collections, see [Using Collections with automation hub](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-ref_projects_collections_support#proc-projects-using-collections-with-hub "Before automation controller can use automation hub as the default source for collections content, you must create an API token in the automation hub UI. You then specify this token in automation controller.").

