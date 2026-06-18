# OpenStack credential type

Select this credential type to enable synchronization of cloud inventory with OpenStack.

Enter the following information for OpenStack credentials:

- **Username**: The username to use to connect to OpenStack.
- **Password (API Key)**: The password or API key to use to connect to OpenStack.
- **Host (Authentication URL)**: The host to be used for authentication.
- **Project (Tenant Name)**: The Tenant name or Tenant ID used for OpenStack. This value is usually the same as the username.
- Optional: **Project (Domain Name)**: Give the project name associated with your domain.
- Optional: **Domain Name**: Give the FQDN to be used to connect to OpenStack.
- Optional: **Region Name**: Give the region name. For some cloud providers, such as OVH, the region must be specified.


If you are interested in using OpenStack Cloud Credentials, see [Associate cloud credentials with a job template](/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-con_controller_cloud_credentials#controller-cloud-credentials "Automation controller can use Cloud Credentials to authenticate to cloud providers."), which includes a sample playbook.
