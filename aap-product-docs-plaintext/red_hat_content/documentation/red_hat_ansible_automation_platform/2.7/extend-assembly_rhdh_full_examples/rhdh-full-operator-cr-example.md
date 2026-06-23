# Full configuration examples
## Full Operator Backstage CR example for Ansible plug-ins

This example shows the full Backstage custom resource configuration for an Operator-based deployment, including the ADT sidecar container and `imagePullSecrets`.

```yaml
apiVersion: rhdh.redhat.com/v1alpha5
kind: Backstage
metadata:
name: developer-hub
namespace: <your_rhdh_namespace>
spec:
application:
appConfig:
configMaps:
- name: app-config-rhdh
mountPath: /opt/app-root/src
dynamicPluginsConfigMapName: dynamic-plugins-rhdh
extraEnvs:
secrets:
- name: <your_scm_credentials_secret>
- name: <your_rhaap_credentials_secret>
extraFiles:
mountPath: /opt/app-root/src
secrets:
- key: private-key.pem
name: <your_scm_credentials_secret>
route:
enabled: true
database:
enableLocalDb: true
deployment:
patch:
spec:
template:
spec:
imagePullSecrets:
- name: rhdh-registry-pull-secret
containers:
- name: ansible-devtools-server
command:
- adt
- server
image: registry.redhat.io/ansible-automation-platform-2.7/ansible-dev-tools-rhel9:latest
imagePullPolicy: Always
ports:
- containerPort: 8000
protocol: TCP
```

