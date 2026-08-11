# Container-based installations

You can change or renew the TLS certificates and keys for your container-based Ansible Automation Platform installation. The process involves a preparation step, either providing new custom certificates or deleting or moving the old certificates, followed by running the installation program.

Important:

Do not manually edit certificate files or restart individual services for container-based installations. Container-based Ansible Automation Platform runs services inside podman containers, so host-level commands such as `systemctl reload nginx.service` do not apply. Always use the installation program to make certificate changes.

