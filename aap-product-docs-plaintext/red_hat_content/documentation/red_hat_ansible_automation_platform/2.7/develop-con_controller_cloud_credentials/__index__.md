# Associate cloud credentials with a job template

Automation controller can use Cloud Credentials to authenticate to cloud providers.

Cloud Credentials can be used when syncing a cloud inventory. They can also be associated with a job template and included in the runtime environment for use by a playbook. The following Cloud Credentials are supported:

- Openstack
- Amazon Web Services
- Google
- Azure
- VMware

## OpenStack

Use this credential type to connect to OpenStack clouds. Automation controller uses the OpenStack SDK to interact with OpenStack clouds. When you create an OpenStack cloud credential, the controller prompts you for the following information:

- **Username**: The username to authenticate to the OpenStack cloud.
- **Password**: The password to authenticate to the OpenStack cloud.
- **Project name**: The project name (also called tenant name) to use when connecting to the OpenStack cloud.
- **Auth URL**: The authentication URL for the OpenStack cloud.
- **Cloud name**: The name of the cloud as defined in your OpenStack clouds.yaml file.
- **Region name** (optional): The region name to use when connecting to the OpenStack cloud.
- **Domain name** (optional): The domain name to use when connecting to the OpenStack cloud.
- **Project domain name** (optional): The project domain name to use when connecting to the OpenStack cloud.
- **Validate SSL certificate**: Select this option to validate the SSL/TLS certificate presented by the OpenStack cloud. Clear this option to disable SSL/TLS certificate validation.


The following sample playbook invokes the `nova_compute` Ansible OpenStack cloud module and requires credentials:

-  `auth_url`
-  `username`
-  `password`
-  `project name`


These fields are made available to the playbook through the environmental variable `OS_CLIENT_CONFIG_FILE`, which points to a YAML file written by the controller based on the contents of the cloud credential. The following sample playbooks load the YAML file into the Ansible variable space:

- OS_CLIENT_CONFIG_FILE example:

```
clouds:
devstack:
auth:
auth_url: http://devstack.yoursite.com:5000/v2.0/
username: admin
password: your_password_here
project_name: demo
```


- Playbook example:

```
- hosts: all
gather_facts: false
vars:
config_file: "{{ lookup('env', 'OS_CLIENT_CONFIG_FILE') }}"
nova_tenant_name: demo
nova_image_name: "cirros-0.3.2-x86_64-uec"
nova_instance_name: autobot
nova_instance_state: 'present'
nova_flavor_name: m1.nano


nova_group:
group_name: antarctica
instance_name: deceptacon
instance_count: 3
tasks:
- debug: msg="{{ config_file }}"
- stat: path="{{ config_file }}"
register: st
- include_vars: "{{ config_file }}"
when: st.stat.exists and st.stat.isreg


- name: "Print out clouds variable"
debug: msg="{{ clouds|default('No clouds found') }}"


- name: "Setting nova instance state to: {{ nova_instance_state }}"
local_action:
module: nova_compute
login_username: "{{ clouds.devstack.auth.username }}"
login_password: "{{ clouds.devstack.auth.password }}"
```

## Amazon Web Services

Amazon Web Services (AWS) cloud credentials are exposed as the following environment variables during playbook execution (in the job template, choose the cloud credential needed for your setup):

-  `AWS_ACCESS_KEY_ID`
-  `AWS-SECRET_ACCESS_KEY`


Each AWS module implicitly uses these credentials when run through the controller without having to set the `aws_access_key_id` or `aws_secret_access_key` module options.

## Google

Use this credential type to authenticate to Google Cloud Platform services. Automation controller supports Google Cloud credentials for use with Ansible modules that manage Google Cloud resources.

Google cloud credentials are exposed as the following environment variables during playbook execution (in the job template, choose the cloud credential needed for your setup):

-  `GCE_EMAIL`
-  `GCE_PROJECT`
-  `GCE_CREDENTIALS_FILE_PATH`


Each Google module implicitly uses these credentials when run through the controller without having to set the `service_account_email`, `project_id`, or `pem_file` module options.

## Azure

Automation controller includes built-in support for managing Microsoft Azure cloud resources.

Azure cloud credentials exist as the following environment variables during playbook execution (in the job template, select the cloud credential needed for your setup):

-  `AZURE_SUBSCRIPTION_ID`
-  `AZURE_CERT_PATH`


Each Azure module uses these credentials when run using automation controller without having to set the `subscription_id` or `management_cert_path` module options.

## VMware

Automation controller integrates with VMware vSphere to manage virtual machines (VMs) as part of its infrastructure. This integration allows users to automate the provisioning, management, and decommissioning of VMs within a VMware environment.

VMware cloud credentials are exposed as the following environment variables during playbook execution (in the job template, choose the cloud credential needed for your setup):

-  `VMWARE_USER`
-  `VMWARE_PASSWORD`
-  `VMWARE_HOST`


The following sample playbook demonstrates the usage of these credentials:

```
- vsphere_guest:
vcenter_hostname: "{{ lookup('env', 'VMWARE_HOST') }}"
username: "{{ lookup('env', 'VMWARE_USER') }}"
password: "{{ lookup('env', 'VMWARE_PASSWORD') }}"
guest: newvm001
from_template: yes
template_src: linuxTemplate
cluster: MainCluster
resource_pool: "/Resources"
vm_extra_config:
folder: MyFolder
```
