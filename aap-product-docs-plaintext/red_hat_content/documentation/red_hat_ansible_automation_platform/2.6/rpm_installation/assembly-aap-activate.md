# 1. Red Hat Ansible Automation Platform installation overview
## 1.2. Managing Ansible Automation Platform subscriptions, updates, and support
### 1.2.6. Activating Red Hat Ansible Automation Platform

Red Hat Ansible Automation Platform uses available subscriptions or a subscription manifest to allow the use of Ansible Automation Platform.

To obtain a subscription, you can do either of the following:

1. Use your Red Hat username and password, service account credentials, or Satellite credentials when you launch Ansible Automation Platform.
2. Upload a subscriptions manifest file either using the Red Hat Ansible Automation Platform interface or manually in an Ansible Playbook.

#### 1.2.6.1. Activate with credentials

Activate your Ansible Automation Platform subscription at the first launch by providing either Red Hat service account credentials or your personal Red Hat username and password. This process automatically retrieves and imports the required license, which grants the platform access to Red Hat content and entitlement services.

Note

You are opted in for Automation Analytics by default when you activate the platform on first login. This helps Red Hat improve the product by delivering you a much better user experience. You can opt out after activating Ansible Automation Platform by taking the following steps:

1. From the navigation panel, select Settings → Automation Execution → System.
2. Clear the **Gather data for Automation Analytics** option.
3. Click Save.

**Procedure**

1. Log in to Red Hat Ansible Automation Platform.

2. Select the **Service Account** tab in the subscription wizard.

3. Enter your **Client ID** and **Client secret**.

4. Select your subscription from the **Subscription** list.


Note
You can also enter your Satellite username and password in the **Satellite** tab if your cluster nodes are registered to Satellite through Subscription Manager.

5. Review the End User License Agreement and select **I agree to the End User License Agreement**.

6. Click Finish.

**Verification**

After your subscription has been accepted, subscription details are displayed. A status of *Compliant* indicates your subscription is in compliance with the number of hosts you have automated within your subscription count. Otherwise, your status shows as *Out of Compliance*, indicating you have exceeded the number of hosts in your subscription. Other important information displayed include the following:

Hosts automated
Host count automated by the job, which consumes the license count

Hosts imported
Host count considering all inventory sources (does not impact hosts remaining)

Hosts remaining
Total host count minus hosts automated

#### 1.2.6.2. Activate with a manifest file

If you have a subscriptions manifest, you can upload the manifest file by using the Red Hat Ansible Automation Platform interface.

Note

You are opted in for Automation Analytics by default when you activate the platform on first login. This helps Red Hat improve the product by delivering you a much better user experience. You can opt out after activating Ansible Automation Platform by taking the following steps:

1. From the navigation panel, select Settings → Automation Execution → System.
2. Clear the **Gather data for Automation Analytics** option.
3. Click Save.

**Prerequisites**

You must have a Red Hat subscription manifest file exported from the Red Hat Customer Portal. For more information, see [Obtaining a manifest file](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/assembly-gateway-licensing#assembly-aap-obtain-manifest-files).

**Procedure**

1. Log in to Red Hat Ansible Automation Platform.


1. If you are not immediately taken to the subscription wizard, go to Settings → Subscription.

2. Select the **Subscription manifest** tab.

3. Click Browse and select your manifest file.

4. Review the End User License Agreement and select **I agree to the End User License Agreement**.

5. Click Finish.


Note
If the BROWSE button is disabled on the subscription wizard page, clear the **USERNAME** and **PASSWORD** fields.

**Verification**

After your subscription has been accepted, subscription details are displayed. A status of *Compliant* indicates your subscription is in compliance with the number of hosts you have automated within your subscription count. Otherwise, your status shows as *Out of Compliance*, indicating you have exceeded the number of hosts in your subscription. Other important information displayed include the following:

Hosts automated
Host count automated by the job, which uses the subscription count

Hosts imported
Host count considering all inventory sources (does not impact hosts remaining)

Hosts remaining
Total host count minus hosts automated

**Next steps**

- You can return to the subscription wizard by selecting Settings → Subscription from the navigation panel and clicking Edit subscription.

