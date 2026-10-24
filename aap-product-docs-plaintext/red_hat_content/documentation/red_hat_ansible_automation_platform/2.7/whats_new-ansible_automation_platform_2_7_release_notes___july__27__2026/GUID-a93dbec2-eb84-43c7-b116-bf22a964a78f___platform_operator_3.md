# Ansible Automation Platform 2.7 Release Notes - July 27, 2026 (2.7-3)
## Platform operator

- Fixed an issue where, when a cluster-wide egress proxy was configured on OpenShift, the Ansible Automation Platform gateway operator propagated the `NO_PROXY` environment variable to operand containers verbatim, without including the internal service names that components use to communicate with each other. This caused internal traffic — including JWT key validation calls — to be routed through the corporate proxy, resulting in authentication failures and component unavailability on proxy-configured clusters. The operator now automatically augments `NO_PROXY` with the required internal cluster service exclusions before writing them to operand containers. (AAP-83822, AAP-84164)
