# 2. Setting up automation mesh
## 2.4. Importing a Certificate Authority (CA) certificate
### 2.4.1. Using custom signed certificates in automation mesh




Learn how to replace the default automation mesh installer-provided certificates with custom,organization-specific certificates.

Note
In the following procedure, replace `&lt;FQDN/IP Address&gt;` and <IP Address> with the Fully Qualified Domain Name (FQDN) or IP address of the node.



**Procedure**

1. Stop the receptor service on all automation controller and execution nodes.

`    # systemctl stop receptor`


1. Generate a new Certificate Authority (CA) for your mesh network.
1. Replace "common ca" in the command below with the required common name.


```
# receptor --cert-init commonname="common ca" bits=4096 outcert=/etc/receptor/tls/ca/mesh-CA.crt outkey=/etc/receptor/tls/ca/mesh-CA.key
```


1. Generate a self-signed certificate request for each Controller and Execution Node.


```
# receptor --cert-makereq commonname=&lt;FQDN/IP Address&gt; bits=4096 nodeid=&lt;FQDN/IP Address&gt; outreq=/etc/receptor/tls/&lt;FQDN/IP Address&gt;.csr outkey=/etc/receptor/tls/&lt;FQDN/IP Address&gt;.key ipaddress=&lt;IP Address&gt; ipaddress=&lt;IP Address&gt;
```


1. Sign the newly created certificates with your CA. Make sure you adjust the `    notafter=` date to meet your organizational requirements. The example shown uses a date far in the future.


```
# receptor --cert-signreq verify=yes cacert=/etc/receptor/tls/ca/mesh-CA.crt cakey=/etc/receptor/tls/ca/mesh-CA.key req=/etc/receptor/tls/&lt;FQDN/IP Address&gt;.csr outcert=/etc/receptor/tls/&lt;FQDN/IP Address&gt;.crt notafter="2034-07-29T20:48:02Z"
```


1. Transfer the newly created and signed certificates to their nodes in the `    /etc/receptor/tls/` directory.
1. The `    mesh-CA.crt` file must be placed in `    /etc/receptor/tls/ca` .
1. Ensure that the permissions and ownership of the certificate files are set correctly.


- All files should be owned by receptor
- All certificate files should have 0640 permissions.

`        # chown -R receptor: /etc/receptor; chmod 0640 /etc/receptor/tls/&lt;FQDN/IP Address&gt;.crt`



1. Start the receptor service on all Controller and Execution nodes.

`    # systemctl start receptor`


1. Verify the node status in the Ansible Automation Platform UI:
1. In the navigation panel, selectAutomation Execution→Infrastructure→Instance Groups
1. Select the default instance group, then go to the Instances tab.
1. Ensure that the status of all nodes is marked as Ready.
1. If any node is marked as **Unavailable** :


1. Select the Unavailable node.
1. ClickRun Health Check.
1. Refresh the page, and the node should now display as Ready.



