# 2.4 multi node automation controller and automation hub deployment to a 2.6 enterprise topology

Upgrade your 2.4 multi-node deployment (automation controller and automation hub) to a 2.6 enterprise topology. Review the infrastructure changes and requirements needed to successfully plan your upgrade.

## 2.4 infrastructure topology diagram

This diagram outlines the 2.4 infrastructure topology for this deployment model.

*Figure 1. 2.4 infrastructure topology diagram*

![2.4 multi controller and hub topology](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/ocp-b-controller-hub-2-4.png)

## 2.6 infrastructure topology diagram

This diagram outlines the 2.6 infrastructure topology that Red Hat has tested with this deployment model.

*Figure 2. 2.6 infrastructure topology diagram*

![2.6 enterprise topology](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/ocp-b-controller-hub-2-6.png)

## Requirements for upgrading a multi node automation controller and automation hub deployment

The following table highlights the requirements for upgrading from Ansible Automation Platform 2.4 to 2.6.

| Existing 2.4 topology                                                                                                                                                                                                                                                                                                              | Tested 2.6 topology                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Requirements for each pod                                                           |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| <br>Redundant deployment with automation controller and automation hub:<br>One automation controller web podOne automation controller task podTwo automation mesh ingress podsOne automation hub web podOne automation hub API podTwo automation hub content podsTwo automation hub worker podsExternally managed database service | <br>Enterprise topology:<br>One automation controller web podOne automation controller task podOne automation hub web podOne automation hub API podTwo automation hub content podsTwo automation hub worker podsOne automation hub Redis podOne Event-Driven Ansible controller API podTwo Event-Driven Ansible controller activation worker podsTwo Event-Driven Ansible controller default worker podsTwo Event-Driven Ansible controller event stream podsOne Event-Driven Ansible controller scheduler podOne platform gateway podTwo automation mesh ingress podsExternally managed database serviceExternally managed RedisExternally managed object storage service (for automation hub) | <br>See the **Operator enterprise topology** section of *Tested deployment models*. |
