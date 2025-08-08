# 3. Installing the Red Hat Edge Manager on Ansible Automation Platform
## 3.3. Self-signed certificates




The Red Hat Edge Manager services automatically generate and store self-signed certificates in the `/etc/flightctl/pki` directory. These include:

-  `    /etc/flightctl/pki/ca.crt`
-  `    /etc/flightctl/pki/ca.key`
-  `    /etc/flightctl/pki/client-enrollment.crt`
-  `    /etc/flightctl/pki/client-enrollment.key`
-  `    /etc/flightctl/pki/server.crt`
-  `    /etc/flightctl/pki/server.key`


You can use your own custom certificates by placing them in the following locations:

- Custom Server Certificate/Key Pair:


-  `        /etc/flightctl/pki/server.crt`
-  `        /etc/flightctl/pki/server.key`

- Custom CA Certificate for Ansible Automation Platform authentication:


-  `        /etc/flightctl/pki/auth/ca.crt`



Note
Ensure that you adjust the `insecureSkipTlsVerify` setting in the `service-config.yaml` if you use a custom CA certificate for your Ansible Automation Platform instance.



