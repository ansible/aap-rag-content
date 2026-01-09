# 2. System requirements
## 2.2. Red Hat Ansible Automation Platform system requirements
### 2.2.2. Additional notes for Red Hat Ansible Automation Platform requirements




- The Ansible Automation Platform database backups are staged on each node at `    /var/backups/automation-platform` through the variable `    backup_dir` . You might need to mount a new volume to `    /var/backups` or change the staging location with the variable `    backup_dir` to prevent issues with disk space before running the `    ./setup.sh -b` script.
- If performing a bundled Ansible Automation Platform installation, the installation setup.sh script attempts to install ansible-core (and its dependencies) from the bundle for you.
- If you have installed Ansible-core manually, the Ansible Automation Platform installation setup.sh script detects that Ansible has been installed and does not attempt to reinstall it.


Note
You must use Ansible-core, which is installed by using DNF. Ansible-core version 2.16 is required for versions 2.5 and later.



