# Install in a disconnected environment
## Verify bundle structure

Before running the installer, verify that your bundle directory contains the required subdirectories:

```
ls -la <path_to_bundle_directory>/
```

Expected output:

```
drwxr-xr-x  4 root root 4096 date time .
drwxr-xr-x  3 root root 4096 date time ..
drwxr-xr-x  2 root root 4096 date time collections
drwxr-xr-x  2 root root 4096 date time images
```

The collections/ directory contains Ansible collections. The images/ directory contains container image tar files.

Important:

If you include `registry_username` or `registry_password` in a disconnected installation inventory file, the installer attempts to connect to the registry, which fails in disconnected environments. Always verify that these variables are not set for disconnected installations.

