# 3. Configuring Red Hat Ansible Automation Platform components on Red Hat Ansible Automation Platform Operator
## 3.3. Configuring automation hub on Red Hat OpenShift Container Platform web console
### 3.3.2. Finding the automation hub route




You can access the automation hub through the platform gateway or through the following procedure.

**Procedure**

1. Log into Red Hat OpenShift Container Platform.
1. Navigate toNetworking→Routes.
1. Under **Location** , click on the URL for your automation hub instance.


The automation hub user interface launches where you can sign in with the administrator credentials specified during the operator configuration process.

Note
If you did not specify an administrator password during configuration, one was automatically created for you. To locate this password, go to your project, selectWorkloads→Secretsand open controller-admin-password. From there you can copy the password and paste it into the Automation hub password field.



