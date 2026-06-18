# Configure TLS/SSL for metrics service databases

Enable TLS/SSL encryption for metrics service database connections to protect metrics data in transit and meet security policies.

## About this task

Use this procedure when securing database connections for compliance requirements.

## Procedure

1.  Configure PostgreSQL for TLS
Edit postgresql.conf:

```
ssl = on
ssl_cert_file = '/path/to/server.crt'
ssl_key_file = '/path/to/server.key'
ssl_ca_file = '/path/to/ca.crt'
```

2.  Configure metrics service for TLS
Edit your inventory file:

```
[all:vars]
automationmetrics_pg_sslmode=require
automationmetrics_pg_cert_auth=true
ca_trust_bundle=/path/to/ca-bundle.crt
```
Note:
When `automationmetrics_pg_cert_auth` is set to `true`, the installer automatically generates TLS certificates for database connections. For custom certificates, use the tasks/tls_postgresql.yml task.

## Results

**TLS/SSL modes**

| Mode          | Encryption                              | Certificate Verification |
| ------------- | --------------------------------------- | ------------------------ |
| `disable`     | No                                      | No                       |
| `allow`       | Attempts encrypted, accepts unencrypted | No                       |
| `prefer`      | Prefers encrypted, accepts unencrypted  | No                       |
| `require`     | Yes                                     | No                       |
| `verify-ca`   | Yes                                     | CA verification          |
| `verify-full` | Yes                                     | CA + hostname            |
