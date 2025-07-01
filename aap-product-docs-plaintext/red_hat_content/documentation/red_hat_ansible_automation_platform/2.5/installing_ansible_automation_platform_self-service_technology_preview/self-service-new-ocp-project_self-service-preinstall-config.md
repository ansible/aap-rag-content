# 3. Pre-installation configuration
## 3.4. Setting up a project for self-service technology preview in OpenShift Container Platform




You must set up a project in OpenShift Container Platform for self-service technology preview. You can create the project from a terminal using the `oc` command. Alternatively, you can create the project in the OpenShift Container Platform console.

For more about OpenShift Container Platform projects, see the _ [Building applications](https://docs.redhat.com/en/documentation/openshift_container_platform/4.15/html/building_applications/projects#working-with-projects) _ guide in the OpenShift Container Platform documentation.

### 3.4.1. Setting up an OpenShift Container Platform project using `oc`




1. In a terminal, log in to OpenShift Container Platform using your credentials:


```
oc login &lt;OpenShift_API_URL&gt; -u &lt;username&gt;
```

For example:


```
$ oc login https://api.&lt;my_cluster&gt;.com:6443 -u kubeadmin    WARNING: Using insecure TLS client config. Setting this option is not supported!        Console URL: https://api.&lt;my_cluster&gt;.com:6443/console    Authentication required for https://api.&lt;my_cluster&gt;.com:6443 (openshift)    Username: kubeadmin    Password:    Login successful.        You have access to 22 projects, the list has been suppressed. You can list all projects with 'oc projects'        Using project "default".
```


1. Create a new project. Use a unique project name.


```
$ oc new-project &lt;self-service-tech-preview-project-name&gt;
```

Lowercase alphanumeric characters ( `    a-z` , `    0-9` ) and the hyphen character ( `    -` ) are permitted for project names. The underscore ( `    _` ) character is not permitted. The maximum length for project names is 63 characters.

Example:


```
$ oc new-project &lt;my-project&gt;        Now using project "my-project" on server "https://openshift.example.com:6443".
```


1. Open your new project:


```
$ oc project &lt;self-service-tech-preview-project-name&gt;
```




### 3.4.2. Setting up a project in the OpenShift Container Platform web console




You can use the OpenShift Container Platform web console to create a project in your cluster.

1. In a browser, log in to the OpenShift Container Platform web console.
1. Choose the **Developer** perspective.
1. Click the **Project** menu and select **Create project** .


1. In the **Create Project** dialog box, enter a unique name **Name** field.


- Lowercase alphanumeric characters ( `            a-z` , `            0-9` ) and the hyphen character ( `            -` ) are permitted for project names.
- The underscore ( `            _` ) character is not permitted.
- The maximum length for project names is 63 characters.

1. Optional: display name and description for your project.

1. ClickClickto create the project.


## 3.5. Creating a plug-in registry in OpenShift




### 3.5.1. Downloading the TAR files




1. Create a directory on your local machine to store the `    .tar` files.


```
$ mkdir /path/to/&lt;ansible-backstage-plugins-local-dir-changeme&gt;
```


1. Set an environment variable ( `    $DYNAMIC_PLUGIN_ROOT_DIR` ) to represent the directory path.


```
$ export DYNAMIC_PLUGIN_ROOT_DIR=/path/to/&lt;ansible-backstage-plugins-local-dir-changeme&gt;
```


1. Download the latest `    .tar` file for the plug-ins from the [Red Hat Ansible Automation Platform Product Software downloads page](https://access.redhat.com/downloads/content/480/ver=2.5/rhel---9/2.5/x86_64/product-software) .

The format of the filename is `    ansible-backstage-rhaap-bundle-x.y.z.tar.gz` .

Substitute the Ansible plug-ins release version, for example `    1.0.0` , for `    x.y.z` .


1. Extract the `    ansible-backstage-rhaap-bundle-&lt;version-number&gt;.tar.gz` contents to `    $DYNAMIC_PLUGIN_ROOT_DIR` .


```
$ tar --exclude='*code*' -xzf ansible-backstage-rhaap-bundle-x.y.z.tar.gz -C $DYNAMIC_PLUGIN_ROOT_DIR
```

Substitute the Ansible plug-ins release version, for example `    1.0.0` , for `    x.y.z` .




**Verification**

Run `ls` to verify that the extracted files are in the `$DYNAMIC_PLUGIN_ROOT_DIR` directory:


```
$ ls $DYNAMIC_PLUGIN_ROOT_DIR
ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz
ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz.integrity
ansible-plugin-backstage-rhaap-backend-dynamic-x.y.z.tgz
ansible-plugin-backstage-rhaap-backend-dynamic-x.y.z.tgz.integrity
ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz
ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz.integrity
```

The files with the `.integrity` file type contain the plugin SHA value.

### 3.5.2. Setting up the plugin registry image




Set up a registry in your OpenShift cluster to host the plug-ins and make them available for installation.

**Procedure**

1. Log in to your OpenShift Container Platform instance with credentials to create a new application.
1. Open your OpenShift project for self-service technology preview.


```
$ oc project &lt;AAP-self-service-tech-preview-project-name&gt;
```


1. Run the following commands to create a plugin registry build in in your OpenShift project.


```
$ oc new-build httpd --name=plugin-registry --binary    $ oc start-build plugin-registry --from-dir=$DYNAMIC_PLUGIN_ROOT_DIR --wait    $ oc new-app --image-stream=plugin-registry
```




**Verification**

Verify that the plugin-registry was deployed successfully:


1. Open the **Topology** view in the **Developer** perspective for your project in the OpenShift web console.
1. Select the plugin registry icon to open the **plugin-registry** details pane.
1. In the **Pods** section of the **plugin-registry** details pane, click **View logs** for the `    plugin-registry-#########-####` pod.

![Developer perspective](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Installing_Ansible_Automation_Platform_self-service_technology_preview-en-US/images/b1594982a3b39036d9063bb57acc195e/self-service-plugin-registry.png)


(1) Plug-in registry


1. Click the **terminal** tab and log in to the container.
1. In the terminal, run `    ls` to confirm that the `    .tar` files are in the plugin registry.


```
ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz    ansible-plugin-backstage-rhaap-backend-dynamic-x.y.z.tgz    ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz
```

The version numbers and file names can differ.




## 3.6. Creating secrets in OpenShift for your environment variables




Before installing the chart, you must create a set of secrets in your OpenShift project. The self-service technology preview Helm chart fetches environment variables from OpenShift secrets.

### 3.6.1. Creating Ansible Automation Platform authentication secrets




1. Log in to your OpenShift Container Platform instance.
1. Open your OpenShift project for self-service technology preview in the **Administrator** view.
1. Click **Secrets** in the side pane.
1. Click **Create** to open the form for creating a new secret.
1. Select the **Key/Value** option.
1. Create a secret named `    secrets-rhaap-self-service-preview` .

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

Value needed: Token for Ansible Automation Platform user authentication (must have `        write` access).



1. Click **Create** to create the secret.


### 3.6.2. Creating Creating GitHub and Gitlab secrets




1. Log in to your OpenShift Container Platform instance.
1. Open your OpenShift project for self-service technology preview.
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


# Chapter 4. Installing the self-service technology preview Helm chart




## 4.1. Configuring the self-service technology preview Helm chart from the OpenShift catalog




**Prerequisites**

1. You have created a project for self-service technology preview in OpenShift.
1. You have created a plugin registry in your project.
1. You have set up secrets for Ansible Automation Platform authentication and SCM authentication.


**Procedure**

1. In a browser, navigate to your OpenShift project for self-service technology preview that you created earlier.
1. Select the **Developer** view.
1. Click the **Helm** option in the OpenShift sidebar.
1. In the **Helm** page, click **Create** and select **Helm Release** .
1. Search for `    AAP` in the Helm Charts filter, and select the `    AAP Technical Preview: Self-service automation` chart.
1. In the modal dialog on the chart page, click **Create** .
1. Select the **YAML view** in the **Create Helm Release** page.
1. Locate the `    clusterRouterBase` key in the YAML file and replace the placeholder value with the base URL of your OpenShift instance.

The base URL is the URL portion of your OpenShift URL that follows `    https://console-openshift-console` , for example `    apps.example.com` :


```
redhat-developer-hub        global:          clusterRouterBase: apps.example.com
```


1. The Helm chart is set up for the Default Ansible Automation Platform organization.

To update the Helm chart to use a different organization, update the value for the `    catalog.providers.rhaap.orgs` key from `    Default` to your Ansible Automation Platform organization name.


1. Click **Create** to launch the deployment.


## 4.2. Verifying the installation




1. In a browser, log in to your OpenShift instance.
1. In the **Developer** view, navigate to the **Topology** view for the namespace where you deployed the Helm chart.

The deployment appears: the label on the icon is `    D` . The name of the deployment is `    &lt;installation-name&gt;-backstage` , for example `    &lt;my-aap-self-service-tech-preview-backstage&gt;` .

While it is deploying, the icon is light blue. The color changes to dark blue when deployment is complete.




![Deployment on OpenShift console](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Installing_Ansible_Automation_Platform_self-service_technology_preview-en-US/images/06c45647f2a2be815da7e2006fd83257/self-service-verify-helm-install.png)


# Chapter 5. Inspecting the deployment on OpenShift




You can inspect the deployment logs and ConfigMap on the OpenShift UI to verify that the deployment conforms with the settings in your Helm chart.

## 5.1. Viewing the deployment logs




1. In a browser, log in to your OpenShift instance.
1. In the **Developer** view, navigate to the **Topology** view for the namespace where you deployed the Helm chart.
1. The deployment appears: the label on the icon is `    D` .

The name of the deployment is `    &lt;installation-name&gt;-backstage` , for example `    &lt;my-aap-self-service-tech-preview-backstage&gt;` .


1. Click the icon representing the deployment.
1. The **Details** pane for the deployment opens.
1. Select the **Resources** tab.
1. Click **View** logs for the deployment pod in the **Pods** section:

![Deployment on OpenShift console](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Installing_Ansible_Automation_Platform_self-service_technology_preview-en-US/images/7db4d1cfa7a66893597c9306c073b561/self-service-view-deployment-logs.png)


The **Pod details** page opens for the deployment pod.


1. Select the **Logs** tab in the **Pod details** page.
1. To view the install messages, select the `    install-dynamic-plugins` container from the **INIT CONTAINERS** section of the dropdown list of containers:

![View install messages](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Installing_Ansible_Automation_Platform_self-service_technology_preview-en-US/images/e9518a231caeb6d563f762c47f17d7e5/self-service-view-install-messages.png)


The log stream displays the progress of the installation of the plug-ins from the plug-in registry.

The log stream for successful installation of the plug-ins resembles the following output:


```
======= Installing dynamic plugin http://plugin-registry:8080/ansible-backstage-plugin-catalog-backend-module-rhaap-dynamic-0.1.0.tgz     *=&gt; Grabbing package archive through pm pack'     •=› Vertfying package Integrity     •*&gt; Extracting package archtve /dynamtc-plugtns-root/anstble-backstage-plugtn-catalog-backend-nodule-rhaap-dynamic-0.1.0.tgz     •*› Removing package archive /dynamic-plugins-root/ansible-backstage-plugin-catalog-backend-module-rhaap-dynamic-0.1.0. tgz     -&gt; Successfully installed dynamic plugin http://plugin-registry:8080/ansible-backstage-plugin-catalog-backend-module-rhaap-dynamic-0.1.0.tgz
```


1. Select the **Environment** tab in the **Pod details** page to view the environment variables for the containers. If you set additional environment variables in your Helm chart, check that they are listed here.

![Pod environment variables](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Installing_Ansible_Automation_Platform_self-service_technology_preview-en-US/images/0a87b7e4f33737aecc0c1af2f37dc039/self-service-pod-env-variables.png)





## 5.2. Viewing the ConfigMaps




1. In a browser, open the project for your self-service technology preview in your OpenShift instance.
1. In the **Developer** view, select **ConfigMaps** in the navigation pane.
1. Select the `    &lt;installation-name&gt;-backstage-app-config` ConfigMap, for example `    my-aap-self-service-tech-preview-backstage-app-config` .
1. Verify that the ConfigMap conforms with the values you updated in the Helm chart.
1. Return to the list of ConfigMaps and select the `    &lt;installation-name&gt;-dynamic-plugins` ConfigMap, for example `    my-aap-self-service-tech-preview-dynamic-plugins` .
1. Verify that the ConfigMap conforms with the expected plugin values.


# Chapter 6. Accessing the self-service technology preview deployment




## 6.1. Adding the deployment URL to the OAuth Application




When you set up your OAuth application in Ansible Automation Platform before deploying self-service technology preview, you added placeholder text for the `Redirect URIs` value.

You must update this value using the URL from the deployed application so that you can run automation on self-service technology preview from self-service technology preview.

1. Determine the `    Redirect URI` from your OpenShift deployment:


1. Open the URL for the deployment from the OpenShift console to display the sign-in page for self-service technology preview.
1. Copy the URL.
1. To determine the `        Redirect URI` value, append `        /api/auth/rhaap/handler/frame` to the end of the deployment URL.

For example, if the URL for the deployment is `        https://my-aap-self-service-tech-preview-backstage-myproject.mycluster.com` , then the `        Redirect URI` value is `        https://my-aap-self-service-tech-preview-backstage-myproject.mycluster.com/api/auth/rhaap/handler/frame` .



1. Update the `    Redirect URIs` field in the OAuth application in Ansible Automation Platform:


1. In a browser, open your instance of Ansible Automation Platform.
1. Navigate toAccess Management→OAuth Applications.
1. In the list view, click the OAuth application you created.
1. Replace the placeholder text in the `        Redirect URIs` field with the value you determined from your OpenShift deployment.
1. Click `        Save` to apply the changes.



## 6.2. Signing in to self-service technology preview




**Prerequisites**

1. You have configured an OAuth application in Ansible Automation Platform for self-service technology preview.
1. You have configured a user account in Ansible Automation Platform.


**Procedure**

1. In a browser, navigate to the URL for self-service technology preview to open the sign-in page.

![Self-service sign-in page](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Installing_Ansible_Automation_Platform_self-service_technology_preview-en-US/images/27208caf5145d17e9c9161f4ca2e9d7d/self-service-sign-in-page.png)



1. Click **Sign In** .
1. The sign-in page for Ansible Automation Platform appears:

![Ansible Automation Platform sign-in page](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Installing_Ansible_Automation_Platform_self-service_technology_preview-en-US/images/cd442c9292d68a910b63db55552d026f/rhaap-sign-in-page.png)



1. Enter your Ansible Automation Platform credentials and click **Log in** .
1. The self-service technology preview UI opens.
1. Click **Templates** to open a landing page where tiles are displayed, representing templates. When the page is populated with templates, the layout resembles the following screenshot:

![Templates view](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Installing_Ansible_Automation_Platform_self-service_technology_preview-en-US/images/b71c6e4e37d131a33959de3a3f21ee58/self-service-templates-view.png)





## 6.3. Adjusting synchronization frequency between Ansible Automation Platform and self-service technology preview




The Helm chart defines how frequently users, teams and organization configuration information is synchronized from Ansible Automation Platform to self-service technology preview.

The frequency is set by the `catalog.providers.rhaap.schedule.frequency` key. By default, the synchronization occurs hourly.

- To adjust the synchronization frequency, edit the value for the `    catalog.providers.rhaap.schedule.frequency` key in the Helm chart.


```
catalog:              ...              providers:                rhaap:                  '{{- include "catalog.providers.env" . }}':                    schedule:                      frequency: {minutes: 60}                      timeout: {seconds: 30}
```




Note
Increasing the synchronization frequency generates extra traffic.

Bear this in mind when deciding the frequency, particularly if you have a large number of users.



# Chapter 7. Telemetry capturing




The telemetry data collection feature helps in collecting and analyzing the telemetry data to improve your experience with Ansible Automation Platform self-service technology preview. This feature is enabled by default.

## 7.1. Telemetry data collected by Red Hat




Red Hat collects and analyses the following data:

- Events of page visits and clicks on links or buttons.
- System-related information, for example, locale, timezone, user agent including browser and OS details.
- Page-related information, for example, title, category, extension name, URL, path, referrer, and search parameters.
- Anonymized IP addresses, recorded as `    0.0.0.0` .
- Anonymized username hashes, which are unique identifiers used solely to identify the number of unique users of the RHDH application.


## 7.2. Disabling telemetry data collection




You can disable and enable the telemetry data collection feature for self-service technology preview by updating the Helm chart for your OpenShift Container Platform project.

1. Log in to the OpenShift Container Platform console and open the project for self-service technology preview in the **Developer** perspective.
1. Navigate to **Helm** .
1. Click the **More actions ⋮** icon for your self-service technology preview Helm chart and select **Upgrade** .
1. Select **YAML view** .
1. Locate the `    redhat-developer-hub.global.dynamic.plugins` section of the Helm chart.
1. To disable telemetry data collection, add the following lines to the `    redhat-developer-hub.global.dynamic.plugins` section.


```
redhat-developer-hub:      global:        ....        dynamic:          plugins:            - disabled: true              package: &gt;-                ./dynamic-plugins/dist/backstage-community-plugin-analytics-provider-segment
```

To re-enable telemetry data collection, delete these lines.


1. ClickUpgradeto apply the changes to the Helm chart and restart the pod.



<span id="idm140465048982272"></span>
# Legal Notice

Copyright© 2025 Red Hat, Inc.
The text of and illustrations in this document are licensed by Red Hat under a Creative Commons Attribution–Share Alike 3.0 Unported license ("CC-BY-SA"). An explanation of CC-BY-SA is available at [http://creativecommons.org/licenses/by-sa/3.0/](http://creativecommons.org/licenses/by-sa/3.0/) . In accordance with CC-BY-SA, if you distribute this document or an adaptation of it, you must provide the URL for the original version.
Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.
Red Hat, Red Hat Enterprise Linux, the Shadowman logo, the Red Hat logo, JBoss, OpenShift, Fedora, the Infinity logo, and RHCE are trademarks of Red Hat, Inc., registered in the United States and other countries.
Linux® is the registered trademark of Linus Torvalds in the United States and other countries.
Java® is a registered trademark of Oracle and/or its affiliates.
XFS® is a trademark of Silicon Graphics International Corp. or its subsidiaries in the United States and/or other countries.
MySQL® is a registered trademark of MySQL AB in the United States, the European Union and other countries.
Node.js® is an official trademark of Joyent. Red Hat is not formally related to or endorsed by the official Joyent Node.js open source or commercial project.
TheOpenStack® Word Mark and OpenStack logo are either registered trademarks/service marks or trademarks/service marks of the OpenStack Foundation, in the United States and other countries and are used with the OpenStack Foundation's permission. We are not affiliated with, endorsed or sponsored by the OpenStack Foundation, or the OpenStack community.
All other trademarks are the property of their respective owners.





