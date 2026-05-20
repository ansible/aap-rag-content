# 2. Installing Red Hat Ansible Automation Platform gateway on Red Hat OpenShift Container Platform
## 2.2. Deploying the platform gateway with existing Ansible Automation Platform components

You can link any components of the Ansible Automation Platform, that you have already installed to a new **Ansible Automation Platform** instance.

The following procedure simulates a scenario where you have automation controller as an existing component and want to add automation hub and Event-Driven Ansible.

**Procedure**

1. Log in to Red Hat OpenShift Container Platform.

2. Navigate to Operators → Installed Operators.

3. Select your Ansible Automation Platform Operator deployment.

4. Click Subscriptions and edit your **Update channel** to **stable-2.6**.

5. Click Details and on the **Ansible Automation Platform** tile click Create instance.

6. From the **Create Ansible Automation Platform** page enter a name for your instance in the **Name** field.


- When deploying an Ansible Automation Platform instance, ensure that `auto_update` is set to the default value of `false` on your existing automation controller instance in order for the integration to work.

7. Click YAML view and copy in the following:

apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
name: example-aap
namespace: aap
spec:
database:
resource_requirements:
requests:
cpu: 200m
memory: 512Mi
storage_requirements:
requests:
storage: 100Gi

# Platform
image_pull_policy: IfNotPresent

# Components
controller:
disabled: false
name: existing-controller-name
eda:
disabled: false
hub:
disabled: false
## uncomment if using file storage for Content pod
storage_type: file
file_storage_storage_class: <your-read-write-many-storage-class>
file_storage_size: 10Gi

## uncomment if using S3 storage for Content pod
# storage_type: S3
# object_storage_s3_secret: example-galaxy-object-storage

## uncomment if using Azure storage


1. For new components, if you do not specify a name, a default name is generated.

8. Click Create.

9. To access your new instance, see [Accessing the platform gateway](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/installing_on_openshift_container_platform/index#operator-access-aap_install-aap-gateway).


Note
If you have an existing controller with a managed Postgres pod, after creating the **Ansible Automation Platform** resource your automation controller instance will continue to use that original Postgres pod. If you were to do a fresh install you would have a single Postgres managed pod for all instances.

