# 10. Simplified event routing
## 10.5. Static Unique Universal Identifiers (UUIDs) for event streams




You can configure an event stream with a static Unique Universal Identifier (UUID) to ensure its webhook URL remains consistent, even if the event stream service is recreated.

This feature is relevant for disaster recovery scenarios where external systems, like firewalls or third-party webhooks, cannot be easily reconfigured to use a new URL. Here are key concepts when considering using static UUIDs:

You must ensure that additional security measures are in place, such as robust credential types (HMAC, mTLS) and network restrictions.

