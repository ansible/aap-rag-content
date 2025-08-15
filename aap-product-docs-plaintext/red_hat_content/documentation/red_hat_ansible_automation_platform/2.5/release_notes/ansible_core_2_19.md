# 3. Technology preview
## 3.1. Technology Preview
### 3.1.1. Ansible-core 2.19




This [technical preview](https://access.redhat.com/articles/7128367) includes an overhaul of the templating system and a new feature labeled Data Tagging. These changes enable reporting of numerous problematic behaviors that went undetected in previous releases, with wide-ranging positive effects on security, performance, and user experience.

Backward compatibility has been preserved where practical, but some breaking changes were necessary. This guide describes some common problem scenarios with example content, error messages, and suggested solutions.

We recommend you test your playbooks and roles in a staging environment with this release to determine where you may need to make changes.

For further information see the [Ansible Porting Guide](https://ansible.readthedocs.io/projects/ansible-core/devel/porting_guides/porting_guide_core_2.19.html#id3) .

