# 3. Configuring Red Hat Ansible Automation Platform components on Red Hat Ansible Automation Platform Operator
## 3.2. Configuring automation controller on Red Hat OpenShift Container Platform web console
### 3.2.1. Prerequisites




- You have installed the Red Hat Ansible Automation Platform catalog in Operator Hub.
- For automation controller, a default StorageClass must be configured on the cluster for the operator to dynamically create needed PVCs. This is not necessary if an external PostgreSQL database is configured.
- For Hub a StorageClass that supports ReadWriteMany must be available on the cluster to dynamically created the PVC needed for the content, redis and api pods. If it is not the default StorageClass on the cluster, you can specify it when creating your AutomationHub object.


#### 3.2.1.1. Configuring your controller image pull policy




Use this procedure to configure the image pull policy on your automation controller.

**Procedure**

1. Log in to Red Hat OpenShift Container Platform.
1. Go toOperators→Installed Operators.
1. Select your Ansible Automation Platform Operator deployment.
1. Select the **Automation Controller** tab.
1. For new instances, clickCreate AutomationController.


1. For existing instances, you can edit the YAML view by clicking the ⋮ icon and thenEdit AutomationController.

1. Clickadvanced Configuration. Under **Image Pull Policy** , click on the radio button to select


-  **Always**
-  **Never**
-  **IfNotPresent**

1. To display the option under **Image Pull Secrets** , click the arrow.


1. Click+beside **Add Image Pull Secret** and enter a value.

1. To display fields under the **Web container resource requirements** drop-down list, click the arrow.


1. Under **Limits** , and **Requests** , enter values for **CPU cores** , **Memory** , and **Storage** .

1. To display fields under the **Task container resource requirements** drop-down list, click the arrow.


1. Under **Limits** , and **Requests** , enter values for **CPU cores** , **Memory** , and **Storage** .

1. To display fields under the **EE Control Plane container resource requirements** drop-down list, click the arrow.


1. Under **Limits** , and **Requests** , enter values for **CPU cores** , **Memory** , and **Storage** .

1. To display fields under the **PostgreSQL init container resource requirements (when using a managed service)** drop-down list, click the arrow.


1. Under **Limits** , and **Requests** , enter values for **CPU cores** , **Memory** , and **Storage** .

1. To display fields under the **Redis container resource requirements** drop-down list, click the arrow.


1. Under **Limits** , and **Requests** , enter values for **CPU cores** , **Memory** , and **Storage** .

1. To display fields under the **PostgreSQL container resource requirements (when using a managed instance)** * drop-down list, click the arrow.


1. Under **Limits** , and **Requests** , enter values for **CPU cores** , **Memory** , and **Storage** .

1. To display the **PostgreSQL container storage requirements (when using a managed instance)** drop-down list, click the arrow.


1. Under **Limits** , and **Requests** , enter values for **CPU cores** , **Memory** , and **Storage** .

1. Under Replicas, enter the number of instance replicas.
1. Under **Remove used secrets on instance removal** , select **true** or **false** . The default is false.
1. Under **Preload instance with data upon creation** , select **true** or **false** . The default is true.


#### 3.2.1.2. Configuring your controller LDAP security




You can configure your LDAP SSL configuration for automation controller through any of the following options:

- The automation controller user interface.
- The platform gateway user interface. See the [Configuring LDAP authentication](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#controller-set-up-LDAP) section of the _Access management and authentication_ guide for additional steps.
- The following procedure steps.


**Procedure**

1. Create a secret in your Ansible Automation Platform namespace for the `    bundle-ca.crt` file (the filename must be `    bundle-ca.crt` ):


```
$ oc create secret -n aap-namespace generic bundle-ca-secret --from-file=bundle-ca.crt
```


1. Add the `    bundle_cacert_secret` to the Ansible Automation Platform customer resource:


```
...    spec:      bundle_cacert_secret: bundle-ca-secret    ...
```

**Verification**

You can verify the expected certificate by running:



```
oc exec -it deployment.apps/aap-gateway - openssl x509 -in /etc/pki/tls/certs/bundle-ca.crt -noout -text
```




#### 3.2.1.3. Configuring your automation controller operator route options




The Red Hat Ansible Automation Platform operator installation form allows you to further configure your automation controller operator route options under **Advanced configuration** .

**Procedure**

1. Log in to Red Hat OpenShift Container Platform.
1. Navigate toOperators→Installed Operators.
1. Select your Ansible Automation Platform Operator deployment.
1. Select the **Automation Controller** tab.
1. For new instances, clickCreate AutomationController.


1. For existing instances, you can edit the YAML view by clicking the ⋮ icon and thenEdit AutomationController.

1. ClickAdvanced configuration.
1. Under **Ingress type** , click the drop-down menu and select **Route** .
1. Under **Route DNS host** , enter a common host name that the route answers to.
1. Under **Route TLS termination mechanism** , click the drop-down menu and select **Edge** or **Passthrough** . For most instances **Edge** should be selected.
1. Under **Route TLS credential secret** , click the drop-down menu and select a secret from the list.
1. Under **Enable persistence for _/var/lib/projects_ directory** select either true or false by moving the slider.


#### 3.2.1.4. Configuring the ingress type for your automation controller operator




The Ansible Automation Platform Operator installation form allows you to further configure your automation controller operator ingress under **Advanced configuration** .

**Procedure**

1. Log in to Red Hat OpenShift Container Platform.
1. Navigate toOperators→Installed Operators.
1. Select your Ansible Automation Platform Operator deployment.
1. Select the **Automation Controller** tab.
1. For new instances, clickCreate AutomationController.


1. For existing instances, you can edit the YAML view by clicking the ⋮ icon and thenEdit AutomationController.

1. ClickAdvanced configuration.
1. Under **Ingress type** , click the drop-down menu and select **Ingress** .
1. Under **Ingress annotations** , enter any annotations to add to the ingress.
1. Under **Ingress TLS secret** , click the drop-down menu and select a secret from the list.


After you have configured your automation controller operator, clickCreateat the bottom of the form view. Red Hat OpenShift Container Platform creates the pods. This may take a few minutes.

You can view the progress by navigating toWorkloads→Podsand locating the newly created instance.

**Verification**

Verify that the following operator pods provided by the Ansible Automation Platform Operator installation from automation controller are running:


| Operator manager controllers | Automation controller | Automation hub | Event-Driven Ansible (EDA) |
| --- | --- | --- | --- |
| The operator manager controllers for each of the three operators, include the following:

- automation-controller-operator-controller-manager
- automation-hub-operator-controller-manager
- resource-operator-controller-manager
- aap-gateway-operator-controller-manager
- ansible-lightspeed-operator-controller-manager
- eda-server-operator-controller-manager | After deploying automation controller, you can see the addition of the following pods:

- controller
- controller-postgres
- controller-web
- controller-task | After deploying automation hub, you can see the addition of the following pods:

- hub-api
- hub-content
- hub-postgres
- hub-redis
- hub-worker | After deploying EDA, you can see the addition of the following pods:

- eda-activation-worker
- da-api
- eda-default-worker
- eda-event-stream
- eda-scheduler |


Note
A missing pod can indicate the need for a pull secret. Pull secrets are required for protected or private image registries. See [Using image pull secrets](https://docs.openshift.com/container-platform/4.11/openshift_images/managing_images/using-image-pull-secrets.html) for more information. You can diagnose this issue further by running `oc describe pod &lt;pod-name&gt;` to see if there is an ImagePullBackOff error on that pod.



