# Set up a project for Ansible automation portal in OpenShift

You must set up a project in OpenShift Container Platform for Ansible automation portal. You can create the project from a terminal using the `oc` command, or in the OpenShift Container Platform web console.

## Set up an OpenShift project using the web console

You can use the OpenShift Container Platform web console to create a project in your cluster for Ansible automation portal.

### Procedure

1.  In a browser, log in to the OpenShift Container Platform web console.
2.  Create a project based on your current perspective:

- From the Developer perspective: select Project then Create Project.
- From the Administrator perspective: select Home> (and then)Project> (and then)Create Project.

3.  In the Create Project dialog box, enter a unique name in the Name field.

- Lowercase alphanumeric characters (`a-z`, `0-9`) and the hyphen character (`-`) are permitted for project names.
- The underscore (`_`) character is not permitted.
- The maximum length for project names is 63 characters.

4. **Optional:** Add a display name and description for your project.
5.  Click Create to create the project.

## Set up an OpenShift project using the CLI

You can run commands from your terminal to create a project in your cluster for Ansible automation portal.

### Before you begin

- You have the login details for your OpenShift cluster.
- You have installed the `oc` CLI tool.

### Procedure

1.  In a terminal, log in to OpenShift Container Platform using your credentials:


```
$ oc login <OpenShift_API_URL> -u <username>
```
The following example shows the output for a successful login:

```
$ oc login https://api.<my_cluster>.com:6443 -u kubeadmin
WARNING: Using insecure TLS client config. Setting this option is not supported!

Console URL: https://api.<my_cluster>.com:6443/console
Authentication required for https://api.<my_cluster>.com:6443 (openshift)
Username: kubeadmin
Password:
Login successful.

You have access to 22 projects, the list has been suppressed. You can list all projects with 'oc projects'

Using project "default".
```

2.  Create a new project. Use a unique project name.


```
$ oc new-project <self-service-project-name>
```
- Lowercase alphanumeric characters (`a-z`, `0-9`) and the hyphen character (`-`) are permitted for project names.
- The underscore (`_`) character is not permitted.
- The maximum length for project names is 63 characters.
Example:

```
$ oc new-project my-project

Now using project "my-project" on server "https://openshift.example.com:6443".
```

3.  Open your new project:


```
$ oc project <self-service-project-name>
```
