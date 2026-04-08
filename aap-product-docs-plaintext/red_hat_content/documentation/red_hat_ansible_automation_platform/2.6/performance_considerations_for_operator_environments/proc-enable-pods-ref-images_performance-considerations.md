# 1. Pod specification modifications
## 1.3. Enabling pods to reference images from other secured registries




If a container group uses a container from a secured registry that requires a credential, you can associate a Container Registry credential with the Execution Environment that is assigned to the job template.

Automation controller uses this to create an `ImagePullSecret` for you in the OpenShift Container Platform namespace where the container group job runs, and cleans it up after the job is done.

Alternatively, if the `ImagePullSecret` already exists in the container group namespace, you can specify the `ImagePullSecret` in the custom pod specification for the `ContainerGroup` .

Note that the image used by a job running in a container group is always overridden by the Execution Environment associated with the job.

**Use of pre-created ImagePullSecrets (Advanced)** If you want to use this workflow and pre-create the `ImagePullSecret` , you can source the necessary information to create it from your local `.dockercfg` file on a system that has previously accessed a secure container registry.

The `.dockercfg file` , or `$HOME/.docker/config.json` for newer Docker clients, is a Docker credentials file that stores your information if you have previously logged into a secured or insecure registry.

**Procedure**

1. If you already have a `    .dockercfg` file for the secured registry, you can create a secret from that file by running the following command:


```
$ oc create secret generic &lt;pull_secret_name&gt; \    --from-file=.dockercfg=&lt;path/to/.dockercfg&gt; \    --type=kubernetes.io/dockercfg
```


1. Or if you have a `    $HOME/.docker/config.json` file:


```
$ oc create secret generic &lt;pull_secret_name&gt; \    --from-file=.dockerconfigjson=&lt;path/to/.docker/config.json&gt; \    --type=kubernetes.io/dockerconfigjson
```


1. If you do not already have a Docker credentials file for the secured registry, you can create a secret by running the following command:


```
$ oc create secret docker-registry &lt;pull_secret_name&gt; \    --docker-server=&lt;registry_server&gt; \    --docker-username=&lt;user_name&gt; \    --docker-password=&lt;password&gt; \    --docker-email=&lt;email&gt;
```


1. To use a secret for pulling images for pods, you must add the secret to your service account. The name of the service account in this example must match the name of the service account the pod uses. The default is the default service account.


```
$ oc secrets link default &lt;pull_secret_name&gt; --for=pull
```


1. Optional: To use a secret for pushing and pulling build images, the secret must be mountable inside a pod. You can do this by running:


```
$ oc secrets link builder &lt;pull_secret_name&gt;
```


1. Optional: For builds, you must also reference the secret as the pull secret from within your build configuration.


**Verification**

When the container group is successfully created, the **Details** tab of the newly created container group remains. This allows you to review and edit your container group information. This is the same menu that is opened if you click theEditicon **✎** from the **Instance Group** link. You can also edit instances and review jobs associated with this instance group.


