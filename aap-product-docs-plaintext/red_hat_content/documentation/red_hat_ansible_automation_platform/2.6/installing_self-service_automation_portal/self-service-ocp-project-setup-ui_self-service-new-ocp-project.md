# 3. Pre-installation configuration
## 3.6. Setting up a project for self-service automation portal in OpenShift Container Platform
### 3.6.1. Setting up a project in the OpenShift Container Platform web console




You can use the OpenShift Container Platform web console to create a project in your cluster.

**Procedure**

1. In a browser, log in to the OpenShift Container Platform web console.
1. Creating a project varies slightly depending on which perspective you have on:


1. From the **Developer** perspective: select **Project** then **Create Project** .
1. From the **Administrator** perspective: select **Home** then **Project** then **Create Project** .

1. In the **Create Project** dialog box, enter a unique name **Name** field.


- Lowercase alphanumeric characters ( `        a-z` , `        0-9` ) and the hyphen character ( `        -` ) are permitted for project names.
- The underscore ( `        _` ) character is not permitted.
- The maximum length for project names is 63 characters.


1. Optional: display name and description for your project.


1. ClickClickto create the project.


### 3.6.2. Setting up an OpenShift Container Platform project using `oc`




You can run commands from your terminal to add a project to your cluster.

**Prerequisites**

- You have the login details for your Openshift cluster.
- You have installed the `    oc` CLI tool.


**Procedure**

1. In a terminal, log in to OpenShift Container Platform using your credentials:


```
oc login &lt;OpenShift_API_URL&gt; -u &lt;username&gt;
```

The following example shows the output for a successful login:


```
$ oc login https://api.&lt;my_cluster&gt;.com:6443 -u kubeadmin    WARNING: Using insecure TLS client config. Setting this option is not supported!        Console URL: https://api.&lt;my_cluster&gt;.com:6443/console    Authentication required for https://api.&lt;my_cluster&gt;.com:6443 (openshift)    Username: kubeadmin    Password:    Login successful.        You have access to 22 projects, the list has been suppressed. You can list all projects with 'oc projects'        Using project "default".
```


1. Create a new project. Use a unique project name.


```
$ oc new-project &lt;self-service-project-name&gt;
```


- Lowercase alphanumeric characters ( `        a-z` , `        0-9` ) and the hyphen character ( `        -` ) are permitted for project names.
- The underscore ( `        _` ) character is not permitted.
- The maximum length for project names is 63 characters.

Example:


```
$ oc new-project &lt;my-project&gt;                Now using project "my-project" on server "https://openshift.example.com:6443".
```



1. Open your new project:


```
$ oc project &lt;self-service-project-name&gt;
```




## 3.7. Creating a plug-in registry in OpenShift




You must create a registry in OpenShift Container Platform for the `.tar` files for self-service automation portal.

### 3.7.1. Downloading the plug-in TAR files




Download the latest `.tar.gz` plug-in files for self-service automation portal from the Red Hat Customer Portal.

**Procedure**

1. Create a directory on your local machine to store the files.


```
$ mkdir /path/to/&lt;automation-portal-plugins&gt;
```


1. Set an environment variable ( `    $DYNAMIC_PLUGIN_ROOT_DIR` ) to represent the directory path.


```
$ export DYNAMIC_PLUGIN_ROOT_DIR=/path/to/&lt;automation-portal-plugins&gt;
```


