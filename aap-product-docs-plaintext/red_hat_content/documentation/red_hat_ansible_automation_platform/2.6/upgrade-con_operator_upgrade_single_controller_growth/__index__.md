# 2.4 single automation controller node deployment to a 2.6 growth topology

Plan your upgrade from a 2.4 single automation controller node setup to a 2.6 growth topology. Review the required infrastructure changes and requirements for a successful upgrade.

## 2.4 infrastructure topology diagram

This diagram outlines the 2.4 infrastructure topology for this deployment model.

*Figure 1. 2.4 infrastructure topology diagram*

![2.4 single controller topology](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/ocp-a-controller-2-4.png)

## 2.6 infrastructure topology diagram

This diagram outlines the 2.6 infrastructure topology that Red Hat has tested with this deployment model.

*Figure 2. 2.6 infrastructure topology diagram*

![2.6 growth topology](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/ocp-a-controller-2-6.png)

## Requirements for upgrading a single automation controller node deployment

The following table highlights the requirements for upgrading from Ansible Automation Platform 2.4 to 2.6.

| Existing 2.4 topology                                                                                                                           | Tested 2.6 topology                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Requirements for each pod                                                       |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------- |
| <br>Non-redundant automation controller-only deployment:<br>One automation controller web podOne automation controller task podOne database pod | <br>Growth topology:<br>One automation controller web podOne automation controller task podOne automation hub web podOne automation hub API podTwo automation hub content podsTwo automation hub worker podsOne automation hub Redis podOne Event-Driven Ansible controller API podOne Event-Driven Ansible controller activation worker podOne Event-Driven Ansible controller default worker podOne Event-Driven Ansible controller event stream podOne Event-Driven Ansible controller scheduler podOne platform gateway podOne database podOne Redis pod | <br>See the **Operator growth topology** section of *Tested deployment models*. |
