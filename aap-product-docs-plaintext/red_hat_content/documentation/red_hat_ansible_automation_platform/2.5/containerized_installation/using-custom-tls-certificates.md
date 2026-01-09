# 5. Advanced containerized deployment
## 5.7. Configuring custom TLS certificates




Red Hat Ansible Automation Platform uses X.509 certificate and key pairs to secure traffic. These certificates secure internal traffic between Ansible Automation Platform components and external traffic for public UI and API connections.

There are two primary ways to manage TLS certificates for your Ansible Automation Platform deployment:

1. Ansible Automation Platform generated certificates (this is the default)
1. User-provided certificates


