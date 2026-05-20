# 3. Setting up Red Hat Ansible Automation Platform Service on AWS
## 3.1. Accepting a Public offer

To set up Red Hat Ansible Automation Platform Service on AWS you must link your Amazon Web Services (AWS) and Red Hat accounts through the AWS Marketplace.

When you link your accounts you can provision and configure your cluster through the Red Hat Hybrid Cloud Console.

**Prerequisites**

- An AWS Account

**Procedure**

1. Log in to your AWS account.

2. Navigate to the **Discover products** page of the AWS Marketplace. If you have already accepted your offer you can find it in the **Manage subscriptions** page.

3. In the search field search for "Red Hat Ansible Automation Platform Service on AWS".


- Depending on your region select one of the following:


- For EMEA, select **Red Hat Limited**.
- For the rest of the world, select **Red Hat**.

4. Click View purchase options.

5. Select your desired contract duration.

6. If you would like your contract to auto renew, click auto renewal settings.

7. Select the contract options.

8. Optional: Add a purchase order number.

9. Click Create contract.

10. Select Click here to set up your account. This redirects you to Red Hat Single Sign-On where you must:


1. Create or sign into your Red Hat account.
2. Connect your AWS account to the Red Hat account. This redirects you to the **Provision environment** page on the Red Hat Hybrid Cloud Console. Here you can start configuring your environment.

11. Enter your AWS account ID and click Verify.


- This account ID must be the account ID that purchased the offer from the AWS Marketplace. The system does not recognize associated or nested accounts.

12. After your AWS ID is validated click Next.

13. Select your required region.

14. Click Provision.

**Verification**

This redirects you to the **Environment details** page of the **Instances**, where you can see all the details of your created instance. Here you can check whether your instance is **Ready** or still in a **Provision in progress** state.

Provisioning your environment can take up to two hours. When it is ready, you will receive a confirmation email at the address linked to your account.

Important

Update your password as soon as possible. The confirmation email includes a link to your admin password, which you will use to log in and change your password. This link is one-time use, so be prepared before clicking it.

If you did not receive the email or the initial admin password has expired, you must submit a [support ticket](https://access.redhat.com/support) and the Red Hat team will assist you with next steps.

