# 1. Introduction to Red Hat Ansible Automation Platform on Microsoft Azure
## 1.9. Product lifecycle and maintenance
### 1.9.2. Planned upgrade windows

Red Hat has defined windows in which upgrades occur, and those windows may change over time in an effort to improve service offerings. Every effort is taken to reduce or eliminate any downtime during these windows. However, these windows are provided to allow for system downtime should it be required.

In the cases where operations require more time than the planned window, then the operation time has precedence over the defined window time. The "upgrade window" timeline is not synonymous with an expected outage timeline; it defines the time over which upgrades are planned to occur.

| <br>  Cadence | <br>  Expected upgrade window | <br>  Time                           | <br>  Purpose                                                                              |
| ------------- | ----------------------------- | ------------------------------------ | ------------------------------------------------------------------------------------------ |
| <br>  Ad Hoc  | <br>  N/A                     | <br>  As needed for security reasons | <br>  Critical CVE patches                                                                 |
| <br>  Daily   | <br>  1 hour                  | <br>  2 AM ET                        | <br>  CVE patches                                                                          |
| <br>  Weekly  | <br>  2 hour                  | <br>  2 AM ET Tuesdays               | <br>  Ansible Automation Platform and infrastructure upgrades (North America Deployments). |
| <br>  Weekly  | <br>  2 hour                  | <br>  2 AM UTC Tuesdays              | <br>  Ansible Automation Platform and infrastructure upgrades (EMEA Deployments).          |
| <br>  Weekly  | <br>  2 hour                  | <br>  2 AM JST Tuesdays              | <br>  Ansible Automation Platform and infrastructure upgrades (APAC Deployments).          |
| <br>  Ad Hoc  | <br>  1 hour                  | <br>  2 AM UTC Sunday                | <br>  Azure Database for PostgreSQL - Flexible Server.                                     |
| <br>  Ad Hoc  | <br>  4 hour                  | <br>  2 AM UTC Sunday                | <br>  AKS cluster node operating system images.                                            |

Note

These windows are only a guidance, and Red Hat reserves the ability to perform platform operations as needed to maintain the health of Ansible on Azure deployments.

