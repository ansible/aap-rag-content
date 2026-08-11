# Upgrade the Ansible automation portal RHEL appliance
## Roll back an upgrade

Bootc maintains two image slots: the booted image and one rollback image. After an upgrade, the previous version becomes the rollback target. After a rollback, the upgraded version becomes the rollback target. You can switch between the two versions as needed.

If the new version has issues, roll back to the previous image.

Procedure:

1. Roll back to the previous image:

```terminal
$ sudo bootc rollback
```

2. Reboot to activate the rollback image:

```terminal
$ sudo systemctl reboot
```

The rollback reverts the system image atomically. Your configuration and data in the `/etc` and `/var` directories are preserved. After reboot, the post-upgrade reconciliation runs again and regenerates plugin configurations from the previous image version.

Verification:

- Confirm the rollback was applied:

```terminal
$ sudo bootc status
```

The booted image shows the previous digest. The upgraded image is now listed as the rollback target.

- Verify that all services are running:

```terminal
$ sudo systemctl status portal postgres devtools
```

