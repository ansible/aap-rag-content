# 2. Setting up automation mesh
## 2.4. Importing a Certificate Authority (CA) certificate
### 2.4.1. Using custom signed certificates in automation mesh

Learn how to replace the default automation mesh installer-provided certificates with custom,organization-specific certificates.

Note

In the following procedure, replace `<FQDN/IP Address>` and <IP Address> with the Fully Qualified Domain Name (FQDN) or IP address of the node.

**Procedure**

1. Stop the receptor service on all automation controller and execution nodes.

`# systemctl stop receptor`

2. Generate a new Certificate Authority (CA) for your mesh network.

3. Replace "common ca" in the command below with the required common name.

# receptor --cert-init commonname="common ca" bits=4096 outcert=/etc/receptor/tls/ca/mesh-CA.crt outkey=/etc/receptor/tls/ca/mesh-CA.key

4. Generate a self-signed certificate request for each Controller and Execution Node.

# receptor --cert-makereq commonname=<FQDN/IP Address> bits=4096 nodeid=<FQDN/IP Address> outreq=/etc/receptor/tls/<FQDN/IP Address>.csr outkey=/etc/receptor/tls/<FQDN/IP Address>.key ipaddress=<IP Address> ipaddress=<IP Address>

5. Sign the newly created certificates with your CA. Make sure you adjust the `notafter=` date to meet your organizational requirements. The example shown uses a date far in the future.

# receptor --cert-signreq verify=yes cacert=/etc/receptor/tls/ca/mesh-CA.crt cakey=/etc/receptor/tls/ca/mesh-CA.key req=/etc/receptor/tls/<FQDN/IP Address>.csr outcert=/etc/receptor/tls/<FQDN/IP Address>.crt notafter="2034-07-29T20:48:02Z"

6. Transfer the newly created and signed certificates to their nodes in the `/etc/receptor/tls/` directory.

7. The `mesh-CA.crt` file must be placed in `/etc/receptor/tls/ca`.

8. Ensure that the permissions and ownership of the certificate files are set correctly.


- All files should be owned by receptor

- All certificate files should have 0640 permissions.

`# chown -R receptor: /etc/receptor; chmod 0640 /etc/receptor/tls/<FQDN/IP Address>.crt`

9. Start the receptor service on all Controller and Execution nodes.

`# systemctl start receptor`

10. Verify the node status in the Ansible Automation Platform UI:

11. In the navigation panel, select Automation Execution → Infrastructure → Instance Groups

12. Select the default instance group, then go to the Instances tab.

13. Ensure that the status of all nodes is marked as Ready.

14. If any node is marked as **Unavailable**:


1. Select the Unavailable node.
2. Click Run Health Check.
3. Refresh the page, and the node should now display as Ready.

