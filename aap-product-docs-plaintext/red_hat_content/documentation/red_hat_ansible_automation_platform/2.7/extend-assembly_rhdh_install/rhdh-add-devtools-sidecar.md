# Install the Ansible plug-ins
## Add the Ansible Developer Tools sidecar container

After the plug-ins load, add the Ansible Developer Tools container as a sidecar container to the Red Hat Developer Hub pod.

### About this task

Note:

The `ansible-dev-tools-rhel9` container image is hosted on `registry.redhat.io` and requires Red Hat Ansible Automation Platform subscription entitlements. If your OpenShift Container Platform cluster's global pull secret does not include AAP-entitled credentials, you must create an `imagePullSecrets` entry in the deployment patch. You can reuse the same `auth.json` credentials created for the dynamic plug-ins registry secret:

```terminal
$ oc create secret docker-registry rhdh-registry-pull-secret \
--from-file=.dockerconfigjson=auth.json \
-n <your_rhdh_namespace>
```

Then add the `imagePullSecrets` field to the deployment patch as shown in the examples below.

### Procedure

1.  Add the Ansible Developer Tools sidecar container to your deployment configuration.
**Operator installation**

Modify the Backstage custom resource to add a `containers` block in the `spec.deployment.patch.spec.template.spec` block:

```yaml
apiVersion: rhdh.redhat.com/v1alpha5
kind: Backstage
metadata:
name: developer-hub
spec:
deployment:
patch:
spec:
template:
spec:
imagePullSecrets:
- name: rhdh-registry-pull-secret
containers:
- command:
- adt
- server
image: registry.redhat.io/ansible-automation-platform-27/ansible-dev-tools-rhel9:latest
imagePullPolicy: Always
ports:
- containerPort: 8000
protocol: TCP
```

**Helm chart installation**

Update the `extraContainers` section in the Helm chart YAML:

```yaml
upstream:
backstage:
# ...
extraContainers:
- command:
- adt
- server
image: >-
registry.redhat.io/ansible-automation-platform-27/ansible-dev-tools-rhel9:latest
imagePullPolicy: IfNotPresent
name: ansible-devtools-server
ports:
- containerPort: 8000
resources:
requests:
cpu: 1
memory: 1Gi
limits:
cpu: 2500m
memory: 2.5Gi
# ...
```

Note:
The image pull policy is `imagePullPolicy: IfNotPresent`. The image is pulled only if it does not already exist on the node. Update it to `imagePullPolicy: Always` if you always want to use the latest image.

The default resource requests and limits are shown in the Helm chart example. To customize these values, for example if your namespace enforces a `LimitRange`, see [Customize Ansible Developer Tools server resources](/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-assembly_rhdh_ocp_configure_optional#customize-devtools-server-resources "Ansible Developer Tools sidecar container ships with default CPU and memory resource requests and limits. Customize these values if your namespace enforces a LimitRange with lower values or if you want to tune resources for your workload.").

2.  Apply the changes. For Operator deployments, click **Save**. For Helm deployments, click **Upgrade**.

