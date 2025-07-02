# 1. Red Hat Ansible Automation Platform installation overview
## 1.2. Managing Ansible Automation Platform licensing, updates and support
### 1.2.6. Obtaining a manifest file




You can obtain a subscription manifest in the [Subscription Allocations](https://access.redhat.com/management/subscription_allocations/) section of Red Hat Subscription Management. After you obtain a subscription allocation, you can download its manifest file and upload it to activate Ansible Automation Platform.

To begin, login to the [Red Hat Customer Portal](https://access.redhat.com/) using your administrator user account and follow the procedures in this section.

#### 1.2.6.1. Create a subscription allocation




Creating a new subscription allocation allows you to set aside subscriptions and entitlements for a system that is currently offline or air-gapped. This is necessary before you can download its manifest and upload it to Ansible Automation Platform.

**Procedure**

1. From the [Subscription Allocations](https://access.redhat.com/management/subscription_allocations/) page, clickNew Subscription Allocation.
1. Enter a name for the allocation so that you can find it later.
1. Select **Type: Satellite 6.16** as the management application.
1. ClickCreate.


**Next steps**

-  [Add the subscriptions](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/rpm_installation/index#proc-add-merge-subscriptions) needed for Ansible Automation Platform to run properly.


#### 1.2.6.2. Adding subscriptions to a subscription allocation




Once an allocation is created, you can add the subscriptions you need for Ansible Automation Platform to run properly. This step is necessary before you can download the manifest and add it to Ansible Automation Platform.

**Procedure**

1. From the [Subscription Allocations](https://access.redhat.com/management/subscription_allocations/) page, click on the name of the **Subscription Allocation** to which you would like to add a subscription.
1. Click the **Subscriptions** tab.
1. ClickAdd Subscriptions.
1. Enter the number of Ansible Automation Platform Entitlement(s) you plan to add.
1. ClickSubmit.


**Next steps**

-  [Download the manifest file](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/rpm_installation/index#proc-aap-generate-manifest-file) from Red Hat Subscription Management.


#### 1.2.6.3. Downloading a manifest file




After an allocation is created and has the appropriate subscriptions on it, you can download the manifest from Red Hat Subscription Management.

**Procedure**

1. From the [Subscription Allocations](https://access.redhat.com/management/subscription_allocations/) page, click on the name of the **Subscription Allocation** to which you would like to generate a manifest.
1. Click the **Subscriptions** tab.
1. ClickExport Manifestto download the manifest file.

This downloads a file _manifest_ <allocation name>_<date>.zip_ to your default downloads folder.




**Next steps**

-  [Upload the manifest file](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/access_management_and_authentication/assembly-gateway-licensing#proc-aap-activate-with-manifest) to activate Red Hat Ansible Automation Platform.