1. Download the setup bundle. In a browser, navigate to the [Red Hat Ansible Automation Platform Product Software downloads page](https://access.redhat.com/downloads/content/480/ver=2.6/rhel---9/2.6/x86_64/product-software) . and select the **Product Software** tab.
1. Click **Download now** next to **Ansible self-service automation portal Setup Bundle** to download the latest version of the plug-ins.

The format of the filename is `    self-service-automation-portal-plugins-x.y.z.tar.gz` .

Substitute the Ansible plug-ins release version, for example `    2.0.0` , for `    x.y.z` .


1. Extract the `    self-service-automation-portal-plugins-&lt;version-number&gt;.tar.gz` contents to `    $DYNAMIC_PLUGIN_ROOT_DIR` .


```
$ tar --exclude='*code*' -xzf self-service-automation-portal-plugins-x.y.z.tar.gz -C $DYNAMIC_PLUGIN_ROOT_DIR
```

Substitute the Ansible plug-ins release version, for example `    2.0.0` , for `    x.y.z` .




**Verification**

Run `ls` to verify that the extracted files are in the `$DYNAMIC_PLUGIN_ROOT_DIR` directory:


```
$ ls $DYNAMIC_PLUGIN_ROOT_DIR
ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz
ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz.integrity
ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz
ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz.integrity
```

The files with the `.integrity` file type contain the plugin SHA value.

### 3.7.2. Setting up the plugin registry image




Set up a registry in your OpenShift cluster to host the plug-ins and make them available for installation.

**Procedure**

1. Log in to your OpenShift Container Platform instance with credentials to create a new application.
1. Open your OpenShift project for self-service automation portal.


```
$ oc project &lt;AAP-self-service-project-name&gt;
```


1. Run the following commands to create a plugin registry build in in your OpenShift project.


```
$ oc new-build httpd --name=plugin-registry --binary    $ oc start-build plugin-registry --from-dir=$DYNAMIC_PLUGIN_ROOT_DIR --wait    $ oc new-app --image-stream=plugin-registry
```




### 3.7.3. Verifying the plug-in registry deployment




You can verify that the plugin-registry deployed correctly in the OpenShift Container Platform web console, or you can use a CLI command.

**Procedure**

1. To verify the deployment using a CLI command:


1. Run the following command from a terminal to verify that the plugin-registry deployed correctly:


```
$ oc exec $(oc get pods -l deployment=plugin-registry -o jsonpath='{.items[0].metadata.name}') -- ls -l /opt/app-root/src
```


1. Confirm that the following required TAR files are in the plugin registry:


```
ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz        ansible-backstage-plugin-auth-backend-module-rhaap-provider-dynamic-x.y.z.tgz        ansible-backstage-plugin-catalog-backend-module-rhaap-dynamic-x.y.z.tgz        ansible-plugin-backstage-self-service-dynamic-x.y.z.tgz
```



1. To confirm that the plugin-registry deployed correctly from the OpenShift Container Platform web console:


1. Open the **Topology** view in the **Developer** perspective for your project in the OpenShift web console.
1. Select the plugin registry icon to open the **plugin-registry** details pane.
1. In the **Pods** section of the **plugin-registry** details pane, click **View logs** for the `        plugin-registry-#########-####` pod.

![Developer perspective](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Installing_self-service_automation_portal-en-US/images/b1594982a3b39036d9063bb57acc195e/self-service-plugin-registry.png)


(1) Plug-in registry


1. Click the **terminal** tab and log in to the container.
1. In the terminal, run `        ls` to confirm that the TAR files are in the plugin registry.


```
ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz        ansible-backstage-plugin-auth-backend-module-rhaap-provider-dynamic-x.y.z.tgz        ansible-backstage-plugin-catalog-backend-module-rhaap-dynamic-x.y.z.tgz        ansible-plugin-backstage-self-service-dynamic-x.y.z.tgz
```

The version numbers and file names can differ.





## 3.8. Creating secrets in OpenShift for your environment variables




Before installing the Helm chart, you must create a set of secrets in your OpenShift project. The self-service automation portal Helm chart fetches environment variables from OpenShift secrets.

### 3.8.1. Creating Ansible Automation Platform authentication secrets




You must create a secret in OpenShift Container Platform for Ansible Automation Platform authentication.

**Procedure**

1. Log in to your OpenShift Container Platform instance.
1. Open your OpenShift project for self-service automation portal in the **Administrator** view.
1. Click **Secrets** in the side pane.
1. Click **Create** to open the form for creating a new secret.
1. Select the **Key/Value** option.
1. Create a secret named `    secrets-rhaap-portal` .

Note
The secret must use this exact name.




1. Add the following key-value pairs to the secret.

Note
The secrets must use the exact key names specified below.




- Key: `        aap-host-url`

Value needed: Ansible Automation Platform instance URL


- Key: `        oauth-client-id`

Value needed: Ansible Automation Platform OAuth client ID


- Key: `        oauth-client-secret`

Value needed: Ansible Automation Platform OAuth client secret value


- Key: `        aap-token`

Value needed: Token for Ansible Automation Platform user authentication (must have `        read` access).



1. ClickCreateto create the secret.


### 3.8.2. Creating GitHub and Gitlab secrets




Create an OpenShift secret to hold Personal Access Tokens for your external Source Control Management systems, such as GitHub or GitLab. This helps securely manage access credentials.

This procedure establishes the required `secrets-scm` Key/Value secret within your OpenShift Container Platform project to securely store the GitHub and/or GitLab Personal Access Tokens (PATs).

**Procedure**

1. Log in to your OpenShift Container Platform instance.
1. Open your OpenShift project for self-service automation portal.
1. Click **Secrets** in the side pane.
1. Click **Create** to open the form for creating a new secret.
1. Select the **Key/Value** option.
1. Create a secret named `    secrets-scm` .

Note
The secret must use this exact name.




1. Add the following key-value pairs to the secret. If you are only using one SCM, just add the key-value pair for that SCM.

Note
The secrets must use the exact key names specified below.




- Key: `        github-token`

Value needed: Github Personal Access Token (PAT)


- Key: `        gitlab-token`

Value needed: Gitlab Personal Access Token (PAT)



1. Click **Create** to create the secret.


# Chapter 4. Installing the self-service automation portal Helm chart




You can use the configured secrets and plugin registry to install the self-service automation portal. Deploy the application onto your OpenShift cluster using the provided Helm chart.

## 4.1. Configuring the self-service automation portal Helm chart from the OpenShift catalog




Deploy the Helm chart from the OpenShift catalog by configuring the base URL and organization name in the YAML view. This launches the self-service automation portal installation.

**Prerequisites**

- You have created a project for self-service automation portal in OpenShift Container Platform.
- You have created a plugin registry in your project.
- You have set up secrets for Ansible Automation Platform authentication and SCM authentication.


**Procedure**

1. In a browser, navigate to your OpenShift project for self-service automation portal that you created earlier.
1. Select the **Developer** view.
1. Click the **Helm** option in the OpenShift sidebar.
1. In the **Helm** page, clickCreateand select **Helm Release** .
1. Search for `    Portal` in the Helm Charts filter, and select the `    Automation Portal` chart.
1. In the modal dialog on the chart page, clickCreate.
1. Select the **YAML view** in the **Create Helm Release** page.
1. Locate the `    clusterRouterBase` key in the YAML file and replace the placeholder value with the base URL of your OpenShift instance.

The base URL is the URL portion of your OpenShift URL that follows `    https://console-openshift-console` , for example `    apps.example.com` :


```
redhat-developer-hub        global:          clusterRouterBase: apps.example.com
```


1. The Helm chart is set up for the Default Ansible Automation Platform organization.

To update the Helm chart to use a different organization, update the value for the `    catalog.providers.rhaap.orgs` key from `    Default` to your Ansible Automation Platform organization name.


```
catalog:        providers:          rhaap:            production:            # Replace 'Default' with the name of the organization you created              orgs: '&lt;your-org-name&gt;'
```


1. ClickCreateto launch the deployment.


## 4.2. Verifying the installation




Verify the Helm chart installation from the OpenShift Container Platform web console.

**Procedure**

1. In a browser, log in to your OpenShift instance.
1. In the **Developer** view, navigate to the **Topology** view for the namespace where you deployed the Helm chart.

The deployment appears: the label on the icon is `    D` . The name of the deployment is `    &lt;installation-name&gt;-backstage` , for example `    &lt;my-self-service-automation-portal-backstage&gt;` .

While it is deploying, the icon is light blue. The color changes to dark blue when deployment is complete.

![Deployment on OpenShift console](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Installing_self-service_automation_portal-en-US/images/06c45647f2a2be815da7e2006fd83257/self-service-verify-helm-install.png)





# Chapter 5. Installing self-service automation portal in air-gapped OpenShift Container Platform environments




You can install self-service automation portal in a disconnected OpenShift Container Platform environment.

## 5.1. Prerequisites




Gather the required tools and access credentials necessary for air-gapped installation. This includes the OpenShift CLI, Helm, Podman, and required registry secrets.

- You have installed the OpenShift CLI ( `    oc` ). See the [Getting started with the OpenShift CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/cli_tools/openshift-cli-oc#cli-getting-started) chapter of the _Understanding OpenShift Container Platform_ guide.
- You have installed Helm 3.10 or newer. See the [Installing Helm](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/building_applications/working-with-helm-charts#installing-helm) chapter of the _OpenShift Container Platform Building applications_ guide.
- You have installed and configured Podman for pulling and pushing container images.
- You have internet access. This is required to pull images and charts from public repositories, including `    registry.redhat.io` and `    <a class="link" href="https://charts.openshift.io/">https://charts.openshift.io/</a>` .
- A Red Hat pull secret, for exmaple `    pull-secret.json` or similar credentials file that allows you to pull images from `    registry.redhat.io` .
- Sufficient disk space to store downloaded images and chart packages.
- Access to public registries: Docker Hub, `    quay.io` , `    registry.redhat.io` , and your disconnected OpenShift cluster’s internal registry.


## 5.2. Preparing for air-gapped installation




Before you can install self-service automation portal in a disconnected OpenShift Container Platform environment, you must complete some processes on a connected bastion host.

### 5.2.1. Mirroring container images




Mirror the required container images from the Red Hat registry to your local disconnected registry. This action prepares the images needed to install the self-service automation portal in an isolated environment.

**Procedure**

1. Log in to `    registry.redhat.io` :


```
$ podman login registry.redhat.io
```

Enter your Red Hat username and password when prompted.

Alternatively, you can use:


```
$ podman login --authfile &lt;path_to_pull_secret.json&gt; registry.redhat.io
```


1. Log in to your disconnected registry:


```
$ podman login &lt;disconnected_registry_url&gt;
```


1. Pull the original image from `    registry.redhat.io` :


```
$ podman pull registry.redhat.io/rhdh/rhdh-hub-rhel9:x.y.z
```


1. Tag the image for your disconnected registry:


```
$ podman tag registry.redhat.io/rhdh/rhdh-hub-rhel9:x.y.z &lt;disconnected_registry_url&gt;/&lt;your_namespace&gt;/rhdh-hub-rhel9:x.y.z
```

Example:


```
$ podman tag registry.redhat.io/rhdh/rhdh-hub-rhel9:1.1.0 my-disconnected-registry.com/myproject/rhdh-hub-rhel9:1.1.0
```


1. Push the tagged image to your disconnected registry:


```
$ podman push &lt;disconnected_registry_url&gt;/&lt;your_namespace&gt;/rhdh-hub-rhel9:x.y.z
```




### 5.2.2. Downloading the helm chart package




Download the Helm chart package and modify the internal image references to point to your disconnected registry. This prepares the installation package for the air-gapped environment.

**Procedure**

1. Add the OpenShift Helm charts repository:


```
$ helm repo add openshift-helm-charts https://charts.openshift.io/
```


1. Update your Helm repositories to fetch the latest chart information:


```
$ helm repo update
```


1. Pull the chart:


```
$ helm pull openshift-helm-charts/redhat-rhaap-portal --version x.y.z
```

This command downloads the chart as a `    .tgz` file, for example redhat-rhaap-portal-1.0.1.tgz.


1. Unpack the chart:


```
$ tar -xvf redhat-rhaap-portal-x.y.z.tgz
```

This creates a directory with a name similar to `    redhat-rhaap-portal-1.0.1/` .


1. Navigate to the unpacked chart directory (for example, `    cd redhat-rhaap-portal-1.0.1` ) and open the `    values.yaml` file in a text editor.
1. Find all the `    image:` entries in `    values.yaml` and replace the original image references with the full path to the image in your disconnected registry.

For example, replace `    image: registry.redhat.io/rhdh/rhdh-hub-rhel9:x.y.z` with `    image: &lt;disconnected_registry_url&gt;/&lt;your_namespace&gt;/rhdh-hub-rhel9:x.y.z`


1. Repack the modified chart:


```
$ helm package redhat-rhaap-portal-x.y.z
```

This creates a new `    .tgz` file with your changes (for example, `    redhat-rhaap-portal-1.0.1.tgz` ).




### 5.2.3. Transferring assets to the disconnected environment




Transfer the modified Helm chart package from the connected bastion host to a machine inside your disconnected network. This action stages the installation assets for deployment within the isolated OpenShift environment.

**Procedure**

- Copy the modified Helm chart `    .tgz` file or files (for example, `    redhat-rhaap-portal-1.0.1.tgz` ) from your connected bastion host to a machine or jump box within your disconnected OpenShift network.


## 5.3. Installing the Helm chart in the disconnected OpenShift environment




You can install the modified Helm chart using the `helm install` command in your disconnected OpenShift environment. This deploys the self-service automation portal using the locally available assets.

Continued steps for installing the Helm chart in a disconnected OpenShift environment are detailed in this section.

### 5.3.1. Accessing the disconnected OpenShift environment




Ensure your disconnected OpenShift cluster is configured to trust the private registry containing the mirrored container images. This step is crucial for successful image pulling during installation.

**Prerequisites**

- You have the necessary kubeconfig and permissions. For example `    cluster-admin` , for setting up image pull secrets or insecure registries.


**Procedure**

1. In a terminal, log in to your disconnected OpenShift cluster using the `    oc` CLI.


```
oc login --token=&lt;your_token&gt; --server=&lt;your_openshift_api_url&gt;
```

Use the following command if you have a kubeconfig:


```
export KUBECONFIG=/path/to/your/kubeconfig    oc login
```


1. Ensure that your OpenShift cluster is configured to trust your disconnected registry:


1. Use `        ImageContentSourcePolicy` for mirroring.
1. Use `        additionalTrustedCA` in `        image.config.openshift.io/cluster` for self-signed certificates.
1. Use `        insecure-registries` for plain HTTP.



### 5.3.2. Defining Parameters and Navigate to Chart Location




Navigate to the transferred Helm chart directory on your jump box. Define environment variables for the installation namespace and cluster router base URL before beginning the installation.

**Procedure**

1. On the machine within your disconnected environment, navigate to the directory where you placed the transferred Helm chart `    .tgz` file.


```
cd /path/to/your/transferred/charts/
```

Example:


```
cd /opt/disconnected-assets/charts/
```


1. If the namespace doesn’t exist, create it:


```
oc new-project ${MY_NAMESPACE}
```


1. Define your namespace and cluster router base as environment variables for easier use:


```
export MY_NAMESPACE="&lt;your_namespace_name&gt;"    export MY_CLUSTER_ROUTER_BASE="&lt;your_cluster_router_base&gt;"
```

Example:


```
export MY_NAMESPACE="rhdh-dev"    export MY_CLUSTER_ROUTER_BASE="apps.yourcluster.example.com"
```




### 5.3.3. Installing the Helm chart




Install the self-service automation portal by using the `helm install` command. You must reference the local Helm chart file and include the required cluster overrides using the `--set` flags.

**Procedure**

- Install the chart using the `    helm install` command, referencing the local `    .tgz` file by its name and using `    --set` flags to provide necessary overrides.

Add more `    --set` flags for any other values that were in your original `    values.yaml` file.


```
$ helm install redhat-rhaap-portal \      redhat-rhaap-portal-x.y.z.tgz \      --namespace ${MY_NAMESPACE} \      --set redhat-developer-hub.global.clusterRouterBase=${MY_CLUSTER_ROUTER_BASE} \      --set redhat-developer-hub.image.name=&lt;disconnected_registry_url&gt;/&lt;your_namespace&gt;/rhdh-hub-rhel9:x.y.z \
```


-  `        redhat-rhaap-portal` : the release name for your Helm deployment.
-  `        redhat-rhaap-portal-x.y.z.tgz` : the local path/filename to your modified Helm chart .tgz file.
-  `        --namespace ${MY_NAMESPACE}` : the OpenShift project (namespace) where the chart will be installed, using your defined variable.
-  `        --set redhat-developer-hub.global.clusterRouterBase=${MY_CLUSTER_ROUTER_BASE}` : the cluster router base, using your defined variable.



## 5.4. Verifying the disconnected installation




Verify the successful installation of the Helm chart in the disconnected environment. Check the Helm release status, monitor the pods, and verify that the application routes are accessible.

**Procedure**

1. Check the Helm release status:


```
$ helm list -n ${MY_NAMESPACE}
```


1. Monitor the pods in your namespace to ensure they are running:


```
$ oc get pods -n ${MY_NAMESPACE}
```


1. Check for `    ImagePullBackOff` or other errors in pod events:


```
$ oc describe pod &lt;pod_name&gt; -n ${MY_NAMESPACE}
```


1. If the chart uses routes to expose services, verify that the routes are created and accessible:


```
$ oc get route -n ${MY_NAMESPACE}
```




# Chapter 6. Inspecting the deployment on OpenShift




You can inspect the deployment logs and ConfigMap on the OpenShift console to verify that the deployment conforms with the settings in your Helm chart.

## 6.1. Viewing the deployment logs




You can view the deployment logs in the OpenShift console. Pay close attention to the install-dynamic-plugins container logs. This helps confirm that the required plug-ins installed successfully.

**Procedure**

1. In a browser, log in to your OpenShift instance.
1. In the **Developer** view, navigate to the **Topology** view for the namespace where you deployed the Helm chart.
1. The deployment appears: the label on the icon is `    D` .

The name of the deployment is `    &lt;installation-name&gt;-backstage` , for example `    &lt;my-self-service-automation-portal-backstage&gt;` .


1. Click the icon representing the deployment.
1. The **Details** pane for the deployment opens.
1. Select the **Resources** tab.
1. Click **View logs** for the deployment pod in the **Pods** section:

![Deployment on OpenShift console](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Installing_self-service_automation_portal-en-US/images/7db4d1cfa7a66893597c9306c073b561/self-service-view-deployment-logs.png)


The **Pod details** page opens for the deployment pod.


1. Select the **Logs** tab in the **Pod details** page.
1. To view the install messages, select the `    install-dynamic-plugins` container from the **INIT CONTAINERS** section of the dropdown list of containers:

![View install messages](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Installing_self-service_automation_portal-en-US/images/e9518a231caeb6d563f762c47f17d7e5/self-service-view-install-messages.png)


The log stream displays the progress of the installation of the plug-ins from the plug-in registry.

The log stream for successful installation of the plug-ins resembles the following output:


```
======= Installing dynamic plugin http://plugin-registry:8080/ansible-backstage-plugin-catalog-backend-module-rhaap-dynamic-0.1.0.tgz     *=&gt; Grabbing package archive through pm pack'     •=› Vertfying package Integrity     •*&gt; Extracting package archtve /dynamtc-plugtns-root/anstble-backstage-plugtn-catalog-backend-nodule-rhaap-dynamic-0.1.0.tgz     •*› Removing package archive /dynamic-plugins-root/ansible-backstage-plugin-catalog-backend-module-rhaap-dynamic-0.1.0. tgz     -&gt; Successfully installed dynamic plugin http://plugin-registry:8080/ansible-backstage-plugin-catalog-backend-module-rhaap-dynamic-0.1.0.tgz
```


1. Select the **Environment** tab in the **Pod details** page to view the environment variables for the containers. If you set additional environment variables in your Helm chart, check that they are listed here.

![Pod environment variables](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Installing_self-service_automation_portal-en-US/images/0a87b7e4f33737aecc0c1af2f37dc039/self-service-pod-env-variables.png)





# Chapter 7. Accessing the self-service automation portal deployment




Complete the necessary post-installation configuration, including updating the OAuth application and setting up initial Role-Based Access Control (RBAC). You can then access and sign in to the portal.

## 7.1. Adding the deployment URL to the OAuth Application




When you set up your OAuth application in Ansible Automation Platform before deploying self-service automation portal, you added placeholder text for the `Redirect URIs` value.

You must update this value using the URL from the deployed application so that you can run automation on self-service automation portal from self-service automation portal.

**Procedure**

1. Determine the `    Redirect URI` from your OpenShift deployment:


1. Open the URL for the deployment from the OpenShift console to display the sign-in page for self-service automation portal.

![Open URL from OpenShift web console](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Installing_self-service_automation_portal-en-US/images/5a9b8eff9be9b2bc899e6d7f8eb1a69c/self-service-topology-get-url.png)



1. Copy the URL for the sign-in page for self-service automation portal.
1. To determine the `        Redirect URI` value, append `        /api/auth/rhaap/handler/frame` to the end of the deployment URL.

For example, if the URL for the deployment is `        https://my-automation-portal-project.mycluster.com` , then the `        Redirect URI` value is `        https://my-automation-portal-project.mycluster.com/api/auth/rhaap/handler/frame` .



1. Update the `    Redirect URIs` field in the OAuth application in Ansible Automation Platform:


1. In a browser, open your instance of Ansible Automation Platform.
1. Navigate toAccess Management→OAuth Applications.
1. In the list view, click the OAuth application you created.
1. Replace the placeholder text in the `        Redirect URIs` field with the value you determined from your OpenShift deployment.
1. Click `        Save` to apply the changes.



## 7.2. Signing in to self-service automation portal




Log in to the deployed self-service automation portal using your existing Ansible Automation Platform credentials. The portal uses these credentials for authentication.

**Prerequisites**

- You have configured an OAuth application in Ansible Automation Platform for self-service automation portal.
- You have configured a user account in Ansible Automation Platform.


**Procedure**

1. In a browser, navigate to the URL for self-service automation portal to open the sign-in page.

![Self-service sign-in page](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Installing_self-service_automation_portal-en-US/images/7301d2b380047719b3fda17728454b83/self-service-sign-in-page.png)



1. ClickSign In.
1. The sign-in page for Ansible Automation Platform appears:

![Ansible Automation Platform sign-in page](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Installing_self-service_automation_portal-en-US/images/cd442c9292d68a910b63db55552d026f/rhaap-sign-in-page.png)



1. Enter your Ansible Automation Platform credentials and click **Log in** .
1. The self-service automation portal web console opens.


**Troubleshooting**

If your are using custom SSL certificates and when attempting to log in to self-service automation portal, it displays the error:


`Login failed; caused by Error: Failed to send POST request: fetch failed`

You must disable SSL validation in the Helm chart configuration.

1. In the self-service automation portal Helm chart, locate the `    checkSSL` parameter and set its value to `    false` :


```
upstream:        backstage:          appConfig:            ansible:              creatorService:                baseUrl: 127.0.0.1                port: '8000'              rhaap:                baseUrl: '${AAP_HOST_URL}'                checkSSL: false &lt;-- Update this to false                token: '${AAP_TOKEN}'
```


1. Apply the updated configuration by upgrading the self-service automation portal Helm chart to allow users to log in.


## 7.3. Setting up initial RBAC rules in self-service automation portal




After you install self-service automation portal and synchronize it with Ansible Automation Platform, only users with Ansible Automation Platform administrator privileges can view the auto-generated templates.

You must configure initial Role-Based Access Control (RBAC) permissions to allow non-admin users to view and execute synchronized Ansible Automation Platform job templates.

### 7.3.1. Understanding the permission model




Self-service automation portal and Ansible Automation Platform use separate but related permission systems. Ansible Automation Platform RBAC is the source of truth for synchronization scope and execution permissions.

**Self-service automation portal RBAC:**

- Controls which users can view templates in the self-service automation portal catalog.
- Controls which users can access portal templates and submit jobs.


**Ansible Automation Platform RBAC:**

-  **Controls synchronization scope:** Only Ansible Automation Platform job templates accessible by the configured Ansible Automation Platform token (ansible.rhaap.token) are synchronized to self-service automation portal.
-  **Controls Ansible Automation Platform job template visibility and execution:** Ansible Automation Platform permissions determine whether authenticated users can view and execute Ansible Automation Platform job templates in self-service automation portal.
-  **Validates execution permissions:** When a self-service automation portal user executes a template, Ansible Automation Platform checks that user’s execute permissions before launching the job.


Note
If a user can see a self-service automation portal template in the catalog but lacks Ansible Automation Platform execution permissions for the associated Ansible Automation Platform job template in Ansible Automation Platform, the user cannot run the Ansible Automation Platform Job.



### 7.3.2. Configuring RBAC for synchronization




Synchronization uses an Ansible Automation Platform token configured in the self-service automation portal to determine which data to synchronize from Ansible Automation Platform.

By default, self-service automation portal synchronizes Ansible Automation Platform Organization, Team, and User identity information. Self-service automation portal also synchronizes Ansible Automation Platform job template information accessible by the configured Ansible Automation Platform token.

Note
For more information on Ansible Automation Platform token best practices, see the [Ansible Automation Platform documentation](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/access_management_and_authentication/gw-token-based-authentication#gw-oauth2-security-controls) .



**Prerequisites**

- You have credentials for an Ansible Automation Platform administrator.
- Synchronization of Ansible Automation Platform Organization information from Ansible Automation Platform is complete.
- Users who execute Ansible Automation Platform job templates through self-service automation portal must have job template **Execute** permissions assigned in Ansible Automation Platform for the respective Ansible Automation Platform job templates.
- The **Allow external users to create OAuth2 tokens** setting is enabled in theSettings→Platform gatewaysettings in Ansible Automation Platform.


**Procedure**

1. Log in to self-service automation portal with an account that has Ansible Automation Platform administrator privileges.
1. In the navigation pane of self-service automation portal, selectAdministration→RBAC.
1. ClickCreateto create a new role and enter a name, for example `    portal-users` .
1. ClickNext.

![Create new role](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Installing_self-service_automation_portal-en-US/images/8e8d2b1e5b8d880bb39cb45ab87a43b6/self-service-create-new-rbac-role.png)



1. In the **Users and Groups** section, select the Ansible Automation Platform teams and users to assign to this role, then clickNext.

**Note:** You can only select Ansible Automation Platform teams and users from the Ansible Automation Platform Organization that you have configured for synchronization with self-service automation portal.


1. ClickNextto configure permissions in the **Add permission policies** section:


1. Select the **Catalog** plugin from the **Select plugins** dropdown menu.
1. Select the checkbox for `        catalog.entity.read` .

![Add permission policies](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Installing_self-service_automation_portal-en-US/images/7002db599883040e018acfd6d7f1e55c/self-service-add-permission-policies.png)




1. Select the **Scaffolder** plugin and enable all scaffolder permissions:


-  `        scaffolder.template.parameter.read`
-  `        scaffolder.template.step.read`
-  `        scaffolder.action.execute`
-  `        scaffolder.task.cancel`
-  `        scaffolder.task.create`
-  `        scaffolder.task.read`

Note
The `        scaffolder.task.read` permission must be enabled so that users can view previous task runs in the **History** page in the self-service automation portal console.





1. ClickNextto review your settings, thenCreateto create the new role.

On successful completion, your new role is included in the **All roles** list when you selectAdministration→RBACin the navigation pane in self-service automation portal.




**Verification**

On successful completion, your new role is included in the **All roles** list when you selectAdministration→RBACin the navigation pane in self-service automation portal.


### 7.3.3. Configuring conditional access




Optionally, you can configure conditional self-service automation portal RBAC policies to filter role access to specific Ansible Automation Platform job templates by tag for specific Ansible Automation Platform teams or users.

Ansible Automation Platform labels applied to Ansible Automation Platform job templates are synchronized to self-service automation portal as tags and can be used for conditional access control.

Note
Ansible Automation Platform labels are converted to lowercase tags with special characters replaced by hyphens (for example, the Ansible Automation Platform label `Network-Automation` becomes the tag `network-automation` ).



**Prerequisites**

- Ansible Automation Platform job templates must have Ansible Automation Platform labels applied and synchronized with self-service automation portal.
- Users who execute Ansible Automation Platform job templates through self-service automation portal must have Ansible Automation Platform job template **Execute** permissions assigned in Ansible Automation Platform for the respective Ansible Automation Platform job templates.


**Procedure**

1. Log in to self-service automation portal with an account that has Ansible Automation Platform administrator privileges.
1. In the navigation pane of self-service automation portal, selectAdministration→RBAC.
1. ClickCreateto create a new role and enter a name, for example `    network-templates` .
1. ClickNext.
1. In the **Users and Groups** section, select the Ansible Automation Platform teams and users to assign to this role (for example, the Ansible Automation Platform network-team), then clickNext.

Note
You can only select Ansible Automation Platform teams and users from the Ansible Automation Platform Organization that you are using in self-service automation portal.




1. ClickNextto configure permissions in the **Add permission policies** section:


- Select the **Catalog** plugin from the **Select plugins** dropdown menu.
- Select the checkbox for `        catalog.entity.read` .
- ClickConditionalto configure a condition-based policy.

1. In the condition builder, configure a rule to filter by tag:


-  **Rule:** Select `        HAS_METADATA` from the dropdown menu
-  **Key:** Enter `        tags`
-  **Value:** Enter the tag value to filter by (for example, `        network-automation` )

1. Select the **Scaffolder** plugin and enable all scaffolder permissions:


-  `        scaffolder.template.parameter.read`
-  `        scaffolder.template.step.read`
-  `        scaffolder.action.execute`
-  `        scaffolder.task.cancel`
-  `        scaffolder.task.create`
-  `        scaffolder.task.read`

1. ClickNextto review your settings, then clickCreateto create the new role.


**Verification**

On successful completion, your new role is included in the **All roles** list when you selectAdministration→RBACin the navigation pane in self-service automation portal.


1. Log in to self-service automation portal as a non-Ansible Automation Platform administrator user who is a member of a team you granted permissions to.
1. Verify that the user can see auto-generated templates in self-service automation portal.


- If you configured conditional access by tag, the user should see only templates with the specified tags.
- If you did not configure conditional access, the user should see all Ansible Automation Platform job templates for which they have job template **Execute** permissions in Ansible Automation Platform.

1. To verify execution permissions work correctly, attempt to execute a template:


1. If the user has job template **Execute** permissions in Ansible Automation Platform for the template, the user can view the template, and the job launches successfully.



### 7.3.4. Permissions reference for Ansible Automation Platform job template access




Permissions for Ansible Automation Platform job templates

| Permission | Resource type | Policy | Description |
| --- | --- | --- | --- |
|  `catalog.entity.read` | catalog-entity | read | Users can view synchronized Ansible Automation Platform job templates in the self-service automation portal. |
|  `scaffolder.template.parameter.read` | scaffolder-template | read | Users can read template parameters. |
|  `scaffolder.action.execute` | scaffolder-action | use | Users can execute actions through templates. |
|  `scaffolder.task.create` |  | create | Users can trigger the execution of Ansible Automation Platform job templates. |
|  `scaffolder.task.read` |  | read | Users can view task execution history and logs on the **History** page. |
|  `scaffolder.task.cancel` |  | use | Users can cancel currently running templates. |


## 7.4. Adjusting synchronization frequency between Ansible Automation Platform and self-service automation portal




The Helm chart defines how frequently users, teams and organization configuration information is synchronized from Ansible Automation Platform to self-service automation portal.

The frequency is set by the `catalog.providers.rhaap.schedule.frequency` key. By default, the synchronization occurs hourly.

**Procedure**

- To adjust the synchronization frequency, edit the value for the `    catalog.providers.rhaap.schedule.frequency` key in the Helm chart.


```
catalog:              ...              providers:                rhaap:                  '{{- include "catalog.providers.env" . }}':                    schedule:                      frequency: {minutes: 60}                      timeout: {seconds: 30}
```

Note
Increasing the synchronization frequency generates extra traffic.

Bear this in mind when deciding the frequency, particularly if you have a large number of users.






# Chapter 8. Upgrading self-service automation portal




To ensure that your self-service automation portal deployment has the latest features and fixes, you must upgrade the plug-in registry and Helm chart to the latest versions.

## 8.1. Downloading the plug-in TAR files




Download the latest `.tar.gz` plug-in files for self-service automation portal from the Red Hat Customer Portal.

**Procedure**

1. Create a directory on your local machine to store the files.


```
$ mkdir /path/to/&lt;automation-portal-plugins&gt;
```


1. Set an environment variable ( `    $DYNAMIC_PLUGIN_ROOT_DIR` ) to represent the directory path.


```
$ export DYNAMIC_PLUGIN_ROOT_DIR=/path/to/&lt;automation-portal-plugins&gt;
```


1. Download the setup bundle. In a browser, navigate to the [Red Hat Ansible Automation Platform Product Software downloads page](https://access.redhat.com/downloads/content/480/ver=2.6/rhel---9/2.6/x86_64/product-software) . and select the **Product Software** tab.
1. Click **Download now** next to **Ansible self-service automation portal Setup Bundle** to download the latest version of the plug-ins.

The format of the filename is `    self-service-automation-portal-plugins-x.y.z.tar.gz` .

Substitute the Ansible plug-ins release version, for example `    2.0.0` , for `    x.y.z` .


1. Extract the `    self-service-automation-portal-plugins-&lt;version-number&gt;.tar.gz` contents to `    $DYNAMIC_PLUGIN_ROOT_DIR` .


```
$ tar --exclude='*code*' -xzf self-service-automation-portal-plugins-x.y.z.tar.gz -C $DYNAMIC_PLUGIN_ROOT_DIR
```

Substitute the Ansible plug-ins release version, for example `    2.0.0` , for `    x.y.z` .




**Verification**

Run `ls` to verify that the extracted files are in the `$DYNAMIC_PLUGIN_ROOT_DIR` directory:


```
$ ls $DYNAMIC_PLUGIN_ROOT_DIR
ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz
ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz.integrity
ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz
ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz.integrity
```

The files with the `.integrity` file type contain the plugin SHA value.

## 8.2. Updating the plug-in registry




To update the plug-in registry, you must upload your plug-in files to OpenShift, and start a new build of the registry.

**Prerequisites**

- You have downloaded the plug-in TAR files for self-service automation portal.
- You have set an environment variable, for example `    $DYNAMIC_PLUGIN_ROOT_DIR` , to represent the path to the local directory where you have stored the TAR files.


**Procedure**

1. In a terminal, log in to your OpenShift Container Platform instance.
1. Open your OpenShift project for self-service automation portal.


```
$ oc project &lt;YOUR_SELF_SERVICE_AUTOMATION_PORTAL_PROJECT&gt;
```


1. Find the name of your current plug-in registry build configuration:


```
$ oc get buildconfig
```


1. From the output, identify the correct build configuration name, for example `    aap-self-service-plugins` .
1. Run the following command to start a new build in in your OpenShift project.


```
$ oc start-build &lt;build_config_name&gt; --from-dir=$DYNAMIC_PLUGIN_ROOT_DIR --wait
```


- The command assumes that `        $DYNAMIC_PLUGIN_ROOT_DIR` represents the directory for your TAR files. Replace this in the command if you have chosen a different environment variable name.
- Replace `        &lt;build_config_name&gt;` with the build configuration name you identified.

When the build starts, the following message is displayed:


```
Uploading directory "/path/to/dynamic_plugin_root" as binary input for the build ...     Uploading finished
```




**Verification**

1. Open the **Topology** view in the **Developer** perspective for your project in the OpenShift web console.
1. Select the plugin registry icon to open the **plugin-registry** details pane.
1. In the **Pods** section of the **plugin-registry** details pane, select **View logs** for the new build pod. The format for the pod name is `    &lt;build_config_name&gt;-&lt;build_number&gt;-build` .
1. Click the **terminal** tab and log in to the container.
1. In the terminal, run `    ls` to view the TAR files in the plugin registry.
1. Verify that the new TAR files have been uploaded.


## 8.3. Updating the self-service automation portal version numbers for a Helm installation




After you have updated your plug-in registry for your self-service automation portal project on your OpenShift Container Platform instance, you must update the Helm chart with the new versions of your plug-ins files.

You can update the Helm chart from the command line using `helm` commands, or from the OpenShift web console.

Note
For upgrades in air-gapped or disconnected environments, the standard procedure cannot be used directly. You must first mirror the necessary container images to your local registry and prepare the Helm chart for offline use.

For detailed instructions on this process, see the [Installing the self-service automation portal in an air-gapped environment](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/installing_self-service_automation_portal/self-service-disconnected-install_aap-self-service-install) section of _ [Installing self-service automation portal](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/installing_self-service_automation_portal) _ .



**Procedure**

-  **Update the Helm chart from the command line:**


1. In a terminal, log in to your OpenShift instance.
1. Open your OpenShift Project that has your self-service automation portal installation.
1. Run the following command to ensure your Helm repository is up to date:


```
$ helm repo update
```


1. Find the latest version of the Helm chart:


```
$ helm search repo openshift-helm-charts/redhat-rhaap-portal
```


1. Upgrade the Helm release:


```
$ helm upgrade &lt;release_name&gt; openshift-helm-charts/redhat-rhaap-portal --version &lt;chart_version&gt;
```

Replace `        &lt;release_name&gt;` with the name of your Helm release and `        &lt;chart_version&gt;` with the new Helm chart version number you identified in the previous step.



-  **Update the Helm chart using the OpenShift web console:**


1. In a browser, log in to your OpenShift Container Platform web console.
1. Switch to the **Developer** perspective.
1. Ensure you are in the OpenShift Project that has your self-service automation portal Helm deployment.
1. From the navigation menu, Select **Helm** .
1. Find your existing self-service automation portal deployment in the list of **Helm releases** and click its name.
1. SelectActions→Upgrade.
1. In the **Upgrade** pane, select the version that you want to upgrade to from the **Chart Version** dropdown list.
1. Review the YAML configuration to ensure your custom values are preserved.
1. ClickUpgradeto begin the upgrade.



**Verification**

After the upgrade completes, verify that the updated self-service automation portal instance is running: . In the OpenShift Container Platform web console, navigate to the **Topology** view for your project. . Check that the self-service automation portal instance is available and that all associated pods are in a **Running** state.


# Chapter 9. Telemetry capturing




The telemetry data collection feature helps in collecting and analyzing the telemetry data to improve your experience with self-service automation portal. This feature is enabled by default.

## 9.1. Telemetry data collected by Red Hat




Red Hat collects and analyses the following data:

- Events of page visits and clicks on links or buttons.
- System-related information, for example, locale, timezone, user agent including browser and OS details.
- Page-related information, for example, title, category, extension name, URL, path, referrer, and search parameters.
- Anonymized IP addresses, recorded as `    0.0.0.0` .
- Anonymized username hashes, which are unique identifiers used solely to identify the number of unique users of the RHDH application.


## 9.2. Disabling telemetry data collection




You can disable and enable the telemetry data collection feature for self-service automation portal by updating the Helm chart for your OpenShift Container Platform project.

**Procedure**

1. Log in to the OpenShift Container Platform console and open the project for self-service automation portal in the **Developer** perspective.
1. Navigate to **Helm** .
1. Click the **More actions ⋮** icon for your self-service automation portal Helm chart and select **Upgrade** .
1. Select **YAML view** .
1. Locate the `    redhat-developer-hub.global.dynamic.plugins` section of the Helm chart.
1. To disable telemetry data collection, add the following lines to the `    redhat-developer-hub.global.dynamic.plugins` section.


```
redhat-developer-hub:      global:        ....        dynamic:          plugins:            - disabled: true              package: &gt;-                ./dynamic-plugins/dist/backstage-community-plugin-analytics-provider-segment
```

To re-enable telemetry data collection, delete these lines.


1. ClickUpgradeto apply the changes to the Helm chart and restart the pod.



<span id="idm140108972376256"></span>
# Legal Notice

Copyright© Red Hat.
The text of and illustrations in this document are licensed by Red Hat under a Creative Commons Attribution–Share Alike 3.0 Unported license ("CC-BY-SA"). An explanation of CC-BY-SA is available at [http://creativecommons.org/licenses/by-sa/3.0/](http://creativecommons.org/licenses/by-sa/3.0/) . In accordance with CC-BY-SA, if you distribute this document or an adaptation of it, you must provide the URL for the original version.
Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.
Red Hat, Red Hat Enterprise Linux, the Shadowman logo, JBoss, OpenShift, Fedora, the Infinity logo, and RHCE are trademarks of Red Hat, Inc., registered in the United States and other countries.
Linux® is the registered trademark of Linus Torvalds in the United States and other countries.
Java® is a registered trademark of Oracle and/or its affiliates.
XFS® is a trademark of Silicon Graphics International Corp. or its subsidiaries in the United States and/or other countries.
MySQL® is a registered trademark of MySQL AB in the United States, the European Union and other countries.
Node.js® is an official trademark of Joyent. Red Hat Software Collections is not formally related to or endorsed by the official Joyent Node.js open source or commercial project.
TheOpenStack® Word Mark and OpenStack logo are either registered trademarks/service marks or trademarks/service marks of the OpenStack Foundation, in the United States and other countries and are used with the OpenStack Foundation's permission. We are not affiliated with, endorsed or sponsored by the OpenStack Foundation, or the OpenStack community.
All other trademarks are the property of their respective owners.





