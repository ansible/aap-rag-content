# 13. Ansible Automation Platform Resource Operator
## 13.2. Using Resource Operator




The Resource Operator itself does not do anything until the user creates an object. As soon as the user creates an **AutomationControllerProject** or **AnsibleJob** resource, the Resource Operator starts processing that object.

**Prerequisites**

- Install the Kubernetes-based cluster of your choice.
- Deploy automation controller using the `    automation-controller-operator` .


**Procedure**

1. After installing the `    automation-controller-resource-operator` in your cluster, you must create a Kubernetes (k8s) secret with the connection information for your automation controller instance.
1. Then you can use Resource Operator to create a k8s resource to manage your automation controller instance.


