# Set up Red Hat Ansible Lightspeed on-premise deployment

As an administrator, you can deploy Ansible Lightspeed on-premise and connect it to IBM watsonx Code Assistant. Once the deployment is complete, you can use the Ansible Lightspeed service through the Ansible Visual Studio (VS) Code extension.

Note:

- Red Hat Ansible Lightspeed on-premise deployments are supported on Red Hat Ansible Automation Platform version 2.4 and later.
- The IBM Cloud service instance of IBM watsonx Code Assistant is available in the following data centers:
* Dallas (`us-south`)
* Frankfurt (`eu-de`)
* Sydney (`au-syd`) (Essentials plan only)


Ansible Lightspeed cloud deployments are configured to connect exclusively to the US (Dallas) IBM data center. Attempts to connect from non-US data centers will result in connection failure. If you want to use a non-Dallas IBM data center, then you must set up Ansible Lightspeed in hybrid deployment model. For more information about IBM’s supported data centers, see the topic Setting up your watsonx Code Assistant for Red Hat Ansible Lightspeed service in *IBM watsonx Code Assistant* documentation.

## Overview

This section provides information about the system requirements, prerequisites, and the process for setting up a Red Hat Ansible Lightspeed on-premise deployment.

### Deployment models

You can use one of the following modes of deployment:

-  **On-premise deployment** Both Red Hat Ansible Lightspeed and the IBM watsonx Code Assistant model (IBM Cloud Pak for Data) are on-premise deployments. Telemetry data is not collected for an on-premise mode of deployment.

-  **Hybrid deployment** Red Hat Ansible Lightspeed is an on-premise deployment, while IBM watsonx Code Assistant model is a cloud deployment. Telemetry data is not collected for hybrid deployments.

A hybrid deployment model provides the following benefits:

* Enables you to set up an on-premise deployment of Red Hat Ansible Lightspeed, with IBM watsonx Code Assistant model on a cloud environment.
* Provides the freedom and flexibility to choose an environment that best suits your organizational needs.
* Enables organizations to use the Ansible Automation Platform for user authentication, instead of logging into the Red Hat cloud.
* Enables organizations to deploy the Ansible Automation Platform in their preferred region.

### System requirements

Your system must meet the following minimum system requirements to install and run the Red Hat Ansible Lightspeed on-premise deployment.

| Requirement    | Minimum requirement |
| -------------- | ------------------- |
| <br>RAM        | <br>5 GB            |
| <br>CPU        | <br>1               |
| <br>Local disk | <br>40 GB           |


To see the rest of the Red Hat Ansible Automation Platform system requirements, see the System requirements section of *Planning your installation*.

Note:

You must also have installed IBM watsonx Code Assistant for Red Hat Ansible Lightspeed on Cloud Pak for Data. The installation includes a base model that you can use to set up your Red Hat Ansible Lightspeed on-premise deployment. For installation information, see the watsonx Code Assistant for Red Hat Ansible Lightspeed on Cloud Pak for Data documentation.

### Prerequisites

- You have installed Red Hat Ansible Automation Platform on your Red Hat OpenShift Container Platform environment.

- You have administrator privileges for Red Hat Ansible Automation Platform.

- You have installed IBM watsonx Code Assistant for Red Hat Ansible Lightspeed on Cloud Pak for Data.

- Your system meets the minimum system requirements to set up Red Hat Ansible Lightspeed on-premise deployment.

- You have obtained an API key and a model ID from IBM watsonx Code Assistant. For information about obtaining an API key and model ID from IBM watsonx Code Assistant, see the IBM watsonx Code Assistant documentation. For information about installing IBM watsonx Code Assistant for Red Hat Ansible Lightspeed on Cloud Pak for Data, see the watsonx Code Assistant for Red Hat Ansible Lightspeed on Cloud Pak for Data documentation.

- You have an existing external PostgreSQL database configured for the Red Hat Ansible Automation Platform, or have a database created for you when configuring the Red Hat Ansible Lightspeed on-premise deployment.

## Configure Ansible VS Code extension for Red Hat Ansible Lightspeed on-premise deployment

