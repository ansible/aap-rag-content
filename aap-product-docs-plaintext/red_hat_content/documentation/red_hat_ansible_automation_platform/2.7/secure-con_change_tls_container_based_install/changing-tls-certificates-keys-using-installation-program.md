# Container-based installations
## Change TLS certificates and keys using the installation program

The following procedure describes how to update the TLS certificates and keys by using the installation program.

### Procedure

1. To prepare the certificates and keys, choose one of the following methods:

- To provide custom certificates - For each service that requires updated TLS certificates, copy the new certificates and keys to a path relative to the Ansible Automation Platform installer. Then update the inventory file variables with the absolute paths to the new files.

```yaml
# Platform gateway
gateway_tls_cert=<path_to_tls_certificate>
gateway_tls_key=<path_to_tls_key>
gateway_pg_tls_cert=<path_to_tls_certificate>
gateway_pg_tls_key=<path_to_tls_key>
gateway_redis_tls_cert=<path_to_tls_certificate>
gateway_redis_tls_key=<path_to_tls_key>

# Automation controller
controller_tls_cert=<path_to_tls_certificate>
controller_tls_key=<path_to_tls_key>
controller_pg_tls_cert=<path_to_tls_certificate>
controller_pg_tls_key=<path_to_tls_key>

# Automation hub
hub_tls_cert=<path_to_tls_certificate>
hub_tls_key=<path_to_tls_key>
hub_pg_tls_cert=<path_to_tls_certificate>
hub_pg_tls_key=<path_to_tls_key>

# Event-Driven Ansible
eda_tls_cert=<path_to_tls_certificate>
eda_tls_key=<path_to_tls_key>
eda_pg_tls_cert=<path_to_tls_certificate>
eda_pg_tls_key=<path_to_tls_key>

# PostgreSQL
postgresql_tls_cert=<path_to_tls_certificate>
postgresql_tls_key=<path_to_tls_key>

# Receptor
receptor_tls_cert=<path_to_tls_certificate>
receptor_tls_key=<path_to_tls_key>
```

- To generate new certificates - If you want the installation program to generate a new certificate for a service, delete or move the existing certificates and keys. *Table 1. Certificate and key file paths per service*

| Service               | Certificate file path             | Key file path                     |
| --------------------- | --------------------------------- | --------------------------------- |
| Automation controller | `~/aap/controller/etc/tower.cert` | `~/aap/controller/etc/tower.key`  |
| Event-Driven Ansible  | `~/aap/eda/etc/eda.cert`          | `~/aap/eda/etc/eda.key`           |
| Platform gateway      | `~/aap/gateway/etc/gateway.cert`  | `~/aap/gateway/etc/gateway.key`   |
| Automation hub        | `~/aap/hub/etc/pulp.cert`         | `~/aap/hub/etc/pulp.key`          |
| PostgreSQL            | `~/aap/postgresql/server.crt`     | `~/aap/postgresql/server.key`     |
| Receptor              | `~/aap/receptor/etc/receptor.crt` | `~/aap/receptor/etc/receptor.key` |
| Redis                 | `~/aap/redis/server.crt`          | `~/aap/redis/server.key`          |

2. After preparing your certificates, run the `install` playbook from your installation directory:
`ansible-playbook -i <inventory_file_name>`

`ansible.containerized_installer.install`

### Results

Verify that the new TLS certificates are in use by checking that the services are running and accessible. To do this, check a specific endpoint by using `curl`:

```
$ curl -vk https://<hostname_or_ip>:<port_number>/api/v2/
```

The output of this command gives details about the TLS handshake. Look for the following output to confirm the correct certificate is being used:

```
*  SSL certificate verify OK
```
