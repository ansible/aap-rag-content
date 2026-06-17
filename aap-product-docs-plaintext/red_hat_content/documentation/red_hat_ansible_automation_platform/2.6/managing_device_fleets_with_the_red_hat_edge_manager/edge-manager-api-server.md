# 2. Red Hat Edge Manager architecture
## 2.2. Red Hat Edge Manager API server

The API server is a core part of the Red Hat Edge Manager service that gives users and agents an option to communicate with the service.

The API server exposes the following endpoints:

User-facing API endpoint
Users can connect to the user-facing API endpoint from the CLI or the web console. Users must authenticate on the platform gateway to obtain a JSON Web Token (JWT) to make HTTPS requests.

Agent-facing API endpoint
Agents connect to the agent-facing endpoint, which is mTLS-protected. The service authenticates devices by using the X.509 client certificates.

The Red Hat Edge Manager service also communicates with various external systems to authenticate and authorize users, get mTLS certificates signed, or query configuration for managed devices.

