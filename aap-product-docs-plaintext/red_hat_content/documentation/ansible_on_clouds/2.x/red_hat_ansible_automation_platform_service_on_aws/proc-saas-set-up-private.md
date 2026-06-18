# 3. Setting up Red Hat Ansible Automation Platform Service on AWS
## 3.2. Accepting a Private offer

A private offer is sent to you directly from a Red Hat seller. A private offer includes specific pricing and licensing terms for your account and has an expiration date. If you do not accept the offer by that date, you will either be moved to the public offer for the product or no longer subscribed to it.

**Prerequisites**

- An AWS Account

- A Red Hat seller issues you a purchase order and provides it to you by email.


* For manual steps see [Viewing and subscribing to a private offer](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-private-offers.html#buyer-private-offers-subscribing) page on the AWS Marketplace

**Procedure**

1. Click the link in the private offer email to accept the terms.

2. Log in to your AWS account.

3. Navigate to the **Private Offers** page of the AWS Marketplace. If you have already accepted your offer you can find it in the **Manage subscriptions** page.

4. Click the URL under the **Offer ID** column. This redirects you to the **Offer Selection** page.

5. Click Create contract.

6. Select Click Set up your account. This redirects you to Red Hat Single Sign-On where you must:


1. Create or sign into your Red Hat account.

2. Connect your AWS account to the Red Hat account.


1. If you are connecting to your accounts for the first time you must accept the terms and conditions and click Connect accounts. This redirects you to the **Provision environment** page on the Red Hat Hybrid Cloud Console. Here you can start configuring your environment.

7. Enter your AWS account ID and click Verify.


- This account ID must be the account ID that purchased the offer from the AWS Marketplace. The system does not recognize associated or nested accounts.

8. After your AWS ID is validated click Next.

9. Select your required region and click Next.

10. Click Provision.

**Verification**

This redirects you to the **Environment details** page of the **Instances**, where you can see all the details of your created instance. Here you can check whether your instance is **Ready** or still in a **Provision in progress** state.

Provisioning your environment can take up to two hours. When it is ready, you will receive a confirmation email at the address linked to your account.

Important

Update your password as soon as possible. The confirmation email includes a link to your admin password, which you will use to log in and change your password. This link is one-time use, so be prepared before clicking it.

If you did not receive the email or the initial admin password has expired, you must submit a [support ticket](https://access.redhat.com/support) and the Red Hat team will assist you with next steps.

