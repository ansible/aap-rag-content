# 1. Pod specification modifications
## 1.1. Introduction




The Kubernetes concept of a pod is one or more containers deployed together on one host, and the smallest compute unit that can be defined, deployed, or managed.

Pods are the equivalent of a machine instance (physical or virtual) to a container. Each pod is allocated its own internal IP address, therefore owning its entire port space, and containers within pods can share their local storage and networking.

Pods have a life cycle. They are defined, then they are assigned to run on a node, then they run until their containers exit or they are removed for some other reason. Pods, depending on policy and exit code, can be removed after exiting, or can be retained to enable access to the logs of their containers.

Red Hat Ansible Automation Platform provides a simple default pod specification, however, you can provide a custom YAML, or JSON document that overrides the default pod specification. This custom document uses custom fields, such as `ImagePullSecrets` , that can be serialized as valid Pod JSON or YAML.

A full list of options can be found in the [OpenShift Online](https://docs.openshift.com/online/pro/architecture/core_concepts/pods_and_services.html) documentation.

**Example of a pod that provides a long-running service**

This example demonstrates many features of pods, most of which are discussed in other topics and thus only briefly mentioned here:

```
apiVersion: v1
kind: Pod
metadata:
annotations: { ... }<span id="CO1-1"><!--Empty--></span><span class="callout">1</span>labels:
deployment: docker-registry-1
deploymentconfig: docker-registry
docker-registry: default
generateName: docker-registry-1-<span id="CO1-2"><!--Empty--></span><span class="callout">2</span>spec:
containers:<span id="CO1-3"><!--Empty--></span><span class="callout">3</span>- env:<span id="CO1-4"><!--Empty--></span><span class="callout">4</span>- name: OPENSHIFT_CA_DATA
value: ...
- name: OPENSHIFT_CERT_DATA
value: ...
- name: OPENSHIFT_INSECURE
value: "false"
- name: OPENSHIFT_KEY_DATA
value: ...
- name: OPENSHIFT_MASTER
value: https://master.example.com:8443
image: openshift/origin-docker-registry:v0.6.2<span id="CO1-5"><!--Empty--></span><span class="callout">5</span>imagePullPolicy: IfNotPresent
name: registry
ports:<span id="CO1-6"><!--Empty--></span><span class="callout">6</span>- containerPort: 5000
protocol: TCP
resources: {}<span id="CO1-7"><!--Empty--></span><span class="callout">7</span>securityContext: { ... }<span id="CO1-8"><!--Empty--></span><span class="callout">8</span>volumeMounts:<span id="CO1-9"><!--Empty--></span><span class="callout">9</span>- mountPath: /registry
name: registry-storage
- mountPath: /var/run/secrets/kubernetes.io/serviceaccount
name: default-token-br6yz
readOnly: true
dnsPolicy: ClusterFirst
imagePullSecrets:<span id="CO1-10"><!--Empty--></span><span class="callout">10</span>- name: default-dockercfg-at06w
restartPolicy: Always<span id="CO1-11"><!--Empty--></span><span class="callout">11</span>serviceAccount: default<span id="CO1-12"><!--Empty--></span><span class="callout">12</span>volumes:<span id="CO1-13"><!--Empty--></span><span class="callout">13</span>- emptyDir: {}
name: registry-storage
- name: default-token-br6yz
secret:
secretName: default-token-br6yz
```

| Label | Description |
| --- | --- |
|  `annotations:` | Pods can be "tagged" with one or more labels, which can then be used to select and manage groups of pods in a single operation. The labels are stored in key:value format in the metadata hash. One label in this example is `docker-registry=default` . |
|  `generateName:` | Pods must have a unique name within their namespace. A pod definition can specify the basis of a name with the `generateName` attribute, and add random characters automatically to generate a unique name. |
|  `containers:` |  `containers` specifies an array of container definitions. In this case (as with most), defines only one container. |
|  `env:` | Environment variables pass necessary values to each container. |
|  `image:` | Each container in the pod is instantiated from its own Docker-formatted container image. |
|  `ports:` | The container can bind to ports made available on the pod’s IP. |
|  `resources:` | When you specify a pod, you can optionally describe how much of each resource a container needs. The most common resources to specify are CPU and memory (RAM). Other resources are available. |
|  `securityContext:` | OpenShift Online defines a security context for containers that specifies whether they are permitted to run as privileged containers, run as a user of their choice, and more. The default context is very restrictive but administrators can change this as required. |
|  `volumeMounts:` | The container specifies where external storage volumes should be mounted within the container. In this case, there is a volume for storing the registry’s data, and one for access to credentials the registry needs for making requests against the OpenShift Online API. |
|  `ImagePullSecrets` | A pod can contain one or more containers, which must be pulled from some registry. If containers come from registries that require authentication, you can give a list of `ImagePullSecrets:` that refer to `ImagePullSecrets` present in the namespace. Having these specified enables Red Hat OpenShift Container Platform to authenticate with the container registry when pulling the image. For further information, see [Resource Management for Pods and Containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) in the Kubernetes documentation. |
|  `restartPolicy:` | The pod restart policy with possible values `Always` , `OnFailure` , and `Never` . The default value is `Always` . |
|  `serviceAccount:` | Pods making requests against the OpenShift Online API is a common enough pattern that there is a `serviceAccount` field for specifying which service account user the pod should authenticate as when making the requests. This enables fine-grained access control for custom infrastructure components. |
|  `volumes:` | The pod defines storage volumes that are available to its container(s) to use. In this case, it provides an ephemeral volume for the registry storage and a secret volume containing the service account credentials. |


You can change the pod used to run jobs in a Kubernetes-based cluster by using automation controller and editing the pod specification in the automation controller UI. The pod specification that is used to create the pod that runs the job is in YAML format. For further information about editing the pod specifications, see [Customizing the pod specification](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/performance_considerations_for_operator_environments/index#proc-customizing-pod-specs) .

