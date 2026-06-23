# Configure platform gateway route timeouts
## Collection upload limits

Collections uploaded to automation hub are typically under 20 MB for public content and under 200 MB for private automation hub. These uploads are affected by the gateway request body size limit.

Platform gateway controls request body size through the `GRPC_SERVER_MAX_RECEIVE_MESSAGE_LENGTH` setting (default: 20 MiB, minimum: 4 MiB), which is enforced by the Envoy proxy. This default matches automation hub's 20 MB limit, so collection uploads work without additional configuration.

For collections larger than 20 MB, such as large private content, increase `GRPC_SERVER_MAX_RECEIVE_MESSAGE_LENGTH` by setting the environment variable to match your largest expected collection size. When increasing this value, also increase `ENVOY_PER_CONNECTION_BUFFER_LIMIT_BYTES` (default: 25 MiB) to remain at least 5 MiB above the request body size limit.

Note:

For containerized deployments, the installer variable `gateway_nginx_client_max_body_size` (default: `5m`) controls nginx body size limits. Since nginx sits in front of Envoy in containerized topologies, this limit is applied first. If collection uploads fail with HTTP 413 errors on containerized deployments, increase this value to at least `20m` to match automation hub's default.

