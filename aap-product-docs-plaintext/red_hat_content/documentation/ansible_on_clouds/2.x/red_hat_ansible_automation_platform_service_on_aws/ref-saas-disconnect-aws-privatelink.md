# 7. Red Hat Ansible Automation Platform Service on AWS Private Link Connectivity
## 7.6. Disconnecting and deleting AWS PrivateLink connectivity

Before you remove any PrivateLink resources, open a [Customer support](https://access.redhat.com/support/cases/?extIdCarryOver=true&sc_cid=RHCTG0250000454096#/case/new/get-support?caseCreate=true) case and wait for Red Hat to complete teardown on the control plane side.

Important

Open a [Customer support](https://access.redhat.com/support/cases/?extIdCarryOver=true&sc_cid=RHCTG0250000454096#/case/new/get-support?caseCreate=true) case with Red Hat **before** deleting PrivateLink resources. Red Hat must delete the consumer VPC endpoint on the control plane side before you remove your Endpoint Service, Network Load Balancer (NLB), or related components. If customer-side resources are deleted first, the connection may remain in a failed or disconnected state and prevent a clean teardown. Once Red Hat confirms removal on the control plane side, you can safely delete your AWS resources.

Note

**PULL** and **PUSH** refer to the automation mesh connectivity models described in [Red Hat Ansible Automation Platform Service on AWS PULL and PUSH models](https://docs.redhat.com/en/documentation/ansible_on_clouds/2.x/html/red_hat_ansible_automation_platform_service_on_aws/saas-pull-push).

- **Ingress PrivateLink (PULL):** Used when users, automation, or execution nodes in your VPC access the Ansible Automation Platform UI, API, or mesh ingress over PrivateLink.
- **Egress PrivateLink (PUSH):** Used when the Ansible Automation Platform control plane connects to private resources in your VPC, such as execution nodes, Git, or private automation hub.

If you configured both directions, submit a **separate** [Customer support](https://access.redhat.com/support/cases/?extIdCarryOver=true&sc_cid=RHCTG0250000454096#/case/new/get-support?caseCreate=true) case for each direction you want to disconnect.

