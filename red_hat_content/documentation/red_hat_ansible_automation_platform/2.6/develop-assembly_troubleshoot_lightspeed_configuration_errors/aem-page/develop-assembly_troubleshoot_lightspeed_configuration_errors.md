+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_troubleshoot_lightspeed_configuration_errors"
title = "Troubleshoot Red Hat Ansible Lightspeed configuration errors - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_lightspeed_intro/", "Build automation faster with Red Hat Ansible Lightspeed"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-assembly_troubleshoot_lightspeed_configuration_errors/aem-page/develop-assembly_troubleshoot_lightspeed_configuration_errors.html"
last_crumb = "Troubleshoot Red Hat Ansible Lightspeed configuration errors"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Troubleshoot Red Hat Ansible Lightspeed configuration errors"
oversized = "false"
page_slug = "develop-assembly_troubleshoot_lightspeed_configuration_errors"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/develop-assembly_troubleshoot_lightspeed_configuration_errors"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-assembly_troubleshoot_lightspeed_configuration_errors/toc/toc.json"
type = "aem-page"
+++

# Troubleshoot Red Hat Ansible Lightspeed configuration errors

This section provides information about errors when configuring the Red Hat Ansible Lightspeed and their workarounds.

## Cannot access the Ansible Lightspeed administrator portal

The Ansible Lightspeed administrator portal can be accessed by the Red Hat organization administrator only.

If you are the Red Hat organization administrator, before you access the Ansible Lightspeed administrator portal, ensure that:

- You have a valid Ansible Automation Platform subscription.

## Cannot save the API key

When you enter the IBM watsonx Code Assistant API key, authentication fails and shows the following error message:

 `IBM Cloud API key is invalid`

Red Hat Ansible Lightspeed verifies the API key by generating an associated access token. To resolve the error, ensure that you have not accidentally included any extra spaces when obtaining the API key from IBM watsonx Code Assistant. If you still cannot upload the API key, contact IBM Support.

## Cannot configure the model ID due to authentication failure

When you enter the model ID in the Red Hat Ansible Lightspeed administrator portal, the authentication fails.

To resolve the error, ensure that:

- You have configured a valid API key before you upload the model ID.
- You have not accidentally included any extra spaces when entering the model ID.

## Cannot configure the model ID due to inference failure

While validating the model ID, Red Hat Ansible Lightspeed performs a test inference. If Red Hat Ansible Lightspeed detects an error, the validation fails and an `Inference failed` message is displayed.

To resolve the error, ensure that:

- You have a valid API key and model ID.
- You have not accidentally included any extra spaces when obtaining the API key and model ID from IBM watsonx Code Assistant.

## Troubleshoot Red Hat Ansible Lightspeed on-premise deployment errors

This section provides information about errors when configuring the Red Hat Ansible Lightspeed on-premise deployment and their workarounds.

### Cannot log out of the Ansible Lightspeed portal

After you log out from the Ansible Lightspeed portal, you are redirected to the automation controller API page instead of Ansible Lightspeed.

This error indicates that the logout redirect URI was not configured while setting up your Red Hat Ansible Lightspeed on-premise deployment. You must configure the logout redirect URI by adding the **LOGOUT_ALLOWED_HOSTS** entry to the YAML file.

### Cannot connect to the Ansible Lightspeed service from the Ansible VS Code extension

The following scenarios are possible:

- The log-in attempt fails with the following error message:     `Enable lightspeed services from settings to use the feature.`

     This error indicates that Ansible Lightspeed is not enabled in the Ansible VS Code extension. To resolve this error, perform the following tasks:

  1. Open the VS Code application.
  2. From the **Activity** bar, click the **Extensions** icon.
  3. From the **Installed Extensions** list, select **Ansible**.
  4. From the **Ansible** extension page, click the **Settings** icon (![Settings icon](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/settings-icon-ansible-vscode-extension.png)) and select **Extension Settings**.
  5. Select **Ansible Lightspeed** settings and then select the **Enable Ansible Lightspeed** checkbox.

- You are redirected to an incorrect Ansible Lightspeed instance on clicking the Connect button. This error indicates an incorrect route URL was used while configuring the Ansible Lightspeed service in Ansible VS Code extension. Ensure that you have configured the correct value in the route URL without any suffix. For more information, see Configuring Ansible VS Code extension for Red Hat Ansible Lightspeed on-premise deployment.

- Cannot request code recommendations     The following error message is displayed:

     `An error occurred attempting to complete your request. Please try again later.`

     This error indicates that the Ansible Lightspeed service is not running or is running with issues. Please check the Lightspeed service logs (the pod with suffix `-api`) for more details and error codes.

