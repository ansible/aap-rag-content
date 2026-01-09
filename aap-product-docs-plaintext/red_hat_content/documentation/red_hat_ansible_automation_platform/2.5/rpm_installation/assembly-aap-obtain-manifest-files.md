# 1. Red Hat Ansible Automation Platform installation overview
## 1.4. Managing Ansible Automation Platform subscriptions, updates, and support
### 1.4.5. Obtaining a manifest file




You can obtain a subscription manifest in the [Subscription Allocations](https://access.redhat.com/management/subscription_allocations/) section of Red Hat Subscription Management.

After you obtain a subscription allocation, you can download its manifest file and upload it to activate Ansible Automation Platform.

To begin, log in to the [Red Hat Customer Portal](https://access.redhat.com/) by using your administrator user account and follow the procedures listed.

#### 1.4.5.1. Create a subscription allocation




With a new subscription allocation you can set aside subscriptions and entitlements for a system that is currently offline or air-gapped. This is necessary before you can download its manifest and upload it to Ansible Automation Platform.

**Procedure**

1. From the [Subscription Allocations](https://access.redhat.com/management/subscription_allocations/) page, clickNew Subscription Allocation.
1. Enter a name for the allocation so that you can find it later.
1. Select **Type: Satellite 6.16** as the management application.
1. ClickCreate.


#### 1.4.5.2. Adding subscriptions to a subscription allocation




After you create an allocation, you can add the subscriptions you need for Ansible Automation Platform to run properly. This step is necessary before you can download the manifest and add it to Ansible Automation Platform.

**Procedure**

1. From the [Subscription Allocations](https://access.redhat.com/management/subscription_allocations/) page, click the name of the **Subscription Allocation** to which you want to add a subscription.
1. Click the **Subscriptions** tab.
1. ClickAdd Subscriptions.
1. Enter the number of Ansible Automation Platform Entitlements you plan to add.
1. ClickSubmit.


#### 1.4.5.3. Downloading a manifest file




After you create an allocation with the appropriate subscriptions on it, you can download the manifest file from Red Hat Subscription Management.

**Procedure**

1. From the [Subscription Allocations](https://access.redhat.com/management/subscription_allocations/) page, click the name of the **Subscription Allocation** to which you want to generate a manifest.
1. Click the **Subscriptions** tab.
1. ClickExport Manifestto download the manifest file.

This downloads a file `    manifest_&lt;allocation name&gt;_&lt;date&gt;.zip` to your default downloads folder.




