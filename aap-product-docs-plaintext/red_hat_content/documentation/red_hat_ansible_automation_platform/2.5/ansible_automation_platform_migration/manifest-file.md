# 5. Migration artifact structure and verification
## 5.2. Manifest file




The `manifest.yml` file serves as the primary metadata document for the migration artifact, containing critical versioning and component information from your source environment.

Structure the manifest as follows:

```
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

