# Contents of the migration artifact

The migration artifact packages all necessary data and configurations from your source environment. Verify its structure and contents to ensure a successful migration.

## Artifact structure

The migration artifact is a comprehensive package containing all necessary components to transfer your Ansible Automation Platform deployment.

Structure the artifact as follows:

```
/
manifest.yml
secrets.yml
sha256sum.txt

-> controller:
controller.pgc
-> custom_configs:
foo.py
bar.py
-> gateway:
gateway.pgc
-> hub:
hub.pgc
```

## Manifest file

The `manifest.yml` file serves as the primary metadata document for the migration artifact. It contains critical versioning and component information from your source environment.

Structure the manifest as follows:

```
---
aap_version: X.Y # The version being migrated
platform: rpm # The source platform type
components:
- name: controller
version: x.y.z
- name: hub
version: x.y.z
- name: gateway
version: x.y.z
```

## Secrets file

The `secrets.yml` file in the migration artifact includes essential Django `SECRET_KEY` values required for authentication between services.

Structure the secrets file as follows:

```
controller_pg_database: <redacted>
controller_secret_key: <redacted>
gateway_pg_database: <redacted>
gateway_secret_key: <redacted>
hub_pg_database: <redacted>
hub_secret_key: <redacted>
hub_db_fields_encryption_key: <redacted>
```


Note:

Ensure the `secrets.yml` file is encrypted and kept in a secure location.

## Migration artifact creation checklist

Use this checklist to verify the migration artifact.

- Database dumps: Include complete database dumps for each component.   * Ensure the automation controller database (`controller.pgc`) is present in the artifact.
* Ensure the automation hub database (`hub.pgc`) is present in the artifact.
* Ensure the platform gateway database (`gateway.pgc`) is present in the artifact.
- Secret dumps: Export and include all security-related information.   * Validate that all secret values are present in the `secrets.yml` file.
- Custom configurations: Package all customizations from the source environment.   * Validate that any custom Python scripts or modules (for example `foo.py`, `bar.py`) are present on the artifact.
* Document any non-standard configurations or environment-specific settings.
- Database information: Document database details.   * Include the database names for all components.
* Document database users and required permissions.
* Note any database-specific configurations or optimizations.
- Verification: Ensure artifact integrity and completeness.   * Verify that all required files are included in the artifact.
* Verify that checksums exist for all included database files.
* Test the artifact’s structure and accessibility.
* Consider encrypting the artifact for secure transfer to the target environment.
* Document any known limitations or special considerations.
