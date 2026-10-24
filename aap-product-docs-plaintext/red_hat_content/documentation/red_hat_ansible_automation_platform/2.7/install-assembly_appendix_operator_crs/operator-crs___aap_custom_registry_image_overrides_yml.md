# Red Hat Ansible Automation Platform custom resources
## Custom resources
### aap-custom-registry-image-overrides.yml

Use this custom resource example to replace default platform component images with images from an internal container registry. This is useful when your deployment team does not have cluster-admin permissions to configure a cluster-level `ImageDigestMirrorSet` and has instead mirrored images manually to an internal registry.

```
---
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
name: myaap
spec:
# Platform gateway images
image: registry.example.com/ansible-automation-platform-<platform_version>/ansible-automation-platform-<platform_version>-gateway-rhel9
image_version: latest
image_proxy: registry.example.com/openshift-service-mesh/proxyv2-rhel9
image_proxy_version: latest

# Gateway database and cache images
postgres_image: registry.example.com/rhel9/postgresql-15
postgres_image_version: latest
redis_image: registry.example.com/rhel9/redis-7
redis_image_version: latest

# Pull secret for gateway, PostgreSQL, and Redis pods
image_pull_secrets:
- internal-registry-pull-secret
image_pull_policy: Always

metrics:
image: registry.example.com/ansible-automation-platform-<platform_version>/ansible-automation-platform-<platform_version>-metrics-rhel9
image_version: latest
image_pull_secrets:
- internal-registry-pull-secret
image_pull_policy: Always

controller:
disabled: false
image: registry.example.com/ansible-automation-platform-<platform_version>/controller-rhel9
image_version: latest
init_container_image: registry.example.com/ansible-automation-platform-<platform_version>/controller-rhel9
init_container_image_version: latest
postgres_image: registry.example.com/rhel9/postgresql-15
postgres_image_version: latest
redis_image: registry.example.com/rhel9/redis-7
redis_image_version: latest
image_pull_secrets:
- internal-registry-pull-secret
image_pull_policy: Always

eda:
disabled: false
image: registry.example.com/ansible-automation-platform-<platform_version>/eda-controller-rhel9
image_version: latest
image_web: registry.example.com/ansible-automation-platform-<platform_version>/eda-controller-ui-rhel9
image_web_version: latest
postgres_image: registry.example.com/rhel9/postgresql-15
postgres_image_version: latest
image_pull_secrets:
- internal-registry-pull-secret
image_pull_policy: Always

hub:
disabled: false
image: registry.example.com/ansible-automation-platform-<platform_version>/hub-rhel9
image_version: latest
image_web: registry.example.com/ansible-automation-platform-<platform_version>/hub-web-rhel9
image_web_version: latest
postgres_image: registry.example.com/rhel9/postgresql-15
postgres_image_version: latest
redis_image: registry.example.com/rhel9/redis-7
redis_image_version: latest
image_pull_secrets:
- internal-registry-pull-secret
image_pull_policy: Always
storage_type: file
file_storage_storage_class: nfs-local-rwx
file_storage_size: 10Gi
```

Note:

Replace `<platform_version>` with your installed version, for example 27.

Replace `registry.example.com` with your internal registry hostname and path, and replace `latest` with a pinned tag or digest for each image. Ensure all images are mirrored and the pull secret exists in the same namespace as the `AnsibleAutomationPlatform` CR before you deploy. The top-level `image_pull_secrets` field applies only to gateway, PostgreSQL, and Redis pods; each component requires its own `image_pull_secrets` entry.
