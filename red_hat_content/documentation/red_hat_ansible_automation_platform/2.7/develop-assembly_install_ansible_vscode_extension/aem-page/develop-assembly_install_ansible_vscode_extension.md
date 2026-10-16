+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_install_ansible_vscode_extension"
template = "docs/aem-title.html"
title = "Install and configure the Ansible VS Code extension - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_lightspeed_intro/", "Build automation faster with Red Hat Ansible Lightspeed code assistant"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-assembly_install_ansible_vscode_extension/aem-page/develop-assembly_install_ansible_vscode_extension.html"
last_crumb = "Install and configure the Ansible VS Code extension"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Install and configure the Ansible VS Code extension"
oversized = "false"
page_slug = "develop-assembly_install_ansible_vscode_extension"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-assembly_install_ansible_vscode_extension"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-assembly_install_ansible_vscode_extension/toc/toc.json"
type = "aem-page"
+++

# Install and configure the Ansible VS Code extension

Install and configure the Ansible VS Code extension to use the cloud-hosted coding assistant or a third-party LLM provider (IBM watsonx, Google Gemini). When enabled, the extension automatically collects recommendations, usage telemetry, and Ansible YAML file state through automated events.

To access Red Hat Ansible Lightspeed code assistant, all Ansible users must install and configure the Ansible VS Code extension in their VS Code. The Ansible VS Code extension uses the Ansible-specific IBM watsonx Granite model configured in the Red Hat Ansible Lightspeed administrator portal as the default mode for all users in your organization.

## Connectivity requirements

To generate code recommendations, the Ansible Lightspeed service in Visual Studio (VS) Code editor requires access to the following outbound domain:

- Red Hat Ansible Lightspeed with IBM watsonx Code Assistant, this is linked below.

The outbound connections are encrypted on TCP protocol port 443.

## Install and configure the Ansible VS Code extension

Install and configure the Ansible VS Code extension to use the cloud-hosted coding assistant or a third-party LLM provider (IBM watsonx, Google Gemini). When enabled, the extension automatically collects recommendations, usage telemetry, and Ansible YAML file state through automated events.

To access Red Hat Ansible Lightspeed code assistant, all Ansible users must install and configure the Ansible VS Code extension in their VS Code. The Ansible VS Code extension uses the Ansible-specific IBM watsonx Granite model configured in the Red Hat Ansible Lightspeed administrator portal as the default mode for all users in your organization.

### Connectivity requirements

To generate code recommendations, the Ansible Lightspeed service in Visual Studio (VS) Code editor requires access to the following outbound domain:

- Red Hat Ansible Lightspeed with IBM watsonx Code Assistant, this is linked below.

The outbound connections are encrypted on TCP protocol port 443.

## Install the Ansible VS Code extension

Use the following procedure to install the Ansible Lightspeed extension in VS Code.

### Before you begin

- VS Code version 1.70.1 or later.

Note:

You can also install VScode derivatives, such as VScode Insider or VS Codium.

### Procedure

1. Open the VS Code application.
2. From the navigation menu, click the **Extensions** icon.
3. In the **Search** field, enter **Ansible**.
4. Select **Ansible** to choose the Ansible language support extension published by Red Hat.
5. Click **Install**.
6. After installation is complete, verify your VSCode installation:
  1. Create a new YAML file using the `.yml` or `.yaml` file extension.
  2. From the **Status** toolbar, click the language indicator and select **Ansible** to associate the Ansible language type with the new YAML file.
  3. Start writing a test playbook. Contextual aids are displayed as you start creating your content.

## Configure the Ansible VS Code extension for cloud or third-party providers

Configure third-party LLM providers, such as IBM watsonx Code Assistant or Google Gemini, within the Ansible VS Code extension.

### Before you begin

- You have installed the Ansible VS Code extension v25.12.3.
- You have obtained a valid API key for your chosen third-party LLM provider.

### Procedure

