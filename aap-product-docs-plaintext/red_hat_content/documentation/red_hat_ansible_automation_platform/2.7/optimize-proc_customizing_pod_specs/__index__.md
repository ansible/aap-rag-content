# Customize pod specifications to improve performance

You can use the following procedure to customize the pod.

## Procedure

1.  In the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Instance Groups.
2.  Check Customize pod specification.
3.  In the **Pod Spec Override** field, specify the namespace by using the toggle to enable and expand the **Pod Spec Override** field.
4.  Click Save.
5.  Optional: Click Expand to view the entire customization window if you want to provide additional customizations.

## What to do next

The image used at job launch time is determined by the execution environment associated with the job. If a Container Registry credential is associated with the execution environment, then automation controller uses `ImagePullSecret` to pull the image. If you prefer not to give the service account permission to manage secrets, you must pre-create the `ImagePullSecret`, specify it on the pod specification, and omit any credential from the execution environment used.

