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




## 3.7. Choose a plug-in delivery method




Self-service automation portal supports two plug-in installation methods. Choose the method that fits your environment:

-  **OCI container (recommended)** : self-service automation portal automatically pulls an Open Container Initiative (OCI) container from `    registry.redhat.io` .
-  **HTTP plug-in registry** : Manually create an HTTP plug-in registry that contains the necessary self-service automation portal plug-ins.


### 3.7.1. OCI container delivery




Use OCI container delivery to automatically pull an OCI container from `registry.redhat.io` that includes the self-service automation portal plug-ins. This is the recommended method for production deployments.

This method is the default for the Helm chart and is the recommended method for production deployments.

**Prerequisites**

- You have a Red Hat account with access to `    registry.redhat.io` .
- You have credentials for `    registry.redhat.io` .
- You have access to the OpenShift project where you will install the Helm chart.
- You have installed the OpenShift CLI ( `    oc` ) and logged in to your cluster.
- You have a registry service account token from the Red Hat Customer Portal.


**Procedure**

1. Create an `    auth.json` file on your local machine.
1. Add the following structure to the `    auth.json` file:


```
{      "auths": {        "registry.redhat.io": {          "auth": "&lt;base64-encoded-username-password&gt;"        }      }    }
```


1. Generate the base64-encoded authentication value:


```
printf '%s' '&lt;username&gt;:&lt;password&gt;' | base64 -w0
```


1. Replace `    &lt;base64-encoded-username-password&gt;` in the `    auth.json` file with the output from the previous step.
1. Create the authentication secret in the target OpenShift project. The secret name must match your Helm release name.

If you install from the OpenShift catalog and you use the default release name `    redhat-rhaap-portal` :


```
oc create secret generic redhat-rhaap-portal-dynamic-plugins-registry-auth \      --from-file=auth.json=./auth.json
```

If you use a custom release name:


```
oc create secret generic &lt;release-name&gt;-dynamic-plugins-registry-auth \      --from-file=auth.json=./auth.json
```




**Verification**

- Verify that the secret exists in the project:


```
oc get secret &lt;release-name&gt;-dynamic-plugins-registry-auth
```

You must use a Red Hat Registry service account to generate the OpenShift secret. Using your standard Red Hat account username and password is not secure and will not work.

The `    install-dynamic-plugins` init container uses `    skopeo` to pull OCI plug-in artifacts. It does not use cluster pull secrets, global pull secrets, or `    imagePullSecrets` . A dedicated auth secret is required even when pulling from `    registry.redhat.io` .




Important
Create this secret in the same OpenShift project as the Helm release, and create it before you install or upgrade the Helm release.



**OpenShift web console steps**

You can create the `dynamic-plugins-registry-auth` secret in the OpenShift web console.

1. In the OpenShift web console, select the OpenShift project where you will install the Helm release.
1. In the **Administrator** view, click **Workloads** → **Secrets** .
1. Click **Create** → **Key/value secret** .
1. Set the secret name to `    &lt;release-name&gt;-dynamic-plugins-registry-auth` .
1. Add a key named `    auth.json` and paste the contents of your `    auth.json` file as the value.
1. Click **Create** .


**Helm chart configuration**

When you configure the Helm chart, set `redhat-developer-hub.global.pluginMode` to match your chosen delivery method:

-  `    oci` — OCI container delivery (recommended).
-  `    tarball` — HTTP plug-in registry.


Verify that `pluginMode` is set to the correct value. If you omit this setting, the chart uses its built-in default.

```
redhat-developer-hub:
global:
pluginMode: oci
```

If you need to change `pluginMode` after installing the Helm release, upgrade the Helm release.

**OpenShift web console:**

1. In the **Developer** view, click **Helm** .
1. Select the Helm release.
1. Click **Actions** → **Upgrade** .
1. In the **YAML view** , set `    redhat-developer-hub.global.pluginMode` to `    oci` (OCI container delivery) or `    tarball` (HTTP plug-in registry).
1. Click **Upgrade** .


**Command line:**

- Run the `    helm upgrade` command with your updated values file:


```
helm upgrade &lt;release-name&gt; &lt;chart&gt; -n &lt;project&gt; -f &lt;values.yaml&gt;
```




