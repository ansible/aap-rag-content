# Operator growth topology
## Metrics service configuration

`spec.metrics.disabled: false` - Enables metrics service deployment (default: false, meaning enabled)

- Setting `disabled: true` will prevent metrics service deployment
- The operator automatically creates a MetricsService CR named `<aap-name>`-metrics

