# Operator-managed NetworkPolicies
## External databases and Redis

When you use an external (customer-managed) PostgreSQL database or Redis instance instead of the operator-deployed defaults, the relevant NetworkPolicy allows egress to the configured port to any destination.

- If you use an external PostgreSQL database, components that connect to it require egress on port 5432 to any destination.
- If you use an external Redis instance, the platform gateway requires egress on port 6379 to any destination.

