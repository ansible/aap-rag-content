# 6. Deploying the Ansible Lightspeed intelligent assistant on OpenShift Container Platform
## 6.4. Deploying the Ansible Lightspeed intelligent assistant
### 6.4.2. Updating the YAML file of the Ansible Automation Platform operator




After you create the chatbot authorization secret, you must update the YAML file of the Ansible Automation Platform operator to use the secret.

**Procedure**

1. Log in to Red Hat OpenShift Container Platform as an administrator.
1. Navigate toOperators→Installed Operators.
1. From the list of installed operators, select the **Ansible Automation Platform** operator.
1. Locate and select the **Ansible Automation Platform** custom resource, and then click the required app.
1. Select the **YAML** tab.
1. Scroll the text to find the `    spec:` section, and add the following details under the `    spec:` section:


```
spec:      lightspeed:        disabled: false        chatbot_config_secret_name: &lt;name of your chatbot configuration secret&gt;
```


1. Click **Save** . The Ansible Lightspeed intelligent assistant service takes a few minutes to set up.


**Verification**

1. Verify that the chat interface service is running successfully:


1. Navigate toWorkloads→Pods.
1. Filter with the term **api** and ensure that the following APIs are displayed in **Running** status:


-  `            myaap-lightspeed-api-&lt;version number&gt;`
-  `            myaap-lightspeed-chatbot-api-&lt;version number&gt;`


1. Verify that the chat interface is displayed on the Ansible Automation Platform:


1. Access the Ansible Automation Platform:


1. Navigate toOperators→Installed Operators.
1. From the list of installed operators, click **Ansible Automation Platform** .
1. Locate and select the **Ansible Automation Platform** custom resource, and then click the app that you created.
1. From the **Details** tab, record the information available in the following fields:


-  **URL** : This is the URL of your Ansible Automation Platform instance.
-  **Gateway Admin User** : This is the username to log into your Ansible Automation Platform instance.
-  **Gateway Admin password** : This is the password to log into your Ansible Automation Platform instance.

1. Log in to the Ansible Automation Platform using the URL, username, and password that you recorded earlier.

1. Access the Ansible Lightspeed intelligent assistant:


1. Click the Ansible Lightspeed intelligent assistant icon![Ansible Lightspeed intelligent assistant icon](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Installing_on_OpenShift_Container_Platform-en-US/images/441ac50ea9d519ddce4a68cfee7a6f54/chatbot-icon.png)
that is displayed at the top right corner of the taskbar.
1. Verify that the chat interface is displayed, as shown in the following image:

![Ansible Lightspeed intelligent assistant](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Installing_on_OpenShift_Container_Platform-en-US/images/b0c9174768a326728e452df5ecd7cde6/aap-ansible-lightspeed-intelligent-assistant.png)
.






