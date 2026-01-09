# 3. Managed Node Configuration
## 3.1. Red Hat Enterprise Linux managed node configuration
### 3.1.2. Compliance profile considerations




In many environments, you can use Ansible Automation Platform to manage systems where security controls have been applied to managed RHEL nodes to meet the requirements of a compliance profile such as CIS, PCI/DSS, the DISA STIG, or similar. The following sections detail the specific set of security controls that must be modified for Ansible Automation Platform to manage the RHEL nodes properly in such environments.

#### 3.1.2.1. Fapolicyd on managed RHEL nodes




When an Ansible Automation Platform job runs against a RHEL managed node, most tasks are executed by copying Python code to the managed node and then executing it locally. The job will fail if the `fapolicyd` service is enabled on the managed node, because the default set of rules that come with RHEL prevents this Python code from running.

To prevent this issue from occurring, use one of the following methods:

- Option 1: Set the fapolicyd service to permissive mode
- Option 2: Create custom fapolicyd rules


#### 3.1.2.2. Option 1: Set the fapolicyd service to permissive mode




The fapolicyd service can be set to "permissive" mode, meaning that it only logs fapolicyd rule violations, rather than enforcing them.

To configure permissive mode for fapolicyd, use the following procedure:

**Procedure**

1. Edit the file `    /etc/fapolicyd/fapolicyd.conf` , and set "permissive = 1".
1. Restart the `    fapolicy` service by running `    systemctl restart fapolicyd.service` .


In environments where this configuration might not meet a required compliance profile or local policy, discuss waiving the relevant security control with your security auditor.

#### 3.1.2.3. Option 2: Create custom fapolicyd rules




Where the `fapolicyd` service must enforce its rules, consider crafting a custom set of rules to permit Ansible Automation Platform to execute its Python code.

The following example procedure treats the "ansible" service account as a trusted entity and enables it to execute content in the local Ansible temporary directory (by default, `$HOME/.ansible/tmp` ).

**Procedure**

1. Create the file `    /etc/fapolicy/rules.d/50-ansible.rules` with the following content:

`    allow perm=any uid=ansible trust=1 : dir=/home/ansible/.ansible/tmp/`


1. Restart the fapolicyd service:

`    sudo systemctl restart fapolicyd.service`




This example rule might require modification to work with any other `fapolicyd` rules that exist on the managed RHEL nodes, and must be thoroughly tested and approved by your security auditor before being put into production.


<span id="idm139835592266304"></span>
