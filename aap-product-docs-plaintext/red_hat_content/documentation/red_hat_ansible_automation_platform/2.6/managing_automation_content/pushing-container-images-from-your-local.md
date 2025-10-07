# 3. Manage containers in private automation hub
## 3.6. Working with signed containers
### 3.6.4. Pushing container images from your local environment




Use the following procedure to sign an automation execution environment on a local system and push the signed execution environment to the automation hub registry.

**Procedure**

1. From a terminal, log in to Podman, or any container client currently in use:


```
&gt; podman pull &lt;container-name&gt;
```


1. After the execution environment is pulled, add tags (for example: latest, rc, beta, or version numbers, such as 1.0; 2.3, and so on):


```
&gt; podman tag &lt;container-name&gt; &lt;server-address&gt;/&lt;container-name&gt;:&lt;tag name&gt;
```


1. Sign the execution environment after changes have been made, and push it back up to the automation hub registry:


```
&gt; podman push &lt;server-address&gt;/&lt;container-name&gt;:&lt;tag name&gt; --tls-verify=false --sign-by &lt;reference to the gpg key on your local&gt;
```

If the execution environment is not signed, it can only be pushed with any current signature embedded. Alternatively, you can use the following script to push the execution environment without signing it:


```
&gt; podman push &lt;server-address&gt;/&lt;container-name&gt;:&lt;tag name&gt; --tls-verify=false
```


1. Once the execution environment has been pushed, navigate toAutomation Content→Execution Environments.
1. To display the new execution environment, click the **Refresh** icon.
1. Click the name of the image to view your pushed image.


**Troubleshooting**

The details page for each execution environment indicates whether it has been signed. If the details page indicates that an image is **Unsigned** , you can sign the execution environment from automation hub using the following steps:


1. Click the execution environment name to navigate to the details page.
1. Click theMore Actionsicon **⋮** . Three options are available:


-  **Sign execution environment**
-  **Use in Controller**
-  **Delete execution environment**

1. Click **Sign execution environment** from the drop-down menu.


**Verification**

The signing service signs the execution environment. After the execution environment is signed, the status changes to "signed".


