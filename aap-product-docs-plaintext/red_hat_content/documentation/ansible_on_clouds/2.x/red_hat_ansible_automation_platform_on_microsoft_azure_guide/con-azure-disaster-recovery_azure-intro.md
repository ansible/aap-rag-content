# 1. Introduction to Red Hat Ansible Automation Platform on Microsoft Azure
## 1.4. Disaster recovery




When you deploy Ansible Automation Platform on Microsoft Azure, you must enable or disable disaster recovery in the `Business Continuity` tab of the form. There is no default setting for disaster recovery.

The disaster recovery feature incurs additional Microsoft Azure infrastructure costs. See [Ansible Automation Platform on Microsoft Azure infrastructure usage](https://docs.redhat.com/en/documentation/ansible_on_clouds/2.x/html-single/red_hat_ansible_automation_platform_on_microsoft_azure_guide/index#con-azure-infrastructure-usage_azure-intro) for details of the Service Shape of the Storage account.

If you want to enable disaster recovery on an existing instance of Ansible Automation Platform on Microsoft Azure, contact Red Hat customer support.

The disaster recovery feature creates a nightly backup of your managed application and stores it in a business continuity region that is geographically distant to your primary region. For information about regional pairings, refer to [Azure cross-region replication pairings for all geographies](https://learn.microsoft.com/en-us/azure/reliability/cross-region-replication-azure#azure-cross-region-replication-pairings-for-all-geographies) in the Microsoft Azure reliability documentation.

For information about recovering your application after a service-impacting event, see the [Disaster recovery for Ansible Automation Platform on Microsoft Azure](https://access.redhat.com/articles/7010302) article on the Red Hat customer portal.

