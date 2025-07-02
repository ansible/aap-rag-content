# 2. Setting up automation mesh
## 2.4. Importing a Certificate Authority (CA) certificate




A Certificate Authority (CA) verifies and signs individual node certificates in an automation mesh environment. You can provide your own CA by specifying the path to the certificate and the private RSA key file in the `inventory` file of your Red Hat Ansible Automation Platform installer.

Note
The Ansible Automation Platform installation program generates a CA if you do not provide one.



**Procedure**

1. Open the `    inventory` file for editing.
1. Add the `    mesh_ca_keyfile` variable and specify the full path to the private RSA key ( `    .key` ).
1. Add the `    mesh_ca_certfile` variable and specify the full path to the CA certificate file ( `    .crt` ).
1. Save the changes to the inventory file.


**Example**

```
[all:vars]
mesh_ca_keyfile=/tmp/<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">&lt;mesh_CA&gt;</span></em></span>.key
mesh_ca_certfile=/tmp/<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">&lt;mesh_CA&gt;</span></em></span>.crt
```


With the CA files added to the inventory file, run the installation program to apply the CA. This process copies the CA to the to `/etc/receptor/tls/ca/` directory on each control and execution node on your mesh network.

**Additional resources**

-  [System Requirements](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/planning_your_installation/platform-system-requirements)


