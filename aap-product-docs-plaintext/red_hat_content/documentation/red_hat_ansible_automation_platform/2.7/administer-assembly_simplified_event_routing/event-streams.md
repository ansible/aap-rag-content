# Respond to events from external systems
## Event streams

Event streams provide the secure, authenticated entry point for external systems to send events over the internet directly to Event-Driven Ansible controller,simplifying remote data ingestion.

Event-Driven Ansible controller supports six different event stream types.

*Table 1. Event Stream Types*

| Type                                                   | Description                                                                                                                                                                                                                                                                                | Vendor examples        |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------- |
| <br>Hashed Message Authentication Code (HMAC)          | <br>Uses a shared secret between Event-Driven Ansible controller and the vendors webhook server. This guarantees message integrity.                                                                                                                                                        | <br>Github             |
| <br>Basic Authentication                               | <br>Uses HTTP basic authentication.                                                                                                                                                                                                                                                        | <br>Datadog, Dynatrace |
| <br>Token Authentication                               | <br>Validates incoming event data using a security token passed in the request header. While the standard HTTP header used is **Authorization**, it can be customized for specific platforms, such as using **X-Gitlab-Token** for GitLab integrations.                                    | <br>Gitlab, ServiceNow |
| <br>OAuth2                                             | <br>Uses Machine-to-Machine (M2M) mode with a grant type called **client credentials**. The token is opaque.                                                                                                                                                                               | <br>Dynatrace          |
| <br>OAuth2 with JWT                                    | <br>Uses M2M mode with a grant type called **client credentials**. The token is JSON Web Token (JWT).                                                                                                                                                                                      | <br>Datadog            |
| <br>Elliptic Curve Digital Signature Algorithm (ECDSA) | <br>Verifies message authenticity using a public/private key pair. The sender signs the message with a private key, and the receiver (Event-Driven Ansible controller) validates it with a public key.                                                                                     | <br>SendGrid, Twilio   |
| <br>Mutual Transport Layer Security (mTLS)             | <br>Ensures two-way authentication between Event-Driven Ansible controller and the client sending events through an event stream. It has two sub-types:<br>CertificateSubject<br>Needs the vendor’s CA certificate to be present in our servers at startup. This supports non-repudiation. | <br>PagerDuty          |


Important:

If you are using an mTLS event stream with a load balancer, you must enable SSL pass-through (or L4 routing) in your load balancer configuration.

This is required because the SSL termination and client certificate validation for mTLS must occur at the platform gateway proxy server. Consult your load balancer documentation for details on enabling SSL pass-through.

Event-Driven Ansible controller also supports four other specialized event streams that are based on the six basic event stream types:

- GitLab event stream
- GitHub event stream
- ServiceNow event stream
- Dynatrace event stream


These specialized types limit the parameters you use by adding default values. For example, the GitHub event stream is a specialization of the HMAC event stream with many of the fields already populated. After the GitHub event stream credential has been saved, the recommended defaults for this event stream are displayed.

