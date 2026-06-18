# ansible-core 2.19

The ansible-core 2.19 release includes an overhaul of the templating system and a new feature labeled Data Tagging.

Note:

Ansible Automation Platform does not include ansible-core 2.19 by default, but it is compatible with 2.19. See related links for more information.

Changes in ansible-core enable reporting of numerous problematic behaviors that went undetected in previous releases, with wide-ranging positive effects on security, performance, and user experience. Backward compatibility has been preserved where practical, but some breaking changes were necessary. This section describes some common problem scenarios with example content, error messages, and suggested solutions.We recommend you test your playbooks and roles in a staging environment with this release to determine where you may need to make changes.
