# Control where automation runs with container groups
## Create a service account in OpenShift Container Platform or Kubernetes

Use service accounts in an OpenShift cluster or Kubernetes to run jobs in a container group through automation controller. After the service account is created, its credentials are provided to automation controller in the form of an OpenShift or Kubernetes API Bearer Token credential.

### Procedure

1.  To create a service account, download and use the following sample service account example, `containergroup sa` and change it as required to obtain the credentials:


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
- verbs:
- get
- list
- watch
- create
- update
- patch
- delete
apiGroups:
- ''
resources:
- pods
- verbs:
- get
apiGroups:
- ''
resources:
- pods/log
- verbs:
- create
apiGroups:
- ''
resources:
- pods/attach
- verbs:
- get
- create
- delete
apiGroups:
- ''
resources:
- secrets
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

3.  Get an API token by generating a service account token:


```
oc create token containergroup-service-account --duration=$((365*24))h > containergroup-sa.token
```

4.  Get the CA certificate:


```
oc get secret -n openshift-ingress wildcard-tls -o jsonpath='{.data.ca\.crt}' | base64 -d > containergroup-ca.crt
```

5.  Use the contents of `containergroup-sa.token` and `containergroup-ca.crt` to provide the information for the [OpenShift or Kubernetes API Bearer Token](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-con_controller_container_groups#controller-create-service-account "Use service accounts in an OpenShift cluster or Kubernetes to run jobs in a container group through automation controller. After the service account is created, its credentials are provided to automation controller in the form of an OpenShift or Kubernetes API Bearer Token credential.") required for the container group.   1.  To create a container group, create a [OpenShift or Kubernetes API Bearer Token](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-con_controller_container_groups#controller-create-service-account "Use service accounts in an OpenShift cluster or Kubernetes to run jobs in a container group through automation controller. After the service account is created, its credentials are provided to automation controller in the form of an OpenShift or Kubernetes API Bearer Token credential.") credential to use with your container group.

