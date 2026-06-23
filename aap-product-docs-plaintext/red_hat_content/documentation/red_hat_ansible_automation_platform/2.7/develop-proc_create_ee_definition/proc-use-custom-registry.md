# Create an execution environment definition using the UI wizard
## Use a custom registry or self-signed certificates

Adjust the execution environment build configuration when targeting a private or internal container registry that uses custom URLs or self-signed certificates.

### Before you begin

- Your AAP administrator has configured templates and internal content sources. See [Host execution environment wizard templates in a private Git repository](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_host_templates_private_repo "Copy the EE Builder wizard templates from the public Ansible GitHub repository to a private repository for use in private or air-gapped environments.").
- You have access to an internal container registry.

### Procedure

1.  In the wizard, select **Custom Registry** instead of private automation hub and enter your internal registry URL.
2.  Clear the **Verify TLS certificates** checkbox if your internal registry uses self-signed certificates.
3.  Select a base image from your internal registry instead of the default `registry.redhat.io` images.

