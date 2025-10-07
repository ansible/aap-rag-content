# 3. Configuring Ansible Automation Platform to use egress proxy
## 3.7. Configuring proxy settings for automation mesh




You can route outbound communication from the receptor on an automation mesh node through a proxy server. If your proxy does not strip out TLS certificates then an installation of Ansible Automation Platform automatically supports the use of a proxy server.

Every node on the mesh must have a Certifying Authority that the installer creates on your behalf.

The default install location for the Certifying Authority is:

`/etc/receptor/tls/ca/mesh-CA.crt`

The certificates and keys created on your behalf use the nodeID for their names:

For the certificate: `/etc/receptor/tls/NODEID.crt`

For the key: `/etc/receptor/tls/NODEID.key`

