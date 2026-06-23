# Optimize request timeouts
## Cascading client timeouts

Cascading timeouts ensure that if an outer layer times out, inner processes also terminate to prevent resource exhaustion. Set the primary timeout at the Gateway level to synchronize timeouts across applications.

