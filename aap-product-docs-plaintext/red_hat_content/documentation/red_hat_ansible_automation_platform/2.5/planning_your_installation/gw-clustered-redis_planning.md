# 3. Caching and queueing system
## 3.3. Clustered Redis




With clustered Redis, data is automatically partitioned over multiple nodes to provide performance stability and nodes are assigned as replicas to provide reliability. Clustered Redis, shared between the platform gateway and Event-Driven Ansible, is provided by default when installing Ansible Automation Platform in containerized and operator-based deployments.

Note
A Redis high availability (HA) compatible deployment require 6 VMs. In RPM deployments, Redis can be colocated on each Ansible Automation Platform component VM except for automation controller, execution nodes, or the PostgreSQL database. In containerized deployments, Redis can be colocated on any Ansible Automation Platform component VMs of your choice except for execution nodes or the PostgreSQL database. See [Tested deployment models](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/tested_deployment_models) for the opinionated deployment options available.



A cluster has three primary nodes and each primary node has a replica node.

If a primary instance becomes unavailable due to failures, the other primary nodes will initiate a failover state to promote a replica node to a primary node.

![Clustered Redis deployment](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Planning_your_installation-en-US/images/cd74e4ccc48246637c57db5612871963/gw-clustered-redis.png)


The benefits of deploying clustered Redis over standalone Redis include the following:

- Data is automatically split across many nodes.
- Data can be dynamically adjusted.
- Automatic failover of the primary nodes initiates during system failures.


For more information about scalability with Redis, see [Scale with Redis Cluster](https://redis.io/docs/latest/operate/oss_and_stack/management/scaling/) in the Redis product documentation.

For more information about deploying Ansible Automation Platform with clustered Redis, see the [RPM installation](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_installation) , [Containerized installation](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation) , and [Installing on OpenShift Container Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/installing_on_openshift_container_platform) guides.

**Disclaimer** : Links contained in this information to external website(s) are provided for convenience only. Red Hat has not reviewed the links and is not responsible for the content or its availability. The inclusion of any link to an external website does not imply endorsement by Red Hat of the website or their entities, products or services. You agree that Red Hat is not responsible or liable for any loss or expenses that may result due to your use of (or reliance on) the external site or content.

