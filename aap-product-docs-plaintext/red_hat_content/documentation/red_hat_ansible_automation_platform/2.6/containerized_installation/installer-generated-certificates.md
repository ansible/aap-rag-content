# 5. Advanced containerized deployment
## 5.7. Configuring custom TLS certificates
### 5.7.1. Ansible Automation Platform generated certificates




By default, the installation program creates a self-signed Certificate Authority (CA) and uses it to generate self-signed TLS certificates for all Ansible Automation Platform services. The self-signed CA certificate and key are generated on one node under the `~/aap/tls/` directory and copied to the same location on all other nodes. This CA is valid for 10 years after the initial creation date.

Self-signed certificates are not part of any public chain of trust. The installation program creates a certificate truststore that includes the self-signed CA certificate under `~/aap/tls/extracted/` and bind-mounts that directory to each Ansible Automation Platform service container under `/etc/pki/ca-trust/extracted/` . This allows each Ansible Automation Platform component to validate the self-signed certificates of the other Ansible Automation Platform services. The CA certificate can also be added to the truststore of other systems or browsers as needed.

