# 5. Migration artifact structure and verification
## 5.1. Artifact structure




The migration artifact serves as a comprehensive package containing all necessary components to successfully transfer your Ansible Automation Platform deployment.

Structure the artifact as follows:

```
/
manifest.yml
secrets.yml
sha256sum.txt
-&gt; controller:
controller.pgc
-&gt; custom_configs:
foo.py
bar.py
-&gt; gateway:
gateway.pgc
-&gt; hub:
hub.pgc
```

