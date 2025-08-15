# 10. Simplified event routing
## 10.1. Event streams




Event streams can send events from remote systems to Event-Driven Ansible controller. In a typical set-up, a server sends data to an event stream over the internet to an Event-Driven Ansible event stream receiver. When the data comes over the internet, the request must be authenticated. Depending on the webhook vendor or remote system, the authentication method could differ.

Event-Driven Ansible controller supports six different event stream types.


<span id="idm140351370516672"></span>
**Table 10.1. Event Stream Types**

| Type | Description | Vendors |
| --- | --- | --- |
|  **HMAC** | Hashed Message Authentication Code (HMAC). Uses a shared secret between Event-Driven Ansible controller and the vendors webhook server. This guarantees message integrity. | Github |
|  **Basic Authentication** | Uses HTTP basic authentication. | Datadog, Dynatrace |
|  **Token Authentication** | Uses Token Authentication. Usually the HTTP Header is **Authorization** but some vendors like Gitlab use **X-Gitlab-Token** . | Gitlab, ServiceNow |
|  **OAuth2** | Uses Machine-to-Machine (M2M) mode with a grant type called **client credentials** . The token is opaque. | Dynatrace |
|  **OAuth2 with JWT** | Uses M2M mode with a grant type called **client credentials** . The token is JSON Web Token (JWT). | Datadog |
|  **ECDSA** | Elliptic Curve Digital Signature Algorithm | SendGrid, Twilio |




Event-Driven Ansible controller also supports four other specialized event streams that are based on the six basic event stream types:

- GitLab Event Stream
- GitHub Event Stream
- ServiceNow Event Stream
- Dynatrace Event Stream


These specialized types limit the parameters you use by adding default values. For example, the GitHub Event Stream is a specialization of the HMAC Event Stream with many of the fields already populated. After the GitHub Event Stream credential has been saved, the recommended defaults for the GitHub Event Stream are displayed.

