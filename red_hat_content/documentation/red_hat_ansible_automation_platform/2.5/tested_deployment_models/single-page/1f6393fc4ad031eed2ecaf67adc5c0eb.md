+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.5/html-single/tested_deployment_models/index"
title = "Tested deployment models - Red Hat Ansible Automation Platform 2.5"

[extra]
modified = "2025-08-07T13:56:07.000Z"
multi_page_path = "/documentation/en-us/red_hat_ansible_automation_platform/2.5/html/tested_deployment_models/index/"
name = "Tested deployment models"
page_slug = "tested_deployment_models"
product = "Red Hat Ansible Automation Platform"
product_version = "2.5"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/tested_deployment_models/index"
type = "single-page"
+++


<span id="idm139937748112064"></span>
Red Hat Ansible Automation Platform2.5
## Plan your deployment of Ansible Automation Platform


Red Hat Customer Content Services

 [Legal Notice](#idm139937756252704) 
 **Abstract** 

This guide provides the Red Hat tested and supported topologies for Red Hat Ansible Automation Platform.




---

# Providing feedback on Red Hat documentation




If you have a suggestion to improve this documentation, or find an error, you can contact technical support at [https://access.redhat.com](https://access.redhat.com) to open a request.

# Chapter 1. Overview of tested deployment models




Red Hat tests Ansible Automation Platform 2.5 with a defined set of topologies to give you opinionated deployment options. Deploy all components of Ansible Automation Platform so that all features and capabilities are available for use without the need to take further action.

Red Hat tests the installation of Ansible Automation Platform 2.5 based on a defined set of infrastructure topologies or reference architectures. Enterprise organizations can use one of the enterprise topologies for production deployments to ensure the highest level of uptime, performance, and continued scalability. Organizations or deployments that are resource constrained can use a growth topology.

It is possible to install Ansible Automation Platform on different infrastructure topologies and with different environment configurations. Red Hat does not fully test topologies outside of published reference architectures. Red Hat recommends using a tested topology for all new deployments and provides commercially reasonable support for deployments that meet minimum requirements.

## 1.1. Installation and deployment models




The following table outlines the different ways to install or deploy Ansible Automation Platform:


<span id="idm139937757102656"></span>
 **Table 1.1. Ansible Automation Platform installation and deployment models** 

| Mode | Infrastructure | Description | Tested topologies |
| --- | --- | --- | --- |
| RPM | Virtual machines and bare metal | The RPM installer deploys Ansible Automation Platform on Red Hat Enterprise Linux by using RPMs to install the platform on host machines. Customers manage the product and infrastructure lifecycle. | -  [RPM growth topology](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/tested_deployment_models/rpm-topologies#rpm-a-env-a) 
-  [RPM enterprise topology](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/tested_deployment_models/rpm-topologies#rpm-b-env-a) |
| Containers | Virtual machines and bare metal | The containerized installer deploys Ansible Automation Platform on Red Hat Enterprise Linux by using Podman which runs the platform in containers on host machines. Customers manage the product and infrastructure lifecycle. | -  [Container growth topology](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/tested_deployment_models/container-topologies#cont-a-env-a) 
-  [Container enterprise topology](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/tested_deployment_models/container-topologies#cont-b-env-a) |
| Operator | Red Hat OpenShift | The Operator uses Red Hat OpenShift Operators to deploy Ansible Automation Platform within Red Hat OpenShift. Customers manage the product and infrastructure lifecycle. | -  [Operator growth topology](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/tested_deployment_models/ocp-topologies#ocp-a-env-a) 
-  [Operator enterprise topology](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/tested_deployment_models/ocp-topologies#ocp-b-env-a) |




# Chapter 2. RPM topologies




The RPM installer deploys Ansible Automation Platform on Red Hat Enterprise Linux by using RPMs to install the platform on host machines. Customers manage the product and infrastructure lifecycle.

## 2.1. RPM growth topology




The growth topology is intended for organizations that are getting started with Ansible Automation Platform and do not require redundancy or higher compute for large volumes of automation. This topology allows for smaller footprint deployments.

### 2.1.1. Infrastructure topology




The following diagram outlines the infrastructure topology that Red Hat has tested with this deployment model that customers can use when self-managing Ansible Automation Platform:


<span id="idm139937748143792"></span>
 **Figure 2.1. Infrastructure topology diagram** 

![RPM growth topology diagram](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Tested_deployment_models-en-US/images/a6bab844df620cd5ae45fac1ec8f2b85/rpm-a-env-a.png)




Each VM has been tested with the following component requirements:


<span id="idm139937748138992"></span>
 **Table 2.1. Virtual machine requirements** 

| Requirement | Minimum requirement |
| --- | --- |
| RAM | 16 GB |
| CPUs | 4 |
| Local disk | 60 GB |
| Disk IOPS | 3000 |





<span id="idm139937751633168"></span>
 **Table 2.2. Infrastructure topology** 

| VM count | Purpose | Example VM group names |
| --- | --- | --- |
| 1 | Platform gateway with colocated Redis |  `automationgateway` |
| 1 | Automation controller |  `automationcontroller` |
| 1 | Private automation hub |  `automationhub` |
| 1 | Event-Driven Ansible |  `automationedacontroller` |
| 1 | Automation mesh execution node |  `execution_nodes` |
| 1 | Ansible Automation Platform managed database |  `database` |




### 2.1.2. Tested system configurations




Red Hat has tested the following configurations to install and run Red Hat Ansible Automation Platform:


<span id="idm139937756946656"></span>
 **Table 2.3. Tested system configurations** 

| Type | Description |  |
| --- | --- | --- |
| Subscription | Valid Red Hat Ansible Automation Platform subscription |  |
| Operating system | - Red Hat Enterprise Linux 8.8 or later minor versions of Red Hat Enterprise Linux 8.
- Red Hat Enterprise Linux 9.2 or later minor versions of Red Hat Enterprise Linux 9. |  |
| CPU architecture | x86_64, AArch64, s390x (IBM Z), ppc64le (IBM Power) |  |
|  `ansible-core` |  `ansible-core` version 2.16 or later | Ansible Automation Platform uses the system-wide ansible-core package to install the platform, but uses ansible-core 2.16 for both its control plane and built-in execution environments. |
| Browser | A currently supported version of Mozilla Firefox or Google Chrome |  |
| Database | PostgreSQL 15 | External (customer supported) databases require ICU support. |




### 2.1.3. Network ports




Red Hat Ansible Automation Platform uses several ports to communicate with its services. These ports must be open and available for incoming connections to the Red Hat Ansible Automation Platform server for it to work. Ensure that these ports are available and are not blocked by the server firewall.


<span id="idm139937749852144"></span>
 **Table 2.4. Network ports and protocols** 

| Port number | Protocol | Service | Source | Destination |
| --- | --- | --- | --- | --- |
| 80/443 | TCP | HTTP/HTTPS | Event-Driven Ansible | Automation hub |
| 80/443 | TCP | HTTP/HTTPS | Event-Driven Ansible | Automation controller |
| 80/443 | TCP | HTTP/HTTPS | Automation controller | Automation hub |
| 80/443 | TCP | HTTP/HTTPS | Platform gateway | Automation controller |
| 80/443 | TCP | HTTP/HTTPS | Platform gateway | Automation hub |
| 80/443 | TCP | HTTP/HTTPS | Platform gateway | Event-Driven Ansible |
| 5432 | TCP | PostgreSQL | Event-Driven Ansible | Database |
| 5432 | TCP | PostgreSQL | Platform gateway | Database |
| 5432 | TCP | PostgreSQL | Automation hub | Database |
| 5432 | TCP | PostgreSQL | Automation controller | Database |
| 6379 | TCP | Redis | Event-Driven Ansible | Redis node |
| 6379 | TCP | Redis | Platform gateway | Redis node |
| 8443 | TCP | HTTPS | Platform gateway | Platform gateway |
| 27199 | TCP | Receptor | Automation controller | Execution node |




### 2.1.4. Example inventory file




Use the example inventory file to perform an installation for this topology:

```
# This is the Ansible Automation Platform installer inventory file intended for the RPM growth deployment topology.
# Consult the Ansible Automation Platform product documentation about this topology's tested hardware configuration.
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/tested_deployment_models/rpm-topologies
#
# Consult the docs if you are unsure what to add
# For all optional variables consult the Ansible Automation Platform documentation:
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_installation


# This section is for your platform gateway hosts
# -----------------------------------------------------
[automationgateway]
gateway.example.org

# This section is for your automation controller hosts
# -----------------------------------------------------
[automationcontroller]
controller.example.org

[automationcontroller:vars]
peers=execution_nodes

# This section is for your Ansible Automation Platform execution hosts
# -----------------------------------------------------
[execution_nodes]
exec.example.org

# This section is for your automation hub hosts
# -----------------------------------------------------
[automationhub]
hub.example.org

# This section is for your Event-Driven Ansible controller hosts
# -----------------------------------------------------
[automationedacontroller]
eda.example.org

# This section is for the Ansible Automation Platform database
# -----------------------------------------------------
[database]
db.example.org

[all:vars]

# Common variables
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_installation/appendix-inventory-files-vars#general-variables
# -----------------------------------------------------
registry_username=&lt;your RHN username&gt;
registry_password=&lt;your RHN password&gt;

redis_mode=standalone

# Platform gateway
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_installation/appendix-inventory-files-vars#platform-gateway-variables
# -----------------------------------------------------
automationgateway_admin_password=&lt;set your own&gt;
automationgateway_pg_host=db.example.org
automationgateway_pg_password=&lt;set your own&gt;

# Automation controller
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_installation/appendix-inventory-files-vars#controller-variables
# -----------------------------------------------------
admin_password=&lt;set your own&gt;
pg_host=db.example.org
pg_password=&lt;set your own&gt;

# Automation hub
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_installation/appendix-inventory-files-vars#hub-variables
# -----------------------------------------------------
automationhub_admin_password=&lt;set your own&gt;
automationhub_pg_host=db.example.org
automationhub_pg_password=&lt;set your own&gt;

# Event-Driven Ansible controller
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_installation/appendix-inventory-files-vars#event-driven-ansible-variables
# -----------------------------------------------------
automationedacontroller_admin_password=&lt;set your own&gt;
automationedacontroller_pg_host=db.example.org
automationedacontroller_pg_password=&lt;set your own&gt;
```

## 2.2. RPM enterprise topology




The enterprise topology is intended for organizations that require Ansible Automation Platform to be deployed with redundancy or higher compute for large volumes of automation.

### 2.2.1. Infrastructure topology




The following diagram outlines the infrastructure topology that Red Hat has tested with this deployment model that customers can use when self-managing Ansible Automation Platform:


<span id="idm139937748222720"></span>
 **Figure 2.2. Infrastructure topology diagram** 

![RPM enterprise topology diagram](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Tested_deployment_models-en-US/images/f2f3c928085ce3b7b53a92d554fbc14d/rpm-b-env-a.png)




Each VM has been tested with the following component requirements:


<span id="idm139937750574208"></span>
 **Table 2.5. Virtual machine requirements** 

| Requirement | Minimum requirement |
| --- | --- |
| RAM | 16 GB |
| CPUs | 4 |
| Local disk | 60 GB |
| Disk IOPS | 3000 |





<span id="idm139937752431552"></span>
 **Table 2.6. Infrastructure topology** 

| VM count | Purpose | Example VM group names |
| --- | --- | --- |
| 2 | Platform gateway with colocated Redis |  `automationgateway` |
| 2 | Automation controller |  `automationcontroller` |
| 2 | Private automation hub with colocated Redis |  `automationhub` |
| 2 | Event-Driven Ansible with colocated Redis |  `automationedacontroller` |
| 1 | Automation mesh hop node |  `execution_nodes` |
| 2 | Automation mesh execution node |  `execution_nodes` |
| 1 | Externally managed database service | N/A |
| 1 | HAProxy load balancer in front of platform gateway (externally managed) | N/A |




Note
- 6 VMs are required for a Redis high availability (HA) compatible deployment. Redis can be colocated on each Ansible Automation Platform component VM except for automation controller, execution nodes, or the PostgreSQL database.
- External Redis is not supported for RPM-based deployments of Ansible Automation Platform.




### 2.2.2. Tested system configurations




Red Hat has tested the following configurations to install and run Red Hat Ansible Automation Platform:


<span id="idm139937749927440"></span>
 **Table 2.7. Tested system configurations** 

| Type | Description |  |
| --- | --- | --- |
| Subscription | Valid Red Hat Ansible Automation Platform subscription |  |
| Operating system | - Red Hat Enterprise Linux 8.8 or later minor versions of Red Hat Enterprise Linux 8.
- Red Hat Enterprise Linux 9.2 or later minor versions of Red Hat Enterprise Linux 9. |  |
| CPU architecture | x86_64, AArch64, s390x (IBM Z), ppc64le (IBM Power) |  |
|  `ansible-core` |  `ansible-core` version 2.16 or later | Ansible Automation Platform uses the system-wide ansible-core package to install the platform, but uses ansible-core 2.16 for both its control plane and built-in execution environments. |
| Browser | A currently supported version of Mozilla Firefox or Google Chrome |  |
| Database | PostgreSQL 15 | External (customer supported) databases require ICU support. |




### 2.2.3. Network ports




Red Hat Ansible Automation Platform uses several ports to communicate with its services. These ports must be open and available for incoming connections to the Red Hat Ansible Automation Platform server for it to work. Ensure that these ports are available and are not blocked by the server firewall.


<span id="idm139937752891376"></span>
 **Table 2.8. Network ports and protocols** 

| Port number | Protocol | Service | Source | Destination |
| --- | --- | --- | --- | --- |
| 80/443 | TCP | HTTP/HTTPS | Event-Driven Ansible | Automation hub |
| 80/443 | TCP | HTTP/HTTPS | Event-Driven Ansible | Automation controller |
| 80/443 | TCP | HTTP/HTTPS | Automation controller | Automation hub |
| 80/443 | TCP | HTTP/HTTPS | HAProxy load balancer | Platform gateway |
| 80/443 | TCP | HTTP/HTTPS | Platform gateway | Automation controller |
| 80/443 | TCP | HTTP/HTTPS | Platform gateway | Automation hub |
| 80/443 | TCP | HTTP/HTTPS | Platform gateway | Event-Driven Ansible |
| 5432 | TCP | PostgreSQL | Event-Driven Ansible | External database |
| 5432 | TCP | PostgreSQL | Platform gateway | External database |
| 5432 | TCP | PostgreSQL | Automation hub | External database |
| 5432 | TCP | PostgreSQL | Automation controller | External database |
| 6379 | TCP | Redis | Event-Driven Ansible | Redis node |
| 6379 | TCP | Redis | Platform gateway | Redis node |
| 8443 | TCP | HTTPS | Platform gateway | Platform gateway |
| 16379 | TCP | Redis | Redis node | Redis node |
| 27199 | TCP | Receptor | Automation controller | Hop node and execution node |
| 27199 | TCP | Receptor | Hop node | Execution node |




### 2.2.4. Example inventory file




Use the example inventory file to perform an installation for this topology:

```
# This is the Ansible Automation Platform enterprise installer inventory file
# Consult the docs if you are unsure what to add
# For all optional variables consult the Red Hat documentation:
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_installation

# This section is for your platform gateway hosts
# -----------------------------------------------------
[automationgateway]
gateway1.example.org
gateway2.example.org

# This section is for your automation controller hosts
# -----------------------------------------------------
[automationcontroller]
controller1.example.org
controller2.example.org

[automationcontroller:vars]
peers=execution_nodes

# This section is for your Ansible Automation Platform execution hosts
# -----------------------------------------------------
[execution_nodes]
hop1.example.org node_type='hop'
exec1.example.org
exec2.example.org

# This section is for your automation hub hosts
# -----------------------------------------------------
[automationhub]
hub1.example.org
hub2.example.org

# This section is for your Event-Driven Ansible controller hosts
# -----------------------------------------------------
[automationedacontroller]
eda1.example.org
eda2.example.org

[redis]
gateway1.example.org
gateway2.example.org
hub1.example.org
hub2.example.org
eda1.example.org
eda2.example.org

[all:vars]
# Common variables
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_installation/appendix-inventory-files-vars#general-variables
# -----------------------------------------------------
registry_username=&lt;your RHN username&gt;
registry_password=&lt;your RHN password&gt;

# Platform gateway
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_installation/appendix-inventory-files-vars#platform-gateway-variables
# -----------------------------------------------------
automationgateway_admin_password=&lt;set your own&gt;
automationgateway_pg_host=&lt;set your own&gt;
automationgateway_pg_database=&lt;set your own&gt;
automationgateway_pg_username=&lt;set your own&gt;
automationgateway_pg_password=&lt;set your own&gt;

# Automation controller
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_installation/appendix-inventory-files-vars#controller-variables
# -----------------------------------------------------
admin_password=&lt;set your own&gt;
pg_host=&lt;set your own&gt;
pg_database=&lt;set your own&gt;
pg_username=&lt;set your own&gt;
pg_password=&lt;set your own&gt;

# Automation hub
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_installation/appendix-inventory-files-vars#hub-variables
# -----------------------------------------------------
automationhub_admin_password=&lt;set your own&gt;
automationhub_pg_host=&lt;set your own&gt;
automationhub_pg_database=&lt;set your own&gt;
automationhub_pg_username=&lt;set your own&gt;
automationhub_pg_password=&lt;set your own&gt;

# Event-Driven Ansible controller
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_installation/appendix-inventory-files-vars#event-driven-ansible-variables
# -----------------------------------------------------
automationedacontroller_admin_password=&lt;set your own&gt;
automationedacontroller_pg_host=&lt;set your own&gt;
automationedacontroller_pg_database=&lt;set your own&gt;
automationedacontroller_pg_username=&lt;set your own&gt;
automationedacontroller_pg_password=&lt;set your own&gt;
```

# Chapter 3. Container topologies




The containerized installer deploys Ansible Automation Platform on Red Hat Enterprise Linux by using Podman which runs the platform in containers on host machines. Customers manage the product and infrastructure lifecycle.

## 3.1. Container growth topology




The growth topology is intended for organizations that are getting started with Ansible Automation Platform and do not require redundancy or higher compute for large volumes of automation. This topology allows for smaller footprint deployments.

### 3.1.1. Infrastructure topology




The following diagram outlines the infrastructure topology that Red Hat has tested with this deployment model that customers can use when self-managing Ansible Automation Platform:


<span id="idm139937751581328"></span>
 **Figure 3.1. Infrastructure topology diagram** 

![Container growth topology diagram](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Tested_deployment_models-en-US/images/02b948e9d139f9a478e80ba4164dceae/cont-a-env-a.png)




A single VM has been tested with the following component requirements:


<span id="idm139937750446592"></span>
 **Table 3.1. Virtual machine requirements** 

| Requirement | Minimum requirement |
| --- | --- |
| RAM | 16 GB |
| CPUs | 4 |
| Local disk | - Total available disk space: 60 GB
- Installation directory: 15 GB (if on a dedicated partition)
-  `    /var/tmp` for online installations: 1 GB
-  `    /var/tmp` for offline or bundled installations: 3 GB
- Temporary directory (defaults to `    /tmp` ) for offline or bundled installations: 10GB |
| Disk IOPS | 3000 |




Note
If performing a bundled installation of the growth topology with `hub_seed_collections=true` , then 32 GB RAM is recommended. Note that with this configuration the install time is going to increase and can take 45 or more minutes alone to complete seeding the collections.




<span id="idm139937752586544"></span>
 **Table 3.2. Infrastructure topology** 

| Purpose | Example group names |
| --- | --- |
| All Ansible Automation Platform components | -  `    automationgateway` 
-  `    automationcontroller` 
-  `    automationhub` 
-  `    automationeda` 
-  `    database` |




### 3.1.2. Tested system configurations




Red Hat has tested the following configurations to install and run Red Hat Ansible Automation Platform:


<span id="idm139937750073040"></span>
 **Table 3.3. System configuration** 

| Type | Description | Notes |
| --- | --- | --- |
| Subscription | - Valid Red Hat Ansible Automation Platform subscription
- Valid Red Hat Enterprise Linux subscription (to consume the BaseOS and AppStream repositories) |  |
| Operating system | - Red Hat Enterprise Linux 9.2 or later minor versions of Red Hat Enterprise Linux 9.
- Red Hat Enterprise Linux 10 or later minor versions of Red Hat Enterprise Linux 10 for enterprise topologies. |  |
| CPU architecture | x86_64, AArch64, s390x (IBM Z), ppc64le (IBM Power) |  |
|  `ansible-core` | - For the installation: `    ansible-core` version 2.14.
- For Ansible Automation Platform operation: `    ansible-core` version 2.16. | - The installation program uses the `    ansible-core` 2.14 package from the RHEL 9 AppStream repository.
- Ansible Automation Platform bundles `    ansible-core` version 2.16 for its operation, so you do not need to install it manually. |
| Browser | A currently supported version of Mozilla Firefox or Google Chrome. |  |
| Database | PostgreSQL 15 | External (customer supported) databases require ICU support. |




### 3.1.3. Network ports




Red Hat Ansible Automation Platform uses several ports to communicate with its services. These ports must be open and available for incoming connections to the Red Hat Ansible Automation Platform server for it to work. Ensure that these ports are available and are not blocked by the server firewall.


<span id="idm139937751763264"></span>
 **Table 3.4. Network ports and protocols** 

| Port number | Protocol | Service | Source | Destination |
| --- | --- | --- | --- | --- |
| 80/443 | TCP | HTTP/HTTPS | Event-Driven Ansible | Automation hub |
| 80/443 | TCP | HTTP/HTTPS | Event-Driven Ansible | Automation controller |
| 80/443 | TCP | HTTP/HTTPS | Automation controller | Automation hub |
| 80/443 | TCP | HTTP/HTTPS | Platform gateway | Automation controller |
| 80/443 | TCP | HTTP/HTTPS | Platform gateway | Automation hub |
| 80/443 | TCP | HTTP/HTTPS | Platform gateway | Event-Driven Ansible |
| 5432 | TCP | PostgreSQL | Event-Driven Ansible | External database |
| 5432 | TCP | PostgreSQL | Platform gateway | External database |
| 5432 | TCP | PostgreSQL | Automation hub | External database |
| 5432 | TCP | PostgreSQL | Automation controller | External database |
| 6379 | TCP | Redis | Event-Driven Ansible | Redis container |
| 6379 | TCP | Redis | Platform gateway | Redis container |
| 8443 | TCP | HTTPS | Platform gateway | Platform gateway |
| 27199 | TCP | Receptor | Automation controller | Execution container |




### 3.1.4. Example inventory file




Use the example inventory file to perform an installation for this topology:

```
# This is the Ansible Automation Platform installer inventory file intended for the container growth deployment topology.
# This inventory file expects to be run from the host where Ansible Automation Platform will be installed.
# Consult the Ansible Automation Platform product documentation about this topology's tested hardware configuration.
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/tested_deployment_models/container-topologies
#
# Consult the docs if you are unsure what to add
# For all optional variables consult the included README.md
# or the Ansible Automation Platform documentation:
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation

# This section is for your platform gateway hosts
# -----------------------------------------------------
[automationgateway]
aap.example.org

# This section is for your automation controller hosts
# -----------------------------------------------------
[automationcontroller]
aap.example.org

# This section is for your automation hub hosts
# -----------------------------------------------------
[automationhub]
aap.example.org

# This section is for your Event-Driven Ansible controller hosts
# -----------------------------------------------------
[automationeda]
aap.example.org

# This section is for the Ansible Automation Platform database
# -----------------------------------------------------
[database]
aap.example.org

[all:vars]
# Ansible
ansible_connection=local

# Common variables
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation/appendix-inventory-files-vars#general-variables
# -----------------------------------------------------
postgresql_admin_username=postgres
postgresql_admin_password=&lt;set your own&gt;

registry_username=&lt;your RHN username&gt;
registry_password=&lt;your RHN password&gt;

redis_mode=standalone

# Platform gateway
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation/appendix-inventory-files-vars#platform-gateway-variables
# -----------------------------------------------------
gateway_admin_password=&lt;set your own&gt;
gateway_pg_host=aap.example.org
gateway_pg_password=&lt;set your own&gt;

# Automation controller
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation/appendix-inventory-files-vars#controller-variables
# -----------------------------------------------------
controller_admin_password=&lt;set your own&gt;
controller_pg_host=aap.example.org
controller_pg_password=&lt;set your own&gt;
controller_percent_memory_capacity=0.5

# Automation hub
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation/appendix-inventory-files-vars#hub-variables
# -----------------------------------------------------
hub_admin_password=&lt;set your own&gt;
hub_pg_host=aap.example.org
hub_pg_password=&lt;set your own&gt;
hub_seed_collections=false

# Event-Driven Ansible controller
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation/appendix-inventory-files-vars#event-driven-ansible-variables
# -----------------------------------------------------
eda_admin_password=&lt;set your own&gt;
eda_pg_host=aap.example.org
eda_pg_password=&lt;set your own&gt;
```

SSH keys are only required when installing on remote hosts. If doing a self contained local VM based installation, you can use `ansible_connection=local` .

## 3.2. Container enterprise topology




The enterprise topology is intended for organizations that require Ansible Automation Platform to be deployed with redundancy or higher compute for large volumes of automation.

### 3.2.1. Infrastructure topology




The following diagram outlines the infrastructure topology that Red Hat has tested with this deployment model that customers can use when self-managing Ansible Automation Platform:


<span id="idm139937750980464"></span>
 **Figure 3.2. Infrastructure topology diagram** 

![Container enterprise topology diagram](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Tested_deployment_models-en-US/images/704824d330eb8422156d4d7cf034ee52/cont-b-env-a.png)




Each VM has been tested with the following component requirements:


<span id="idm139937750975520"></span>
 **Table 3.5. Virtual machine requirements** 

| Requirement | Minimum requirement |
| --- | --- |
| RAM | 16 GB |
| CPUs | 4 |
| Local disk | - Total available disk space: 60 GB
- Installation directory: 15 GB (if on a dedicated partition)
-  `    /var/tmp` for online installations: 1 GB
-  `    /var/tmp` for offline or bundled installations: 3 GB
- Temporary directory (defaults to `    /tmp` ) for offline or bundled installations: 10GB |
| Disk IOPS | 3000 |





<span id="idm139937751709696"></span>
 **Table 3.6. Infrastructure topology** 

| VM count | Purpose | Example VM group names |
| --- | --- | --- |
| 2 | Platform gateway with colocated Redis |  `automationgateway` |
| 2 | Automation controller |  `automationcontroller` |
| 2 | Private automation hub with colocated Redis |  `automationhub` |
| 2 | Event-Driven Ansible with colocated Redis |  `automationeda` |
| 1 | Automation mesh hop node |  `execution_nodes` |
| 2 | Automation mesh execution node |  `execution_nodes` |
| 1 | Externally managed database service | N/A |
| 1 | HAProxy load balancer in front of platform gateway (externally managed) | N/A |




Note
- 6 VMs are required for a Redis high availability (HA) compatible deployment. When installing Ansible Automation Platform with the containerized installer, Redis can be colocated on any Ansible Automation Platform component VMs of your choice except for execution nodes or the PostgreSQL database. They might also be assigned VMs specifically for Redis use.
- External Redis is not supported for containerized Ansible Automation Platform.




### 3.2.2. Tested system configurations




Red Hat has tested the following configurations to install and run Red Hat Ansible Automation Platform:


<span id="idm139937750428592"></span>
 **Table 3.7. System configuration** 

| Type | Description | Notes |
| --- | --- | --- |
| Subscription | - Valid Red Hat Ansible Automation Platform subscription
- Valid Red Hat Enterprise Linux subscription (to consume the BaseOS and AppStream repositories) |  |
| Operating system | - Red Hat Enterprise Linux 9.2 or later minor versions of Red Hat Enterprise Linux 9.
- Red Hat Enterprise Linux 10 or later minor versions of Red Hat Enterprise Linux 10 for enterprise topologies. |  |
| CPU architecture | x86_64, AArch64, s390x (IBM Z), ppc64le (IBM Power) |  |
|  `ansible-core` | - For the installation: `    ansible-core` version 2.14.
- For Ansible Automation Platform operation: `    ansible-core` version 2.16. | - The installation program uses the `    ansible-core` 2.14 package from the RHEL 9 AppStream repository.
- Ansible Automation Platform bundles `    ansible-core` version 2.16 for its operation, so you do not need to install it manually. |
| Browser | A currently supported version of Mozilla Firefox or Google Chrome. |  |
| Database | PostgreSQL 15 | External (customer supported) databases require ICU support. |




### 3.2.3. Network ports




Red Hat Ansible Automation Platform uses several ports to communicate with its services. These ports must be open and available for incoming connections to the Red Hat Ansible Automation Platform server for it to work. Ensure that these ports are available and are not blocked by the server firewall.


<span id="idm139937748244752"></span>
 **Table 3.8. Network ports and protocols** 

| Port number | Protocol | Service | Source | Destination |
| --- | --- | --- | --- | --- |
| 80/443 | TCP | HTTP/HTTPS | Event-Driven Ansible | Automation hub |
| 80/443 | TCP | HTTP/HTTPS | Event-Driven Ansible | Automation controller |
| 80/443 | TCP | HTTP/HTTPS | Automation controller | Automation hub |
| 80/443 | TCP | HTTP/HTTPS | HAProxy load balancer | Platform gateway |
| 80/443 | TCP | HTTP/HTTPS | Platform gateway | Automation controller |
| 80/443 | TCP | HTTP/HTTPS | Platform gateway | Automation hub |
| 80/443 | TCP | HTTP/HTTPS | Platform gateway | Event-Driven Ansible |
| 5432 | TCP | PostgreSQL | Event-Driven Ansible | External database |
| 5432 | TCP | PostgreSQL | Platform gateway | External database |
| 5432 | TCP | PostgreSQL | Automation hub | External database |
| 5432 | TCP | PostgreSQL | Automation controller | External database |
| 6379 | TCP | Redis | Event-Driven Ansible | Redis node |
| 6379 | TCP | Redis | Platform gateway | Redis node |
| 8443 | TCP | HTTPS | Platform gateway | Platform gateway |
| 16379 | TCP | Redis | Redis node | Redis node |
| 27199 | TCP | Receptor | Automation controller | Hop node and execution node |
| 27199 | TCP | Receptor | Hop node | Execution node |




### 3.2.4. Example inventory file




Use the example inventory file to perform an installation for this topology:

```
# This is the Ansible Automation Platform enterprise installer inventory file
# Consult the docs if you are unsure what to add
# For all optional variables consult the included README.md
# or the Red Hat documentation:
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation

# This section is for your platform gateway hosts
# -----------------------------------------------------
[automationgateway]
gateway1.example.org
gateway2.example.org

# This section is for your automation controller hosts
# -----------------------------------------------------
[automationcontroller]
controller1.example.org
controller2.example.org

# This section is for your Ansible Automation Platform execution hosts
# -----------------------------------------------------
[execution_nodes]
hop1.example.org receptor_type='hop'
exec1.example.org
exec2.example.org

# This section is for your automation hub hosts
# -----------------------------------------------------
[automationhub]
hub1.example.org
hub2.example.org

# This section is for your Event-Driven Ansible controller hosts
# -----------------------------------------------------
[automationeda]
eda1.example.org
eda2.example.org

[redis]
gateway1.example.org
gateway2.example.org
hub1.example.org
hub2.example.org
eda1.example.org
eda2.example.org

[all:vars]

# Common variables
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation/appendix-inventory-files-vars#general-variables
# -----------------------------------------------------
postgresql_admin_username=&lt;set your own&gt;
postgresql_admin_password=&lt;set your own&gt;
registry_username=&lt;your RHN username&gt;
registry_password=&lt;your RHN password&gt;

# Platform gateway
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation/appendix-inventory-files-vars#platform-gateway-variables
# -----------------------------------------------------
gateway_admin_password=&lt;set your own&gt;
gateway_pg_host=externaldb.example.org
gateway_pg_database=&lt;set your own&gt;
gateway_pg_username=&lt;set your own&gt;
gateway_pg_password=&lt;set your own&gt;

# Automation controller
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation/appendix-inventory-files-vars#controller-variables
# -----------------------------------------------------
controller_admin_password=&lt;set your own&gt;
controller_pg_host=externaldb.example.org
controller_pg_database=&lt;set your own&gt;
controller_pg_username=&lt;set your own&gt;
controller_pg_password=&lt;set your own&gt;

# Automation hub
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation/appendix-inventory-files-vars#hub-variables
# -----------------------------------------------------
hub_admin_password=&lt;set your own&gt;
hub_pg_host=externaldb.example.org
hub_pg_database=&lt;set your own&gt;
hub_pg_username=&lt;set your own&gt;
hub_pg_password=&lt;set your own&gt;

# Event-Driven Ansible controller
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation/appendix-inventory-files-vars#event-driven-ansible-variables
# -----------------------------------------------------
eda_admin_password=&lt;set your own&gt;
eda_pg_host=externaldb.example.org
eda_pg_database=&lt;set your own&gt;
eda_pg_username=&lt;set your own&gt;
eda_pg_password=&lt;set your own&gt;
```

# Chapter 4. Operator topologies




The Ansible Automation Platform Operator uses Red Hat OpenShift Operators to deploy Ansible Automation Platform within Red Hat OpenShift. Customers manage the product and infrastructure lifecycle.

Important
You can only install a single instance of the Ansible Automation Platform Operator into a single namespace. Installing multiple instances in the same namespace can lead to improper operation for both Operator instances.



## 4.1. Operator growth topology




The growth topology is intended for organizations that are getting started with Ansible Automation Platform and do not require redundancy or higher compute for large volumes of automation. This topology allows for smaller footprint deployments.

### 4.1.1. Infrastructure topology




The following diagram outlines the infrastructure topology that Red Hat has tested with this deployment model that customers can use when self-managing Ansible Automation Platform:


<span id="idm139937747651680"></span>
 **Figure 4.1. Infrastructure topology diagram** 

![Operator growth topology diagram](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Tested_deployment_models-en-US/images/3a13707c5b317e9a4cd69aa815402091/ocp-a-env-a.png)




A Single Node OpenShift (SNO) cluster has been tested with the following requirements: 32 GB RAM, 16 CPUs, 128 GB local disk, and 3000 IOPS.


<span id="idm139937747646672"></span>
 **Table 4.1. Infrastructure topology** 

| Count | Component |
| --- | --- |
| 1 | Automation controller web pod |
| 1 | Automation controller task pod |
| 1 | Automation hub API pod |
| 2 | Automation hub content pod |
| 2 | Automation hub worker pod |
| 1 | Automation hub Redis pod |
| 1 | Event-Driven Ansible API pod |
| 1 | Event-Driven Ansible activation worker pod |
| 1 | Event-Driven Ansible default worker pod |
| 1 | Event-Driven Ansible event stream pod |
| 1 | Event-Driven Ansible scheduler pod |
| 1 | Platform gateway pod |
| 1 | Database pod |
| 1 | Redis pod |




Note
You can deploy multiple isolated instances of Ansible Automation Platform into the same Red Hat OpenShift Container Platform cluster by using a namespace-scoped deployment model. This approach allows you to use the same cluster for several deployments.



### 4.1.2. Tested system configurations




Red Hat has tested the following configurations to install and run Red Hat Ansible Automation Platform:


<span id="idm139937751555632"></span>
 **Table 4.2. Tested system configurations** 

| Type | Description |
| --- | --- |
| Subscription | Valid Red Hat Ansible Automation Platform subscription |
| Operating system | Red Hat Enterprise Linux 9.2 or later minor versions of Red Hat Enterprise Linux 9 |
| CPU architecture | x86_64, AArch64, s390x (IBM Z), ppc64le (IBM Power) |
| Red Hat OpenShift | - Version: 4.14
- num_of_control_nodes: 1
- num_of_worker_nodes: 1 |
| Ansible-core | Ansible-core version 2.16 or later |
| Browser | A currently supported version of Mozilla Firefox or Google Chrome. |
| Database | PostgreSQL 15 |




### 4.1.3. Example custom resource file




Use the following example custom resource (CR) to add your Ansible Automation Platform instance to your project:

```
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
  name: &lt;aap instance name&gt;
spec:
  eda:
    automation_server_ssl_verify: 'no'
  hub:
    storage_type: 's3'
    object_storage_s3_secret: '&lt;name of the Secret resource holding s3 configuration&gt;'
```

### 4.1.4. Nonfunctional requirements




Ansible Automation Platform’s performance characteristics and capacity are impacted by its resource allocation and configuration. With OpenShift, each Ansible Automation Platform component is deployed as a pod. You can specify resource requests and limits for each pod.

Use the Ansible Automation Platform Custom Resource (CR) to configure resource allocation for OpenShift installations. Each configurable item has default settings. These settings are the minimum requirements for an installation, but might not meet your production workload needs.

By default, each component’s deployments are set for minimum resource requests but no resource limits. OpenShift only schedules the pods with available resource requests, but the pods are allowed to consume unlimited RAM or CPU provided that the OpenShift worker node itself is not under node pressure.

In the Operator growth topology, Ansible Automation Platform is deployed on a Single Node OpenShift (SNO) with 32 GB RAM, 16 CPUs, 128 GB Local disk, and 3000 IOPS. This is not a shared environment, so Ansible Automation Platform pods have full access to all of the compute resources of the OpenShift SNO. In this scenario, the capacity calculation for the automation controller task pods is derived from the underlying OpenShift Container Platform node that runs the pod. It does not have access to the entire node. This capacity calculation influences how many concurrent jobs automation controller can run.

OpenShift manages storage distinctly from VMs. This impacts how automation hub stores its artifacts. In the Operator growth topology, we use S3 storage because automation hub requires a `ReadWriteMany` type storage, which is not a default storage type in OpenShift.

### 4.1.5. Network ports




Red Hat Ansible Automation Platform uses several ports to communicate with its services. These ports must be open and available for incoming connections to the Red Hat Ansible Automation Platform server for it to work. Ensure that these ports are available and are not blocked by the server firewall.


<span id="idm139937748593632"></span>
 **Table 4.3. Network ports and protocols** 

| Port number | Protocol | Service | Source | Destination |
| --- | --- | --- | --- | --- |
| 80/443 | HTTP/HTTPS | Receptor | Execution node | OpenShift Container Platform ingress |
| 80/443 | HTTP/HTTPS | Receptor | Hop node | OpenShift Container Platform ingress |
| 80/443 | HTTP/HTTPS | Platform | Customer clients | OpenShift Container Platform ingress |
| 27199 | TCP | Receptor | OpenShift Container Platform cluster | Execution node |
| 27199 | TCP | Receptor | OpenShift Container Platform cluster | Hop node |




## 4.2. Operator enterprise topology




The enterprise topology is intended for organizations that require Ansible Automation Platform to be deployed with redundancy or higher compute for large volumes of automation.

### 4.2.1. Infrastructure topology




The following diagram outlines the infrastructure topology that Red Hat has tested with this deployment model that customers can use when self-managing Ansible Automation Platform:


<span id="idm139937749405024"></span>
 **Figure 4.2. Infrastructure topology diagram** 

![Operator enterprise topology diagram](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Tested_deployment_models-en-US/images/d9ddd7c5a9eeececcb68fcaa798aaebb/ocp-b-env-a.png)




The following infrastructure topology describes an OpenShift Cluster with 3 primary nodes and 2 worker nodes.

Each OpenShift Worker node has been tested with the following component requirements: 16 GB RAM, 4 CPUs, 128 GB local disk, and 3000 IOPS.


<span id="idm139937749399120"></span>
 **Table 4.4. Infrastructure topology** 

| Count | Component |
| --- | --- |
| 1 | Automation controller web pod |
| 1 | Automation controller task pod |
| 1 | Automation hub API pod |
| 2 | Automation hub content pod |
| 2 | Automation hub worker pod |
| 1 | Automation hub Redis pod |
| 1 | Event-Driven Ansible API pod |
| 2 | Event-Driven Ansible activation worker pod |
| 2 | Event-Driven Ansible default worker pod |
| 2 | Event-Driven Ansible event stream pod |
| 1 | Event-Driven Ansible scheduler pod |
| 1 | Platform gateway pod |
| 2 | Mesh ingress pod |
| N/A | Externally managed database service |
| N/A | Externally managed Redis |
| N/A | Externally managed object storage service (for automation hub) |




### 4.2.2. Tested system configurations




Red Hat has tested the following configurations to install and run Red Hat Ansible Automation Platform:


<span id="idm139937754270400"></span>
 **Table 4.5. Tested system configurations** 

| Type | Description |
| --- | --- |
| Subscription | Valid Red Hat Ansible Automation Platform subscription |
| Operating system | Red Hat Enterprise Linux 9.2 or later minor versions of Red Hat Enterprise Linux 9 |
| CPU architecture | x86_64, AArch64, s390x (IBM Z), ppc64le (IBM Power) |
| Red Hat OpenShift | - Red Hat OpenShift on AWS Hosted Control Planes 4.15.16
    
    
    - 2 worker nodes in different availability zones (AZs) at t3.xlarge |
| Ansible-core | Ansible-core version 2.16 or later |
| Browser | A currently supported version of Mozilla Firefox or Google Chrome. |
| AWS RDS PostgreSQL service | - engine: "postgres"
- engine_version: 15"
- parameter_group_name: "default.postgres15"
- allocated_storage: 20
- max_allocated_storage: 1000
- storage_type: "gp2"
- storage_encrypted: true
- instance_class: "db.t4g.small"
- multi_az: true
- backup_retention_period: 5
- database: must have ICU support |
| AWS Memcached Service | - engine: "redis"
- engine_version: "6.2"
- auto_minor_version_upgrade: "false"
- node_type: "cache.t3.micro"
- parameter_group_name: "default.redis6.x.cluster.on"
- transit_encryption_enabled: "true"
- num_node_groups: 2
- replicas_per_node_group: 1
- automatic_failover_enabled: true |
| s3 storage | HTTPS only accessible through AWS Role assigned to automation hub SA at runtime by using AWS Pod Identity |




### 4.2.3. Example custom resource file




For example CR files for this topology, see the [ocp-b.env-a](https://github.com/ansible/test-topologies/blob/aap-2.5/ocp-b.env-a/README.md) directory in the `test-topologies` GitHub repository.

### 4.2.4. Nonfunctional requirements




Ansible Automation Platform’s performance characteristics and capacity are impacted by its resource allocation and configuration. With OpenShift, each Ansible Automation Platform component is deployed as a pod. You can specify resource requests and limits for each pod.

Use the Ansible Automation Platform custom resource to configure resource allocation for OpenShift installations. Each configurable item has default settings. These settings are the exact configuration used within the context of this reference deployment architecture and presumes that the environment is being deployed and managed by an Enterprise IT organization for production purposes.

By default, each component’s deployments are set for minimum resource requests but no resource limits. OpenShift only schedules the pods with available resource requests, but the pods are allowed to consume unlimited RAM or CPU provided that the OpenShift worker node itself is not under node pressure.

In the Operator enterprise topology, Ansible Automation Platform is deployed on a Red Hat OpenShift on AWS (ROSA) Hosted Control Plane (HCP) cluster with 2 t3.xlarge worker nodes spread across 2 AZs within a single AWS Region. This is not a shared environment, so Ansible Automation Platform pods have full access to all of the compute resources of the ROSA HCP cluster. In this scenario, the capacity calculation for the automation controller task pods is derived from the underlying HCP worker node that runs the pod. It does not have access to the CPU or memory resources of the entire node. This capacity calculation influences how many concurrent jobs automation controller can run.

OpenShift manages storage distinctly from VMs. This impacts how automation hub stores its artifacts. In the Operator enterprise topology, we use S3 storage because automation hub requires a `ReadWriteMany` type storage, which is not a default storage type in OpenShift. Externally provided Redis, PostgreSQL, and object storage for automation hub are specified. This provides the Ansible Automation Platform deployment with additional scalability and reliability features, including specialized backup, restore, and replication services and scalable storage.

### 4.2.5. Network ports




Red Hat Ansible Automation Platform uses several ports to communicate with its services. These ports must be open and available for incoming connections to the Red Hat Ansible Automation Platform server for it to work. Ensure that these ports are available and are not blocked by the server firewall.


<span id="idm139937754218336"></span>
 **Table 4.6. Network ports and protocols** 

| Port number | Protocol | Service | Source | Destination |
| --- | --- | --- | --- | --- |
| 80/443 | HTTP/HTTPS | Object storage | OpenShift Container Platform cluster | External object storage service |
| 80/443 | HTTP/HTTPS | Receptor | Execution node | OpenShift Container Platform ingress |
| 80/443 | HTTP/HTTPS | Receptor | Hop node | OpenShift Container Platform ingress |
| 5432 | TCP | PostgreSQL | OpenShift Container Platform cluster | External database service |
| 6379 | TCP | Redis | OpenShift Container Platform cluster | External Redis service |
| 27199 | TCP | Receptor | OpenShift Container Platform cluster | Execution node |
| 27199 | TCP | Receptor | OpenShift Container Platform cluster | Hop node |




# Chapter 5. Automation mesh nodes




Automation mesh is an overlay network intended to ease the distribution of work across a large and dispersed collection of workers. This is done through nodes that establish peer-to-peer connections with each other by using existing networks.

## 5.1. Tested system configurations




Each automation mesh VM has been tested with the following component requirements: 16 GB RAM, 4 CPUs, 60 GB local disk, and 3000 IOPS.

## 5.2. Network ports




Automation mesh uses several ports to communicate with its services. These ports must be open and available for incoming connections to the Red Hat Ansible Automation Platform server for it to work. Ensure that these ports are available and are not blocked by the server firewall.


<span id="idm139937753128592"></span>
 **Table 5.1. Network ports and protocols** 

| Port number | Protocol | Service | Source | Destination |
| --- | --- | --- | --- | --- |
| 80/443 | HTTP/HTTPS | Receptor | Execution node | OpenShift Container Platform mesh ingress |
| 80/443 | HTTP/HTTPS | Receptor | Hop node | OpenShift Container Platform mesh ingress |
| 27199 | TCP | Receptor | OpenShift Container Platform cluster | Execution node |
| 27199 | TCP | Receptor | OpenShift Container Platform cluster | Hop node |




# Appendix A. Additional resources for tested deployment models




This appendix provides a reference for the additional resources relevant to the tested deployment models outlined in Tested deployment models.

- For additional information about each of the tested topologies described in this document, see the [test-topologies GitHub repo](https://github.com/ansible/test-topologies/) .
- For questions around IBM cloud specific configurations or issues, see [IBM support](https://www.ibm.com/mysupport) .



<span id="idm139937756252704"></span>
# Legal Notice

Copyright© 2025 Red Hat, Inc.
The text of and illustrations in this document are licensed by Red Hat under a Creative Commons Attribution–Share Alike 3.0 Unported license ("CC-BY-SA"). An explanation of CC-BY-SA is available at [http://creativecommons.org/licenses/by-sa/3.0/](http://creativecommons.org/licenses/by-sa/3.0/) . In accordance with CC-BY-SA, if you distribute this document or an adaptation of it, you must provide the URL for the original version.
Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.
Red Hat, Red Hat Enterprise Linux, the Shadowman logo, the Red Hat logo, JBoss, OpenShift, Fedora, the Infinity logo, and RHCE are trademarks of Red Hat, Inc., registered in the United States and other countries.
Linux® is the registered trademark of Linus Torvalds in the United States and other countries.
Java® is a registered trademark of Oracle and/or its affiliates.
XFS® is a trademark of Silicon Graphics International Corp. or its subsidiaries in the United States and/or other countries.
MySQL® is a registered trademark of MySQL AB in the United States, the European Union and other countries.
Node.js® is an official trademark of Joyent. Red Hat is not formally related to or endorsed by the official Joyent Node.js open source or commercial project.
TheOpenStack® Word Mark and OpenStack logo are either registered trademarks/service marks or trademarks/service marks of the OpenStack Foundation, in the United States and other countries and are used with the OpenStack Foundation's permission. We are not affiliated with, endorsed or sponsored by the OpenStack Foundation, or the OpenStack community.
All other trademarks are the property of their respective owners.





