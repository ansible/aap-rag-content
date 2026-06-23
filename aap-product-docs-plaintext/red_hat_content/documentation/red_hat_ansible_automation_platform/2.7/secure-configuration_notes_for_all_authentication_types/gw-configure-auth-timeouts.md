# Configuration notes for all authentication types
## Configure authenticator timeouts

Configure layered timeout settings for password-based authenticators, such as LDAP, RADIUS, and TACACS+. Properly aligning these upstream and downstream timeouts helps ensure that your authentication requests do not fail.

The system processes authentication requests through a chain of services, each with its own timeout setting:

- **Envoy timeout**: The total time a request can take before the initial entry point (Envoy) terminates the connection. This is the highest-level timeout.
- **gRPC timeout**: A downstream timeout that bounds the time spent communicating with the internal authentication service.
- **Authenticator timeout**: The lowest-level timeout, which defines how long an individual authenticator (LDAP, RADIUS, TACACS+) waits for a response from its third-party server.

