# Understand secret handling
## Secret handling for operational use

Learn how automation controller handles operational secrets that are required for the service to run properly.

The operational secrets found in automation controller are as follows:

- `/etc/tower/SECRET_KEY`: A secret key used for encrypting automation secrets in the database. If the `SECRET_KEY` changes or is unknown, you cannot access encrypted fields in the database.
- `/etc/tower/tower.{cert,key}`: An SSL/TLS certificate and key for the automation controller web service. The system installs self-signed certificate or key by default; you can give a locally appropriate certificate and key.
- A database password in `/etc/tower/conf.d/postgres.py` and a message bus password in `/etc/tower/conf.d/channels.py`.


The system stores these secrets unencrypted on the automation controller server, because they must be read by the automation controller service at startup in an automated fashion. UNIX permissions protect all secrets, restricting them to root and the automation controller awx service user.

If you need to hide these secrets, the files that these secrets are read from are interpreted by Python. You can adjust these files to retrieve these secrets by some other mechanism anytime a service restarts. This is a customer provided modification that might need to be reapplied after every upgrade. Red Hat Support and Red Hat Consulting have examples of such modifications.

Note:

If the secrets system is down, automation controller cannot get the information and can fail in a way that is recoverable once the service is restored. Using some redundancy on that system is highly recommended.

If you believe the `SECRET_KEY` that automation controller generated for you has been compromised and needs to be regenerated, you can run a tool from the installation program that behaves much as the automation controller backup and restore tool.

Important:

Ensure that you backup your automation controller database before you generate a new secret key.

To generate a new secret key:

1. Follow the procedure described in the [Backing up and Restoring](/documentation/en-us/red_hat_ansible_automation_platform/2.7/assembly_ag_controller_backup_and_restore#controller-backup-and-restore "You can backup and restore your system by using the Ansible Automation Platform setup playbook.") section.
2. Use the inventory from your install (the same inventory with which you run backups and restores), and run the following command:

```
setup.sh -k.
```

A backup copy of the earlier key is saved in `/etc/tower/`.

