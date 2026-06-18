# Install and configure the Dev Containers extension

If you are installing the containerized version of Ansible development tools, you must install the [Microsoft Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension in VS Code.

## About this task

## Procedure

1.  Open VS Code.
2.  Click the **Extensions** (![Extensions](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/vscode-extensions-icon.png)) icon in the Activity Bar, or click View> (and then)Extensions, to display the **Extensions** view.
3.  In the search field in the **Extensions** view, type `Dev Containers`.
4.  Select the Dev Containers extension from Microsoft and click Install. If you are using Podman or Podman Desktop as your containerization platform, you must modify the default settings in the `Dev Containers` extension.

5.  Replace docker with podman in the `Dev Containers` extension settings:
1.  In VS Code, open the settings editor.
2.  Search for `@ext:ms-vscode-remote.remote-containers`. Alternatively, click the **Extensions** icon in the activity bar and click the gear icon for the `Dev Containers` extension.

6.  Set `Dev > Containers:Docker Path` to `podman`.
7.  Set `Dev > Containers:Docker Compose Path` to `podman-compose`.
