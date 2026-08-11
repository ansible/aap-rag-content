# Disable the automation intelligent assistant on an operator-based deployment
## Before you begin

- You have administrator access to the OpenShift Container Platform cluster.
- The Ansible Automation Platform operator is installed and the automation intelligent assistant is deployed.

## Procedure

1.  Log in to OpenShift Container Platform as a platform administrator.
2.  Navigate to Operators> (and then)Installed Operators.
3.  From the list of installed operators, select the Ansible Automation Platform operator.
4.  Locate and select the Ansible Automation Platform custom resource, and then click the required app.
5.  Select the YAML tab.
6.  In the `spec` section, locate the `lightspeed` subsection and set `disabled` to `true`:


```
spec:
lightspeed:
disabled: true
```

7.  Click **Save**.
8.  Wait for the operator to reconcile. This prevents the Lightspeed custom resource from being recreated after deletion.
9.  Navigate to Operators> (and then)Ansible Automation Platform operator> (and then)AnsibleLightspeedand delete the AnsibleLightspeed custom resource named lightspeed.
Alternatively, delete the custom resource from the command line:

```
oc delete ansiblelightspeed lightspeed -n <namespace>
```

10.  Wait for the Lightspeed pods to terminate. This process can take several minutes.

