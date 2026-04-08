# 1. Types of workloads
## 1.3. Primary workloads for automation controller
### 1.3.1. Automation controller project synchronization




Users define the source of automation content within the automation controller projects, such as Ansible Playbooks. The primary workload for these projects is synchronization. Project update jobs in the API manage synchronization. These jobs are also known as source control updates in the UI.

These project update jobs run only on the control plane and in task pods within the OpenShift Container Platform. Their role is to update the automation controller with the latest automation content from its defined source, such as a Git repository.

Updating projects is not performance-sensitive, provided that they store only playbooks and Ansible-related text files. However, issues might arise when projects become excessively large. Do not store large volumes of binary data within a project. If jobs require access to additional data, retrieve this data from object storage or file storage within the playbook’s scope.

