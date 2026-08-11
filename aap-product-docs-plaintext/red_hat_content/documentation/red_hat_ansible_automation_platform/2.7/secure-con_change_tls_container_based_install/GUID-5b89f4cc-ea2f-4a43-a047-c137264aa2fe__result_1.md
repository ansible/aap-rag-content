# Container-based installations
## Renew self-signed TLS certificates using the installation program
### Results

**Verification**

To verify the CA file and certificate file on Event-Driven Ansible controller:

`openssl verify -CAfile ~/aap/eda/etc/eda.cert ~/aap/eda/etc/eda.cert`

`openssl s_client -connect <EDA_FQDN>:443`

To verify the CA file and certificate file on platform gateway:

`openssl verify -CAfile ~/aap/gateway/etc/gateway.cert`

`~/aap/gateway/etc/gateway.cert`

`openssl s_client -connect <GATEWAY_FQDN>:443`

Verify the CA file and certificate file on automation hub:

`openssl verify -CAfile ~/aap/hub/etc/pulp.cert ~/aap/hub/etc/pulp.cert`

`openssl s_client -connect <HUB_FQDN>:443`

To verify the CA file and certificate file on automation controller:

`~/aap/controller/etc/tower.cert`

`openssl s_client -connect <CONTROLLER_FQDN>:443`

