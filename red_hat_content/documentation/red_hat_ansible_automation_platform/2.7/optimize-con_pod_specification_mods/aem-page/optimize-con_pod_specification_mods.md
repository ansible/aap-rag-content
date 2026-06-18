+++
title = "Introduction - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/optimize-con_pod_specification_mods"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/optimize-assembly_pod_spec_modifications/", "Performance tuning for operator environments"]]
category = "Optimize"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/optimize-con_pod_specification_mods/aem-page/optimize-con_pod_specification_mods.html"
last_crumb = "Introduction"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Introduction"
oversized = "false"
page_slug = "optimize-con_pod_specification_mods"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/optimize-con_pod_specification_mods"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/optimize-con_pod_specification_mods/toc/toc.json"
type = "aem-page"
+++

# Introduction

The Kubernetes concept of a pod is one or more containers deployed together on one host, and the smallest compute unit that can be defined, deployed, or managed.

Pods are the equivalent of a machine instance (physical or virtual) to a container. Each pod is allocated its own internal IP address, therefore owning its entire port space, and containers within pods can share their local storage and networking.

Pods have a life cycle. They are defined, then they are assigned to run on a node, then they run until their containers exit or they are removed for some other reason. Pods, depending on policy and exit code, can be removed after exiting, or can be retained to enable access to the logs of their containers.

Red Hat Ansible Automation Platform provides a simple default pod specification, however, you can provide a custom YAML, or JSON document that overrides the default pod specification. This custom document uses custom fields, such as `ImagePullSecrets`, that can be serialized as valid Pod JSON or YAML.

 **Example of a pod that provides a long-running service**

This example demonstrates many features of pods, most of which are discussed in other topics and thus only briefly mentioned here:

```
apiVersion: v1
kind: Pod
metadata:
  annotations: { ... }
  labels:
    deployment: docker-registry-1
    deploymentconfig: docker-registry
    docker-registry: default
  generateName: docker-registry-1-
spec:
  containers:
  - env:
    - name: OPENSHIFT_CA_DATA
      value: ...
    - name: OPENSHIFT_CERT_DATA
      value: ...
    - name: OPENSHIFT_INSECURE
      value: "false"
    - name: OPENSHIFT_KEY_DATA
      value: ...
    - name: OPENSHIFT_MASTER
      value: https://master.example.com:8443
    image: openshift/origin-docker-registry:v0.6.2
    imagePullPolicy: IfNotPresent
    name: registry
    ports:
    - containerPort: 5000
      protocol: TCP
    resources: {}
    securityContext: { ... }              volumeMounts:
    - mountPath: /registry
      name: registry-storage
    - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
      name: default-token-br6yz
      readOnly: true
  dnsPolicy: ClusterFirst
  imagePullSecrets:
  - name: default-dockercfg-at06w
  restartPolicy: Always
  serviceAccount: default
  volumes:
  - emptyDir: {}
    name: registry-storage
  - name: default-token-br6yz
    secret:
      secretName: default-token-br6yz
```

| Label                   | Description                                                                                                                                                                                                                                                                                                                                                                                          |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br> `annotations:`     | <br>Pods can be "tagged" with one or more labels, which can then be used to select and manage groups of pods in a single operation. The labels are stored in key:value format in the metadata hash. One label in this example is `docker-registry=default`.                                                                                                                                          |
| <br> `generateName:`    | <br>Pods must have a unique name within their namespace. A pod definition can specify the basis of a name with the `generateName` attribute, and add random characters automatically to generate a unique name.                                                                                                                                                                                      |
| <br> `containers:`      | <br>`containers` specifies an array of container definitions. In this case (as with most), defines only one container.                                                                                                                                                                                                                                                                               |
| <br> `env:`             | <br>Environment variables pass necessary values to each container.                                                                                                                                                                                                                                                                                                                                   |
| <br> `image:`           | <br>Each container in the pod is instantiated from its own Docker-formatted container image.                                                                                                                                                                                                                                                                                                         |
| <br> `ports:`           | <br>The container can bind to ports made available on the pod’s IP.                                                                                                                                                                                                                                                                                                                                  |
| <br> `resources:`       | <br>When you specify a pod, you can optionally describe how much of each resource a container needs. The most common resources to specify are CPU and memory (RAM). Other resources are available.                                                                                                                                                                                                   |
| <br> `securityContext:` | <br>OpenShift Online defines a security context for containers that specifies whether they are permitted to run as privileged containers, run as a user of their choice, and more. The default context is very restrictive but administrators can change this as required.                                                                                                                           |
| <br> `volumeMounts:`    | <br>The container specifies where external storage volumes should be mounted within the container. In this case, there is a volume for storing the registry’s data, and one for access to credentials the registry needs for making requests against the OpenShift Online API.                                                                                                                       |
| <br> `ImagePullSecrets` | <br>A pod can contain one or more containers, which must be pulled from some registry. If containers come from registries that require authentication, you can give a list of `ImagePullSecrets:` that refer to `ImagePullSecrets` present in the namespace. Having these specified enables Red Hat OpenShift Container Platform to authenticate with the container registry when pulling the image. |
| <br> `restartPolicy:`   | <br>The pod restart policy with possible values `Always`, `OnFailure`, and `Never`. The default value is `Always`.                                                                                                                                                                                                                                                                                   |
| <br> `serviceAccount:`  | <br>Pods making requests against the OpenShift Online API is a common enough pattern that there is a `serviceAccount` field for specifying which service account user the pod should authenticate as when making the requests. This enables fine-grained access control for custom infrastructure components.                                                                                        |
| <br> `volumes:`         | <br>The pod defines storage volumes that are available to its container(s) to use. In this case, it provides an ephemeral volume for the registry storage and a secret volume containing the service account credentials.                                                                                                                                                                            |


You can change the pod used to run jobs in a Kubernetes-based cluster by using automation controller and editing the pod specification in the automation controller UI. The pod specification that is used to create the pod that runs the job is in YAML format.
