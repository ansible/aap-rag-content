# 5. Migrating Red Hat Ansible Automation Platform to Red Hat Ansible Automation Platform Operator
## 5.3. Migrating data to the Ansible Automation Platform Operator




When migrating a 2.5 containerized or RPM installed deployment to OpenShift Container Platform you must create a secret with credentials to access the PostgreSQL database from the original deployment, then specify it when creating the Ansible Automation Platform object.

Important
The operator does not support Event-Driven Ansible migration at this time.



**Prerequisites**

You have completed the following procedures:


-  [Installing the Red Hat Ansible Automation Platform Operator on Red Hat OpenShift](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/installing_on_openshift_container_platform/index#install-aap-operator_operator-platform-doc)
-  [Creating a secret key](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/installing_on_openshift_container_platform/index#create-secret-key-secret_aap-migration)
-  [Creating a postgresql configuration secret](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/installing_on_openshift_container_platform/index#create-postresql-secret_aap-migration)
-  [Verifying network connectivity](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/installing_on_openshift_container_platform/index#verify-network-connectivity_aap-migration)


