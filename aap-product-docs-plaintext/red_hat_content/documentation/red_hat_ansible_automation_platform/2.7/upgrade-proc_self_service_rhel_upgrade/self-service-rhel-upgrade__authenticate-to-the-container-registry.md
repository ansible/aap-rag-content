# Upgrade the Ansible automation portal RHEL appliance
## Authenticate to the container registry

To pull new appliance images from `registry.redhat.io`, authenticate to the registry and save the credentials where bootc can find them.

Procedure:

1. SSH into the Ansible automation portal RHEL appliance and log in to the container registry:

```terminal
$ sudo podman login --authfile /etc/ostree/auth.json registry.redhat.io
```

