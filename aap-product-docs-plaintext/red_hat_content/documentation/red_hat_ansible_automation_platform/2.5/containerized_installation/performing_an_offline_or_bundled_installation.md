# 2. Ansible Automation Platform containerized installation
## 2.6. Configuring the inventory file
### 2.6.3. Performing an offline or bundled installation




To perform an offline installation, add the following under the `[all:vars]` group:

```
bundle_install=true
# The bundle directory must include /bundle in the path
bundle_dir=&lt;full_path_to_the_bundle_directory&gt;
```

