# 2. Installing Red Hat Ansible Automation Platform gateway on Red Hat OpenShift Container Platform
## 2.3. Accessing platform gateway through the OpenShift Container Platform UI

Use the **Ansible Automation Platform** instance as your default. This instance links the automation controller, automation hub, and Event-Driven Ansible deployments to a single interface.

**Procedure**

1. Log in to Red Hat OpenShift Container Platform.

2. Navigate to Networking → Routes

3. Click the link under **Location** for **Ansible Automation Platform**.

4. This redirects you to the Ansible Automation Platform login page. Enter "admin" as your username in the **Username** field.

5. For the password you must:


1. Go to Workloads → Secrets.
2. Click <your instance name>-admin-password and copy the password.
3. Paste the password into the **Password** field.

6. Click Login.

7. Apply your subscription:


1. Click Subscription manifest or Username/password.
2. Upload your manifest or enter your username and password.
3. Select your subscription from the **Subscription** list.
4. Click Next. This redirects you to the **Analytics** page.

8. Click Next.

9. Select the **I agree to the terms of the license agreement** checkbox.

10. Click Next.

**Verification**

You now have access to the platform gateway user interface.

**Troubleshooting**

If you cannot access the Ansible Automation Platform see [Frequently asked questions on platform gateway](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/installing_on_openshift_container_platform/index#operator-aap-troubleshooting_configure-aap-operator) for help with troubleshooting and debugging.

