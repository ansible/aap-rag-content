# Modules in the ansible.platform collection
## Application and token management

| Module           | Description                                                                                                                                      | Supported states                  |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------- |
| `application`    | Create, update, or delete OAuth2 applications for platform gateway. Configure grant types, client types, and redirect URIs.                      | present, absent, exists, enforced |
| `token`          | Create or delete OAuth2 tokens. Each run creates a new token; this module is not idempotent. The token value is only available at creation time. | present, absent                   |
| `ca_certificate` | Manage CA certificates for mutual TLS (mTLS) authentication.                                                                                     | present, absent, exists           |

