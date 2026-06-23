# Control where automation runs with container groups
## Customize the pod specification

Ansible Automation Platform provides a simple default pod specification, however, you can provide a custom YAML or JSON document that overrides the default pod specification.

### About this task

This field uses any custom fields such as `ImagePullSecrets`, that can be "serialized" as valid pod JSON or YAML. A full list of options can be found in the [Pods and Services](https://docs.openshift.com/online/pro/architecture/core_concepts/pods_and_services.html) section of the OpenShift documentation.

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Instance Groups.
2.  Click Create group and select **Create container group**.
3.  Check the option for **Customize pod spec**.
4.  Enter a custom Kubernetes or OpenShift Pod specification in the **Pod spec override** field.
![Customize pod specification](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ag-instance-group-customize-cg-pod.png)
5.  Click Create container group.  Note:
The image when a job launches is determined by which execution environment is associated with the job. If you associate a container registry credential with the execution environment, then automation controller attempts to make an `ImagePullSecret` to pull the image. If you prefer not to give the service account permission to manage secrets, you must pre-create the `ImagePullSecret` and specify it on the pod specification, and omit any credential from the execution environment used.

For more information, see the [Allowing Pods to Reference Images from Other Secured Registries](https://access.redhat.com/RegistryAuthentication#allowing-pods-to-reference-images-from-other-secured-registries-8) section of the *Red Hat Container Registry Authentication* article.

6.  When you have created the container group successfully, the **Details** tab of the newly created container group remains, which enables you to review and edit your container group information. This is the same menu that is opened if you click the ![Edit](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/leftpencil.png) icon from the **Instance Groups** list view. You can also edit **Instances** and review **Jobs** associated with this instance group.


![Instance group successfully created](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ag-instance-group-successfully-created.png)
Container groups and instance groups are labeled accordingly.

