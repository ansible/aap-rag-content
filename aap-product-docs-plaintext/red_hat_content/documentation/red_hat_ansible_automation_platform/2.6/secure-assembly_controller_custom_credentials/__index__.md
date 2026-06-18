# Custom credential types

As a system administrator, you can define a custom credential type in a standard format by using a YAML or JSON-like definition. You can define a custom credential type that works in ways similar to existing credential types.

For example, a custom credential type can inject an API token for a third-party web service into an environment variable, for your playbook or custom inventory script to consume.

Custom credentials support the following ways of injecting their authentication information:

- Environment variables
- Ansible extra variables
- File-based templating, which means generating `.ini` or `.conf` files that contain credential values


You can attach one SSH and multiple cloud credentials to a job template. Each cloud credential must be of a different type. Only one of each type of credential is permitted. Vault credentials and machine credentials are separate entities.

Note:

- When creating a new credential type, you must avoid collisions in the `extra_vars`, `env`, and file namespaces.
- Environment variable or extra variable names must not start with `ANSIBLE_` because they are reserved.
- You must have System administrator (superuser) permissions to be able to create and edit a credential type (`CredentialType`) and to be able to view the `CredentialType.injection` field.

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

![Create organization](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/organizations-galaxy-credentials.png)

It is important to specify the order of these credentials as order sets precedence for the sync and lookup of the content. For more information, see [Creating an organization](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-proc_controller_create_organization#proc-controller-create-organization "Ansible Automation Platform automatically creates a default organization. If you have a self-support level license, you have only the default organization available and cannot delete it.").

For more information about how to set up a project by using collections, see [Using Collections with automation hub](/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-ref_projects_collections_support#proc-projects-using-collections-with-hub "Before automation controller can use automation hub as the default source for collections content, you must create an API token in the automation hub UI. You then specify this token in automation controller.").

## Backwards-compatible API considerations

When using the automation controller API, there are some considerations to remember regarding backwards compatibility between version 1 (`api/v1/`) and version 2 (`api/v2/`).

Support for version 2 of the API (`api/v2/`) means a one-to-many relationship for job templates to credentials (including multicloud support).

You can filter credentials the v2 API:

```
curl "https://controller.example.org/api/v2/credentials/?credential_type__namespace=aws"
```
In the V2 Credential Type model, the relationships are defined as follows:

| Machine      | SSH                                                                 |
| ------------ | ------------------------------------------------------------------- |
| <br>Vault    | <br>Vault                                                           |
| <br>Network  | <br>Sets environment variables, for example `ANSIBLE_NET_AUTHORIZE` |
| <br>SCM      | <br>Source Control                                                  |
| <br>Cloud    | <br>EC2, AWS                                                        |
| <br>Cloud    | <br>Many others                                                     |
| <br>Insights | <br>Insights                                                        |
| <br>Galaxy   | <br>galaxy.ansible.com, console.redhat.com                          |
| <br>Galaxy   | <br>on-premise automation hub                                       |

### Content verification

Automation controller uses GNU Privacy Guard (GPG) to verify content.

For more information, see [The GNU Privacy Handbook](https://www.gnupg.org/gph/en/manual/c14.html#:~:text=GnuPG%20uses%20public%2Dkey%20cryptography,the%20user%20wants%20to%20communicate).
