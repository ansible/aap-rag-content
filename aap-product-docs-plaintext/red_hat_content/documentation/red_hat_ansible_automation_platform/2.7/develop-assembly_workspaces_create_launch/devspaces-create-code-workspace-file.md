# Create and launch an Ansible development workspace
## Create a code-workspace file for an Ansible development workspace

To configure VS Code extensions that are included in your Ansible development workspace, you must add a `.code-workspace` JSON file to your git repository.

### About this task

### Procedure

1.  In your Git repository for your Ansible development workspace, create a new file named `.code-workspace`.
2.  Copy and paste the following sample code into the `.code-workspace` file:


```
{
"settings": {
"ansible.lightspeed.suggestions.enabled": true,
"ansible.lightspeed.enabled": true,
"ansible.ansible.useFullyQualifiedCollectionNames": true,
"ansible.validation.enabled": true,
"ansible.validation.lint.enabled": true,
"files.trimTrailingWhitespace": true,
"files.trimFinalNewlines": true,
"files.insertFinalNewline": true,
"ansible.validation.lint.arguments": "--profile production --offline",
"openshiftToolkit.showWelcomePage": false,
"editor.wordWrap": "on",
"files.autoSave": "off"
},
"folders": [
{
"name": "ansible-devspaces",
"path": "/projects/ansible-devspaces"
}
],
"extensions": {
"recommendations": [
"redhat.ansible",
"redhat.vscode-yaml",
"redhat.vscode-openshift-connector",
"ms-python.python"
]
}
}
```

3.  If you want to add extra extensions to your Ansible development workspace, add them in the `extensions.recommendations` section of the file.
4.  Add the `.code-workspace` file to your Git repository and push the changes.

