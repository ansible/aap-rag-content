# Modules in the ansible.platform collection
## Gateway infrastructure

| Module            | Description                                                                                                  | Supported states                  |
| ----------------- | ------------------------------------------------------------------------------------------------------------ | --------------------------------- |
| `service`         | Configure API service routes for automation controller, automation hub, and Event-Driven Ansible controller. | present, absent, exists, enforced |
| `route`           | Configure non-API gateway routes.                                                                            | present, absent, exists, enforced |
| `service_cluster` | Manage service clusters with health check and outlier detection settings.                                    | present, absent, exists, enforced |
| `service_node`    | Add or remove individual service nodes within clusters.                                                      | present, absent, exists, enforced |
| `service_type`    | Define service type definitions with login and logout paths.                                                 | present, absent, exists, enforced |
| `service_key`     | Manage service authentication keys for inter-service communication.                                          | present, absent, exists, enforced |
| `http_port`       | Configure HTTP listener ports for the Envoy proxy.                                                           | present, absent, exists, enforced |
| `ui_plugin_route` | Configure UI plugin routes for front-end plugin integration.                                                 | present, absent, exists, enforced |

