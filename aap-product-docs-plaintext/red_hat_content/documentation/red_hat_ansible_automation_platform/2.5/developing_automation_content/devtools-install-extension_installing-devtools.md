# 3. Installing Ansible development tools
## 3.1. Requirements
### 3.1.4. Installing the VS Code Ansible extension




The Ansible extension adds language support for Ansible to VS Code. It incorporates Ansible development tools to facilitate creating and running automation content.

For a full description of the Ansible extension, see the [Visual Studio Code Marketplace](https://marketplace.visualstudio.com/items?itemName=redhat.ansible) .

Use the following procedure to install the Ansible VS Code extension:

**Procedure**

1. Open VS Code.
1. Click the **Extensions** (![Extensions](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Developing_automation_content-en-US/images/417ed5315a44493c6a44ae5c12dc6fab/vscode-extensions-icon.png)
) icon in the Activity Bar, or clickView→Extensions, to display the **Extensions** view.
1. In the search field in the **Extensions** view, type `    Ansible Red Hat` .
1. Select the Ansible extension and clickInstall.


**Verification**

When the language for a file is recognized as Ansible, the Ansible extension provides features such as auto-completion, hover, diagnostics, and goto. The language identified for a file is displayed in the Status bar at the bottom of the VS Code window.


The following files are assigned the Ansible language:

- YAML files in a `    /playbooks` directory
- Files with the following double extension: `    .ansible.yml` or `    .ansible.yaml`
- Certain YAML names recognized by Ansible, for example `    site.yml` or `    site.yaml`
- YAML files whose filename contains "playbook": `    <span class="strong strong"><strong><span class="Role ARG Spec Role ARG Spec">playbook</span></strong></span>.yml` or `    <span class="strong strong"><strong><span class="Role ARG Spec Role ARG Spec">playbook</span></strong></span>.yaml`


**Troubleshooting**

If the extension does not identify the language for your playbook files as Ansible, follow the procedure in [Associating the Ansible language to YAML files](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/developing_automation_content/installing-devtools#devtools-extension-set-language_installing-devtools) .


