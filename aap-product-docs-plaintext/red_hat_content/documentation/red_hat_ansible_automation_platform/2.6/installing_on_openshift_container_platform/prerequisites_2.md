# 5. Configuring Red Hat Ansible Automation Platform components on Red Hat Ansible Automation Platform Operator
## 5.3. Configuring automation hub on Red Hat OpenShift Container Platform web console
### 5.3.1. Prerequisites




- You have installed the Ansible Automation Platform Operator in Operator Hub.


#### 5.3.1.1. Storage options for Ansible Automation Platform Operator installation on Red Hat OpenShift Container Platform




Automation hub requires `ReadWriteMany` file-based storage, Azure Blob storage, or Amazon S3 storage for operation so that multiple pods can access shared content, such as collections.

The process for configuring object storage on the `AutomationHub` CR is similar for Amazon S3 and Azure Blob Storage.

If you are using file-based storage and your installation scenario includes automation hub, ensure that the storage option for Ansible Automation Platform Operator is set to `ReadWriteMany` . `ReadWriteMany` is the default storage option.

In addition, OpenShift Data Foundation provides a `ReadWriteMany` or S3 implementation. Also, you can set up NFS storage configuration to support `ReadWriteMany` . This, however, introduces the NFS server as a potential, single point of failure.

**Additional resources**

