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

## Enable pods to reference images from other secured registries

If a container group uses a container from a secured registry that requires a credential, you can associate a Container Registry credential with the Execution Environment that is assigned to the job template.

### About this task

Automation controller uses this to create an `ImagePullSecret` for you in the OpenShift Container Platform namespace where the container group job runs, and cleans it up after the job is done.

Alternatively, if the `ImagePullSecret` already exists in the container group namespace, you can specify the `ImagePullSecret` in the custom pod specification for the `ContainerGroup`.

Note that the image used by a job running in a container group is always overridden by the Execution Environment associated with the job.

**Use of pre-created ImagePullSecrets (Advanced)** If you want to use this workflow and pre-create the `ImagePullSecret`, you can source the necessary information to create it from your local `.dockercfg` file on a system that has previously accessed a secure container registry.

The `.dockercfg file`, or `$HOME/.docker/config.json` for newer Docker clients, is a Docker credentials file that stores your information if you have previously logged into a secured or insecure registry.

### Procedure

1.  If you already have a `.dockercfg` file for the secured registry, you can create a secret from that file by running the following command:


```
$ oc create secret generic <pull_secret_name> \
--from-file=.dockercfg=<path/to/.dockercfg> \
--type=kubernetes.io/dockercfg
```

2.  Or if you have a `$HOME/.docker/config.json` file:


```
$ oc create secret generic <pull_secret_name> \
--from-file=.dockerconfigjson=<path/to/.docker/config.json> \
--type=kubernetes.io/dockerconfigjson
```

3.  If you do not already have a Docker credentials file for the secured registry, you can create a secret by running the following command:


```
$ oc create secret docker-registry <pull_secret_name> \
--docker-server=<registry_server> \
--docker-username=<user_name> \
--docker-password=<password> \
--docker-email=<email>
```

4.  To use a secret for pulling images for pods, you must add the secret to your service account. The name of the service account in this example must match the name of the service account the pod uses. The default is the default service account.

```
$ oc secrets link default <pull_secret_name> --for=pull
```

5.  Optional: To use a secret for pushing and pulling build images, the secret must be mountable inside a pod. You can do this by running:


```
$ oc secrets link builder <pull_secret_name>
```

6.  Optional: For builds, you must also reference the secret as the pull secret from within your build configuration.

### Results

When the container group is successfully created, the **Details** tab of the newly created container group remains. This allows you to review and edit your container group information. This is the same menu that is opened if you click the Edit icon **✎** from the **Instance Group** link. You can also edit instances and review jobs associated with this instance group.
