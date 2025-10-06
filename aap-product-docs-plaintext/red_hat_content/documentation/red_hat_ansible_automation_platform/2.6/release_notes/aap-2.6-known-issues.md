# Chapter 7. Known issues




This section provides information about known issues in Ansible Automation Platform 2.6.

- For role based authentication mappings, the role list includes all roles within the platform. Only the role assignments of Org Admin, Org Member, Team Admin, Team Member, and Platform Auditor are supported at this time. The list will be limited to only those that can be applied at a platform level in a subsequent release.
- If you have an existing deployment of Red Hat Ansible Lightspeed on Ansible Automation Platform 2.5, upgrading to Ansible Automation Platform 2.6 will cause your Red Hat Ansible Lightspeed deployment to fail. To avoid this failure, do not upgrade to Ansible Automation Platform 2.6 until a forthcoming patch is released on October 22, 2025. However, new deployments of Red Hat Ansible Lightspeed will work correctly on Ansible Automation Platform 2.6.(AAP-54064)


