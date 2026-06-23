# Contents of the migration artifact
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

