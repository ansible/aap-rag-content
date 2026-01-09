# 10. Simplified event routing
## 10.1. Event streams




Event streams provide the secure, authenticated entry point for external systems to send events over the internet directly to {DAcontroller},simplifying remote data ingestion.

Event-Driven Ansible controller supports six different event stream types.


<span id="idm140618138417392"></span>
**Table 10.1. Event Stream Types**

| Type | Description | Vendor examples |
| --- | --- | --- |
|  **Hashed Message Authentication Code (HMAC)** | Uses a shared secret between Event-Driven Ansible controller and the vendors webhook server. This guarantees message integrity. | Github |
|  **Basic Authentication** | Uses HTTP basic authentication. | Datadog, Dynatrace |
|  **Token Authentication** | Uses Token Authentication. Usually the HTTP Header is **Authorization** but some vendors like Gitlab use **X-Gitlab-Token** . | Gitlab, ServiceNow |
|  **OAuth2** | Uses Machine-to-Machine (M2M) mode with a grant type called **client credentials** . The token is opaque. | Dynatrace |
|  **OAuth2 with JWT** | Uses M2M mode with a grant type called **client credentials** . The token is JSON Web Token (JWT). | Datadog |
|  **Elliptic Curve Digital Signature Algorithm (ECDSA)** | Verifies message authenticity using a public/private key pair. The sender signs the message with a private key, and the receiver (EDA Controller) validates it with a public key. | SendGrid, Twilio |
|  **Mutual Transport Layer Security (mTLS)** | Ensures two-way authentication between Event-Driven Ansible controller and the client sending events through an event stream. It has two sub-types:

- Certificate
- Subject


Needs the vendor’s CA certificate to be present in our servers at startup. This supports non-repudiation. | PagerDuty |




Important
If you are using an mTLS event stream with a load balancer, you must enable SSL pass-through (or L4 routing) in your load balancer configuration.

This is required because the SSL termination and client certificate validation for mTLS must occur at the platform gateway proxy server. Consult your load balancer documentation for details on enabling SSL pass-through.



Event-Driven Ansible controller also supports four other specialized event streams that are based on the six basic event stream types:

- GitLab event stream
- GitHub event stream
- ServiceNow event stream
- Dynatrace event stream


These specialized types limit the parameters you use by adding default values. For example, the GitHub event stream is a specialization of the HMAC event stream with many of the fields already populated. After the GitHub event stream credential has been saved, the recommended defaults for this event stream are displayed.