1. Open the VS Code application.
2. From the Activity bar, click the **Extensions** icon ![Extensions](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/extensions-icon-vscode.png).
3. From the Installed Extensions list, select **Ansible**.
4. From the **Ansible** extension page, click the **Settings** icon and select **Extension Settings**.
5. Select **Ansible Lightspeed** settings, and specify the following information:
    | UI field                                | Description                                                                                                                                                                                              |
    | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | Ansible Lightspeed: Enabled             | Select this checkbox to enable the Red Hat Ansible Lightspeed service.                                                                                                                                   |
    | Ansible Lightspeed: Provider            | Select the active AI service for code generation.<br>Choose the AI provider from the following options:<br>  `wca`: (Default setting) Uses IBM watsonx Code Assistant as the AI provider.  `google`: Uses Google Gemini as the AI provider. |
    | Ansible Lightspeed: Model Name          | Specify the specific AI model version to use for code generation:<br>  For IBM watsonx Code Assistant: (Required) The IBM watsonx Code Assistant model name or ID that you want to use for code generation.  For Google Gemini: (Optional) The system applies a recommended default model if left blank. |
    | Ansible Lightspeed: Api Key             | Specify the secret credential required to authenticate requests with third-party model providers.<br>  For IBM watsonx Code Assistant: (Optional) This field is not used for the IBM WCA provider. IBM watsonx Code Assistant relies on a separate OAuth2 login flow via the Red Hat portal.  For Google Gemini: (Required) Paste your active Google Gemini API key into this field. This token authorizes the extension to send prompts to Google’s servers. |
    | Ansible Lightspeed: Api Endpoint        | Specify the destination URL for network requests sent by the Ansible VS Code extension.<br>  For IBM watsonx Code Assistant: (Required) This field allows modification of the service URL for IBM watsonx Code Assistant connections. The default URL is `https://c.ai.ansible.redhat.com`.  For Google Gemini: (Not configurable) This setting is not configurable when using the Google provider. The extension automatically manages the correct endpoint URL for Google services internally. |
    | Ansible Lightspeed Suggestions: Enabled | Toggle the automatic display of inline code completions within the Ansible VS Code editor. Inline suggestions are currently available for the IBM watsonx Code Assistant provider only.                  |
    | Ansible Lightspeed: Timeout             | Define the maximum duration the Ansible VS Code extension waits for a server response. The default timeout for API calls is 3000 milliseconds.                                                           |

### Results

Your settings are automatically saved in VS Code.

Note:

If your organization recently subscribed to the Red Hat Ansible Automation Platform, it might take a few hours for Red Hat Ansible Lightspeed to detect the new subscription. In VS Code, use the **Refresh** button in the Ansible extension from the Activity bar to check again.

## Configure the Ansible VS Code extension for a containerized deployment

Configure the Ansible VS Code extension to connect to the intelligent assistant running on containerized Ansible Automation Platform (port 8447). This configuration enables the Ansible users in your organization to use the Ansible Lightspeed coding assistant to create Ansible content.

### Before you begin

- You have installed VS Code version 1.70.1 or later.
- Your organization administrator has configured an IBM watsonx Code Assistant model for your organization.
- Your network or firewall configuration permits ingress traffic on port 8447. This port is required for containerized installations to connect IBM watsonx Code Assistant with the Ansible VS Code extension, which then provides access to the Ansible Lightspeed coding assistant.

### Procedure

1. Open the VS Code application.
2. From the Activity bar, click the **Extensions** icon ![Extensions](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/extensions-icon-vscode.png).
3. From the Installed Extensions list, select **Ansible**.
4. From the **Ansible** extension page, click the **Settings** icon and select **Extension Settings**.
5. Select **Ansible Lightspeed** settings, and specify the following information:
  1. Ensure that the **Enable Ansible Lightspeed with watsonx Code Assistant inline suggestions** checkbox is selected.
  2. In the **URL for Ansible Lightspeed** field, verify that you have the following URL: `https://<node.ansible.com>:8447`.
  3. Select the **Enable Ansible Lightspeed with watsonx Code Assistant inline suggestions** checkbox.