-  [Persistent storage using NFS](https://docs.openshift.com/container-platform/4.15/storage/persistent_storage/persistent-storage-nfs.html)
-  [How do I create a storage class for NFS dynamic storage provisioning in an OpenShift environment?](https://www.ibm.com/support/pages/how-do-i-create-storage-class-nfs-dynamic-storage-provisioning-openshift-environment)


##### 5.3.1.1.1. Provisioning OCP storage with `ReadWriteMany` access mode




To ensure successful installation of Ansible Automation Platform Operator, you must provision your storage type for automation hub initially to `ReadWriteMany` access mode.

**Procedure**

1. Go toStorage→PersistentVolume.
1. ClickCreate PersistentVolume.
1. In the first step, update the `    accessModes` from the default `    ReadWriteOnce` to `    ReadWriteMany` .


1. See [Provisioning](https://docs.redhat.com/en/documentation/openshift_container_platform/4.10/html-single/storage/index#persistent-storage-nfs-provisioning_persistent-storage-nfs) to update the access mode. for a detailed overview.

1. Complete the additional steps in this section to create the persistent volume claim (PVC).


##### 5.3.1.1.2. Configuring object storage on Amazon S3




Red Hat supports Amazon Simple Storage Service (S3) for automation hub. You can configure it when deploying the `AnsibleAutomationPlatform` custom resource (CR), or you can configure it for an existing instance.

**Prerequisites**

- Create an Amazon S3 bucket to store the objects.
- Note the name of the S3 bucket.


**Procedure**

1. Create a Kubernetes secret containing the AWS credentials and connection details, and the name of your Amazon S3 bucket. The following example creates a secret called `    test-s3` :


```
$ oc -n $HUB_NAMESPACE apply -f- &lt;&lt;EOF    apiVersion: v1    kind: Secret    metadata:      name: 'test-s3'    stringData:      s3-access-key-id: $S3_ACCESS_KEY_ID      s3-secret-access-key: $S3_SECRET_ACCESS_KEY      s3-bucket-name: $S3_BUCKET_NAME      s3-region: $S3_REGION    EOF
```


1. Add the secret to the Ansible Automation Platform custom resource (CR) under the `    hub` section in the `    spec` :


```
apiVersion: aap.ansible.com/v1alpha1    kind: AnsibleAutomationPlatform    metadata:      name: myaap    spec:      hub:        storage_type: S3        object_storage_s3_secret: test-s3
```

Note
If you have an existing automation hub instance, specify its name using `    hub.name: existing-hub-name` to apply these settings to the existing instance.

For more examples of Ansible Automation Platform custom resources, see [Appendix: Red Hat Ansible Automation Platform custom resources](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/installing_on_openshift_container_platform/index#appendix-operator-crs_operator-platform-doc) .




1. If you are applying this secret to an existing instance, restart the API pods for the change to take effect. `    &lt;hub-name&gt;` is the name of your hub instance.


```
$ oc -n $HUB_NAMESPACE delete pod -l app.kubernetes.io/name=&lt;hub-name&gt;-api
```




##### 5.3.1.1.3. Configuring object storage on Azure Blob




Red Hat supports Azure Blob Storage for automation hub. You can configure it when deploying the `AnsibleAutomationPlatform` custom resource (CR), or you can configure it for an existing instance.

**Prerequisites**

- Create an Azure Storage blob container to store the objects.
- Note the name of the blob container.


**Procedure**

1. Create a Kubernetes secret containing the credentials and connection details for your Azure account, and the name of your Azure Storage blob container. The following example creates a secret called `    test-azure` :


```
$ oc -n $HUB_NAMESPACE apply -f- &lt;&lt;EOF    apiVersion: v1    kind: Secret    metadata:      name: 'test-azure'    stringData:      azure-account-name: $AZURE_ACCOUNT_NAME      azure-account-key: $AZURE_ACCOUNT_KEY      azure-container: $AZURE_CONTAINER      azure-container-path: $AZURE_CONTAINER_PATH      azure-connection-string: $AZURE_CONNECTION_STRING    EOF
```


1. Add the secret to the Ansible Automation Platform custom resource (CR) under the `    hub` section in the `    spec` :


```
apiVersion: aap.ansible.com/v1alpha1    kind: AnsibleAutomationPlatform    metadata:      name: myaap    spec:      hub:        storage_type: azure        object_storage_azure_secret: test-azure
```

Note
If you have an existing automation hub instance, specify its name using `    hub.name: existing-hub-name` to apply these settings to the existing instance.

For more examples of Ansible Automation Platform custom resources, see [Appendix: Red Hat Ansible Automation Platform custom resources](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/installing_on_openshift_container_platform/index#appendix-operator-crs_operator-platform-doc) .




1. If you are applying this secret to an existing instance, restart the API pods for the change to take effect. `    &lt;hub-name&gt;` is the name of your hub instance.


```
$ oc -n $HUB_NAMESPACE delete pod -l app.kubernetes.io/name=&lt;hub-name&gt;-api
```




#### 5.3.1.2. Configure your automation hub operator route options




The Red Hat Ansible Automation Platform operator installation form allows you to further configure your automation hub operator route options under **Advanced configuration** .

**Procedure**

1. Log in to Red Hat OpenShift Container Platform.
1. Navigate toOperators→Installed Operators.
1. Select your Ansible Automation Platform Operator deployment.
1. Select the **Ansible Automation Platform** tab.
1. Click the ⋮ icon next to your Ansible Automation Platform instance and selectEdit AnsibleAutomationPlatform.
1. ClickYAML viewand locate the `    spec.hub:` section.
1. Configure the route options under the `    hub:` section:


```
spec:      hub:        ingress_type: Route        route_host: hub.example.com  # Custom hostname for the route        route_tls_termination_mechanism: Edge  # Options: Edge, Passthrough        route_tls_secret: hub-tls-secret  # Optional: TLS credential secret
```


1. ClickSave.

Note
Edge termination is recommended for most instances. After configuring your route, you can customize additional route settings by adding them to the `    hub:` section in the Ansible Automation Platform custom resource.

For more examples of Ansible Automation Platform custom resources, see [Appendix: Red Hat Ansible Automation Platform custom resources](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/installing_on_openshift_container_platform/index#appendix-operator-crs_operator-platform-doc) .






#### 5.3.1.3. Configuring the ingress type for your automation hub operator




The Ansible Automation Platform Operator installation form allows you to further configure your automation hub operator ingress under **Advanced configuration** .

**Procedure**

1. Log in to Red Hat OpenShift Container Platform.
1. Navigate toOperators→Installed Operators.
1. Select your Ansible Automation Platform Operator deployment.
1. Select the **Ansible Automation Platform** tab.
1. Click the ⋮ icon next to your Ansible Automation Platform instance and selectEdit AnsibleAutomationPlatform.
1. ClickYAML viewand locate the `    spec.hub:` section.
1. Configure the ingress options under the `    hub:` section:


```
spec:      hub:        ingress_type: Ingress        ingress_annotations: |          nginx.ingress.kubernetes.io/proxy-body-size: "0"          nginx.ingress.kubernetes.io/proxy-connect-timeout: "600"        ingress_tls_secret: hub-ingress-tls-secret
```


1. ClickSave.

Note
These ingress settings apply to the automation hub component managed by this Ansible Automation Platform instance. The operator automatically updates the ingress configuration for the hub.

For more examples of Ansible Automation Platform custom resources, see [Appendix: Red Hat Ansible Automation Platform custom resources](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/installing_on_openshift_container_platform/index#appendix-operator-crs_operator-platform-doc) .






**Verification**

After you have configured your automation hub ingress settings, Red Hat OpenShift Container Platform updates the pods. This may take a few minutes.


You can view the progress by navigating toWorkloads→Podsand locating the newly created instance.

Verify that the following operator pods provided by the Ansible Automation Platform Operator installation from automation hub are running:

| Operator manager controllers | Automation controller | Automation hub |
| --- | --- | --- |
| The operator manager controllers for each of the 3 operators, include the following:

- automation-controller-operator-controller-manager
- automation-hub-operator-controller-manager
- resource-operator-controller-manager | After deploying automation controller, you will see the addition of these pods:

- controller
- controller-postgres | After deploying automation hub, you will see the addition of these pods:

- hub-api
- hub-content
- hub-postgres
- hub-redis
- hub-worker |


Note
A missing pod can indicate the need for a pull secret. Pull secrets are required for protected or private image registries. See [Using image pull secrets](https://docs.openshift.com/container-platform/4.11/openshift_images/managing_images/using-image-pull-secrets.html) for more information. You can diagnose this issue further by running `oc describe pod &lt;pod-name&gt;` to see if there is an ImagePullBackOff error on that pod.



