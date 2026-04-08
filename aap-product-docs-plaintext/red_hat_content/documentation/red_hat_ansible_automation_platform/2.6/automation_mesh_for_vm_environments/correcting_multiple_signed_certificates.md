# 2. Setting up automation mesh
## 2.4. Importing a Certificate Authority (CA) certificate
### 2.4.2. Correcting multiple signed certificates




If `/etc/receptor/tls/ca/mesh-CA.crt` (for RPM-based installs) or `$HOME/aap/receptor/etc/mesh-CA.crt` (for containerized installs) contains more than 10 certificates, an error occurs.

Take the following steps on all automation controller and execution nodes within the Ansible Automation Platform environment.

**For an RPM-based install**

**Procedure**

1. Make a backup of the `    mesh-CA.crt` file

`    cp -p /etc/receptor/tls/ca/mesh-CA.crt /etc/receptor/tls/ca/mesh-CA.crt-$(date +%F)`


1. Delete everything past the first certificate within the `    mesh-CA.crt` file, that is, keep only the first certificate that is present at the top of the file.
1. Restart receptor

`    systemctl restart receptor`




**For a Containerized install**

1. Make a backup of the `    mesh-CA.crt` file

`    cp -p $HOME/aap/receptor/etc/mesh-CA.crt $HOME/aap/receptor/etc/mesh-CA.crt-$(date +%F)`


1. Delete everything past the first certificate within the `    mesh-CA.crt` file, that is, keep only the first certificate that is present at the top of the file.
1. Restart receptor

`    systemctl --user restart receptor`




**Additional resources**

-  [System Requirements](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/planning_your_installation/platform-system-requirements)


