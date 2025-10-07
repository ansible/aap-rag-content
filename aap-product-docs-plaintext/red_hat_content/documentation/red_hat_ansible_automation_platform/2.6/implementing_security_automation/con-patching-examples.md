# 3. Ansible Automation Platform security automation use cases
## 3.2. Patch automation with Ansible Automation Platform
### 3.2.2. Patching examples




The following playbooks are provided as patching examples, and should be modified to fit the target environment and tested thoroughly before being used in production. These examples use the `ansible.builtin.dnf` module for managing packages on RHEL and other operating systems that use the `dnf` package manager. Modules for patching other Linux operating systems, Microsoft Windows, and many network devices are also available.

#### 3.2.2.1. Keeping everything up to date




For some Red Hat Enterprise Linux servers, such as a lab or other non-production systems, you might want to install all available patches on a regular cadence. The following example playbook might be used in a job template that is scheduled to run weekly, and updates the system with all of the latest RPMs.

```
- name: Install all available RPM updates
hosts: target_hosts
become: true

tasks:
- name: Install latest RPMs
ansible.builtin.dnf:
name: '*'
state: latest
```

id="ref-install-security-updates"]

#### 3.2.2.2. Installing security updates only




For organizations with a policy requiring that all RPMs including security errata be kept up to date, the following playbook might be used in a regularly scheduled job template.

```
- name: Install all security-related RPM updates
hosts: target_hosts
become: true

tasks:
- name: Install latest RPMs with security errata
ansible.builtin.dnf:
name: '*'
security: true
state: latest
```

#### 3.2.2.3. Specifying package versions




For production systems, a well-established configuration management practice is to deploy only known, tested combinations of software to ensure that systems are configured correctly and perform as expected. This includes deploying only known versions of operating system software and patches to ensure that system updates do not introduce problems with production applications.

Note
The following example playbook installs a specific version of the `httpd` RPM and its dependencies when the target host uses the RHEL 9 operating system. This playbook does not take action if the specified versions are already in place or if a different version of RHEL is installed.



```
- name: Install specific RPM versions
hosts: target_hosts
gather_facts: true
become: true

vars:
httpd_packages_rhel9:
- httpd-2.4.53-11.el9_2.5
- httpd-core-2.4.53-11.el9_2.5
- httpd-filesystem-2.4.53-11.el9_2.5
- httpd-tools-2.4.53-11.el9_2.5
- mod_http2-1.15.19-4.el9_2.4
- mod_lua-2.4.53-11.el9_2.5

tasks:
- name: Install httpd and dependencies
ansible.builtin.dnf:
name: '{{ httpd_packages_rhel9 }}'
state: present
allow_downgrade: true
when:
- ansible_distribution == "RedHat"
- ansible_distribution_major_version == "9"
```

Note
By setting `allow_downgrade: true` , if a newer version of any defined package is installed on the system, it is downgraded to the specified version instead.



id="ref-complex-patching-scenarios"]

