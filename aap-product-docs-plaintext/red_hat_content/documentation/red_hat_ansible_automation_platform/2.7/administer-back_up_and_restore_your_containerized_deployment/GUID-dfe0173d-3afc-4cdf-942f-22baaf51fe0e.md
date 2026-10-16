# Back up and restore your containerized deployment
## Recover from a broken or degraded environment

If your containerized Ansible Automation Platform deployment is broken or degraded, rerun the installation playbook as a first recovery step before deciding to uninstall and restore from backup.

### About this task

When your environment is broken or degraded, choose a recovery approach based on whether users are active in the environment:

- **In-place recovery**: Attempt in-place repair by rerunning the installation playbook. Reinstall only if rerunning the playbook does not resolve the issue. Use this approach when users are not actively working in the environment.
- **Restore to separate infrastructure**: Perform a fresh installation on new hosts and restore your data from a backup. Use this approach when users are active in the broken environment, because continued use of a degraded environment can corrupt data. For more information, see [Restore containerized Ansible Automation Platform](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-back_up_and_restore_your_containerized_deployment#proc-restore-aap-container "Restore your container-based installation of Ansible Automation Platform from a backup, or to a different environment.").

Important:

Where possible, use a backup that was taken before the environment became broken. A backup taken from a broken or degraded environment might contain the same data or configuration that caused the breakage, and restoring it can reproduce the original problem.

### Procedure

1. Go to the Red Hat Ansible Automation Platform installation directory on your Red Hat Enterprise Linux host.
2. Run the installation playbook:


```
$ ansible-playbook -i <path_to_inventory> ansible.containerized_installer.install
```

3. Verify that the environment is stable and accessible.
If the environment is stable, no further action is required. A restore is not needed unless data loss occurred.

4. If the environment is still broken, run the uninstall playbook:


```
$ ansible-playbook -i <path_to_inventory> ansible.containerized_installer.uninstall
```

5. Run the installation playbook:


```
$ ansible-playbook -i <path_to_inventory> ansible.containerized_installer.install
```

6. Run the restore playbook:


```
$ ansible-playbook -i <path_to_inventory> ansible.containerized_installer.restore
```

For more information about restore prerequisites and procedures, see [Restore containerized Ansible Automation Platform](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-back_up_and_restore_your_containerized_deployment#proc-restore-aap-container "Restore your container-based installation of Ansible Automation Platform from a backup, or to a different environment.").

