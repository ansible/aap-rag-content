# Upgrade the Ansible automation portal RHEL appliance
## Upgrade the appliance

Procedure:

1. [Back up and restore data](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-ref_self_service_portal_cli_commands "The Ansible automation portal appliance provides the ansible-portal management CLI for administration and troubleshooting.").

2. Run the upgrade:

```terminal
$ sudo bootc upgrade
```
The upgrade is staged and does not take effect until you reboot. The current version continues running. You can schedule the reboot for a convenient maintenance window.

`bootc upgrade` pulls the latest image for the current tag. To upgrade to a specific version, use `bootc switch` with a version tag:



```terminal
$ sudo bootc switch registry.redhat.io/ansible-automation-platform/bootc-automation-portal-rhel9:*version*
```

3. Reboot to activate the new image:

```terminal
$ sudo systemctl reboot
```

Verification:

- Verify that the new image is booted:

```terminal
$ sudo bootc status
```
The booted digest matches the digest from the upgrade output. The previous version is retained as a rollback target.

- Check the portal service logs:

```terminal
$ sudo journalctl -u portal -f
```

- Verify that all services are running:

```terminal
$ sudo systemctl status portal postgres devtools
```
All three services (`portal`, `postgres`, `devtools`) show `active (running)`.

