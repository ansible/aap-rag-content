# 1. Introduction to Red Hat Ansible Automation Platform on Microsoft Azure
## 1.5. Ansible Automation Platform on Microsoft Azure infrastructure usage




When you install Ansible Automation Platform on Microsoft Azure, you deploy the following infrastructure into your Microsoft Azure subscription:

Exact infrastructure usage depends on the length of time that the managed application is deployed in your tenancy, and the automation requirements that might cause the Kubernetes cluster to autoscale to meet the demands of your workload.

Microsoft provides a [Pricing calculator](https://azure.microsoft.com/en-us/pricing/calculator/) to estimate your costs for Microsoft Azure products and services. Red Hat has configured an example scenario in the pricing calculator: use the [Red Hat Ansible Automation Platform on Azure Infrastructure Estimate](https://azure.com/e/d12a08795a4942c1801c610810791764) to tune Kubernetes expected auto scaling variables based on your organization’s workloads.

If Red Hat determines that a deployment’s automation might exceed the capabilities of the current tier of the deployment, then Red Hat site reliability engineers will work with you to upgrade the infrastructure tier based on automation needs.

