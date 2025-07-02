# 1. Pod specification modifications
## 1.2. Customizing the pod specification




You can use the following procedure to customize the pod.

**Procedure**

1. In the automation controller UI, go toAutomation Execution→Infrastructure→Instance Groups.
1. CheckCustomize pod specification.
1. In the **Pod Spec Override** field, specify the namespace by using the toggle to enable and expand the **Pod Spec Override** field.
1. ClickSave.
1. Optional: ClickExpandto view the entire customization window if you want to provide additional customizations.


The image used at job launch time is determined by the execution environment associated with the job. If a Container Registry credential is associated with the execution environment, then automation controller uses `ImagePullSecret` to pull the image. If you prefer not to give the service account permission to manage secrets, you must pre-create the `ImagePullSecret` , specify it on the pod specification, and omit any credential from the execution environment used.

