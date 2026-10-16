# Understand metrics service architecture
## Transmission phase

1. Anonymized data packaged for transmission
2. Secure HTTPS connection established to Red Hat Data Ingress endpoint using **Segment** (a third-party data pipeline service)
3. Data transmitted through the Gateway /api/metrics/ endpoint (no direct customer-facing endpoints in 2.7 GA)
4. Transmission status logged in `metrics_service` database
5. HTTP/HTTPS proxy supported for environments without direct internet access

Note:

Segment is a third-party data pipeline service that securely routes anonymized metrics from your environment to Red Hat analytics infrastructure. The Segment write key is pre-configured during installation.

**Message size handling**

Metrics service splits anonymized data deterministically into separate messages. If any message exceeds 32 KB, the service splits it further. This ensures reliable transmission of large datasets without message size errors.

