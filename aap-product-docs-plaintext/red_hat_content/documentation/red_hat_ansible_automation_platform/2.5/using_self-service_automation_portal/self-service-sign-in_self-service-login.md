# 2. Logging in to self-service automation portal
## 2.1. Signing in to self-service automation portal




**Prerequisites**

1. You have configured an OAuth application in Ansible Automation Platform for self-service automation portal.
1. You have configured a user account in Ansible Automation Platform.


**Procedure**

1. In a browser, navigate to the URL for self-service automation portal to open the sign-in page.

![Self-service sign-in page](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_self-service_automation_portal-en-US/images/7301d2b380047719b3fda17728454b83/self-service-sign-in-page.png)



1. ClickSign In.
1. The sign-in page for Ansible Automation Platform appears:

![Ansible Automation Platform sign-in page](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_self-service_automation_portal-en-US/images/cd442c9292d68a910b63db55552d026f/rhaap-sign-in-page.png)



1. Enter your Ansible Automation Platform credentials and click **Log in** .
1. The self-service automation portal web console opens.


**Troubleshooting**

If your are using custom SSL certificates and when attempting to log in to self-service automation portal, it displays the error:


`Login failed; caused by Error: Failed to send POST request: fetch failed`

You must disable SSL validation in the Helm chart configuration.

1. In the self-service automation portal Helm chart, locate the `    checkSSL` parameter and set its value to `    false` :


```
upstream:        backstage:          appConfig:            ansible:              creatorService:                baseUrl: 127.0.0.1                port: '8000'              rhaap:                baseUrl: '${AAP_HOST_URL}'                checkSSL: false &lt;-- Update this to false                token: '${AAP_TOKEN}'
```


1. Apply the updated configuration by upgrading the self-service automation portal Helm chart to allow users to log in.


