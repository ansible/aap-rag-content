# Install in a disconnected environment
## Disconnected installation inventory requirements

Disconnected (bundled) installations require different inventory variables from online installations. The following table shows the key differences:

*Table 1. Online vs disconnected inventory comparison*

| Variable            | Online Installation                 | Disconnected Installation           |
| ------------------- | ----------------------------------- | ----------------------------------- |
| `registry_username` | Required (when`registry_auth=true`) | Not used (do not set)               |
| `registry_password` | Required (when`registry_auth=true`) | Not used (do not set)               |
| `bundle_install`    | Not used (defaults to`false`)       | Required (set to`true`)             |
| `bundle_dir`        | Not used                            | Required (path to bundle directory) |

**Disconnected inventory example**

The following example shows a minimal disconnected installation inventory configuration:

```
[all:vars]
# Disconnected installation settings
bundle_install=true
bundle_dir=<path_to_bundle_directory>

# Database credentials (required)
postgresql_admin_username=postgres
postgresql_admin_password=<password>

# Do NOT set registry credentials for disconnected installations
# Setting registry_username or registry_password causes the installer
# to attempt registry connections, which will fail in disconnected environments
```

