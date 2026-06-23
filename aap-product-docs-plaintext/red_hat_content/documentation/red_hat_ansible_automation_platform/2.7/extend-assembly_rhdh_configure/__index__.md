# Configure the Ansible plug-ins

After installing the Ansible plug-ins, configure them to connect to your Ansible Automation Platform instance and enable software templates.

Add the following configuration to your Red Hat Developer Hub custom ConfigMap (for example, `app-config-rhdh`).

- For Operator deployments, edit the ConfigMap directly.
- For Helm deployments, edit the ConfigMap referenced in `upstream.backstage.extraAppConfig`.

