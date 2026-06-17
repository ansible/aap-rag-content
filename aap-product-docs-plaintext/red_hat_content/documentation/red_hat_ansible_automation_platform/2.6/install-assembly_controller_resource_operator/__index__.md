# Ansible Automation Platform Resource Operator

The **Ansible Automation Platform Resource Operator** is a custom resource that allows you to manage and define automation controller objects, such as projects and job templates, through YAML files.

## Resource Operator overview

Resource Operator is a custom resource (CR) that you can deploy after you have created your platform gateway deployment.

With Resource Operator you can define resources such as projects, job templates, and inventories in YAML files.

Ansible Automation Platform then uses the YAML files to create these resources. You can create the YAML through the **Form view** that prompts you for keys and values for your YAML code. Alternatively, to work with YAML directly, you can select **YAML view**.

The Resource Operator provides the following CRs:

- AnsibleJob
- JobTemplate
- Automation controller project
- Automation controller schedule
- Automation controller workflow
- Automation controller workflow template:
- Automation controller inventory
- Automation controller credential

## Use Resource Operator

The Resource Operator itself does not do anything until the user creates an object. As soon as the user creates an **AutomationControllerProject** or **AnsibleJob** resource, the Resource Operator starts processing that object.

### Before you begin

- Install the Kubernetes-based cluster of your choice.
- Deploy automation controller using the `automation-controller-operator`.

### About this task

### Procedure

1.  After installing the `automation-controller-resource-operator` in your cluster, you must create a Kubernetes (k8s) secret with the connection information for your Ansible Automation Platform instance.
2.  Then you can use Resource Operator to create a k8s resource to manage your Ansible Automation Platform instance.

## Connect Resource Operator to Ansible Automation Platform

To connect Resource Operator with platform gateway you must create a Kubernetes secret with the connection information for your Ansible Automation Platform instance.

### About this task

Use the following procedure to create an OAuth2 token for your user in the platform gateway UI.

Note:

You can only create OAuth 2 Tokens for your own user through the API or UI, which means you can only configure or view tokens from your own user profile.

### Procedure

1.  Log in to Red Hat OpenShift Container Platform.
2.  In the navigation panel, select Access Management> (and then)Users.
3.  Select the username you want to create a token for.
4.  Select Tokens> (and then)Automation Execution
5.  Click Create Token.
6.  You can leave **Applications** empty. Add a description and select **Read** or **Write** for the **Scope**. Note:
Make sure you provide a valid user when creating tokens. Otherwise, you get an error message that you tried to issue the command without either specifying a user, or supplying a username that does not exist.

## Create an Ansible Automation Platform connection secret for Resource Operator

To make your connection information available to the Resource Operator, create a k8s secret with the token and host value.

### About this task

### Procedure

1.  The following is an example of the YAML for the connection secret. Save the following example to a file, for example, `aap-connection-secret.yml`.

```
apiVersion: v1
kind: Secret
metadata:
name: aap-access
type: Opaque
stringData:
token: <generated-token>
host: https://aap-host.example.com/
```

2.  Edit the file with your host and token value.
3.  Apply it to your cluster by running the `kubectl create` command:


```
kubectl create -f aap-connection-secret.yml
```
