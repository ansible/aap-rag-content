# Chapter 1. Overview of access management and authentication

Ansible Automation Platform features a platform interface where you can set up centralized authentication, configure access management, and configure global and system level settings from a single location.

The first time you log in to the Ansible Automation Platform, you must enter your subscription information to activate the platform. For more information about licensing and subscriptions, see *Managing Ansible Automation Platform licensing, updates and support* in the [RPM installation](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_installation/assembly-platform-install-overview#assembly-gateway-licensing), [Containerized installation](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/assembly-gateway-licensing), or [Installing on OpenShift Container Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/installing_on_openshift_container_platform/assembly-gateway-licensing-operator-copy) guide.

A system administrator can configure access, permissions and system settings through the following tasks:

- [Configuring authentication in the Ansible Automation Platform](#gw-configure-authentication "Chapter&nbsp;2.&nbsp;Configuring authentication in the Ansible Automation Platform"), where you set up simplified login for users by selecting from several authentication methods available and define permissions and assign them to users with authenticator maps.
- [Configuring access to external applications with token-based authentication](#gw-token-based-authentication "Chapter&nbsp;3.&nbsp;Configuring access to external applications with token-based authentication"), where you can configure authentication of third-party tools and services with the platform through integrated OAuth 2 token support.
- [Managing access with role based access control](#gw-managing-access "Chapter&nbsp;4.&nbsp;Managing access with role-based access control"), where you configure user access based on their role within a platform organization.
- [Configuring Ansible Automation Platform](#assembly-gw-settings "Chapter&nbsp;6.&nbsp;Configuring Ansible Automation Platform"), where you can configure global and system level settings for the platform and services.

