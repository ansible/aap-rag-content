# Upgrade the Ansible automation portal RHEL appliance
## Authenticate to the container registry

To pull new appliance images from `registry.redhat.io`, authenticate to the registry and save the credentials where bootc can find them.

Important:

Bootc and Podman use separate credential stores. The `--authfile /etc/ostree/auth.json` flag saves credentials to the location that `bootc upgrade` and `bootc switch` read. Running `podman login` without `--authfile` stores credentials only for Podman and does not authenticate bootc operations.

Procedure:

1. SSH into the Ansible automation portal RHEL appliance and log in to the container registry:

```terminal
$ sudo podman login --authfile /etc/ostree/auth.json registry.redhat.io
```

