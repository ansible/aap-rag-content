+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.5/html-single/installing_ansible_plug-ins_for_red_hat_developer_hub/index"
title = "Installing Ansible plug-ins for Red Hat Developer Hub - Red Hat Ansible Automation Platform 2.5"

[extra]
modified = "2025-06-12T17:32:14.000Z"
multi_page_path = "/documentation/en-us/red_hat_ansible_automation_platform/2.5/html/installing_ansible_plug-ins_for_red_hat_developer_hub/index/"
name = "Installing Ansible plug-ins for Red Hat Developer Hub"
page_slug = "installing_ansible_plug-ins_for_red_hat_developer_hub"
product = "Red Hat Ansible Automation Platform"
product_version = "2.5"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/installing_ansible_plug-ins_for_red_hat_developer_hub/index"
type = "single-page"
+++


<span id="idm139651268784432"></span>
Red Hat Ansible Automation Platform2.5
## Install and configure Ansible plug-ins for Red Hat Developer Hub


Red Hat Customer Content Services

 [Legal Notice](#idm139651272926544) 
 **Abstract** 

This guide describes how to install and configure Ansible plug-ins for Red Hat Developer Hub so that users can learn about Ansible, explore curated collections, and develop automation projects.




---

# Preface




Thank you for your interest in Red Hat Ansible Automation Platform. Ansible Automation Platform is a commercial offering that helps teams manage complex multi-tier deployments by adding control, knowledge, and delegation to Ansible-powered environments.

This guide describes how to install Ansible plug-ins for Red Hat Developer Hub. This document has been updated to include information for the latest release of Ansible Automation Platform.

# Providing feedback on Red Hat documentation




If you have a suggestion to improve this documentation, or find an error, you can contact technical support at [https://access.redhat.com](https://access.redhat.com) to open a request.

# Chapter 1. Ansible plug-ins for Red Hat Developer Hub




## 1.1. Red Hat Developer Hub




Red Hat Developer Hub (RHDH) serves as an open developer platform designed for building developer portals.

## 1.2. Ansible plug-ins for Red Hat Developer Hub




Ansible plug-ins for Red Hat Developer Hub deliver an Ansible-first Red Hat Developer Hub user experience that simplifies the automation experience for Ansible users of all skill levels. The Ansible plug-ins provide curated content and features to accelerate Ansible learner onboarding and streamline Ansible use case adoption across your organization.

The Ansible plug-ins provide:

- A customized home page and navigation tailored to Ansible users.
- Curated Ansible learning paths to help users new to Ansible.
- Software templates for creating Ansible playbook and collection projects that follow best practices.
- Links to supported development environments and tools with opinionated configurations.


## 1.3. Architecture




![Ansible plugin for Red Hat Developer Hub architecture](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Installing_Ansible_plug-ins_for_Red_Hat_Developer_Hub-en-US/images/40f3afc9e44e83daaf1c4baf53c668a9/rhdh-ansible-plugin-architecture.png)


# Chapter 2. Installing the Ansible plug-ins with a Helm chart on OpenShift Container Platform




The following procedures describe how to install Ansible plug-ins in Red Hat Developer Hub instances on Red Hat OpenShift Container Platform using a Helm chart.

The workflow is as follows:

1. Download the Ansible plug-ins files.
1. Create a plug-in registry in your OpenShift cluster to host the Ansible plug-ins.
1. Add the plug-ins to the Helm chart.
1. Create a custom ConfigMap.
1. Add your custom ConfigMap to your Helm chart.
1. Edit your custom ConfigMap and Helm chart according to the required and optional configuration procedures.
    
    Note
    You can save changes to your Helm and ConfigMap after each update to your configuration. You do not have to make all the changes to these files in a single session.
    
    
    
    


## 2.1. Prerequisites




- Red Hat Developer Hub installed on Red Hat OpenShift Container Platform.
    
    
    - For Helm installation, follow the steps in the [Installing Red Hat Developer Hub on OpenShift Container Platform with the Helm chart](https://docs.redhat.com/en/documentation/red_hat_developer_hub/1.4/html/installing_red_hat_developer_hub_on_openshift_container_platform/index#assembly-install-rhdh-ocp-helm) section of _Installing Red Hat Developer Hub on OpenShift Container Platform_ .
    - For Operator installation, follow the steps in the [Installing Red Hat Developer Hub on OpenShift Container Platform with the Operator](https://docs.redhat.com/en/documentation/red_hat_developer_hub/1.4/html/installing_red_hat_developer_hub_on_openshift_container_platform/index#assembly-install-rhdh-ocp-operator) section of _Installing Red Hat Developer Hub on OpenShift Container Platform_ .
    
- A valid subscription to Red Hat Ansible Automation Platform.
- An OpenShift Container Platform instance with the appropriate permissions within your project to create an application.
- The Red Hat Developer Hub instance can query the automation controller API.
- Optional: To use the integrated learning paths, you must have outbound access to developers.redhat.com.


## 2.2. Recommended RHDH preconfiguration




Red Hat recommends performing the following initial configuration tasks in RHDH. However, you can install the Ansible plug-ins for Red Hat Developer Hub before completing these tasks.

-  [Setting up authentication in RHDH](https://docs.redhat.com/en/documentation/red_hat_developer_hub/1.4/html/authentication/index) 
-  [Installing and configuring RBAC in RHDH](https://docs.redhat.com/en/documentation/red_hat_developer_hub/1.4/html/authorization/index) 


Note
Red Hat provides a [repository of software templates for RHDH](https://github.com/ansible/ansible-rhdh-templates/blob/main/all.yaml) that uses the `publish:github` action. To use these software templates, you must install the required GitHub dynamic plugins.



## 2.3. Downloading the Ansible plug-ins files




1. Download the latest `    .tar` file for the plug-ins from the [Red Hat Ansible Automation Platform Product Software downloads page](https://access.redhat.com/downloads/content/480/ver=2.5/rhel---9/2.5/x86_64/product-software) . The format of the filename is `    ansible-backstage-rhaap-bundle-x.y.z.tar.gz` . Substitute the Ansible plug-ins release version, for example `    1.0.0` , for `    x.y.z` .
1. Create a directory on your local machine to store the `    .tar` files.
    
    
    ```
    $ mkdir /path/to/&lt;ansible-backstage-plugins-local-dir-changeme&gt;
    ```
    
    
1. Set an environment variable ( `    $DYNAMIC_PLUGIN_ROOT_DIR` ) to represent the directory path.
    
    
    ```
    $ export DYNAMIC_PLUGIN_ROOT_DIR=/path/to/&lt;ansible-backstage-plugins-local-dir-changeme&gt;
    ```
    
    
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

The files with the `.integrity` file type contain the plugin SHA value. The SHA value is used during the plug-in configuration.

## 2.4. Creating a registry for the Ansible plug-ins




Set up a registry in your OpenShift cluster to host the Ansible plug-ins and make them available for installation in Red Hat Developer Hub (RHDH).

 **Procedure** 

1. Log in to your OpenShift Container Platform instance with credentials to create a new application.
1. Open your Red Hat Developer Hub OpenShift project.
    
    
    ```
    $ oc project &lt;YOUR_DEVELOPER_HUB_PROJECT&gt;
    ```
    
    
1. Run the following commands to create a plug-in registry build in the OpenShift cluster.
    
    
    ```
    $ oc new-build httpd --name=plugin-registry --binary    $ oc start-build plugin-registry --from-dir=$DYNAMIC_PLUGIN_ROOT_DIR --wait    $ oc new-app --image-stream=plugin-registry
    ```
    
    


 **Verification** 

To verify that the plugin-registry was deployed successfully, open the **Topology** view in the **Developer** perspective on the Red Hat Developer Hub application in the OpenShift Web console.


1. Click the plug-in registry to view the log.
    
    ![Developer perspective](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Installing_Ansible_plug-ins_for_Red_Hat_Developer_Hub-en-US/images/569de994c3fd61a583f4b81b85bf852e/rhdh-plugin-registry.png)
    
    
    (1) Developer hub instance
    
    (2) Plug-in registry
    
    
1. Click the terminal tab and login to the container.
1. In the terminal, run `    ls` to confirm that the `    .tar` files are in the plugin registry.
    
    
    ```
    ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz    ansible-plugin-backstage-rhaap-backend-dynamic-x.y.z.tgz    ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz
    ```
    
    The version numbers and file names can differ.
    
    


## 2.5. Required configuration




### 2.5.1. Adding the Ansible plug-ins configuration




1. In the OpenShift Developer UI, navigate toHelm→developer-hub→Actions→Upgrade→Yaml view.
1. Update the Helm chart configuration to add the dynamic plug-ins in the Red Hat Developer Hub instance. Under the `    plugins` section in the YAML file, add the dynamic plug-ins that you want to enable.
    
    
    ```
    global:      ...        plugins:          - disabled: false            integrity: &lt;SHA512 Integrity key for ansible-plugin-backstage-rhaap-dynamic plugin&gt;            package: 'http://plugin-registry:8080/ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz'            pluginConfig:              dynamicPlugins:                frontend:                  ansible.plugin-backstage-rhaap:                    appIcons:                      - importName: AnsibleLogo                        name: AnsibleLogo                    dynamicRoutes:                      - importName: AnsiblePage                        menuItem:                          icon: AnsibleLogo                          text: Ansible                        path: /ansible          - disabled: false            integrity: &lt;SHA512 Integrity key for ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic plugin&gt;            package: &gt;-              http://plugin-registry:8080/ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz            pluginConfig:              dynamicPlugins:                backend:                  ansible.plugin-scaffolder-backend-module-backstage-rhaap: null          - disabled: false            integrity: &lt;SHA512 Integrity key for ansible-plugin-backstage-rhaap-backend-dynamic plugin&gt;            package: &gt;-              http://plugin-registry:8080/ansible-plugin-backstage-rhaap-backend-dynamic-x.y.z.tgz            pluginConfig:              dynamicPlugins:                backend:                  ansible.plugin-backstage-rhaap-backend: null
    ```
    
    
1. In the `    package` sections, replace `    x.y.z` in the plug-in filenames with the correct version numbers for the Ansible plug-ins.
1. For each Ansible plug-in, update the integrity values using the corresponding `    .integrity` file content.
1. ClickUpgrade.
    
    The developer hub pods restart and the plug-ins are installed.
    
    


 **Verification** 

To verify that the plug-ins have been installed, open the `install-dynamic-plugin` container logs and check that the Ansible plug-ins are visible in Red Hat Developer Hub:


1. Open the Developer perspective for the Red Hat Developer Hub application in the OpenShift Web console.
1. Select the **Topology** view.
1. Select the Red Hat Developer Hub deployment pod to open an information pane.
1. Select the **Resources** tab of the information pane.
1. In the **Pods** section, click **View logs** to open the **Pod details** page.
1. In the **Pod details** page, select the **Logs** tab.
1. Select `    install-dynamic-plugins` from the drop-down list of containers to view the container log.
1. In the `    install-dynamic-plugin` container logs, search for the Ansible plug-ins.
    
    The following example from the log indicates a successful installation for one of the plug-ins:
    
    
    ```
    =&gt; Successfully installed dynamic plugin http://plugin-registry-1:8080/ansible-plugin-backstage-rhaap-dynamic-1.1.0.tgz
    ```
    
    The following image shows the container log in the **Pod details** page. The version numbers and file names can differ.
    
    ![container logs for install-dynamic-plugin](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Installing_Ansible_plug-ins_for_Red_Hat_Developer_Hub-en-US/images/70103d03251d3babcbbacc093de282f4/rhdh-check-plugin-config.png)
    
    
    


### 2.5.2. Adding the Ansible Development Tools sidecar container




After the plug-ins are loaded, add the Ansible Development Container ( `ansible-devtools-server` ) in the Red Hat Developer Hub pod as a sidecar container.

#### 2.5.2.1. Adding a pull secret to the Red Hat Developer Hub Helm configuration




 **Prerequisite** 

The Ansible Development Container download requires a Red Hat Customer Portal account and Red Hat Service Registry account.


 **Procedure** 

1. Create a new [Red Hat Registry Service account](https://access.redhat.com/terms-based-registry/) , if required.
1. Click the token name under the **Account name** column.
1. Select the **OpenShift Secret** tab and follow the instructions to add the pull secret to your Red Hat Developer Hub OpenShift project.
1. Add the new secret to the Red Hat Developer Hub Helm configuration, replacing `    &lt;your-redhat-registry-pull-secret&gt;` with the name of the secret you generated on the Red Hat Registry Service Account website:
    
    
    ```
    upstream:      backstage:        ...        image:          ...          pullSecrets:            - &lt;your-redhat-registry-pull-secret&gt;        ...
    ```
    
    


For more information, refer to the [Red Hat Container Registry documentation](https://access.redhat.com/RegistryAuthentication) .

#### 2.5.2.2. Adding the Ansible Developer Tools container




You must update the Helm chart configuration to add an extra container.

 **Procedure** 

1. Log in to the OpenShift UI.
1. Navigate toHelm→developer-hub→Actions→upgrade→Yaml viewto open the Helm chart.
1. Update the `    extraContainers` section in the YAML file.
    
    Add the following code:
    
    
    ```
    upstream:      backstage:        ...        extraContainers:          - command:              - adt              - server            image: &gt;-              registry.redhat.io/ansible-automation-platform-25/ansible-dev-tools-rhel8:latest            imagePullPolicy: IfNotPresent            name: ansible-devtools-server            ports:              - containerPort: 8000        ...
    ```
    
    Note
    The image pull policy is `    imagePullPolicy: IfNotPresent` . The image is pulled only if it does not already exist on the node. Update it to `    imagePullPolicy: Always` if you always want to use the latest image.
    
    
    
    
1. ClickUpgrade.


 **Verification** 

To verify that the container is running, check the container log:


![View container log](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Installing_Ansible_plug-ins_for_Red_Hat_Developer_Hub-en-US/images/6abd3ad41671a23156c96a0710df0fe8/rhdh-check-devtools-container.png)


### 2.5.3. Adding a custom ConfigMap




Create a Red Hat Developer Hub ConfigMap following the procedure in the [Creating and using config maps](https://docs.redhat.com/en/documentation/openshift_container_platform/4.15/html-single/nodes/index#configmaps) section of the OpenShift Container Platform _Nodes_ guide. The following examples use a custom ConfigMap named `app-config-rhdh` .

To edit your custom ConfigMap, log in to the OpenShift UI and navigate toSelect Project ( developerHubProj )→ConfigMaps→{developer-hub}-app-config→EditConfigMaps→app-config-rhdh.

### 2.5.4. Configuring the Ansible Dev Tools Server




The `creatorService` URL is required for the Ansible plug-ins to provision new projects using the provided software templates.

 **Procedure** 

1. Edit your custom Red Hat Developer Hub config map, `    app-config-rhdh` , that you created in [Adding a custom ConfigMap](#rhdh-add-custom-configmap_rhdh-ocp-required-installation) .
1. Add the following code to your Red Hat Developer Hub `    app-config-rhdh.yaml` file.
    
    
    ```
    kind: ConfigMap    apiVersion: v1    metadata:      name: app-config-rhdh    ...    data:      app-config-rhdh.yaml: |-        ansible:          creatorService:            baseUrl: 127.0.0.1            port: '8000'    ...
    ```
    
    


### 2.5.5. Configuring Ansible Automation Platform details




The Ansible plug-ins query your Ansible Automation Platform subscription status with the controller API using a token.

Note
The Ansible plug-ins continue to function regardless of the Ansible Automation Platform subscription status.



 **Procedure** 

1. Create a Personal Access Token (PAT) with “Read” scope in automation controller, following the [Applications](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/access_management_and_authentication/gw-token-based-authentication#assembly-controller-applications) section of _Access management and authentication_ .
1. Edit your custom Red Hat Developer Hub config map, for example `    app-config-rhdh` .
1. Add your Ansible Automation Platform details to `    app-config-rhdh.yaml` .
    
    
    1. Set the `        baseURL` key with your automation controller URL.
    1. Set the `        token` key with the generated token value that you created in Step 1.
    1. Set the `        checkSSL` key to `        true` or `        false` .
        
        If `        checkSSL` is set to `        true` , the Ansible plug-ins verify whether the SSL certificate is valid.
        
        
        ```
        data:          app-config-rhdh.yaml: |            ...            ansible:            ...              rhaap:                baseUrl: '&lt;https://MyControllerUrl&gt;'                token: '&lt;AAP Personal Access Token&gt;'                checkSSL: true
        ```
        
        
    


Note
You are responsible for protecting your Red Hat Developer Hub installation from external and unauthorized access. Manage the backend authentication key like any other secret. Meet strong password requirements, do not expose it in any configuration files, and only inject it into configuration files as an environment variable.



### 2.5.6. Configuring `showCaseLocation` 




You must configure `showCaseLocation` in your custom config map.

 **Procedure** 

1. Edit your custom Red Hat Developer Hub config map, `    app-config-rhdh` , that you created in [Adding a custom ConfigMap](#rhdh-add-custom-configmap_rhdh-ocp-required-installation) .
1. Add the following code to your Red Hat Developer Hub `    app-config-rhdh.yaml` file.
    
    
    ```
    kind: ConfigMap    apiVersion: v1    metadata:      name: app-config-rhdh    ...    data:      app-config-rhdh.yaml: |-        ansible:          rhaap:          ...            showCaseLocation:              type: file              target: '/tmp/aap-showcases/'    ...
    ```
    
    


### 2.5.7. Adding Ansible plug-ins software templates




Red Hat Ansible provides software templates for Red Hat Developer Hub to provision new playbooks and collection projects based on Ansible best practices.

 **Procedure** 

1. Edit your custom Red Hat Developer Hub config map, for example `    app-config-rhdh` .
1. Add the following code to your Red Hat Developer Hub `    app-config-rhdh.yaml` file.


```
data:
  app-config-rhdh.yaml: |
    catalog:
      ...
      locations:
        ...
        - type: url
          target: https://github.com/ansible/ansible-rhdh-templates/blob/main/all.yaml
          rules:
            - allow: [Template]
```

For more information, refer to the [Managing templates](https://docs.redhat.com/en/documentation/red_hat_developer_hub/1.2/html-single/administration_guide_for_red_hat_developer_hub/assembly-admin-templates#assembly-admin-templates) section of the _Administration guide for Red Hat Developer Hub_ .

### 2.5.8. Configuring Role Based Access Control




Red Hat Developer Hub offers Role-based Access Control (RBAC) functionality. RBAC can then be applied to the Ansible plug-ins content.

Assign the following roles:

- Members of the `    admin:superUsers` group can select templates in the **Create** tab of the Ansible plug-ins to create playbook and collection projects.
- Members of the `    admin:users` group can view templates in the **Create** tab of the Ansible plug-ins.


The following example adds RBAC to Red Hat Developer Hub.

```
data:
  app-config-rhdh.yaml: |
    plugins:
    ...
    permission:
      enabled: true
      rbac:
        admin:
          users:
            - name: user:default/&lt;user-scm-ida&gt;
          superUsers:
            - name: user:default/&lt;user-admin-idb&gt;
```

For more information about permission policies and managing RBAC, refer to the [Authorization](https://docs.redhat.com/en/documentation/red_hat_developer_hub/1.4/html-single/authorization/index) guide for Red Hat Developer Hub.

## 2.6. Optional configuration for Ansible plug-ins




### 2.6.1. Enabling Red Hat Developer Hub authentication




Red Hat Developer Hub (RHDH) provides integrations for multiple Source Control Management (SCM) systems. This is required by the plug-ins to create repositories.

Refer to the [Enabling authentication in Red Hat Developer Hub](https://docs.redhat.com/en/documentation/red_hat_developer_hub/1.2/html-single/administration_guide_for_red_hat_developer_hub/index#enabling-authentication) chapter of the _Administration guide for Red Hat Developer Hub_ .

### 2.6.2. Configuring Ansible plug-ins optional integrations




The Ansible plug-ins provide integrations with Ansible Automation Platform and other optional Red Hat products.

To edit your custom ConfigMap, log in to the OpenShift UI and navigate toSelect Project ( developerHubProj )→ConfigMaps→{developer-hub}-app-config-rhdh→app-config-rhdh.

#### 2.6.2.1. Configuring OpenShift Dev Spaces




When OpenShift Dev Spaces is configured for the Ansible plug-ins, users can click a link from the catalog item view in Red Hat Developer Hub and edit their provisioned Ansible Git projects using Dev Spaces.

Note
OpenShift Dev Spaces is a separate product and it is optional. The plug-ins will function without it.

It is a separate Red Hat product and is not included in the Ansible Automation Platform or Red Hat Developer Hub subscription.



If the OpenShift Dev Spaces link is not configured in the Ansible plug-ins, the **Go to OpenShift Dev Spaces dashboard** link in the **DEVELOP** section of the Ansible plug-ins landing page redirects users to the [Ansible development tools home page](https://www.redhat.com/en/technologies/management/ansible/development-tools) .

 **Prerequisites** 

- A Dev Spaces installation. Refer to the [Installing Dev Spaces](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.14/html-single/administration_guide/installing-devspaces) section of the _Red Hat OpenShift Dev Spaces Administration guide_ .


 **Procedure** 

1. Edit your custom Red Hat Developer Hub config map, for example `    app-config-rhdh` .
1. Add the following code to your Red Hat Developer Hub `    app-config-rhdh.yaml` file.
    
    
    ```
    data:      app-config-rhdh.yaml: |-        ansible:          devSpaces:            baseUrl: &gt;-              https://&lt;Your OpenShift Dev Spaces URL&gt;
    ```
    
    
1. Replace `    &lt;Your OpenShft Dev Spaces URL&gt;` with your OpenShift Dev Spaces URL.
1. In the OpenShift Developer UI, select the `    Red Hat Developer Hub` pod.
1. Open **Actions** .
1. Click **Restart rollout** .


#### 2.6.2.2. Configuring the private automation hub URL




Private automation hub provides a centralized, on-premise repository for certified Ansible collections, execution environments and any additional, vetted content provided by your organization.

If the private automation hub URL is not configured in the Ansible plug-ins, users are redirected to the [Red Hat Hybrid Cloud Console automation hub](https://console.redhat.com/ansible/automation-hub) .

Note
The private automation hub configuration is optional but recommended. The Ansible plug-ins will function without it.



 **Prerequisites:** 

- A private automation hub instance.
    
    For more information on installing private automation hub, refer to the installation guides in the [Ansible Automation Platform documentation](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5) .
    
    


 **Procedure:** 

1. Edit your custom Red Hat Developer Hub config map, for example `    app-config-rhdh` .
1. Add the following code to your Red Hat Developer Hub `    app-config-rhdh.yaml` file.
    
    
    ```
    data:      app-config-rhdh.yaml: |-        ansible:        ...          automationHub:            baseUrl: '&lt;https://MyOwnPAHUrl&gt;'        ...
    ```
    
    
1. Replace `    &lt;https://MyOwnPAHUrl/&gt;` with your private automation hub URL.
1. In the OpenShift Developer UI, select the `    Red Hat Developer Hub` pod.
1. Open **Actions** .
1. Click **Restart rollout** .


## 2.7. Full examples




### 2.7.1. Full app-config-rhdh ConfigMap example for Ansible plug-ins entries




```
kind: ConfigMap
...
metadata:
  name: app-config-rhdh
  ...
data:
  app-config-rhdh.yaml: |-
    ansible:
      creatorService:
        baseUrl: 127.0.0.1
        port: '8000'
      rhaap:
        baseUrl: '&lt;https://MyControllerUrl&gt;'
        token: '&lt;AAP Personal Access Token&gt;'
        checkSSL: &lt;true or false&gt;
        showCaseLocation:
          type: file
          target: '/tmp/aap-showcases/'
      # Optional integrations
      devSpaces:
        baseUrl: '&lt;https://MyDevSpacesURL&gt;'
      automationHub:
        baseUrl: '&lt;https://MyPrivateAutomationHubURL&gt;'

    ...
    catalog:
      locations:
        - type: url
          target: https://github.com/ansible/ansible-rhdh-templates/blob/main/all.yaml
          rules:
            - allow: [Template]
    ...
```

### 2.7.2. Full Helm chart config example for Ansible plug-ins




```
global:
  ...
  dynamic:
    ...
    plugins:
      - disabled: false
        integrity: &lt;SHA512 Integrity key for ansible-plugin-backstage-rhaap plugin&gt;
        package: 'http://plugin-registry:8080/ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz'
        pluginConfig:
          dynamicPlugins:
            frontend:
              ansible.plugin-backstage-rhaap:
                appIcons:
                  - importName: AnsibleLogo
                    name: AnsibleLogo
                dynamicRoutes:
                  - importName: AnsiblePage
                    menuItem:
                      icon: AnsibleLogo
                      text: Ansible
                    path: /ansible
      - disabled: false
        integrity: &lt;SHA512 Integrity key for ansible-plugin-scaffolder-backend-module-backstage-rhaap plugin&gt;
        package: &gt;-
          http://plugin-registry:8080/ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz
        pluginConfig:
          dynamicPlugins:
            backend:
              ansible.plugin-scaffolder-backend-module-backstage-rhaap: null
      - disabled: false
        integrity: &lt;SHA512 Integrity key for ansible-plugin-backstage-rhaap-backend plugin&gt;
        package: &gt;-
          http://plugin-registry:8080/ansible-plugin-backstage-rhaap-backend-dynamic-x.y.z.tgz
        pluginConfig:
          dynamicPlugins:
            backend:
              ansible.plugin-backstage-rhaap-backend: null
...
upstream:
  backstage:
    ...
    extraAppConfig:
      - configMapRef: app-config-rhdh
        filename: app-config-rhdh.yaml
    extraContainers:
      - command:
          - adt
          - server
        image: &gt;-
          registry.redhat.io/ansible-automation-platform-25/ansible-dev-tools-rhel8:latest
        imagePullPolicy: IfNotPresent
        name: ansible-devtools-server
        ports:
          - containerPort: 8000
...
```

# Chapter 3. Installing the Ansible plug-ins with the Operator on OpenShift Container Platform




The following procedures describe how to install Ansible plug-ins in Red Hat Developer Hub instances on Red Hat OpenShift Container Platform using the Operator.

## 3.1. Prerequisites




- Red Hat Developer Hub installed on Red Hat OpenShift Container Platform.
    
    
    - For Helm installation, follow the steps in the [Installing Red Hat Developer Hub on OpenShift Container Platform with the Helm chart](https://docs.redhat.com/en/documentation/red_hat_developer_hub/1.4/html/installing_red_hat_developer_hub_on_openshift_container_platform/index#assembly-install-rhdh-ocp-helm) section of _Installing Red Hat Developer Hub on OpenShift Container Platform_ .
    - For Operator installation, follow the steps in the [Installing Red Hat Developer Hub on OpenShift Container Platform with the Operator](https://docs.redhat.com/en/documentation/red_hat_developer_hub/1.4/html/installing_red_hat_developer_hub_on_openshift_container_platform/index#assembly-install-rhdh-ocp-operator) section of _Installing Red Hat Developer Hub on OpenShift Container Platform_ .
    
- A valid subscription to Red Hat Ansible Automation Platform.
- An OpenShift Container Platform instance with the appropriate permissions within your project to create an application.
- The Red Hat Developer Hub instance can query the automation controller API.
- Optional: To use the integrated learning paths, you must have outbound access to developers.redhat.com.


## 3.2. Recommended RHDH preconfiguration




Red Hat recommends performing the following initial configuration tasks in RHDH. However, you can install the Ansible plug-ins for Red Hat Developer Hub before completing these tasks.

-  [Setting up authentication in RHDH](https://docs.redhat.com/en/documentation/red_hat_developer_hub/1.4/html/authentication/index) 
-  [Installing and configuring RBAC in RHDH](https://docs.redhat.com/en/documentation/red_hat_developer_hub/1.4/html/authorization/index) 


Note
Red Hat provides a [repository of software templates for RHDH](https://github.com/ansible/ansible-rhdh-templates/blob/main/all.yaml) that uses the `publish:github` action. To use these software templates, you must install the required GitHub dynamic plugins.



## 3.3. Adding a sidecar container for Ansible development tools to the RHDH Operator Custom Resource




Add a sidecar container for Ansible development tools in the Developer Hub pod. To do this, you must modify the base ConfigMap for the Red Hat Developer Hub deployment.

1. In the OpenShift console, select the **Topology** view.
1. Click **More actions ⋮** on the developer-hub instance and select **Edit backstage** to open the **Backstage details** page.
1. Select the **YAML** tab.
1. In the editing pane, add a `    containers` block in the `    spec.deployment.patch.spec.template.spec` block:
    
    
    ```
    apiVersion: rhdh.redhat.com/v1alpha3    kind: Backstage    metadata:      name: developer-hub    spec:      deployment:        patch:          spec:            template:              spec:                containers:                  - command:                      - adt                      - server                    image: registry.redhat.io/ansible-automation-platform-25/ansible-dev-tools-rhel8:latest                    imagePullPolicy: always                    ports:                      - containerPort: 8000                        protocol: TCP                    terminationMessagePolicy: file
    ```
    
    
1. ClickSave.


Note
If you want to add extra environment variables to your deployment, you can add them in the `spec.application.extraEnvs` block:

```
spec:
  application:
    ...
    extraEnvs:
      envs:
        - name: &lt;env_variable_name&gt;
          value: &lt;env_variable_value&gt;
```



## 3.4. Downloading the Ansible plug-ins files




1. Download the latest `    .tar` file for the plug-ins from the [Red Hat Ansible Automation Platform Product Software downloads page](https://access.redhat.com/downloads/content/480/ver=2.5/rhel---9/2.5/x86_64/product-software) . The format of the filename is `    ansible-backstage-rhaap-bundle-x.y.z.tar.gz` . Substitute the Ansible plug-ins release version, for example `    1.0.0` , for `    x.y.z` .
1. Create a directory on your local machine to store the `    .tar` files.
    
    
    ```
    $ mkdir /path/to/&lt;ansible-backstage-plugins-local-dir-changeme&gt;
    ```
    
    
1. Set an environment variable ( `    $DYNAMIC_PLUGIN_ROOT_DIR` ) to represent the directory path.
    
    
    ```
    $ export DYNAMIC_PLUGIN_ROOT_DIR=/path/to/&lt;ansible-backstage-plugins-local-dir-changeme&gt;
    ```
    
    
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

The files with the `.integrity` file type contain the plugin SHA value. The SHA value is used during the plug-in configuration.

## 3.5. Creating a registry for the Ansible plug-ins




Set up a registry in your OpenShift cluster to host the Ansible plug-ins and make them available for installation in Red Hat Developer Hub (RHDH).

 **Procedure** 

1. Log in to your OpenShift Container Platform instance with credentials to create a new application.
1. Open your Red Hat Developer Hub OpenShift project.
    
    
    ```
    $ oc project &lt;YOUR_DEVELOPER_HUB_PROJECT&gt;
    ```
    
    
1. Run the following commands to create a plug-in registry build in the OpenShift cluster.
    
    
    ```
    $ oc new-build httpd --name=plugin-registry --binary    $ oc start-build plugin-registry --from-dir=$DYNAMIC_PLUGIN_ROOT_DIR --wait    $ oc new-app --image-stream=plugin-registry
    ```
    
    


 **Verification** 

To verify that the plugin-registry was deployed successfully, open the **Topology** view in the **Developer** perspective on the Red Hat Developer Hub application in the OpenShift Web console.


1. Click the plug-in registry to view the log.
    
    ![Developer perspective](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Installing_Ansible_plug-ins_for_Red_Hat_Developer_Hub-en-US/images/569de994c3fd61a583f4b81b85bf852e/rhdh-plugin-registry.png)
    
    
    (1) Developer hub instance
    
    (2) Plug-in registry
    
    
1. Click the terminal tab and login to the container.
1. In the terminal, run `    ls` to confirm that the `    .tar` files are in the plugin registry.
    
    
    ```
    ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz    ansible-plugin-backstage-rhaap-backend-dynamic-x.y.z.tgz    ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz
    ```
    
    The version numbers and file names can differ.
    
    


## 3.6. Installing the dynamic plug-ins




To install the dynamic plugins, add them to your ConfigMap for your RHDH plugin settings (for example, `rhaap-dynamic-plugins-config` ).

If you have not already created a ConfigMap file for your RHDH plugin settings, create one by following the procedure in the [Creating and using config maps](https://docs.redhat.com/en/documentation/openshift_container_platform/4.15/html-single/nodes/index#configmaps) section of the OpenShift Container Platform _Nodes_ guide.

The example ConfigMap used in the following procedure is called `rhaap-dynamic-plugins-config` .

 **Procedure** 

1. Select **ConfigMaps** in the navigation pane of the OpenShift console.
1. Select the `    rhaap-dynamic-plugins-config` ConfigMap from the list.
1. Select the **YAML** tab to edit the `    rhaap-dynamic-plugins-config` ConfigMap.
1. In the `    data.dynamic-plugins.yaml.plugins` block, add the three dynamic plug-ins from the plug-in registry.
    
    
    - For the `        integrity` hash values, use the `        .integrity` files in your `        $DYNAMIC_PLUGIN_ROOT_DIR` directory that correspond to each plug-in, for example use `        ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz.integrity` for the `        ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz` plug-in.
    - Replace `        x.y.z` with the correct version of the plug-ins.
        
        
        ```
        kind: ConfigMap        apiVersion: v1        metadata:         name: rhaap-dynamic-plugins-config        data:         dynamic-plugins.yaml: |           ...           plugins:             - disabled: false               package: 'http://plugin-registry:8080/ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz'               integrity: &lt;SHA512 value&gt; # Use hash in ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz.integrity               pluginConfig:                 dynamicPlugins:                   frontend:                     ansible.plugin-backstage-rhaap:                       appIcons:                         - importName: AnsibleLogo                           name: AnsibleLogo                       dynamicRoutes:                         - importName: AnsiblePage                           menuItem:                             icon: AnsibleLogo                             text: Ansible                           path: /ansible             - disabled: false               package: &gt;-                 http://plugin-registry:8080/ansible-plugin-backstage-rhaap-backend-dynamic-x.y.z.tgz               integrity: &lt;SHA512 value&gt; # Use hash in ansible-plugin-backstage-rhaap-backend-dynamic-x.y.z.tgz.integrity               pluginConfig:                 dynamicPlugins:                   backend:                     ansible.plugin-backstage-rhaap-backend: null             - disabled: false               package: &gt;-                 http://plugin-registry:8080/ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz               integrity: &lt;SHA512 value&gt; # Use hash in ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz.integrity               pluginConfig:                 dynamicPlugins:                   backend:                     ansible.plugin-scaffolder-backend-module-backstage-rhaap: null             - ...&lt;REDACTED&gt;
        ```
        
        
    
1. ClickSave.
1. To view the progress of the rolling restart:
    
    
    1. In the **Topology** view, select the deployment pod and click **View logs** .
    1. Select `        install-dynamic-plugins` from the list of containers.
    


 **Verification** 

1. In the OpenShift console, select the **Topology** view.
1. Click the **Open URL** icon on the deployment pod to open your Red Hat Developer Hub instance in a browser window.


The Ansible plug-in is present in the navigation pane, and if you select **Administration** , the installed plug-ins are listed in the **Plugins** tab.

## 3.7. Adding a custom ConfigMap




Create a Red Hat Developer Hub ConfigMap following the procedure in the [Creating and using config maps](https://docs.redhat.com/en/documentation/openshift_container_platform/4.15/html-single/nodes/index#configmaps) section of the OpenShift Container Platform _Nodes_ guide. The following examples use a custom ConfigMap named `app-config-rhdh` .

To edit your custom ConfigMap, log in to the OpenShift UI and navigate toSelect Project ( developerHubProj )→ConfigMaps→{developer-hub}-app-config→EditConfigMaps→app-config-rhdh.

## 3.8. Configuring the Ansible Dev Tools Server




The `creatorService` URL is required for the Ansible plug-ins to provision new projects using the provided software templates.

 **Procedure** 

1. Edit your custom Red Hat Developer Hub config map, `    app-config-rhdh` , that you created in [Adding a custom ConfigMap](#rhdh-add-custom-configmap_rhdh-ocp-required-installation) .
1. Add the following code to your Red Hat Developer Hub `    app-config-rhdh.yaml` file.
    
    
    ```
    kind: ConfigMap    apiVersion: v1    metadata:      name: app-config-rhdh    ...    data:      app-config-rhdh.yaml: |-        ansible:          creatorService:            baseUrl: 127.0.0.1            port: '8000'    ...
    ```
    
    


## 3.9. Configuring Ansible Automation Platform details




The Ansible plug-ins query your Ansible Automation Platform subscription status with the controller API using a token.

Note
The Ansible plug-ins continue to function regardless of the Ansible Automation Platform subscription status.



 **Procedure** 

1. Create a Personal Access Token (PAT) with “Read” scope in automation controller, following the [Applications](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/access_management_and_authentication/gw-token-based-authentication#assembly-controller-applications) section of _Access management and authentication_ .
1. Edit your custom Red Hat Developer Hub config map, for example `    app-config-rhdh` .
1. Add your Ansible Automation Platform details to `    app-config-rhdh.yaml` .
    
    
    1. Set the `        baseURL` key with your automation controller URL.
    1. Set the `        token` key with the generated token value that you created in Step 1.
    1. Set the `        checkSSL` key to `        true` or `        false` .
        
        If `        checkSSL` is set to `        true` , the Ansible plug-ins verify whether the SSL certificate is valid.
        
        
        ```
        data:          app-config-rhdh.yaml: |            ...            ansible:            ...              rhaap:                baseUrl: '&lt;https://MyControllerUrl&gt;'                token: '&lt;AAP Personal Access Token&gt;'                checkSSL: true
        ```
        
        
    


Note
You are responsible for protecting your Red Hat Developer Hub installation from external and unauthorized access. Manage the backend authentication key like any other secret. Meet strong password requirements, do not expose it in any configuration files, and only inject it into configuration files as an environment variable.



## 3.10. Adding Ansible plug-ins software templates




Red Hat Ansible provides software templates for Red Hat Developer Hub to provision new playbooks and collection projects based on Ansible best practices.

 **Procedure** 

1. Edit your custom Red Hat Developer Hub config map, for example `    app-config-rhdh` .
1. Add the following code to your Red Hat Developer Hub `    app-config-rhdh.yaml` file.


```
data:
  app-config-rhdh.yaml: |
    catalog:
      ...
      locations:
        ...
        - type: url
          target: https://github.com/ansible/ansible-rhdh-templates/blob/main/all.yaml
          rules:
            - allow: [Template]
```

For more information, refer to the [Managing templates](https://docs.redhat.com/en/documentation/red_hat_developer_hub/1.2/html-single/administration_guide_for_red_hat_developer_hub/assembly-admin-templates#assembly-admin-templates) section of the _Administration guide for Red Hat Developer Hub_ .

## 3.11. Configuring Role Based Access Control




Red Hat Developer Hub offers Role-based Access Control (RBAC) functionality. RBAC can then be applied to the Ansible plug-ins content.

Assign the following roles:

- Members of the `    admin:superUsers` group can select templates in the **Create** tab of the Ansible plug-ins to create playbook and collection projects.
- Members of the `    admin:users` group can view templates in the **Create** tab of the Ansible plug-ins.


The following example adds RBAC to Red Hat Developer Hub.

```
data:
  app-config-rhdh.yaml: |
    plugins:
    ...
    permission:
      enabled: true
      rbac:
        admin:
          users:
            - name: user:default/&lt;user-scm-ida&gt;
          superUsers:
            - name: user:default/&lt;user-admin-idb&gt;
```

For more information about permission policies and managing RBAC, refer to the [Authorization](https://docs.redhat.com/en/documentation/red_hat_developer_hub/1.4/html-single/authorization/index) guide for Red Hat Developer Hub.

## 3.12. Optional configuration for Ansible plug-ins




### 3.12.1. Enabling Red Hat Developer Hub authentication




Red Hat Developer Hub (RHDH) provides integrations for multiple Source Control Management (SCM) systems. This is required by the plug-ins to create repositories.

Refer to the [Enabling authentication in Red Hat Developer Hub](https://docs.redhat.com/en/documentation/red_hat_developer_hub/1.2/html-single/administration_guide_for_red_hat_developer_hub/index#enabling-authentication) chapter of the _Administration guide for Red Hat Developer Hub_ .

### 3.12.2. Configuring Ansible plug-ins optional integrations




The Ansible plug-ins provide integrations with Ansible Automation Platform and other optional Red Hat products.

To edit your custom ConfigMap, log in to the OpenShift UI and navigate toSelect Project ( developerHubProj )→ConfigMaps→{developer-hub}-app-config-rhdh→app-config-rhdh.

#### 3.12.2.1. Configuring OpenShift Dev Spaces




When OpenShift Dev Spaces is configured for the Ansible plug-ins, users can click a link from the catalog item view in Red Hat Developer Hub and edit their provisioned Ansible Git projects using Dev Spaces.

Note
OpenShift Dev Spaces is a separate product and it is optional. The plug-ins will function without it.

It is a separate Red Hat product and is not included in the Ansible Automation Platform or Red Hat Developer Hub subscription.



If the OpenShift Dev Spaces link is not configured in the Ansible plug-ins, the **Go to OpenShift Dev Spaces dashboard** link in the **DEVELOP** section of the Ansible plug-ins landing page redirects users to the [Ansible development tools home page](https://www.redhat.com/en/technologies/management/ansible/development-tools) .

 **Prerequisites** 

- A Dev Spaces installation. Refer to the [Installing Dev Spaces](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.14/html-single/administration_guide/installing-devspaces) section of the _Red Hat OpenShift Dev Spaces Administration guide_ .


 **Procedure** 

1. Edit your custom Red Hat Developer Hub config map, for example `    app-config-rhdh` .
1. Add the following code to your Red Hat Developer Hub `    app-config-rhdh.yaml` file.
    
    
    ```
    data:      app-config-rhdh.yaml: |-        ansible:          devSpaces:            baseUrl: &gt;-              https://&lt;Your OpenShift Dev Spaces URL&gt;
    ```
    
    
1. Replace `    &lt;Your OpenShft Dev Spaces URL&gt;` with your OpenShift Dev Spaces URL.
1. In the OpenShift Developer UI, select the `    Red Hat Developer Hub` pod.
1. Open **Actions** .
1. Click **Restart rollout** .


#### 3.12.2.2. Configuring the private automation hub URL




Private automation hub provides a centralized, on-premise repository for certified Ansible collections, execution environments and any additional, vetted content provided by your organization.

If the private automation hub URL is not configured in the Ansible plug-ins, users are redirected to the [Red Hat Hybrid Cloud Console automation hub](https://console.redhat.com/ansible/automation-hub) .

Note
The private automation hub configuration is optional but recommended. The Ansible plug-ins will function without it.



 **Prerequisites:** 

- A private automation hub instance.
    
    For more information on installing private automation hub, refer to the installation guides in the [Ansible Automation Platform documentation](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5) .
    
    


 **Procedure:** 

1. Edit your custom Red Hat Developer Hub config map, for example `    app-config-rhdh` .
1. Add the following code to your Red Hat Developer Hub `    app-config-rhdh.yaml` file.
    
    
    ```
    data:      app-config-rhdh.yaml: |-        ansible:        ...          automationHub:            baseUrl: '&lt;https://MyOwnPAHUrl&gt;'        ...
    ```
    
    
1. Replace `    &lt;https://MyOwnPAHUrl/&gt;` with your private automation hub URL.
1. In the OpenShift Developer UI, select the `    Red Hat Developer Hub` pod.
1. Open **Actions** .
1. Click **Restart rollout** .


## 3.13. Full app-config-rhdh ConfigMap example for Ansible plug-ins entries




```
kind: ConfigMap
...
metadata:
  name: app-config-rhdh
  ...
data:
  app-config-rhdh.yaml: |-
    ansible:
      creatorService:
        baseUrl: 127.0.0.1
        port: '8000'
      rhaap:
        baseUrl: '&lt;https://MyControllerUrl&gt;'
        token: '&lt;AAP Personal Access Token&gt;'
        checkSSL: &lt;true or false&gt;
        showCaseLocation:
          type: file
          target: '/tmp/aap-showcases/'
      # Optional integrations
      devSpaces:
        baseUrl: '&lt;https://MyDevSpacesURL&gt;'
      automationHub:
        baseUrl: '&lt;https://MyPrivateAutomationHubURL&gt;'

    ...
    catalog:
      locations:
        - type: url
          target: https://github.com/ansible/ansible-rhdh-templates/blob/main/all.yaml
          rules:
            - allow: [Template]
    ...
```

# Chapter 4. Ansible plug-ins subscription warning messages




The Ansible plug-ins display a subscription warning banner in the user interface in the following scenarios:

-  [Unable to connect to Ansible Automation Platform](#rhdh-warning-unable-connect-aap_rhdh-subscription-warnings) 
-  [Unable to authenticate to Ansible Automation Platform](#rhdh-warning-unable-authenticate-aap_rhdh-subscription-warnings) 
-  [Invalid Ansible Automation Platform configuration](#rhdh-warning-invalid-aap-config_rhdh-subscription-warnings) 
-  [Ansible Automation Platform subscription is out of compliance](#rhdh-warning-aap-ooc_rhdh-subscription-warnings) 
-  [Invalid Ansible Automation Platform subscription](#rhdh-warning-invalid-aap-subscription_rhdh-subscription-warnings) 


## 4.1. Unable to connect to Ansible Automation Platform




The following warning indicates that the automation controller details are not configured, or the controller instance API is unreachable to query the subscription status.

```
Unable to connect to Ansible Automation Platform
Verify that Ansible Automation Platform is reachable and correctly configured in the Ansible plug-ins.
To get help, please refer to the Ansible plug-ins installation guide.
```


<span id="remediation_steps"></span>
#### Remediation steps


1. Verify that Ansible Automation Platform is reachable and correctly configured in the `    rhaap` section of the ConfigMap.
1. Ensure the `    checkSSL` key is correctly set for your environment.
1. After correcting the configuration details, restart the Red Hat Developer Hub pod to initiate a subscription query.


## 4.2. Unable to authenticate to Ansible Automation Platform




The following warning indicates that the Ansible plug-ins were not able to authenticate with Ansible Automation Platform to query the subscription status.

```
Unable to authenticate to Ansible Automation Platform
Verify that the authentication details for Ansible Automation Platform are correctly configured in the Ansible plug-ins.
For help, please refer to the Ansible plug-ins installation guide.
```


<span id="remediation_steps_2"></span>
#### Remediation steps


1. Verify that the automation controller Personal Access Token (PAT) configured in the Ansible plug-ins is correct. For more information, refer to the [Adding tokens](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/access_management_and_authentication/gw-token-based-authentication#proc-controller-apps-create-tokens) section of _TitleCentralAuth_ .
1. After correcting the authentication details, restart the Red Hat Developer Hub pod to initiate a subscription query.


## 4.3. Invalid Ansible Automation Platform configuration




The following warning indicates that the Ansible Automation Platform configuration section is invalid or incomplete.

```
Invalid resource for Ansible Automation Platform
Verify that the resource url for Ansible Automation Platform are correctly configured in the Ansible plug-ins.
For help, please refer to the Ansible plug-ins installation guide.
```


<span id="remediation_steps_3"></span>
#### Remediation steps


1. Verify that the `    rhaap` section of the Ansible plug-ins ConfigMap is correctly configured and contains all the necessary entries. For more information, refer to [Configuring Ansible Automation Platform details](#rhdh-configure-aap-details_rhdh-ocp-required-installation) .
1. After correcting the configuration, restart the Red Hat Developer Hub pod to initiate a subscription query.


## 4.4. Ansible Automation Platform subscription is out of compliance




The following warning indicates that the Ansible plug-ins successfully retrieved the Ansible Automation Platform subscription status. However, the subscription is out of compliance.

```
Subscription non-compliant
The connected Ansible Automation Platform subscription is out of compliance.
Contact your Red Hat account team to obtain a new subscription entitlement.
Learn more about account compliance.
```


<span id="remediation_steps_4"></span>
#### Remediation steps


1. Contact your Red Hat account team to obtain a new subscription entitlement.
1. Learn more about [account compliance](https://access.redhat.com/solutions/6988859) .
1. When the subscription is in compliance, restart the Red Hat Developer Hub pod to initiate a new subscription query.


## 4.5. Invalid Ansible Automation Platform subscription




The following warning indicates that the Ansible plug-ins successfully retrieved the Ansible Automation Platform subscription status. However, the subscription type is invalid for Ansible Automation Platform.

```
Invalid subscription
The connected Ansible Automation Platform subscription is invalid.
Contact your Red Hat account team, or start an Ansible Automation Platform trial.
```


<span id="remediation_steps_5"></span>
#### Remediation steps


1. Contact your Red Hat account team to obtain a new subscription entitlement or [start an Ansible Automation Platform trial](http://red.ht/aap-rhdh-plugins-start-trial) .
1. When you have updated the subscription, restart the Red Hat Developer Hub pod to initiate a new subscription query.


# Chapter 5. Upgrading the Ansible plug-ins on a Helm installation on OpenShift Container Platform




To upgrade the Ansible plug-ins, you must update the `plugin-registry` application with the latest Ansible plug-ins files.

## 5.1. Downloading the Ansible plug-ins files




1. Download the latest `    .tar` file for the plug-ins from the [Red Hat Ansible Automation Platform Product Software downloads page](https://access.redhat.com/downloads/content/480/ver=2.5/rhel---9/2.5/x86_64/product-software) . The format of the filename is `    ansible-backstage-rhaap-bundle-x.y.z.tar.gz` . Substitute the Ansible plug-ins release version, for example `    1.0.0` , for `    x.y.z` .
1. Create a directory on your local machine to store the `    .tar` files.
    
    
    ```
    $ mkdir /path/to/&lt;ansible-backstage-plugins-local-dir-changeme&gt;
    ```
    
    
1. Set an environment variable ( `    $DYNAMIC_PLUGIN_ROOT_DIR` ) to represent the directory path.
    
    
    ```
    $ export DYNAMIC_PLUGIN_ROOT_DIR=/path/to/&lt;ansible-backstage-plugins-local-dir-changeme&gt;
    ```
    
    
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

The files with the `.integrity` file type contain the plugin SHA value. The SHA value is used during the plug-in configuration.

## 5.2. Updating the plug-in registry




Rebuild your plug-in registry application in your OpenShift cluster with the latest Ansible plug-ins files.

 **Prerequisites** 

- You have downloaded the Ansible plug-ins files.
- You have set an environment variable, for example ( `    $DYNAMIC_PLUGIN_ROOT_DIR` ), to represent the path to the local directory where you have stored the `    .tar` files.


 **Procedure** 

1. Log in to your OpenShift Container Platform instance with credentials to create a new application.
1. Open your Red Hat Developer Hub OpenShift project.
    
    
    ```
    $ oc project &lt;YOUR_DEVELOPER_HUB_PROJECT&gt;
    ```
    
    
1. Run the following commands to update your plug-in registry build in the OpenShift cluster. The commands assume that `    $DYNAMIC_PLUGIN_ROOT_DIR` represents the directory for your `    .tar` files. Replace this in the command if you have chosen a different environment variable name.
    
    
    ```
    $ oc start-build plugin-registry --from-dir=$DYNAMIC_PLUGIN_ROOT_DIR --wait
    ```
    
    
1. When the registry has started, the output displays the following message:
    
    
    ```
    Uploading directory "/path/to/dynamic_plugin_root" as binary input for the build …    Uploading finished    build.build.openshift.io/plugin-registry-1 started
    ```
    
    


 **Verification** 

Verify that the `plugin-registry` has been updated.


1. In the OpenShift UI, click **Topology** .
1. Click the **redhat-developer-hub** icon to view the pods for the plug-in registry.
1. Click **View logs** for the plug-in registry pod.
1. Open the **Terminal** tab and run `    ls` to view the `    .tar` files in the `    plug-in registry` .
1. Verify that the new `    .tar` file has been uploaded.


## 5.3. Updating the Ansible plug-ins version numbers for a Helm installation




 **Procedure** 

1. Log in to your OpenShift Container Platform instance.
1. In the OpenShift Developer UI, navigate toHelm→developer-hub→Actions→Upgrade→Yaml view.
1. Update the Ansible plug-ins version numbers and associated `    .integrity` file values.
    
    
    ```
    ...    global:    ...        plugins:          - disabled: false            integrity: &lt;SHA512 value&gt;            package: 'http://plugin-registry:8080/ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz'            pluginConfig:              dynamicPlugins:                frontend:                  ansible.plugin-backstage-rhaap:                    appIcons:                      - importName: AnsibleLogo                        name: AnsibleLogo                    dynamicRoutes:                      - importName: AnsiblePage                        menuItem:                          icon: AnsibleLogo                          text: Ansible                        path: /ansible          - disabled: false            integrity: &lt;SHA512 value&gt;            package: &gt;-              http://plugin-registry:8080/ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz            pluginConfig:              dynamicPlugins:                backend:                  ansible.plugin-scaffolder-backend-module-backstage-rhaap: null          - disabled: false            integrity: &lt;SHA512 value&gt;            package: &gt;-              http://plugin-registry:8080/ansible-plugin-backstage-rhaap-backend-dynamic-x.y.z.tgz            pluginConfig:              dynamicPlugins:                backend:                  ansible.plugin-backstage-rhaap-backend: null
    ```
    
    
1. ClickUpgrade.
    
    The developer hub pods restart and the plug-ins are installed.
    
    


 **Verification** 

1. In the OpenShift UI, click **Topology** .
1. Make sure that the Red Hat Developer Hub instance is available.


# Chapter 6. Upgrading the Ansible plug-ins on an Operator installation on OpenShift Container Platform




To upgrade the Ansible plug-ins, you must update the `plugin-registry` application with the latest Ansible plug-ins files.

## 6.1. Downloading the Ansible plug-ins files




1. Download the latest `    .tar` file for the plug-ins from the [Red Hat Ansible Automation Platform Product Software downloads page](https://access.redhat.com/downloads/content/480/ver=2.5/rhel---9/2.5/x86_64/product-software) . The format of the filename is `    ansible-backstage-rhaap-bundle-x.y.z.tar.gz` . Substitute the Ansible plug-ins release version, for example `    1.0.0` , for `    x.y.z` .
1. Create a directory on your local machine to store the `    .tar` files.
    
    
    ```
    $ mkdir /path/to/&lt;ansible-backstage-plugins-local-dir-changeme&gt;
    ```
    
    
1. Set an environment variable ( `    $DYNAMIC_PLUGIN_ROOT_DIR` ) to represent the directory path.
    
    
    ```
    $ export DYNAMIC_PLUGIN_ROOT_DIR=/path/to/&lt;ansible-backstage-plugins-local-dir-changeme&gt;
    ```
    
    
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

The files with the `.integrity` file type contain the plugin SHA value. The SHA value is used during the plug-in configuration.

## 6.2. Updating the plug-in registry




Rebuild your plug-in registry application in your OpenShift cluster with the latest Ansible plug-ins files.

 **Prerequisites** 

- You have downloaded the Ansible plug-ins files.
- You have set an environment variable, for example ( `    $DYNAMIC_PLUGIN_ROOT_DIR` ), to represent the path to the local directory where you have stored the `    .tar` files.


 **Procedure** 

1. Log in to your OpenShift Container Platform instance with credentials to create a new application.
1. Open your Red Hat Developer Hub OpenShift project.
    
    
    ```
    $ oc project &lt;YOUR_DEVELOPER_HUB_PROJECT&gt;
    ```
    
    
1. Run the following commands to update your plug-in registry build in the OpenShift cluster. The commands assume that `    $DYNAMIC_PLUGIN_ROOT_DIR` represents the directory for your `    .tar` files. Replace this in the command if you have chosen a different environment variable name.
    
    
    ```
    $ oc start-build plugin-registry --from-dir=$DYNAMIC_PLUGIN_ROOT_DIR --wait
    ```
    
    
1. When the registry has started, the output displays the following message:
    
    
    ```
    Uploading directory "/path/to/dynamic_plugin_root" as binary input for the build …    Uploading finished    build.build.openshift.io/plugin-registry-1 started
    ```
    
    


 **Verification** 

Verify that the `plugin-registry` has been updated.


1. In the OpenShift UI, click **Topology** .
1. Click the **redhat-developer-hub** icon to view the pods for the plug-in registry.
1. Click **View logs** for the plug-in registry pod.
1. Open the **Terminal** tab and run `    ls` to view the `    .tar` files in the `    plug-in registry` .
1. Verify that the new `    .tar` file has been uploaded.


## 6.3. Updating the Ansible plug-ins version numbers for an Operator installation




 **Procedure** 

1. Log in to your OpenShift Container Platform instance.
1. In the OpenShift UI, open the ConfigMap where you added the Ansible plug-ins during installation. This example uses a ConfigMap file called `    rhaap-dynamic-plugins-config` .
1. Update `    x.y.z` with the version numbers for the updated Ansible plug-ins.
1. Update the integrity values for each plug-in with the `    .integrity` value from the corresponding extracted Ansible plug-ins `    .tar` file.
    
    
    ```
    kind: ConfigMap    apiVersion: v1    metadata:     name: rhaap-dynamic-plugins-config    data:     dynamic-plugins.yaml: |       ...       plugins: # Update the Ansible plug-in entries below with the updated plugin versions         - disabled: false           package: 'http://plugin-registry:8080/ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz'           integrity: &lt;SHA512 value&gt; # Use hash in ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz.integrity    	 ...         - disabled: false           package: &gt;-             http://plugin-registry:8080/ansible-plugin-backstage-rhaap-backend-dynamic-x.y.z.tgz           integrity: &lt;SHA512 value&gt; # Use hash in ansible-plugin-backstage-rhaap-backend-dynamic-x.y.z.tgz.integrity           ...         - disabled: false           package: &gt;-             http://plugin-registry:8080/ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz           integrity: &lt;SHA512 value&gt; # Use hash in ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz.integrity    	 ...
    ```
    
    
1. ClickSave.
    
    The developer hub pods restart and the plug-ins are installed.
    
    


 **Verification** 

1. In the OpenShift UI, click **Topology** .
1. Make sure that the Red Hat Developer Hub instance is available.


# Chapter 7. Uninstalling the Ansible plug-ins from a Helm installation on OpenShift Container Platform




To uninstall the Ansible plug-ins, you must remove any software templates that use the `ansible:content:create` action from Red Hat Developer Hub, and remove the plug-ins configuration from the Helm chart in OpenShift.

## 7.1. Uninstalling a Helm chart installation




 **Procedure** 

1. In Red Hat Developer Hub, remove any software templates that use the `    ansible:content:create` action.
1. In the OpenShift Developer UI, navigate toHelm→developer-hub→Actions→Upgrade→Yaml view.
1. Remove the Ansible plug-ins configuration under the `    plugins` section.
    
    
    ```
    ...    global:    ...        plugins:          - disabled: false            integrity: &lt;SHA512 value&gt;            package: 'http://plugin-registry:8080/ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz'            pluginConfig:              dynamicPlugins:                frontend:                  ansible.plugin-backstage-rhaap:                    appIcons:                      - importName: AnsibleLogo                        name: AnsibleLogo                    dynamicRoutes:                      - importName: AnsiblePage                        menuItem:                          icon: AnsibleLogo                          text: Ansible                        path: /ansible          - disabled: false            integrity: &lt;SHA512 value&gt;            package: &gt;-              http://plugin-registry:8080/ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz            pluginConfig:              dynamicPlugins:                backend:                  ansible.plugin-scaffolder-backend-module-backstage-rhaap: null          - disabled: false            integrity: &lt;SHA512 value&gt;            package: &gt;-              http://plugin-registry:8080/ansible-plugin-backstage-rhaap-backend-dynamic-x.y.z.tgz            pluginConfig:              dynamicPlugins:                backend:                  ansible.plugin-backstage-rhaap-backend: null
    ```
    
    
1. Remove the `    extraContainers` section.
    
    
    ```
    upstream:      backstage: |        ...        extraContainers:          - command:              - adt              - server            image: &gt;-              registry.redhat.io/ansible-automation-platform-25/ansible-dev-tools-rhel8:latest            imagePullPolicy: IfNotPresent            name: ansible-devtools-server            ports:              - containerPort: 8000        image:          pullPolicy: Always          pullSecrets:            - ...            - rhdh-secret-registry        ...
    ```
    
    
1. ClickUpgrade.
1. Edit your custom Red Hat Developer Hub config map, for example `    app-config-rhdh` .
1. Remove the `    ansible` section.
    
    
    ```
    data:      app-config-rhdh.yaml: |        ...        ansible:          analytics:            enabled: true          devSpaces:            baseUrl: '&lt;https://MyOwnDevSpacesUrl/&gt;'          creatorService:            baseUrl: '127.0.0.1'            port: '8000'          rhaap:            baseUrl: '&lt;https://MyAapSubcriptionUrl&gt;'            token: '&lt;TopSecretAAPToken&gt;'            checkSSL: true          automationHub:            baseUrl: '&lt;https://MyOwnPAHUrl/&gt;'
    ```
    
    
1. Restart the Red Hat Developer Hub deployment.
1. Remove the `    plugin-registry` OpenShift application.
    
    
    ```
    oc delete all -l app=plugin-registry
    ```
    
    


# Chapter 8. Uninstalling an Operator installation on OpenShift Container Platform




To delete the dynamic plug-ins from your installation, you must edit the ConfigMaps that reference Ansible.

The deployment auto reloads when the ConfigMaps are updated. You do not need to reload the deployment manually.

## 8.1. Removing the Ansible plug-ins from the ConfigMap




 **Procedure** 

1. Open the custom ConfigMap where you referenced the Ansible plug-ins. For this example, the ConfigMap name is `    rhaap-dynamic-plugins-config` .
1. Locate the dynamic plug-ins in the `    plugins:` block.
    
    
    - To disable the plug-ins, update the `        disabled` attribute to `        true` for the three plug-ins.
    - To delete the plug-ins, delete the lines that reference the plug-ins from the `        plugins:` block:
        
        
        ```
        kind: ConfigMap        apiVersion: v1        metadata:         name: rhaap-dynamic-plugins-config        data:         dynamic-plugins.yaml: |           ...           plugins: # Remove the Ansible plug-ins entries below the ‘plugins’ YAML key             - disabled: false               package: 'http://plugin-registry:8080/ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz'               integrity: &lt;SHA512 value&gt;        	 ...             - disabled: false               package: &gt;-                 http://plugin-registry:8080/ansible-plugin-backstage-rhaap-backend-dynamic-x.y.z.tgz               integrity: &lt;SHA512 value&gt;               ...             - disabled: false               package: &gt;-                 http://plugin-registry:8080/ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz               integrity: &lt;SHA512 value&gt;        	 ...
        ```
        
        
    
1. ClickSave.


## 8.2. Removing Ansible Automation Platform and Dev Spaces from the custom Red Hat Developer Hub ConfigMap




 **Procedure** 

1. Open the custom Red Hat Developer Hub ConfigMap where you added configuration for the templates and for connecting to Ansible Automation Platform and Dev Spaces. In this example, the Red Hat Developer Hub ConfigMap name is `    app-config-rhdh` .
    
    
    ```
    kind: ConfigMap    apiVersion: v1    metadata:     name: rhdh-app-config    data:     app-config-custom.yaml: |       ...       catalog:         ...         locations: # Remove the YAML entry below the 'locations' YAML key           - type: url             target: https://github.com/ansible/ansible-rhdh-templates/blob/main/all.yaml             rules:               - allow: [Template]         ...       # Remove the entire 'ansible' YAML key and all sub-entries       ansible:         devSpaces:           baseUrl: '&lt;https://YOUR_DEV_SPACES_URL&gt;'         creatorService:           baseUrl: '127.0.0.1'           port: '8000'         rhaap:           baseUrl: '&lt;https://YOUR_AAP_URL&gt;'           token: &lt;REDACTED&gt;           checkSSL: false
    ```
    
    
1. Remove the `    url` in the `    locations:` block to delete the templates from the RHDH instance.
1. Remove the `    ansible:` block to delete the Ansible-specific configuration.
1. ClickSave.


## 8.3. Uninstalling the sidecar container




To remove the sidecar container for Ansible development tools from the developer-hub pod, you must modify the base ConfigMap for the Red Hat Developer Hub deployment.

 **Procedure** 

1. In the OpenShift console, select the **Topology** view.
1. Click **More actions ⋮** on the developer-hub instance and select **Edit backstage** to edit the base ConfigMap.
1. Select the **YAML** tab.
1. In the editing pane, remove the `    containers` block for the sidecar container from the `    spec.deployment.patch.spec.template.spec` block:
    
    
    ```
    ...    spec:      deployment:        patch:          spec:            template:              spec:                containers:                  - command:                      - adt                      - server                    image: ghcr.io/ansible/community-ansible-dev-tools:latest                    imagePullPolicy: always                    ports:                      - containerPort: 8000                        protocol: TCP                    terminationMessagePolicy: file
    ```
    
    
1. ClickSave.


# Chapter 9. Red Hat Developer Hub data telemetry capturing




Red Hat Developer Hub (RHDH) sends telemetry data to Red Hat using the `backstage-plugin-analytics-provider-segment` plug-in, which is enabled by default. This includes telemetry data from the Ansible plug-ins.

Red Hat collects and analyzes the following data to improve your experience with Red Hat Developer Hub:

- Events of page visits and clicks on links or buttons.
- System-related information, for example, locale, timezone, user agent including browser and OS details.
- Page-related information, for example, title, category, extension name, URL, path, referrer, and search parameters.
- Anonymized IP addresses, recorded as 0.0.0.0.
- Anonymized username hashes, which are unique identifiers used solely to identify the number of unique users of the RHDH application.
- Feedback and sentiment provided in the Ansible plug-ins feedback form.


With Red Hat Developer Hub, you can disable or customize the telemetry data collection feature. For more information, refer to the [Telemetry data collection and analysis](https://docs.redhat.com/en/documentation/red_hat_developer_hub/1.4/html/telemetry_data_collection_and_analysis/index) guide in the Red Hat Developer Hub documentation.


<span id="idm139651272926544"></span>
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





