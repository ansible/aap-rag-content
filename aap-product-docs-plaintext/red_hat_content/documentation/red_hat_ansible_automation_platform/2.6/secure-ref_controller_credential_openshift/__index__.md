# OpenShift or Kubernetes API Bearer Token credential type

Select this credential type to create instance groups that point to a Kubernetes or OpenShift container.

For more information, see [Determine where automation runs with instance groups](/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-assembly_ug_controller_instance_groups#controller-instance-groups "An Instance Group enables you to group instances in a clustered environment. Policies dictate how instance groups behave and how jobs are executed. The following view displays the capacity levels based on policy algorithms:")and [Control where automation runs with container groups](/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-con_controller_container_groups#controller-container-groups "Ansible Automation Platform supports container groups, which enable you to run jobs in automation controller regardless of whether automation controller is installed as a standalone, in a virtual environment, or in a container.").

Provide the following information for container credentials:

- **OpenShift or Kubernetes API Endpoint** (required): The endpoint used to connect to an OpenShift or Kubernetes container.
- **API authentication bearer token** (required): The token used to authenticate the connection.
- Optional: **Verify SSL**: You can check this option to verify the server’s SSL/TLS certificate is valid and trusted. Environments that use internal or private *Certificate Authority* (CA) must leave this option unchecked to disable verification.
- **Certificate Authority data**: Include the `BEGIN CERTIFICATE` and `END CERTIFICATE` lines when pasting the certificate, if provided.


A container group is a type of instance group that has an associated credential that enables connection to an OpenShift cluster. To set up a container group, you must have the following items:

- A namespace you can start into. Although every cluster has a default namespace, you can use a specific namespace.

- A service account that has the roles that enable it to start and manage pods in this namespace.

- If you use execution environments in a private registry, and have a container registry credential associated with them in automation controller, the service account also requires the roles to get, create, and delete secrets in the namespace. If you do not want to give these roles to the service account, you can pre-create the `ImagePullSecrets` and specify them on the pod spec for the container group. In this case, the execution environment must not have a Container Registry credential associated, or automation controller attempts to create the secret for you in the namespace.

- A token associated with that service account (OpenShift or Kubernetes Bearer Token)

- A CA certificate associated with the cluster

## Creating a service account in an Openshift cluster

Create a service account in an Openshift or Kubernetes cluster to be used to run jobs in a container group through automation controller. After you create the service account, its credentials are provided to automation controller in the form of an Openshift or Kubernetes API bearer token credential.

### About this task

After you create a service account, use the information in the new service account to configure automation controller.

### Procedure

1.  To create a service account, download and use the sample service account, `containergroup sa`, and change it as needed to obtain the credentials:


```
---
apiVersion: v1
kind: ServiceAccount
metadata:
name: containergroup-service-account
namespace: containergroup-namespace
---
kind: Role
apiVersion: rbac.authorization.k8s.io/v1
metadata:
name: role-containergroup-service-account
namespace: containergroup-namespace
rules:
- apiGroups: [""]
resources: ["pods"]
verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
- apiGroups: [""]
resources: ["pods/log"]
verbs: ["get"]
- apiGroups: [""]
resources: ["pods/attach"]
verbs: ["get", "list", "watch", "create"]
---
kind: RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
name: role-containergroup-service-account-binding
namespace: containergroup-namespace
subjects:
- kind: ServiceAccount
name: containergroup-service-account
namespace: containergroup-namespace
roleRef:
kind: Role
name: role-containergroup-service-account
apiGroup: rbac.authorization.k8s.io
```

2.  Apply the configuration from `containergroup-sa.yml`:


```
oc apply -f containergroup-sa.yml
```

3.  Get the secret name associated with the service account:


```
export SA_SECRET=$(oc get sa containergroup-service-account -o json | jq '.secrets[0].name' | tr -d '"')
```

4.  Get the token from the secret:


```
oc get secret $(echo ${SA_SECRET}) -o json | jq '.data.token' | xargs | base64 --decode > containergroup-sa.token
```

5.  Get the CA cert:


```
oc get secret $SA_SECRET -o json | jq '.data["ca.crt"]' | xargs | base64 --decode > containergroup-ca.crt
```

6.  Use the contents of `containergroup-sa.token` and `containergroup-ca.crt` to provide the information for the [OpenShift or Kubernetes API Bearer Token](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-ref_controller_credential_openshift#ref-controller-credential-openShift "Select this credential type to create instance groups that point to a Kubernetes or OpenShift container.") required for the container group.
