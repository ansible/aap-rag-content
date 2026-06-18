# Configure Redis

When you create an Ansible Automation Platform instance through the Ansible Automation Platform Operator, standalone Redis is assigned by default. If you would prefer to deploy clustered Redis, you can use the following procedure.

## Before you begin

- You have installed an Ansible Automation Platform Operator deployment.

## About this task

Important:

Switching Redis modes on an existing instance is not supported and can lead to unexpected consequences, including data loss. To change the Redis mode, you must deploy a new instance.

## Procedure

1.  Log in to Red Hat OpenShift Container Platform.
2.  Navigate to Operators> (and then)Installed Operators.
3.  Select your Ansible Automation Platform Operator deployment.
4.  Select the **Details** tab.
5.  On the **Ansible Automation Platform** tile click Create instance.   1.  For existing instances, you can edit the YAML view by clicking the ⋮ icon and then Edit AnsibleAutomationPlatform.
2.  Change the **redis_mode** value to "cluster".
3.  Click Reload, then Save.
6.  Click to expand **Advanced configuration**.
7.  For the **Redis Mode** list, select **Cluster**.
8.  Configure the rest of your instance as necessary, then click Create.

## Results

Your instance deploys with a cluster Redis with 6 Redis replicas as default.

Note:

You can modify your automation hub default redis cache PVC volume size, for help with this see, [Modifying the default redis cache PVC volume size automation hub](https://access.redhat.com/articles/7117186).
