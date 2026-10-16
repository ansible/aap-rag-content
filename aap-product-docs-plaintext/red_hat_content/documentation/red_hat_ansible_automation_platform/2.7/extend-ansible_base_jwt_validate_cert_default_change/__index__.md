# ANSIBLE_BASE_JWT_VALIDATE_CERT default change for Red Hat Ansible Lightspeed

Starting with Ansible Automation Platform 2.7, the `ANSIBLE_BASE_JWT_VALIDATE_CERT` setting defaults to `True`.

On-premise deployments that use self-signed certificates between the Lightspeed service and the platform gateway must install a trusted CA certificate or explicitly disable validation to maintain connectivity.

Important:

If your deployment uses self-signed certificates, the Lightspeed service fails to authenticate users after upgrading. Add your CA certificate to the trust store or disable certificate validation.
