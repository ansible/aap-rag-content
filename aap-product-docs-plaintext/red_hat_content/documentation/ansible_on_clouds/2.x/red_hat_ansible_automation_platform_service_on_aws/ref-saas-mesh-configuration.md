# 5. Red Hat Ansible Automation Platform Service on AWS Service Definition
## 5.5. Multi-Region Active/Passive infrastructure
### 5.5.6. Automation mesh configuration and ingress architecture

The Red Hat Ansible Automation Platform automation mesh adapts natively to regional failover events, minimizing configuration modifications.

#### 5.5.6.1. Configure ingress without AWS PrivateLink

For deployments with automation mesh, configuration relies on persistent, load-balanced ingress endpoints that resolve dynamically during a disaster recovery event.

**Procedure**

1. Locate the configuration files or installation playbooks for the remote execution nodes.

2. Configure the remote execution nodes to peer directly with the designated ingress routing addresses matching the custom domain or deployment naming convention:

1. `mesh-ingress-0.<exampledomain.com>`

2. `mesh-ingress-1.<exampledomain.com>`


Note
When peered with these standard endpoints, remote execution nodes automatically reconnect and self-heal following a failover window. No manual reconfiguration of local mesh nodes or topology files is required.

#### 5.5.6.2. Configure ingress with AWS PrivateLink

Unlike standard deployments where DNS handles traffic redirection automatically (as described in [Network and DNS routing](#ref-saas-network-dns-routing "5.5.4.2.&nbsp;Network and DNS Routing")), the automated self-healing behavior of the automation mesh endpoints does not automatically bridge across separate private cloud networks when using AWS PrivateLink.

**Procedure**

1. Pre-configure or manually verify corresponding AWS PrivateLink connections, route tables, and security policy rules inside the secondary region’s AWS infrastructure.
2. Ensure that [remote execution nodes](https://docs.redhat.com/en/documentation/ansible_on_clouds/2.x/html/red_hat_ansible_automation_platform_service_on_aws/saas-pull-push#con-saas-automation) are permitted to establish a network path to the secondary control plane endpoints during a failover scenario.