- Cannot request code recommendations     The following error message is displayed:

     `The IBM watsonx Code Assistant is unavailable. Please try again later.`

     or:

     `IBM watsonx Code Assistant Model ID is invalid. Please contact your administrator.`

     This error indicates that the model secret contains incorrect values. To resolve this error, ensure that you have not accidentally added any whitespace characters (extra line, space, and so on) to the `username`, `model_url`, and `model_api_key` parameters in the model connection secret. For more information, see Creating connection secrets.

### Cannot connect to the Ansible Lightspeed service due to SSL connection error

If you are using self-signed certificates on the model server, you might encounter SSL certification verification errors, causing the connection between Ansible Lightspeed service and the model server to fail. The following error message is displayed:

```
Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED]
certificate verify failed: self signed certificate in certificate chain (_ssl.c:1006)'))
```
To resolve this error, use one of the following workarounds based on your Ansible Automation Platform version:

- For Red Hat Ansible Automation Platform 2.5 and later:


Specify the optional key/value pair as `model_verify_ssl=true` in the model secret to connect to an IBM watsonx Code Assistant model. For details about the procedure, see Creating connection secrets.

- For Red Hat Ansible Automation Platform 2.4:


You can disable the SSL protection between the model server and the Ansible Lightspeed service. For example, you can disable the SSL protection when you are on a testing environment. To disable the SSL protection, you must add the following extra setting in the Red Hat Ansible Lightspeed Custom Resource Definition (CRD) YAML file under the `spec:` section:

```
extra_settings:
    - setting: ANSIBLE_AI_MODEL_MESH_API_VERIFY_SSL
      value: false
```


 Important:

**Reenabling the SSL protection** You must re-enable the SSL protection when deploying on a production environment. To re-enable the SSL protection, simply remove the extra setting from the YAML file.

To reenable the SSL protection, perform the following tasks: . Go to the Red Hat OpenShift Container Platform. . Select Operators> (and then)Installed Operators. . From the **Projects** list, select the namespace that you created when you installed the Red Hat Ansible Automation Platform operator. . Locate and select the **Ansible Automation Platform** operator. . Locate and select the Ansible Automation Platform custom resource, and then click the required app. . Select the **YAML** tab. The editor switches to a YAML editor view. . Scroll and find the spec: section, and add the following parameter under the `spec:` section:

```
extra_settings:
    - setting: ANSIBLE_AI_MODEL_MESH_API_VERIFY_SSL
      value: false
```


1. Click **Save**.
2. Restart the automation controller pods to apply the revised YAML:
  1. From the Red Hat OpenShift Container Platform, select Workloads> (and then)Pods.

  2. Locate and select the Ansible Lightspeed pod that you updated.

  3. Click the **Edit** icon beside the pod and select **Delete Pod**. The select pod gets deleted and a new pod gets created.

## Troubleshoot Ansible Visual Studio Code extension errors

Use this topic to troubleshoot issues with Ansible VS Code.

### Cannot view the generated code recommendations using the Ansible VS Code extension

The following scenarios are possible:

- You receive a `403 error` message. To resolve this error, ensure that:

  * Your organization administrator has configured Red Hat Ansible Lightspeed for your organization.
  * You meet **one** of the following requirements:
    + Your organization has a trial or paid subscription to both the Red Hat Ansible Automation Platform and IBM watsonx Code Assistant.
    + Your organization has a trial or paid subscription to the Red Hat Ansible Automation Platform, and you have a Red Hat Ansible Lightspeed trial account.

- You have not configured the required Ansible VS code extension settings.   * To resolve this error, ensure that you have enabled the **Lightspeed:Enabled** and Lightspeed> (and then)Suggestions:Enabled settings.

- You receive a `Failure on completion requests` error when you make inference requests in VS Code. This error occurs because your organization has a trial or paid subscription to both Ansible Automation Platform and IBM watsonx Code Assistant. However, your organization administrator has not configured an IBM watsonx Code Assistant model for your organization.

- You receive an `Ansible Lightspeed encountered an error. Try again after some time.` error message when you make single-task or multitask requests. This error occurs when you use a remote SSH extension with VS Code to request single or multitask recommendations in playbooks. However, the task recommendations are generated when using a role. This error occurs in workspaces that contain a large number of roles.

- Your VS Code Workspace settings override user settings. If your Workspace settings are configured, they can override our user settings even if you have configured the Ansible VS Code extension correctly. The Workspace settings can disable your VS Code extension settings, and therefore you cannot access the Ansible Lightspeed service.

     To resolve this error, ensure that there are no Workspace settings configured in VS Code.

