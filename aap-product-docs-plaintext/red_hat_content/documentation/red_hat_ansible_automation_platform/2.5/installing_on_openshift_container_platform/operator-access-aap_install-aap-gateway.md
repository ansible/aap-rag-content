# 2. Configuring the Red Hat Ansible Automation Platform Operator on Red Hat OpenShift Container Platform
## 2.3. Accessing the platform gateway




You should use the **Ansible Automation Platform** instance as your default. This instance links the automation controller, automation hub, and Event-Driven Ansible deployments to a single interface.

**Procedure**

1. Log in to Red Hat OpenShift Container Platform.
1. Navigate toNetworking→Routes
1. Click the link under **Location** for **Ansible Automation Platform** .
1. This redirects you to the Ansible Automation Platform login page. Enter "admin" as your username in the **Username** field.
1. For the password you need to:


1. Go to toWorkloads→Secrets.
1. Click<your instance name>-admin-passwordand copy the password.
1. Paste the password into the **Password** field.

1. ClickLogin.
1. Apply your subscription:


1. ClickSubscription manifestorUsername/password.
1. Upload your manifest or enter your username and password.
1. Select your subscription from the **Subscription** list.
1. ClickNext. This redirects you to the **Analytics** page.

1. ClickNext.
1. Select the **I agree to the terms of the license agreement** checkbox.
1. ClickNext.


**Verification**

You now have access to the platform gateway user interface.


**Troubleshooting**

If you cannot access the Ansible Automation Platform see [Frequently asked questions on platform gateway](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/installing_on_openshift_container_platform/index#operator-aap-troubleshooting_configure-aap-operator) for help with troubleshooting and debugging.


