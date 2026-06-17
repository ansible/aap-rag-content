# 2. Hardening Ansible Automation Platform
## 2.2. Installation
### 2.2.2. Security-relevant variables in the installation inventory

The installation inventory file defines the architecture of the Ansible Automation Platform infrastructure and provides several variables that can be used to modify the initial configuration of the infrastructure components. For more information on the installation program inventory, see [About the installation program inventory file](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/planning_your_installation/con-inventory-introduction_planning).

#### 2.2.2.1. RPM deployment variables

The following table lists several security-relevant variables and their recommended values for an RPM-based deployment.

**Table 2.2. Security-relevant inventory variables**

| **RPM deployment variable** | **Recommended Value** | **Details** |
| --- | --- | --- |
| <br> `postgres_use_ssl` | <br>  true | <br>  The installation program configures the installer-managed Postgres database to accept SSL/TLS-based connections when this variable is set. <br>  The default for this variable is false which means SSL/TLS is not used for PostgreSQL connections. <br>  When set to true, the platform connects to PostgreSQL by using SSL/TLS. |
| <br> `pg_sslmode` `automation_gateway_pg_sslmode` `automationhub_pg_sslmode` `automationcontroller_pg_sslmode` | <br>  verify-full | <br>  These variables control mutual TLS (mTLS) authentication to the database. By default, when each service connects to the database, it tries an encrypted connection, but it is not enforced. <br>  Setting this variable to `verify-full` enforces an mTLS negotiation between the service and the database. The `postgres_use_ssl` variable must also be set to `true` for this pg_sslmode to be effective. <br> **NOTE**: If a third-party database is used instead of the installer-managed database, the third-party database must be set up independently to accept mTLS connections. |
| <br> `nginx_disable_hsts` `automation_gateway_disable_hsts` `automationhub_disable_hsts` `automationcontroller_disable_hsts` | <br>  false | <br>  If set to `true`, these variables disable HTTPS *strict transport Security* (HSTS) connections to each of the component web services. <br>  The default is `false`. If these variables are absent from the installation program inventory it is effectively equivalent to defining the variables as `false`. |

#### 2.2.2.2. Container deployment variables

The following table lists several security-relevant variables and their recommended values for a container-based deployment.

**Table 2.3. Security-relevant containerized inventory variables**

| **Container deployment variable** | **Recommended Value** | **Details** |
| --- | --- | --- |
| <br> `postgresql_disable_tls` | <br>  false | <br>  If set to `true`, this variable disables TLS connections to the installation program-managed PostgreSQL database. <br>  The default is `false`<br>  If this variable is absent from the installation program inventory, it is effectively equivalent to defining the variable as `false`. |
| <br> `controller_pg_sslmode` `gateway_pg_sslmode` `hub_pg_sslmode` `eda_pg_sslmode` | <br>  verify-full | <br>  These variables control mutual TLS (mTLS) authentication to the database. <br>  By default, when each service connects to the database, it tries an encrypted connection, but it is not enforced. Setting this variable to `verify-full` enforces an mTLS negotiation between the service and the database.       Note   <br>  If a third-party database is used instead of the installation program-managed database, the third-party database must be set up independently to accept mTLS connections. |
| <br> `controller_nginx_disable_https` `gateway_nginx_disable_https` `hub_nginx_disable_https` `eda_nginx_disable_https` | <br> `false` | <br>  If set to `true`, these variables disable HTTPS connections to each of the component web services. <br>  The default is `false`. <br>  If these variables are absent from the installation program inventory, it is effectively equivalent to defining the variables as `false`. |
| <br> `controller_nginx_disable_hsts` `gateway_nginx_disable_hsts` `hub_nginx_disable_hsts` `eda_nginx_disable_hsts` | <br> `false` | <br>  If set to 'true', these variables disable HTTPS Strict Transport Security (HSTS) connections to each of the component web services. <br>  The default is `false`. <br>  If these variables are absent from the installation program inventory it is effectively equivalent to defining the variables as `false`. |

In an enterprise architecture where a load balancer is used in front of multiple platform gateways, SSL/TLS client connections can be terminated at the load balancer or passed through to the individual AAP servers. If SSL/TLS is being terminated at the load balancer, re-encrypt traffic from the load balancer to the individual Ansible Automation Platform servers. This ensures that end-to-end encryption is in use. In this scenario, the `*_disable_https` variables listed are set to the default value of `false`.

