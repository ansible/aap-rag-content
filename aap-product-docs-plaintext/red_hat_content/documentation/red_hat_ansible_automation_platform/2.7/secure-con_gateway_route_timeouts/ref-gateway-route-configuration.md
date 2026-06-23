# Configure platform gateway route timeouts
## When to configure gateway settings

Adjust platform gateway settings when you experience upload errors or timeouts after routing traffic through platform gateway in Ansible Automation Platform 2.7.

### Symptoms requiring configuration changes

Adjust platform gateway settings if you experience:

- **HTTP 413 Request Entity Too Large errors** when uploading collections: increase `GRPC_SERVER_MAX_RECEIVE_MESSAGE_LENGTH` and `ENVOY_PER_CONNECTION_BUFFER_LIMIT_BYTES` (and `gateway_nginx_client_max_body_size` for containerized deployments).
- **Timeout errors** during container image pushes: increase route timeout values.
- **Incomplete transfers or interrupted uploads:** increase route timeout values.

### Affected operations

| Operation                                           | Primary setting                          | Size range   |
| --------------------------------------------------- | ---------------------------------------- | ------------ |
| Collection uploads to automation hub                | `GRPC_SERVER_MAX_RECEIVE_MESSAGE_LENGTH` | Up to 200 MB |
| Container image push (`podman push`, `docker push`) | Route timeout                            | 1-10+ GB     |
| Execution environment uploads                       | Route timeout                            | 1-10+ GB     |
| Bulk content synchronization                        | Route timeout                            | Varies       |

