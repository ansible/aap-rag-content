# Ansible Automation Platform 2.7 patch release September 21, 2026 (2.7-9)
## Django Ansible Base

- Fixed an issue where authentication mappings that assign a global role to an organization or team are now rejected at save time instead of failing silently at login. (AAP-92091)
- Fixed an issue where an issue where OIDC RP-initiated logout incorrectly revoked all OAuth tokens for a user. Logout now removes only tokens belonging to the OAuth application that initiated logout and that were used only for authentication. (AAP-92790)
- Fixed an issue where namespace-scoped role assignments from Gateway not being applied in Hub. (AAP-93576)

