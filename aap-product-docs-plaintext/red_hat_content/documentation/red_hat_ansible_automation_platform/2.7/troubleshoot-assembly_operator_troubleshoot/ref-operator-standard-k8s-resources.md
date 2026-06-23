# Troubleshoot your Operator-based deployment of Ansible Automation Platform
## Standard Kubernetes resources

Standard Kubernetes resources are a core part of the OpenShift Container Platform. The following table describes the standard resources you can inspect to troubleshoot the state and configuration of an application.

| **Resource name**     | **Description**                                                                                          |
| --------------------- | -------------------------------------------------------------------------------------------------------- |
| <br> `pod`            | <br>Smallest deployable unit containing one or more containers running the application workloads.        |
| <br> `deployment`     | <br>Manages pod configuration and scaling.                                                               |
| <br> `pvc`            | <br>A PersistentVolumeClaim (PVC) is a request for storage resources, used for persistent data storage.  |
| <br> `service`        | <br>Exposes pods as network services with stable IP addresses and DNS names within the cluster.          |
| <br> `ingress`        | <br>Manages external HTTP and HTTPS access to services within the cluster.                               |
| <br> `route`          | <br>An OpenShift-specific resource for exposing services externally (similar to an ingress).             |
| <br> `secrets`        | <br>Stores sensitive data like passwords, tokens, and certificates.                                      |
| <br> `serviceaccount` | <br>Provides identity for processes running in pods to access permissions to other Kubernetes resources. |

