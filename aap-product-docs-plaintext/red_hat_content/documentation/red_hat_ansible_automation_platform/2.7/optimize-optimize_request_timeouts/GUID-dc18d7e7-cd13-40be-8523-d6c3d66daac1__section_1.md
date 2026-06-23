# Optimize request timeouts
## Cascading client timeouts
### Timeout mathematical relationships

Ansible Automation Platform maintains a downward mathematical cascade to ensure correct behavior and assist with debugging. Ansible Automation Platform applies the following logic to internal layers:

- The `client_request_timeout` serves as the primary value from which others are derived.
- The sum of the Envoy `request_timeout` and the gRPC authentication timeout (`gateway_grpc_auth_service_timeout`) is less than the `client_request_timeout`.
- The Nginx read timeout (`nginx_read_timeout`) is less than or equal to the Envoy `request_timeout`.
- The Python web server timeout (`python_webserver_timeout`) is less than or equal to the `nginx_read_timeout`.

