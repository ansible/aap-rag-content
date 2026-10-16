# Ansible Automation Platform 2.7 patch release September 14, 2026 (2.7-8)
## Containerized installer

- Gateway uWSGI request buffer size is increased to 32 KB so Entra ID and other SSO logins no longer fail when the callback request exceeds 10 KB. (AAP-89129)

