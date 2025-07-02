# 2. Hardening Ansible Automation Platform
## 2.3. Initial configuration
### 2.3.1. Use a configuration as code paradigm




The Red Hat Community of Practice has created a set of automation content available through collections to manage Ansible Automation Platform infrastructure and configuration as code. This enables automation of the platform itself through _Configuration as Code_ (CaC). While many of the benefits of this approach are clear, there are security implications to consider.

The following Ansible content collections are available for managing Ansible Automation Platform components using an infrastructure as code methodology, all of which are found on the [Ansible Automation Hub](https://console.redhat.com/ansible/automation-hub) :


<span id="idm140248014950096"></span>
**Table 2.5. Ansible content collections**

|  **Validated Collection** |  **Collection Purpose** |
| --- | --- |
|  `infra.aap_utilities` | Ansible content for automating day 1 and day 2 operations of Ansible Automation Platform, including installation, backup and restore, certificate management, and more. |
|  `infra.aap_configuration` | A collection of roles to manage the creation of Ansible Automation Platform components, including users and groups (RBAC), projects, job templates and workflows, credentials, and more. This collection includes functionality from the older `infra.controller_configuration` , `infra.ah_configuration` and `infra.eda_configuration` and should be used in their place with Ansible Automation Platform 2.5. |
|  `infra.ee_utilities` | A collection of roles for creating and managing execution environment images, or migrating from the older Tower virtualenvs to execution environments. |




Many organizations use CI/CD platforms to configure pipelines or other methods to manage this type of infrastructure. However, using Ansible Automation Platform natively, a webhook can be configured to link a Git-based repository natively. In this way, Ansible can respond to Git events to trigger Job Templates directly. This removes the need for external CI components from this overall process and thus reduces the attack surface.

These practices enable version control of all infrastructure and configuration. Apply Git best practices to ensure proper code quality inspection before being synchronized into Ansible Automation Platform. Relevant Git best practices include the following:

- Creating pull requests.
- Ensuring that inspection tools are in place.
- Ensuring that no plain text secrets are committed.
- Ensuring that pre-commit hooks and any other policies are followed.


CaC also encourages using external vault systems which removes the need to store any sensitive data in the repository, or deal with having to individually vault files as needed. This is particularly important when storing Ansible Automation Platform configuration in a source code repository, as automation controller credentials and Event-Driven Ansible credentials must be provided to the collection variables in plain text which should not be committed to a source repository. For more information on using external vault systems, see the [External credential vault considerations](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/hardening_and_compliance/hardening-aap#con-external-credential-vault_hardening-aap) section in this guide.

