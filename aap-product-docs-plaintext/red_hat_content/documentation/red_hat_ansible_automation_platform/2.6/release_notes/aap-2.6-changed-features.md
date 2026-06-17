# Chapter 6. Changed features

Changed features are not deprecated and will continue to be supported until further notice.

The following table provides information about features that are changed in Ansible Automation Platform 2.6:

| Component | Feature |
| --- | --- |
| <br>  Platform gateway | <br>  The determination for matching to existing user records upon login has changed from previous versions. The new process leverages email address as the primary matching criteria for existing user accounts across multiple authentication methods. See [Access Management](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/access_management_and_authentication/index) for more details. Within 2.5, each authentication method would result in a user record being created regardless of the email matching from the different IdP sources. |
| <br>  Platform-operator,    Ansible Automation Platform Hub Operator | <br>  Added `postgres_extra_settings` to Ansible Automation Platform operators to apply PostgreSQL configuration file level changes to managed Postgres. |
| <br>  Platform-operator,    Event-Driven Ansible | <br>  Added `postgres_extra_settings` to Ansible Automation Platform operators to apply PostgreSQL configuration file level changes to managed Postgres. |
| <br>  Platform-operator,    gateway-operator | <br>  Added `postgres_extra_settings` to Ansible Automation Platform operators to apply PostgreSQL configuration file level changes to managed Postgres. |