**Additional resources**

-  [Registry Service Accounts](https://access.redhat.com/login?redirectTo=https%3A%2F%2Faccess.redhat.com%2Farticles%2FRegistryAuthentication)


### 3.7.2. HTTP plug-in registry




The HTTP plug-in registry method hosts plug-in tarball files in a local OpenShift registry that the dynamic plug-in installer pulls during startup.

#### 3.7.2.1. Log into OpenShift CLI




To deploy a plug-in registry, you must install the OpenShift CLI ( `oc` ) locally and log in to your cluster.

See [Installing OpenShift CLI in the OpenShift Container Platform](https://docs.redhat.com/en/documentation/openshift_container_platform/4.8/html/cli_tools/openshift-cli-oc#installing-openshift-cli) documentation.

**Procedure**

1. Log in to OpenShift Container Platform using your credentials:


```
oc login &lt;OpenShift_API_URL&gt; -u &lt;username&gt;
```


1. Create a new project or switch to an existing project:


```
oc new-project &lt;project-name&gt;
```

Or:


```
oc project &lt;project-name&gt;
```




#### 3.7.2.2. Download plug-ins and push to the registry




To provide Ansible plug-ins to Red Hat Developer Hub, download the setup bundle and push the extracted files to a local Red Hat OpenShift registry.

By setting up a centralized httpd service, you can access these plug-in files through Helm chart configuration.

**Procedure**

1. Create a directory on your local machine to store the plug-in files.


```
mkdir /path/to/&lt;ansible-backstage-plugins-local-dir&gt;
```


1. Set an environment variable `    $DYNAMIC_PLUGIN_ROOT_DIR` to represent the directory path.


```
export DYNAMIC_PLUGIN_ROOT_DIR=/path/to/&lt;ansible-backstage-plugins-local-dir&gt;
```


1. Download the setup bundle. In a browser, navigate to the [Red Hat Ansible Automation Platform Product Software downloads page](https://access.redhat.com/downloads/content/480/ver=2.6/rhel---9/2.6/x86_64/product-software) . and select the **Product Software** tab.
1. Click **Download now** next to **Ansible self-service automation portal Setup Bundle** to download the latest version of the plug-ins.

The format of the filename is `    self-service-automation-portal-plugins-x.y.z.tar.gz` .

Substitute the Ansible plug-ins release version, for example `    2.0.0` , for `    x.y.z` .


1. Extract the contents to `    $DYNAMIC_PLUGIN_ROOT_DIR` :


```
$ tar --exclude='*code*' -xzf self-service-automation-portal-plugins-x.y.z.tar.gz -C $DYNAMIC_PLUGIN_ROOT_DIR
```


1. Verify that the extracted files are in the `    $DYNAMIC_PLUGIN_ROOT_DIR` directory:


```
ls $DYNAMIC_PLUGIN_ROOT_DIR
```

You should see the following files:


```
ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz    ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz.integrity    ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz    ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz.integrity
```

The files with the .integrity file type contain the plug-in SHA value.


1. Create an httpd service as part of your OpenShift project:


```
oc new-build httpd --name=plugin-registry --binary
oc start-build plugin-registry --from-dir=$DYNAMIC_PLUGIN_ROOT_DIR --wait
oc new-app --image-stream=plugin-registry
```

**Verification**

1. Run the following command to verify that the plug-in registry deployed correctly:


```
oc exec $(oc get pods -l deployment=plugin-registry -o jsonpath='{.items[0].metadata.name}') -- ls -l /opt/app-root/src
```


1. Confirm that the required tarball files are in the plug-in registry.


**Helm chart configuration** When you configure the Helm chart, set `redhat-developer-hub.global.pluginMode` to `tarball` :

```
redhat-developer-hub:
global:
pluginMode: tarball
```

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


# Chapter 4. Install the self-service automation portal Helm chart




You can use the configured secrets and plugin registry to install the self-service automation portal. Deploy the application onto your OpenShift cluster using the provided Helm chart.

## 4.1. Configure the self-service automation portal Helm chart from the OpenShift catalog




Deploy the Helm chart from the OpenShift catalog by configuring the base URL and organization name in the YAML view. This launches the self-service automation portal installation.

**Prerequisites**

- You have created a project for self-service automation portal in OpenShift Container Platform.
- You have created secrets in OpenShift Container Platform for Ansible Automation Platform authentication.
- If you configure SCM integration (for example, importing from private repositories or using templates that access SCM), you have created secrets in OpenShift for SCM authentication.
- You have completed one of the plug-in delivery methods:


- For OCI delivery: You have created the `        &lt;release-name&gt;-dynamic-plugins-registry-auth` secret.



**Procedure**

1. In the OpenShift Container Platform web console, select the **Developer** view.
1. Select your project and click theHelmoption in the OpenShift sidebar.
1. ClickCreateand select **Helm Release** .
1. Search for `    Portal` in the Helm Charts filter, and select the `    Automation Portal` chart.
1. ClickCreateand select the **YAML view** .
1. Update the `    clusterRouterBase` value with the base URL of your OpenShift instance.

Important
You must replace the default `    apps.example.com` placeholder value. If the default value remains, Helm chart validation fails.




```
redhat-developer-hub:      global:        clusterRouterBase: apps.example.com
```


1. Configure the plug-in delivery mode by setting the `    pluginMode` key:


- For OCI delivery, set the value to `        oci` .


```
redhat-developer-hub:          global:            pluginMode: oci
```



1.  **Optional:** To use a specific plug-in version, update the `    imageTagInfo` value:


```
redhat-developer-hub:      global:        imageTagInfo: "2.1"
```


1. Set the Ansible Automation Platform organization to synchronize. The default value is `    Default` . Update the `    orgs` key to match your organization name:


```
redhat-developer-hub:      upstream:        backstage:          appConfig:            catalog:              providers:                rhaap:                  '{{- include "catalog.providers.env" . }}':                    orgs: "&lt;your-aap-organization-name&gt;"
```


1.  **Optional:** Update the `    CUSTOMER_SUPPORT_URL` to point to your support portal:


```
redhat-developer-hub:      upstream:        backstage:          extraEnvVars:            - name: CUSTOMER_SUPPORT_URL              value: https://access.redhat.com/support
```


1. ClickCreate.


**Additional resources**

-  [Choose a plug-in delivery method](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/installing_self-service_automation_portal/index#self-service-create-ocp-registry_self-service-preinstall-config)


## 4.2. Verify the installation




Verify the Helm chart installation from the OpenShift Container Platform web console.

**Procedure**

1. In a browser, log in to your OpenShift instance.
1. In the **Developer** view, navigate to the **Topology** view for the namespace where you deployed the Helm chart.

The deployment appears: the label on the icon is `    D` . The name of the deployment is `    &lt;installation-name&gt;-backstage` , for example `    &lt;my-self-service-automation-portal-backstage&gt;` .

While it is deploying, the icon is light blue. The color changes to dark blue when deployment is complete.

![Deployment on OpenShift console](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Installing_self-service_automation_portal-en-US/images/06c45647f2a2be815da7e2006fd83257/self-service-verify-helm-install.png)





# Chapter 5. Installing self-service automation portal using RHEL appliances




Deploy the self-service automation portal using pre-built virtual machine appliances for OpenShift Virtualization or VMware `vSphere` .

## 5.1. Prerequisites




- You have a valid subscription to Red Hat Ansible Automation Platform.
- You have the URL for your Ansible Automation Platform instance.
- You have configured an OAuth application in Ansible Automation Platform and retrieved the Client ID and Client Secret.
- You have generated an admin token for Ansible Automation Platform authentication.
- You have obtained the self-service automation portal appliance disk images (QCOW2 or VMDK) from Red Hat.


## 5.2. About self-service automation portal RHEL appliances




The self-service automation portal RHEL 9 virtual machine appliances provide pre-configured virtual machines that you can deploy across multiple virtualization platforms.

The appliances are available in the following formats:

-  **QCOW2** - For OpenShift Virtualization and KVM-based environments
-  **VMDK** - For VMware `    vSphere` infrastructure


### 5.2.1. Supported platforms




You can deploy self-service automation portal appliances on the following platforms:

Note
self-service automation portal appliances support AMD64/x86_64 platforms only.



### 5.2.2. Initial configuration




After starting the appliance, an interactive configuration wizard guides you through the initial setup. The wizard prompts you to configure:

- SSH key authentication for administrative access
- Network settings
- Ansible Automation Platform OAuth application credentials
- Ansible Automation Platform admin token for authentication


After the configuration wizard completes, the appliance displays the portal URL that you can access from your browser.

Note
You cannot log in to the virtual machine console with a username and password after the wizard completes. Administrative access is available only through SSH using the key you provided during initial configuration.



## 5.3. Install self-service automation portal on OpenShift Virtualization




Deploy the self-service automation portal appliance on OpenShift Virtualization to run the portal as a virtual machine alongside container workloads within your OpenShift Container Platform cluster. This approach enables you to use your existing OpenShift infrastructure to host the portal.

**Prerequisites**

- OpenShift Container Platform cluster (4.x) with OpenShift Virtualization operator installed and configured.
- Cluster administrator or equivalent permissions to create VirtualMachine resources.
- A storage class configured that supports ReadWriteOnce (RWO) access mode for virtual machine disks.
- The self-service automation portal disk image in QCOW2 format.
- The `    virtctl` CLI tool installed. You can download it from the OpenShift web console under **Virtualization** → **Overview** → **Download virtctl** .
- Access to the OpenShift web console or `    oc` CLI tool.
- Network configuration details for the appliance (IP address, gateway, DNS) or access to a DHCP-enabled network.
- Sufficient cluster resources: minimum 4 GiB allocatable memory for the virtual machine.


**Procedure**

1. Install the `    virtctl` CLI tool.

Download `    virtctl` from your OpenShift cluster:


```
curl -kL -o virtctl.tar.gz \      "https://hyperconverged-cluster-cli-download-openshift-cnv.apps.&lt;cluster&gt;/amd64/linux/virtctl.tar.gz"    tar -xzf virtctl.tar.gz    chmod +x virtctl    sudo mv virtctl /usr/local/bin/
```

Alternatively, download `    virtctl` from the OpenShift web console by navigating to **Virtualization** → **Overview** and clicking **Download virtctl** .


1. Create the target namespace:


```
oc create namespace aap-portal
```


1. Upload the disk image.

The Containerized Data Importer (CDI) automatically converts the QCOW2 format to raw format during the upload process. The PVC size must be significantly larger than the QCOW2 file size to accommodate the expanded raw image. A minimum of 40 GiB is required.


```
virtctl image-upload dv aap-portal-disk \      --size=40GiB \      --image-path=/path/to/disk.qcow2 \      --uploadproxy-url=https://cdi-uploadproxy-openshift-cnv.apps.&lt;cluster&gt; \      --insecure \      --force-bind \      --wait-secs=600 \      -n aap-portal
```

| Option | Description |
| --- | --- |
|  `dv` | Creates a DataVolume resource. This is the recommended approach as it handles PVC creation and disk conversion automatically. |
|  `--size` | PVC size. Must be larger than the virtual disk size to accommodate QCOW2 to raw conversion. Use 40 GiB minimum for self-service automation portal. |
|  `--force-bind` | Forces immediate PVC binding. This flag is required for storage classes using WaitForFirstConsumer binding mode. |
|  `--insecure` | Allows connection to upload proxy with self-signed certificates. This is required for most OpenShift installations. |
|  `--wait-secs` | Timeout in seconds for waiting for the upload pod. Increase this value for slower environments or larger images. |


Wait for the upload to complete. The "Processing completed successfully" message confirms that CDI has successfully converted the QCOW2 image to raw format.


1. Create the virtual machine.

Create a file named `    vm-aap-portal.yaml` :


```
apiVersion: kubevirt.io/v1    kind: VirtualMachine    metadata:      name: aap-portal      namespace: aap-portal    spec:      runStrategy: Always      template:        spec:          domain:            devices:              disks:              - disk:                  bus: virtio                name: rootdisk              interfaces:              - masquerade: {}                name: default            resources:              requests:                memory: 4GiB          networks:          - name: default            pod: {}          volumes:          - name: rootdisk            dataVolume:              name: aap-portal-disk
```


1. Apply the manifest:


```
oc apply -f vm-aap-portal.yaml
```


1. Monitor the virtual machine startup.

The virtual machine starts automatically when using `    runStrategy: Always` :


```
oc get vmi -n aap-portal -w
```

Wait for the PHASE to show `    Running` and READY to show `    True` .


1. Access the virtual machine console.

Connect to the virtual machine console using the CLI:


```
virtctl console aap-portal -n aap-portal
```

Alternatively, use the web console:


1. Navigate to **Virtualization** → **VirtualMachines** .
1. Click the `        aap-portal` virtual machine.
1. Select the **Console** tab.

1. Complete the initial configuration wizard.

Follow the on-screen prompts in the console.




**Verification**

- Verify that the virtual machine is running:


```
oc get vmi -n aap-portal
```

The output shows the virtual machine in `    Running` phase with `    READY` status set to `    True` .


- Access the portal URL displayed at the end of the configuration wizard from your browser.


**Troubleshooting**


**Additional resources**

-  [Completing the initial configuration wizard](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/installing_self-service_automation_portal/index#proc-self-service-initial-config-wizard_self-service-install-rhel-appliance)


## 5.4. Install self-service automation portal on VMware vSphere




Deploy the self-service automation portal appliance on VMware vSphere infrastructure to integrate the portal into your existing VMware environment. This procedure guides you through creating a virtual machine and importing the VMDK disk image.

**Prerequisites**

- VMware vSphere x86-64 environment with appropriate permissions to create and manage virtual machines.
- SSH access to an ESXi host connected to your target VMFS datastore.
- The self-service automation portal disk image in VMDK format.
- Network configuration details for the appliance (IP address, gateway, DNS).


**Procedure**

1. Create a blank virtual machine in vSphere with the following specifications:


- Appropriate CPU and memory allocation per Ansible Automation Platform guidelines
- Compatible guest operating system type
- Network adapter configured for your environment

1. Upload the disk image to the datastore.

Transfer the `    disk.vmdk` file to the virtual machine’s folder on the VMFS datastore:


1. Navigate to the **Datastores** view in vSphere.
1. Browse to the folder created for your blank virtual machine.
1. Click **Upload** and select the `        disk.vmdk` file.

1. Convert the disk to vSphere format.

The disk image must be converted to a vSphere-compatible VMFS format before it can be attached to the virtual machine.


1. Enable SSH on the ESXi host if not already enabled ( **Host** → **Actions** → **Services** → **Enable SSH** ).
1. Connect to the ESXi host using SSH.
1. Navigate to the virtual machine folder on the datastore.
1. Execute the conversion command:


```
vmkfstools -i disk.vmdk disk-vmfs.vmdk -d thin
```

Upon successful completion, you see the following output:


```
Destination disk format: VMFS thin-provisioned        Cloning disk 'disk.vmdk'...        Clone: 100% done.
```



1. Attach the converted disk to the virtual machine:


1. Edit the virtual machine settings in vSphere.
1. Remove the default hard disk that was created with the blank virtual machine.
1. Add a new hard disk and select **Existing Hard Disk** .
1. Browse to and select the converted disk: `        disk-vmfs.vmdk` .
1. Save the virtual machine settings.

1. Start the virtual machine and complete the initial configuration:


1. Open the virtual machine console in vSphere.
1. Power on the virtual machine.
1. Follow the on-screen configuration wizard instructions.



**Verification**

- Verify that the virtual machine boots successfully and displays the configuration wizard.
- Access the portal URL displayed at the end of the configuration wizard from your browser.


**Additional resources**

-  [Completing the initial configuration wizard](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/installing_self-service_automation_portal/index#proc-self-service-initial-config-wizard_self-service-install-rhel-appliance)
- The `    -d thin` option creates a thin-provisioned disk, which only consumes datastore space as data is written. This is the recommended option for most deployments.
- After confirming the virtual machine boots successfully, you can delete the original `    disk.vmdk` file to reclaim datastore space.


## 5.5. Complete the initial configuration wizard




Complete the initial configuration to connect your self-service automation portal appliance to Ansible Automation Platform and make the portal accessible. An interactive text-based configuration wizard guides you through setting up SSH access, network configuration, and Ansible Automation Platform authentication.

**Prerequisites**

- The virtual machine appliance is running and displaying the configuration wizard in the console.
- You have the Ansible Automation Platform OAuth application Client ID and Client Secret.
- You have the Ansible Automation Platform admin token.
- You have an SSH public key for administrative access.


**Procedure**

1. When you SSH into the virtual machine for the first time, the configuration wizard displays in the terminal.
1. Configure the default admin password:


1. Enter the default password `        PortalFirstBoot!` when prompted.
1. The wizard prompts you to reset the password.
1. Enter and confirm your new password.

Note
After SSH key authentication is configured in the next step, password-based login will be deactivated.





1. Configure SSH key authentication:


1. The wizard prompts you to enter an SSH public key for the `        admin` user.
1. Paste your SSH public key when prompted.
1. After you add the SSH key, the SSH connection closes. Reconnect using your SSH key to continue.

Note
SSH key authentication is the only method for accessing the virtual machine after initial configuration. Username and password authentication is not available.





1. Configure account security:


1. Confirm the SSH key configuration.
1. The wizard validates the provided key.

1. Configure network settings (if not using DHCP):


1. Enter the IP address, subnet mask, gateway, and DNS servers when prompted.
1. The wizard applies the network configuration.

1. Configure Ansible Automation Platform integration:

The wizard prompts you to enter the following information:


1.  **Ansible Automation Platform URL:** The full URL of your Ansible Automation Platform instance (for example, `        https://controller.example.com` ).
1.  **OAuth Client ID:** The Client ID from the OAuth application you created in Ansible Automation Platform.
1.  **OAuth Client Secret:** The Client Secret from the OAuth application.
1.  **Admin Token:** The admin token generated for Ansible Automation Platform authentication.

Important
The OAuth application in Ansible Automation Platform must be configured with the correct redirect URI: `        https://&lt;PORTAL_IP&gt;:&lt;CONFIGURED_PORT&gt;/api/auth/rhaap/handler/frame` , where `        &lt;PORTAL_IP&gt;` is the IP address or hostname of the portal appliance and `        &lt;CONFIGURED_PORT&gt;` defaults to `        443` . You can change the port at any time by using the TUI or CLI.





1. Review the configuration summary.

The wizard displays a summary of your configuration and prompts you to confirm.


1. Apply the configuration.

The wizard applies the configuration and starts the self-service automation portal services.


1. Note the portal URL.

After the configuration completes, the wizard displays the portal URL (for example, `    Portal URL:<a class="link" href="https://192.168.2.2:443">https://192.168.2.2:443</a>` ).

Important
Record this URL. You cannot log in to the virtual machine console with a username and password after the wizard completes.






**Verification**

- Access the portal URL from your browser.
- Log in using your Ansible Automation Platform credentials.


**Additional resources**

-  [Portal CLI commands reference](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/installing_self-service_automation_portal/index#ref-self-service-portal-cli-commands_self-service-install-rhel-appliance)


## 5.6. Portal CLI commands reference




The self-service automation portal appliance provides CLI commands for management and troubleshooting.

### 5.6.1. Accessing the appliance




You can access the appliance using SSH with the key you provided during initial configuration:

```
ssh -i /path/to/ssh-key/id_ed25519 -p &lt;port-number&gt; admin@&lt;VM_IP&gt;
```

Replace the following placeholders:

-  `    /path/to/ssh-key/id_ed25519` with the path to your SSH private key.
-  `    &lt;port-number&gt;` with the SSH port number (default is 22).
-  `    &lt;VM_IP&gt;` with the IP address or hostname of your appliance.


### 5.6.2. Available commands




The following commands are available for managing the self-service automation portal appliance:

#### 5.6.2.1. portal-config




Manages the portal configuration settings.

**Usage:**

```
sudo portal-config show    # View current configuration
sudo portal-config edit    # Modify configuration settings
```

**Description:**

-  `    portal-config show` displays the current portal configuration, including Ansible Automation Platform connection details and service settings.
-  `    portal-config edit` opens an interactive editor to modify the portal configuration.


Use `portal-config` to update existing configuration settings after the initial setup is complete.

#### 5.6.2.2. portal-setup




Runs the initial configuration wizard or imports a configuration.

**Usage:**

```
sudo portal-setup              # Run the initial configuration wizard
sudo portal-setup import       # Import a configuration file
```

**Description:**

-  `    portal-setup` launches the interactive configuration wizard, which is the same wizard that runs automatically on first boot.
-  `    portal-setup import` imports a previously exported configuration file.


Important
**Difference between portal-setup and portal-config:**

- Use `    portal-setup` to run the complete initial configuration wizard or to import an entire configuration from a file. This command is typically used during initial deployment or when migrating to a new appliance.
- Use `    portal-config` to view or modify individual configuration settings on an already-configured appliance. This command is used for day-to-day configuration updates.




#### 5.6.2.3. portal-status




Checks the status of portal services.

**Usage:**

```
portal-status
```

**Description:**

Displays the current status of all self-service automation portal services, including:

- Service running state (active/inactive)
- Service health checks
- Resource usage
- Network connectivity status


Use this command to verify that all services are running correctly after installation or troubleshooting.

**Example output:**

```
Portal Status:
✓ Web Service: Running
✓ Database: Connected
✓ AAP Connection: Connected
✓ Authentication: Configured
```

#### 5.6.2.4. portal-backup




Creates a backup of the portal configuration and data.

**Usage:**

```
sudo portal-backup
sudo portal-backup --output /path/to/backup
```

**Description:**

Creates a backup archive containing the portal configuration, settings, and data. Use this command before making significant configuration changes or for disaster recovery planning.

The backup includes:

- Portal configuration settings
- Ansible Automation Platform OAuth application credentials
- User customizations
- Service configurations


Note
Store backup files in a secure location. Backup archives contain sensitive credentials and should be protected accordingly.



### 5.6.3. Additional resources




- For information about the initial configuration wizard, see [Completing the initial configuration wizard](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/installing_self-service_automation_portal/index#proc-self-service-initial-config-wizard_self-service-install-rhel-appliance) .
- For troubleshooting information, see [Troubleshooting RHEL appliances](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/installing_self-service_automation_portal/index#ref-self-service-rhel-troubleshooting_self-service-install-rhel-appliance) .


## 5.7. Troubleshooting RHEL appliances




Common issues and solutions for deploying and managing self-service automation portal RHEL appliances.

### 5.7.1. General troubleshooting




### 5.7.2. OpenShift Virtualization troubleshooting




### 5.7.3. VMware vSphere troubleshooting




### 5.7.4. QEMU troubleshooting




### 5.7.5. Getting help




If you encounter issues not covered in this troubleshooting guide:

1. Use the `    journalctl -u portal.service -f` command to collect detailed logs for analysis.
1. Use the `    portal-status` command to verify service health.
1. Review the virtual machine console output for error messages.
1. Contact Red Hat Support with the following information:


- The virtualization platform you are using (OpenShift Virtualization, VMware vSphere, or QEMU)
- The appliance version and disk image filename
- Output from `        portal-status` and `        journalctl -u portal.service -f`
- Any error messages from the virtual machine console or platform logs



**Additional resources**

-  [Portal CLI commands reference](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/installing_self-service_automation_portal/index#ref-self-service-portal-cli-commands_self-service-install-rhel-appliance) .
-  [Completing the initial configuration wizard](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/installing_self-service_automation_portal/index#proc-self-service-initial-config-wizard_self-service-install-rhel-appliance) .


## 5.8. Additional resources




-  [Creating an OAuth application in Ansible Automation Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/installing_self-service_automation_portal/index#self-service-create-oauth-app_self-service-preinstall-config)


//// AAP-64365: Chapter 6 commented out - may be restored later


<span id="idm139874767936720"></span>
# Legal Notice

Copyright© Red Hat.
Except as otherwise noted below, the text of and illustrations in this documentation are licensed by Red Hat under the Creative Commons Attribution–Share Alike 3.0 Unported license . If you distribute this document or an adaptation of it, you must provide the URL for the original version.
Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.
Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of Red Hat, LLC. or its subsidiaries in the United States and other countries.
Linux® is the registered trademark of Linus Torvalds in the United States and other countries.
XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its subsidiaries in the United States and other countries.
TheOpenStack® Word Mark and OpenStack logo are trademarks or registered trademarks of the Linux Foundation, used under license.
All other trademarks are the property of their respective owners.