- You entered a multitask prompt, but code recommendations were not generated. To resolve this error, log out of VS Code and log in again using your Red Hat account.

- You clicked a different location or switched to a different window; therefore, the populated code recommendations disappeared. The Red Hat Ansible Lightspeed service could take multiple seconds per task to populate the code recommendations. If you are using a multitask prompt, the Red Hat Ansible Lightspeed service takes a bit longer to populate the results. Do not move your cursor or press any key while the code recommendation is being generated. If you change the cursor location or press any key, the Ansible VS Code extension cancels the request and the Red Hat Ansible Lightspeed service does not process your request. In this scenario, you must get the cursor back to its original position and repopulate the results.

### Cannot request code recommendations by using the Ansible VS Code extension

The following error message is displayed: `Your trial to the generative AI model has expired. Refer to your IBM Cloud Account to re-enable access to the IBM watsonx Code Assistant.`

To resolve this error, refer to your IBM Cloud account and select an upgrade option.

### Cannot connect to Ansible VS code extension when using a proxy configuration or a self-signed certificate or both

You might encounter errors when connecting with to the Ansible VS code extension through a proxy. Connections to the outbound domain `https://c.ai.ansible.redhat.com` fail and a network error message is displayed.

To resolve this issue, you must add the URL `https://c.ai.ansible.redhat.com/` in VS Code proxy settings. If you are using Red Hat Single Sign-On (RH-SSO) to authenticate users, then you must also grant access to `https://sso.redhat.com` in VS code proxy settings.

To modify the proxy settings in VS code, perform the following tasks:

1. Open Visual Studio Code.
2. Navigate to **File > Preferences > Settings**.
3. Select Application> (and then)Proxy in the sidebar.
4. In the **Http: Proxy** field, add the following URLs to the proxy:
  - `https://c.ai.ansible.redhat.com/`
  - `https://sso.redhat.com`, if you are using RH-SSO to authenticate users.
5. In the **http: Proxy Support** drop down list, select **Override**.
6. Search for and select the following configuration keys:
  - **Electron Fetch**
  - **System Certificates V2** if you are using your own Certificate Authority (CA).


For information about how to set up proxy support in VS Code, see the Related Links section below.

### Cannot connect to Ansible VS code extension due to network issues

If you encounter network issues, use the **Network Proxy Test** extension to test the connection:

1. Install the VS code extension **Network Proxy Test**.

2. Use the **Network Proxy Test: Test Connection** action to target the server and the endpoint using the parameter `/check/status end-point`. For example:

     `https://c.ai.ansible.redhat.com/check/status/` to test the connection to Red Hat Ansible Lightspeed cloud service.

## Troubleshoot Ansible code bot errors

This section provides information about errors when using the Ansible code bot and their workarounds.

### Cannot access Ansible code bot

After you install Ansible code bot and attempt to log in, you receive the following error message:

 `Your organization does not have a valid Red Hat Ansible Lightspeed subscription`

After you install Ansible code bot, you are redirected to a page that shows an active subscription status, as shown in the following image:

*Figure 1. Ansible code bot login screen with an active subscription*

![Ansible code bot login screen with an active subscription](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/code-bot-login-screen.png)

If the login screen displays an inactive subscription status, Ansible code bot does not scan your Git repositories. The error occurs because your organization does not have a valid Ansible Automation Platform subscription. To resolve this error, ensure that you are part of an organization that has a valid Red Hat Ansible Automation Platform subscription.

### Cannot scan your Git repository using Ansible code bot

If the Ansible code bot is not configured correctly, it does not scan your Git repositories or does not create pull requests.

To resolve Ansible code bot errors, ensure that:

- You have selected all the Git repositories that you want to scan.
- You have a `.yml` configuration file named `ansible-code-bot.yml` in your repository `.github` folder. For example, `.github/ansible-code-bot.yml`.


Run a manual scan on your git repositories by adding the **ansible-code-bot-scan** topic to your repository. For more information, see Manually scan your Git repositories.

If the Ansible code bot still cannot scan your Git repository, the following scenarios are possible:

- The Ansible code bot did not identify any ansible-lint violations in the Git repository.
- The Ansible code bot does not have permission to scan the Git repository.
- Your organization does not have a valid Red Hat Ansible Automation Platform subscription.

### Cannot create pull requests

You might encounter an error where the Ansible code bot cannot create pull requests after scanning your Git repositories.

To resolve this error, ensure that:

- You have verified that there are are no duplicate pull requests. For more information, see How Ansible code bot handles duplicate pull requests.
- You have deleted the branches after closing the pull requests created by the Ansible code bot. For more information, see Deleting a branch used for a pull request.
