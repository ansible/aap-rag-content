# Ansible Automation Platform 2.7 patch release September 14, 2026 (2.7-8)
## Automation Platform Gateway

- Fixed an issue where encrypted preferences could not be decrypted after a `SECRET_KEY` change, causing the gateway to crash with an unactionable traceback; the gateway now exits with a clear message identifying which preferences are affected and their failure type. (AAP-90126)
- Fixed an issue where the `rotate_secret_key` management command failed to re-encrypt fields stored in PostgreSQL `jsonb` columns, leaving `AuthenticatorUser.extra_data` records encrypted with the old key and causing user authentication failures after the deployment secret was updated. (AAP-88914)