6. Optional: If you want to use the custom model instead of the default model, in the **Model ID Override** field, enter the custom model ID. The **model-override** setting enables you to override the default model and use the custom model, after your organization administrator has created a custom model and has shared the model ID with you separately. Your settings are automatically saved in VS Code.

  Note:
      If your organization recently subscribed to the Red Hat Ansible Automation Platform, it might take a few hours for Red Hat Ansible Lightspeed to detect the new subscription. In VS Code, use the **Refresh** button in the Ansible extension from the Activity bar to check again.

### What to do next

- After you configure the Ansible VS Code extension with the generated Ansible Lightspeed URL, you can use the Ansible VS Code extension and start developing Ansible content.   1. [Log in to Red Hat Ansible Lightspeed through the Ansible VS Code extension](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_install_ansible_vscode_extension#login-vscode-extension "After installing and configuring the VS Code extension, you can log in to the Ansible Lightspeed service.").
  2. [Develop Ansible content](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_developing_ansible_content#developing-ansible-content "As an automation developer, you can use Red Hat Ansible Lightspeed to implement your organization’s automation strategy. Red Hat Ansible Lightspeed can help you create and use custom automation content.").

### Configure a wildcard OAuth redirect URI for OpenShift Dev Spaces

When developers use Ansible Lightspeed from OpenShift Dev Spaces in an air-gapped environment, each Dev Spaces workspace generates a unique callback URL. Instead of registering each workspace URL individually, you can register a single wildcard OAuth redirect URI that covers all workspaces.

#### Before you begin

- Ansible Lightspeed is deployed on your Ansible Automation Platform environment.
- OpenShift Dev Spaces is installed and configured for your developers.
- You have administrator access to the Ansible Lightspeed Django admin interface or the `wisdom-manage` CLI.

#### About this task

On-prem Ansible Lightspeed includes a custom OAuth application model (`wildcard_oauth2.Application`) that supports glob wildcards in both the host and path components of a redirect URI. This capability is available in Ansible Automation Platform 2.6 and later.

#### Procedure

1. Identify the redirect URI pattern for your Dev Spaces environment.
      Each Dev Spaces workspace generates a callback URL in the following format:

```
https://<devspaces-host>/<user>/<workspace>/<port>/<endpoint>/callback
```

    To find the exact path depth, capture the `redirect_uri` parameter from a failing `/o/authorize/` request in your browser's developer tools or server logs. Count the number of path segments between the host and `/callback`.

2. Construct the wildcard redirect URI.
      Replace each dynamic path segment with `*`. For example, if the callback URL has four dynamic segments:

```
https://<devspaces-host>/*/*/*/*/callback
```

  Important:
  Each `*` matches exactly one path segment and does not match across `/` separators. The number of `*` segments in your wildcard pattern must match the actual number of dynamic path segments in the Dev Spaces callback URL. Wildcards in the hostname are permitted only within subdomain labels and cannot be used in the primary domain name or top-level domain. If the segment count does not match or the hostname pattern is invalid, authentication fails. For more information, see the Security considerations section.

3. Open the Ansible Lightspeed Django admin interface.
      Navigate to OAuth2 Provider> (and then)Applications and select the VS Code Lightspeed OAuth Application.

    Alternatively, use the `wisdom-manage` CLI to update the application.

4. Add the wildcard redirect URI to the application.
      In the Redirect uris field, add the wildcard URI on a new line alongside any existing redirect URIs, such as `vscode://redhat.ansible` entries. For example:

```
vscode://redhat.ansible
https://devspaces.example.com/*/*/*/*/callback
```

5. Save the application.

#### Results

To verify the configuration, open a Dev Spaces workspace, launch the Ansible extension, and sign in to Lightspeed. The OAuth authorization-code flow should complete without requiring individual workspace registration.

#### What to do next

**Security considerations**

The wildcard pattern is anchored to the registered URI. This means:

- Suffix-spoof hosts (for example, `devspaces.example.com.attacker.io`) and off-domain hosts are rejected.
- Only URIs that match the exact pattern, including the host and path depth, are accepted.
- Wildcards (`*`) are permitted only within subdomain labels of a hostname. They cannot be used in the primary domain name or the top-level domain (the last two labels).   * Valid: `*.example.com`, `sub*.example.com`, `*.*.example.com`
  * Invalid: `*.com`, `*.example.*`, `subdomain.*.com`
- Wildcard patterns in redirect network locations do not match IP addresses. For example, `http://*.0.1/...` does not match `123.123.0.1`.

To minimize risk, scope the host label as tightly as possible. Do not use wildcards in the domain portion of the URI.

## Log in to Ansible Lightspeed through the Ansible VS Code extension

After installing and configuring the VS Code extension, you can log in to the Ansible Lightspeed service.

### About this task

Red Hat Ansible Lightspeed provides different sign-in methods depending on whether you are using the cloud service or the on-premise deployment.

- **Ansible Lightspeed on-premise deployments**     Users are authenticated using your Red Hat Ansible Automation Platform login.

    To sign in, you can use the **Connect** button in the Ansible Lightspeed view, or the **Sign in with Ansible Lightspeed to use Ansible** option in the Accounts menu. Once prompted in the browser, select **Log in with Ansible Automation Platform**, and log in with the authorization mechanism that your automation controller is configured with.

- **Ansible Lightspeed cloud service**     Users are authenticated using Red Hat Single Sign-On (RH-SSO).

    To sign in from VS Code, you can use the **Connect** button in the Ansible Lightspeed view, or the **Sign in with Ansible Lightspeed to use Ansible** option in the Accounts menu. Follow the on-screen prompts to log in and access the Ansible Lightspeed service using your RH-SSO.

  Note:
      If you are using a cloud development environment at a domain unknown by Ansible Lightspeed, such as on-premise Red Hat OpenShift Dev Spaces, your Accounts sign-in menu provides the option **Sign-in with Red Hat to use Ansible**.

    This option uses a device code flow to successfully complete the sign-in process and requires the Red Hat Authentication extension v0.2.0 or later. If you require this authentication flow but don’t see the **Sign-in with Red Hat to use Ansible** option, ensure you are using the Ansible VS Code extension v24.5.2 or later.

### Procedure

1. Open the VS Code application.
2. Sign in using either the **Connect** button in the Ansible Lightspeed view or the Accounts menu.

  - **Sign in using the Connect button**:
    1. From the VS Code activity bar, click the **Ansible** icon.
    2. In the **Ansible Lightspeed** view, click **Connect**.
    3. Follow the on-screen prompts to sign in to Ansible Lightspeed.
  - **Sign in using the Accounts menu**:
    1. From the VS Code activity bar, click the Accounts menu.
    2. Sign in with Ansible Lightspeed to use Ansible or sign in with Red Hat to use Ansible, depending on the sign-in option you are presented with.
      Note:

      * The sign-in options are displayed when the VS Code extension is in an active state. The extension is activated after you open the Ansible side panel or after you open an Ansible file in the VS Code editor. If you do not see this option, use the **Connect** button to link to the Ansible Lightspeed service.
      * If you are using a cloud development environment at a domain unknown by Ansible Lightspeed, such as on-premise Red Hat OpenShift Dev Spaces, your Accounts sign-in menu provides the option **Sign-in with Red Hat to use Ansible**. This option uses a device code flow to successfully complete the sign-in process and requires the Red Hat Authentication extension v0.2.0 or later. If you require this authentication flow but don’t see the **Sign-in with Red Hat to use Ansible** option, ensure you are using the Ansible VS Code extension v24.5.2 or later.

    3. Follow the on-screen prompts to sign in to Red Hat Ansible Lightspeed.

### Results

On successful authentication, the login screen is displayed along with your username and your assigned user role.
