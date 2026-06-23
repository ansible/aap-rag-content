# Edit the inventory file
## Import a CA certificate

A Certificate Authority (CA) verifies and signs individual node certificates in an automation mesh environment. You can provide your own CA by specifying the path to the certificate and the private RSA key file in the `inventory` file of your Red Hat Ansible Automation Platform installer.

### About this task

Note:

The Ansible Automation Platform installation program generates a CA if you do not provide one.

### Procedure

1.  Open the `inventory` file for editing.
2.  Add the `mesh_ca_keyfile` variable and specify the full path to the private RSA key (`.key`).
3.  Add the `mesh_ca_certfile` variable and specify the full path to the CA certificate file (`.crt`).
4.  Save the changes to the inventory file.

```
[all:vars]
mesh_ca_keyfile=/tmp/<mesh_CA>.key
mesh_ca_certfile=/tmp/<mesh_CA>.crt
```

5.  With the CA files added to the inventory file, run the installation program to apply the CA.

### Results

This process copies the CA to the to `/etc/receptor/tls/ca/` directory on each control and execution node on your mesh network.
