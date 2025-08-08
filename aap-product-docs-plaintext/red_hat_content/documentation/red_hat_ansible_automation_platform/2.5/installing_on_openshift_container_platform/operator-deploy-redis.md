# 3. Configuring Red Hat Ansible Automation Platform components on Red Hat Ansible Automation Platform Operator
## 3.4. Deploying clustered Redis on Red Hat Ansible Automation Platform Operator




When you create an Ansible Automation Platform instance through the Ansible Automation Platform Operator, standalone Redis is assigned by default. To deploy clustered Redis, use the following procedure.

For more information about Redis, refer to Caching and queueing system in the _Planning your installation_ guide.

**Prerequisites**

- You have installed an Ansible Automation Platform Operator deployment.


**Procedure**

1. Log in to Red Hat OpenShift Container Platform.
1. Navigate toOperators→Installed Operators.
1. Select your Ansible Automation Platform Operator deployment.
1. Select the **Details** tab.
1. On the **Ansible Automation Platform** tile clickCreate instance.


1. For existing instances, you can edit the YAML view by clicking the ⋮ icon and thenEdit AnsibleAutomationPlatform.
1. Change the **redis_mode** value to "cluster".
1. ClickReload, thenSave.

1. Click to expand **Advanced configuration** .
1. For the **Redis Mode** list, select **Cluster** .
1. Configure the rest of your instance as necessary, then clickCreate.


**Verification**

Your instance deploys with a cluster Redis with 6 Redis replicas as default.


Note
You can modify your automation hub default redis cache PVC volume size, for help with this see, [Modifying the default redis cache PVC volume size automation hub](https://access.redhat.com/articles/7117186) .