To access the on-premise deployment of Red Hat Ansible Lightspeed, all Ansible users within your organization must install the Ansible Visual Studio (VS) Code extension in their VS Code editor, and configure the extension to connect to the on-premise deployment.

### Before you begin

- You have installed VS Code version 1.70.1 or later.

### Procedure

1.  Obtain the URL of your Ansible Lightspeed instance:
1.  In Red Hat OpenShift Container Platform, select Networking> (and then)Routes and locate the Red Hat Ansible Lightspeed instance that was created.
2.  From the **Location** column, copy the URL of your Ansible Lightspeed instance. The URL will be in the following format: `https://<lightspeed_route>/complete/aap/`

2.  Open the VS Code application.
3.  From the **Activity** bar, click the **Extensions** icon.
4.  From the **Installed Extensions** list, select **Ansible**.
5.  From the **Ansible** extension page, click the **Settings** icon (![Settings icon](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/settings-icon-ansible-vscode-extension.png)) and select **Extension Settings**.
6.  Select **Ansible Lightspeed** settings and specify the following information:

- In the **URL for Ansible Lightspeed** field, enter the **Route URL** of the Red Hat Ansible Lightspeed on-premise deployment. Ansible users must have Ansible Automation Platform controller credentials. After configuring Ansible VS Code extension to connect to Red Hat Ansible Lightspeed on-premise deployment, you must [log in to Ansible Lightspeed through the Ansible VS Code extension](/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_install_ansible_vscode_extension#login-vscode-extension "After installing and configuring the VS Code extension, you can log in to the Ansible Lightspeed service.").

Note:
If your organization recently subscribed to the Red Hat Ansible Automation Platform, it might take a few hours for Red Hat Ansible Lightspeed to detect the new subscription. In VS Code, use the **Refresh** button in the Ansible extension from the Activity bar to check again.

## Connect to a different IBM watsonx Code Assistant model

After you have set up the Red Hat Ansible Lightspeed on-premise deployment successfully, you can modify the deployment if you want to connect to another IBM watsonx Code Assistant model.

### Before you begin

- You have set up a Red Hat Ansible Lightspeed on-premise deployment.
- You have obtained an API key and a model ID of the IBM watsonx Code Assistant model you want to connect to.
- You have created a new model configuration secret for the IBM watsonx Code Assistant model that you want to connect to. For information about creating a model configuration secrets, see [Creating a model configuration secret](/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-proc_install_aap_lightspeed_operator#create-connection-secrets "You must create a configuration secret to connect to an IBM watsonx Code Assistant model, which can be either an on-premise deployment or a cloud deployment.").

### About this task

For example, you connected to the default IBM watsonx Code Assistant model but now want to connect to a custom model instead. To connect to another IBM watsonx Code Assistant model, you must create new connection secrets, and then update the connection secrets and parameters on an existing Ansible Automation Platform operator.

### Procedure

1.  Go to the Red Hat OpenShift Container Platform.
2.  Select Operators> (and then)Installed Operators.
3.  From the list of installed operators, select the **Ansible Automation Platform** operator.
4.  Locate and select the **Ansible Automation Platform** custom resource, and then click the required app.
5.  Select the **YAML** tab.
6.  Scroll the text to find the `spec` section under `Lightspeed` category. For example:


```
spec:
lightspeed:
disabled: false
model_config_secret_name: <Name of the model configuration secret that you recently created.>
```

7.  Replace the `model_config_secret_name` value with the name of the IBM watsonx Code Assistant that you want to connect to.
8.  Click **Save**. The new Ansible Lightspeed pods are created. After the new pods are running successfully, the old Ansible Lightspeed pods are terminated.

## Monitor your Red Hat Ansible Lightspeed on-premise deployment

After the Red Hat Ansible Lightspeed on-premise deployment is successful, use the following procedure to monitor the metrics on an API endpoint `/metrics`.

### Procedure

1.  Create a **system auditor** user:
1.  Create a user with a **system auditor** role in the Red Hat Ansible Automation Platform. For the procedure, see the [Creating a user](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/getting_started_with_ansible_automation_platform/assembly-gs-platform-admin#proc-gs-platform-admin-create-user) section of *Getting started with Ansible Automation Platform*.
2.  Verify that you can log in to the Ansible Lightspeed portal for on-premise deployment (`https://<lightspeed_route>/`) as the newly-created system auditor user, and then log out.
2.  Create a token for the **system auditor** user:
1.  Log in to the Ansible Lightspeed portal for on-premise deployment (`https://<lightspeed_route>/admin`) as an administrator by using the following credentials:

- Username: **admin**
- Password: The secret that is named as `<lightspeed-custom-resource-name>-admin-password` in the Red Hat OpenShift Container Platform cluster namespace where Red Hat Ansible Lightspeed is deployed.

2.  On the Django administration window, select **Users** from the Users area. A list of users is displayed.
3.  Verify that the user with the system auditor role is listed in the **Users** list.
4.  From the Django Oauth toolkit area, select Access tokens> (and then)Add.
5.  Provide the following information and click **Save**:

- **User**: Use the magnifying glass icon to search and select the user with the system auditor role.

- **Token**: Specify a token for the user. Copy this token for later use.

- **Id token**: Select the token ID.

- **Application**: Select **Ansible Lightspeed for VS Code**.

- **Expires**: Select the date and time when you want the token to expire.

- **Scope**: Specify the scope as **read write**. An access token is created for the user with a system auditor role.

6.  Log out from the Ansible Lightspeed portal for on-premise deployment.
3.  Monitor your Red Hat Ansible Lightspeed on-premise deployment, by using the authorization token of the user with the system auditor role, to access the metrics endpoint `https://<lightspeed_route>/metrics`.

## Use the Ansible Lightspeed REST API

As the platform administrator, you can configure and use the Ansible Lightspeed REST API to build a custom automation development and tooling workflow outside of VS Code. For information about the Ansible Lightspeed REST API, see [Ansible AI Connect. 1.0.0 (v1)](https://developers.redhat.com/api-catalog/api/ansible-lightspeed) in the API catalog.

### Before you begin

- Ensure that you are using the Red Hat Ansible Automation Platform operator patch version 2.5-20250305.9 or later and Red Hat Ansible Lightspeed operator version 2.5.250225 or later.

### About this task

Note:

The Ansible Lightspeed REST API is available for Ansible Automation Platform 2.5 and later.

### Procedure

1.  Select the platform user for whom you want to grant REST API access. You can select an existing user or create a platform user in the Red Hat Ansible Automation Platform. For the procedure, see the [Creating a user](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/getting_started_with_ansible_automation_platform/assembly-gs-platform-admin#proc-gs-platform-admin-create-user) section of *Getting started with Ansible Automation Platform*.

2.  Verify that you can log in to the Ansible Lightspeed portal for on-premise deployment (`https://<lightspeed_route>/`) as the platform user you selected or created, and then log out.
3.  Create a token for the platform user:
1.  Log in to the Ansible Lightspeed portal for on-premise deployment (`https://<lightspeed_route>/admin`) as an administrator by using the following credentials:

- Username: **admin**
- Password: The secret that is named as `<lightspeed-custom-resource-name>-admin-password` in the Red Hat OpenShift Container Platform cluster namespace where Red Hat Ansible Lightspeed is deployed.

2.  On the Django administration window, select **Users** from the Users area. A list of users is displayed.
3.  Verify that the platform user is listed in the **Users** list.
4.  From the Django Oauth toolkit area, select Access tokens> (and then)Add.
5.  Provide the following information and click **Save**:

- **User**: Use the magnifying glass icon to search and select the newly-created or existing user for whom you want to grant API access.

- **Token**: Specify a token for the user. Copy this token for later use.

- **Id token**: Select the token ID.

- **Application**: Select **Ansible Lightspeed for VS Code**.

- **Expires**: Select the date and time when you want the token to expire.

- **Scope**: Specify the scope as **read write**. An access token is created for the user.

6.  Log out from the Ansible Lightspeed portal for on-premise deployment.
4.  Make a direct call to the Ansible Lightspeed REST API by specifying the newly-created token in the authorization header:


```
curl -H "Authorization: Bearer <token>"
https://<lightspeed_route>/api/v1/me/
```
