# Replace self-signed SSL certificates
## Replace the SSL certificates

Prerequisites:

- A TLS certificate and private key in PEM format, issued by a certificate authority trusted by your organization.
- SSH access to the appliance.


Procedure:

1. Copy your certificates to the appliance:

```terminal
$ sudo cp *certificate-file*.pem /etc/portal/ssl/cert.pem
$ sudo cp *private-key-file*.pem /etc/portal/ssl/key.pem
$ sudo chmod 644 /etc/portal/ssl/cert.pem
$ sudo chmod 600 /etc/portal/ssl/key.pem
```

2. Restart the Ansible automation portal service:

```terminal
$ sudo systemctl restart portal
```

Verification:

- Verify that the Ansible automation portal is using the new certificate:

```terminal
$ curl -vk https://localhost 2>&1 | grep -i "issuer"
```
The output displays the issuer from your certificate, not the self-signed issuer.

