+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-ref_aap_operational_secrets"
template = "docs/aem-title.html"
title = "Understand how Ansible Automation Platform manages secrets - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_hardening_aap/", "Harden the platform security posture"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-ref_aap_operational_secrets/aem-page/secure-ref_aap_operational_secrets.html"
last_crumb = "Understand how Ansible Automation Platform manages secrets"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Understand how Ansible Automation Platform manages secrets"
oversized = "false"
page_slug = "secure-ref_aap_operational_secrets"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/secure-ref_aap_operational_secrets"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-ref_aap_operational_secrets/toc/toc.json"
type = "aem-page"
+++

# Understand how Ansible Automation Platform manages secrets

Ansible Automation Platform uses several secrets (passwords, keys, and so on) operationally. These secrets are stored unencrypted on the various Ansible Automation Platform servers, as each component service must read them at startup.

All files are protected by UNIX permissions, and restricted to the root user or the appropriate service account user. These files should be routinely monitored to ensure there has been no unauthorized access or modification.

## Container-based installation secrets

Container-based installations of Red Hat Ansible Automation Platform use Podman secrets to store operational secrets. These secrets can be listed using the `podman secret list` command.

By default, Podman stores data in the home directory of the user who installed and runs the containerized Red Hat Ansible Automation Platform services. Podman secrets are stored in the file `$HOME/.local/share/containers/storage/secrets/filedriver/secretsdata.json` as base64-encoded strings, so while they are not in plain text the values are only obfuscated.

The data stored in a Podman secret can be shown using the command `podman secret inspect --showsecret <secret>`.

This file should be routinely monitored to ensure there has been no unauthorized access or modification.

## Automation use secrets

Ansible Automation Platform stores a variety of secrets in the database that are either used for automation or are a result of automation. Automation use secrets include:

- All secret fields of all credential types (passwords, secret keys, authentication tokens, secret cloud credentials).
- Secret tokens and passwords for external services defined in automation controller settings.
- “password” type survey field entries.

You can grant users and teams the ability to use these credentials without actually exposing the credential to the user. This means that if a user moves to a different team or leaves the organization, you do not have to re-key all of your systems.

Ansible Automation Platform uses SSH (or the Windows equivalent) to connect to remote hosts. To pass the key from automation controller to SSH, the key must be decrypted before it can be written to a named pipe. Automation controller then uses that pipe to send the key to SSH (so that it is never written to disk). If passwords are used, automation controller handles those by responding directly to the password prompt and decrypting the password before writing it to the prompt.

As an administrator with superuser access, you can define a custom credential type in a standard format by using a YAML/JSON-like definition. This allows the assignment of new credential types to jobs and inventory updates. This, in turn, lets you to define a custom credential type that works in ways similar to existing credential types. For example, you can create a custom credential type that injects an API token for a third-party web service into an environment variable. Your playbook or custom inventory script can then consume this.

To encrypt secret fields, Ansible Automation Platform uses the *Advanced Encryption Standard* (AES) in *Cipher Block Chaining* (CBC) mode with a 256-bit key for encryption, *Public-Key cryptography Standard* (PKCS7) padding, and *Hash-Based Message Authentication Code* (HMAC) using SHA256 for authentication. The encryption and decryption processes derive the AES-256 bit encryption key from the `SECRET_KEY`, the field name of the model field, and the database-assigned auto-incremented record ID. Thus, if any attribute used in the key generation process changes, Ansible Automation Platform fails to correctly decrypt the secret. Ansible Automation Platform is designed such that the `SECRET_KEY` is never readable in playbooks Ansible Automation Platform launches. This means that these secrets are never readable by Ansible Automation Platform users, and no secret field values are ever made available through the Ansible Automation Platform REST API. If a secret value is used in a playbook, you must use `no_log` on the task so that it is not accidentally logged.

## Protect sensitive data with no_log

If you save Ansible output to a log, you expose any secret data in your Ansible output, such as passwords and usernames. To keep sensitive values out of your logs, mark tasks that expose them with the `no_log: True` attribute.

However, the `no_log` attribute does not affect debugging output, so be careful not to debug playbooks in a production environment.
