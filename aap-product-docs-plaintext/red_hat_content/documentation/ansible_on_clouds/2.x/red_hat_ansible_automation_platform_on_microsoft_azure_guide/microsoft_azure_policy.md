# 6. Support for Red Hat Ansible Automation Platform on Microsoft Azure
## 6.3. Microsoft Azure Policy




In some situations, using Azure Policy to enforce, for example, tagging rules and conventions, can adversely affect the Resource Group where the components of Ansible Automation Platform on Microsoft Azure reside. The enforcement of Azure Policy could prevent changes, impact operations, or block deployment of new components in the Resource Group. These situations are identified by Red Hat during maintenance or daily operations. You must exclude the enforcement of Azure Policy, for example by using exceptions, on resources associated with the managed application.

For more information about working with Azure Policy, see the [Azure Policy and Ansible on Azure](https://access.redhat.com/articles/7013454) article on the Red Hat customer portal.

