# 3. Setting up Red Hat Ansible Lightspeed for your organization
## 3.3. Setting up Red Hat Ansible Lightspeed on-premise deployment
### 3.3.6. Updating the Redirect URIs




When Ansible users log in or log out of Ansible Lightspeed service, the Red Hat Ansible Automation Platform redirects the user’s browser to a specified URL. You must configure the redirect URLs so that users can log in and log out of the application successfully.

**Prerequisites**

- You have created and deployed a Red Hat Ansible Lightspeed instance to your namespace.


**Procedure**

1. Get the URL of the Ansible Lightspeed instance:


1. Go to Red Hat OpenShift Container Platform.
1. SelectNetworking→Routes.
1. Locate the Red Hat Ansible Lightspeed instance that you created.
1. Copy the Location URL of the Red Hat Ansible Lightspeed instance.

1. Update the **login** redirect URI:


1. In the automation controller, go toAdministration→Applications.
1. Select the Lightspeed Oauth application that you created.
1. In the **Redirect URIs** field of the Oauth application, enter the URL in the following format:

`        https://&lt;lightspeed_route&gt;/complete/aap/`

An example of the URL is `        https://lightspeed-on-prem-web-service.com/complete/aap/` .

Important
The Redirect URL must include the following information:


- The prefix `            https://`
- The `            &lt;lightspeed_route&gt;` URL, which is the URL of the Red Hat Ansible Lightspeed instance that you copied earlier
- The suffix `            /complete/aap/` that includes a backslash sign ( **/** ) at the end



1. Click **Save** .

1. Update the **logout** redirect URI based on your setup:

**Procedure when both the Red Hat Ansible Lightspeed instance and automation controller are installed using Ansible Automation Platform operator** :


1. Log in to the cluster on which the Ansible Automation Platform instance is running.
1. Identify the **AutomationController** custom resource.
1. Select **[YAML view]** .
1. Add the following entry to the YAML file:


```
```yaml          spec:          ...          extra_settings:            - setting: LOGOUT_ALLOWED_HOSTS              value: "'&lt;lightspeed_route-HostName&gt;'"          ```
```

Important
Ensure the following while specifying the `        value:` parameter:


- Specify the hostname without the network protocol, such as `            https://` .

For example, the correct hostname would be `            my-aiconnect-instance.somewhere.com` , and not `            https://my-aiconnect-instance.somewhere.com` .


- Use the single and double quotes exactly as specified in the codeblock.

If you change the single quotes to double quotes and vice versa, you will encounter errors when logging out.


- Use a comma to specify multiple instances of Red Hat Ansible Lightspeed deployment.

If you are running multiple instances of Red Hat Ansible Lightspeed application with a single Red Hat Ansible Automation Platform deployment, add a comma (,) and then add the other hostname values. For example, you can add multiple hostnames, such as `            "'my-lightspeed-instance1.somewhere.com','my-lightspeed-instance2.somewhere.com'"`





1. Apply the revised YAML. This task restarts the automation controller pods.



**Procedure when the Ansible Automation Platform operator is run on a virtual machine** :

1. Log in to the virtual machine with the Ansible Automation Platform controller.
1. In the **/etc/tower/conf.d/custom.py** file, add the following parameter:
`    LOGOUT_ALLOWED_HOSTS = "&lt;lightspeed_route-HostName&gt;"`

Important

- If the **/etc/tower/conf.d/custom.py** file does not exist, create it.
- Specify the hostname without the network protocol, such as `        https://` .

For example, the correct hostname would be `        my-aiconnect-instance.somewhere.com` , and not `        <a class="link" href="https://my-aiconnect-instance.somewhere.com">https://my-aiconnect-instance.somewhere.com</a>` .


- Use the single and double quotes in pairs; do not mix single quotes with double quotes.



1. Restart the automation controller by executing the following command:
`    $ automation-controller-service restart`


**Procedure when the platform gateway is run on a virtual machine** :

1. Log in to the virtual machine with the platform gateway.
1. Add the following parameter in either the **gateway/settings.py** file or in the **ansible-automation-platform/gateway/settings.py** file:
`    LOGOUT_ALLOWED_HOSTS = "&lt;lightspeed_route-HostName&gt;"`

Important

- Specify the hostname without the network protocol, such as `        https://` .

For example, the correct hostname would be `        my-aiconnect-instance.somewhere.com` , and not `        <a class="link" href="https://my-aiconnect-instance.somewhere.com">https://my-aiconnect-instance.somewhere.com</a>` .


- Use double quotes exactly as specified in the codeblock.





**Additional resources**

-  [Troubleshooting Red Hat Ansible Lightspeed on-premise deployment errors](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#troubleshooting-lightspeed-onpremise-config_troubleshooting-lightspeed)


