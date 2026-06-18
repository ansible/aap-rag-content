# Upgrade the Ansible automation portal RHEL appliance in a disconnected environment

In disconnected environments, you can upgrade the Ansible automation portal RHEL appliance using a mirror registry. Configure the mirror registry so that `bootc upgrade` pulls images from your internal registry instead of `registry.redhat.io`.

## Before you begin

- A mirror registry is accessible from the Ansible automation portal RHEL appliance on the internal network.
- The new appliance image is copied to the mirror registry.
- You have SSH access to the appliance.

## About this task

Once the mirror registry is configured, `bootc upgrade` checks the mirror automatically.

## Procedure

1.  On a connected machine, copy the new appliance image to your internal registry:


```terminal
$ skopeo copy \
docker://registry.redhat.io/ansible-automation-platform/bootc-automation-portal-rhel9:*version* \
docker://mirror.internal.example.com:5000/ansible-automation-platform/bootc-automation-portal-rhel9:*version*
```

2.  On the Ansible automation portal RHEL appliance, create a registry mirror configuration:


```terminal
$ sudo tee /etc/containers/registries.conf.d/50-mirror.conf > /dev/null << 'EOF'
[[registry]]
prefix = "registry.redhat.io"
location = "registry.redhat.io"

[[registry.mirror]]
location = "mirror.internal.example.com:5000"
insecure = false
EOF
```
Replace `mirror.internal.example.com:5000` with your mirror registry address.

3.  If your mirror registry uses a self-signed certificate, add the CA certificate to the system trust store:


```terminal
$ sudo cp ca.crt /etc/pki/ca-trust/source/anchors/
$ sudo update-ca-trust
```
Alternatively, set `insecure = true` in the mirror block. This is not recommended for production environments.

4.  Authenticate to the mirror registry:


```terminal
$ sudo ansible-portal registry-login
```

5.  Authenticate bootc to the mirror registry.
Bootc requires credentials in `/etc/ostree/auth.json` to pull images:

```terminal
$ sudo podman login --authfile /etc/ostree/auth.json mirror.internal.example.com:5000
```

6.  Run the upgrade:


```terminal
$ sudo bootc upgrade
```
If your mirror does not carry Red Hat GPG signatures, add `--no-signature-verification` to the `bootc switch` command when switching image sources. This flag is not needed for `bootc upgrade` when the image source is already configured.

7.  Reboot to activate the new image:


```terminal
$ sudo systemctl reboot
```

## Results

Note:

The mirror configuration in `/etc/containers/registries.conf.d/` survives bootc upgrades because bootc preserves `/etc` using a three-way merge. You do not need to reconfigure the mirror after each upgrade.

Verify that the new image is booted:

```terminal
$ sudo bootc status
```
Verify that all services are running:

```terminal
$ sudo systemctl status portal postgres devtools
```

## What to do next

**Sync new versions to the mirror**

When a new appliance version is available, copy it to the mirror from a connected machine:

1. Copy the new image version to the mirror registry:

```terminal
$ skopeo copy \
docker://registry.redhat.io/ansible-automation-platform/bootc-automation-portal-rhel9:*new-version* \
docker://mirror.internal.example.com:5000/ansible-automation-platform/bootc-automation-portal-rhel9:*new-version*
```

2. On the appliance, run the upgrade and reboot:

```terminal
$ sudo bootc upgrade
$ sudo systemctl reboot
```
