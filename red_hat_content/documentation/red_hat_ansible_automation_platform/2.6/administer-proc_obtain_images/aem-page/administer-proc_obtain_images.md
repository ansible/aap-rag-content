+++
title = "Pull execution environments for use in automation hub - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-proc_obtain_images"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-define__create__and_build_execution_environments/", "Define, create, and build execution environments"]]
category = "Administer"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/administer-proc_obtain_images/aem-page/administer-proc_obtain_images.html"
last_crumb = "Pull execution environments for use in automation hub"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Pull execution environments for use in automation hub"
oversized = "false"
page_slug = "administer-proc_obtain_images"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/administer-proc_obtain_images"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/administer-proc_obtain_images/toc/toc.json"
type = "aem-page"
+++

# Pull execution environments for use in automation hub

Before you can push execution environments to your private automation hub, you must first pull them from an existing registry and tag them for use.

## Before you begin

- You have permissions to pull automation execution environments from `registry.redhat.io`.

## About this task

The following example details how to pull an execution environment from the Red Hat Ecosystem Catalog (`registry.redhat.io`).

## Procedure

1.  Log in to Podman with your `registry.redhat.io` credentials:
  

```
$ podman login registry.redhat.io
```

2.  Pull an execution environment:
  

```
$ podman pull registry.redhat.io/<ee_name>:<tag>
```

## Results

To verify that the execution environment you pulled is contained in the list, take these steps:

1. List the images in local storage:

```
$ podman images
```

2. Check the execution environment name, and verify that the tag is correct.

## Tag execution environments

After you pull execution environments from a registry, tag them for use in your private automation hub remote registry.

### Before you begin

- You have pulled an execution environment from an external registry.
- You have the FQDN or IP address of the automation hub instance.

### Procedure

 Tag a local execution environment with the automation hub container repository:

```
$ podman tag registry.redhat.io/<ee_name>:<tag> <automation_hub_hostname>/<ee_name>
```

### Results

1. List the images in local storage:

```
$ podman images
```

2. Verify that the execution environment you tagged with your automation hub information is contained in the list.

## Push an execution environment to private automation hub

You can push tagged execution environments to private automation hub to create new containers and populate the remote registry.

### Before you begin

- You have permissions to create new containers.
- You have the FQDN or IP address of the Ansible Automation Platform instance.

### Procedure

1.  Log in to Podman using your Ansible Automation Platform location and credentials:
  

```
$ podman login -u=<username> -p=<password> <aap_url>
```
  Warning:
      Let Podman prompt you for your password when you log in. Entering your password at the same time as your username can expose your password to the shell history.

2.  Push your execution environment to your automation hub remote registry:
  

```
$ podman push <automation_hub_url>/<ee_name>
```

### Results

1. Log in to Ansible Automation Platform.
2. Navigate to Automation Content> (and then)Execution Environments.
3. Locate the container in the container repository list.

The `push` operation re-compresses image layers during the upload, which is not guaranteed to be reproducible and is client-implementation dependent. This may lead to image-layer digest changes and a failed push operation, resulting in `Error: Copying this image requires changing layer representation, which is not possible (image is signed or the destination specifies a digest)`.

## Pull and sync images from automation hub to your local system

Pull Ansible Automation Platform execution environments from the automation hub registry to your local machine. Use the provided `podman pull` command for the `latest` version in the repository, or specify a tag to copy a specific execution environment.

### Pull an image

Use the user interface to pull an execution environment from your private automation hub remote registry to make a copy to your local machine.

#### Before you begin

- You must have permission to view and pull from a private container repository.
- If you are pulling automation execution environments from a password or token-protected registry, [create a credential](/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-manage_execution_environments_in_private_automation_hub#GUID-c616972e-1012-4d50-a64b-dc38f0d5105b "When you set up your container repository, you can add a description, include a README, add teams that can access the repository, and tag automation execution environments.") first.

#### Procedure

1.  From the navigation panel, select Automation Content> (and then)Execution Environments.
2.  Select your execution environment.
3.  In the **Pull this image** entry, click Copy to clipboard.
4.  Paste and run the command in your terminal.

#### Results

- Run `podman images` to view images on your local machine.

### Sync images from a container registry

You can pull automation execution environments from the private automation hub remote registry to sync an image to your local machine. To sync an execution environment from a remote registry, you must first configure a remote registry.

#### Before you begin

You must have permission to view and pull from a private container repository.

#### Procedure

1.  From the navigation panel, select Automation Content> (and then)Execution Environments.
2.  Add `<https://registry.redhat.io>` to the registry.
3.  Add any required credentials to authenticate. Note:
      Some remote registries are aggressive with rate limiting. Set a rate limit under **Advanced Options**.

4.  From the navigation panel, select Automation Content> (and then)Execution Environments.
5.  Click Create execution environment in the page header.
6.  Select the registry you want to pull from. The **Name** field displays the name of the automation execution environments displayed on your local registry. Note:
      The **Upstream name** field is the name of the image on the remote server. For example, if the upstream name is set to "alpine" and the **Name** field is "local/alpine", the alpine image is downloaded from the remote and renamed to "local/alpine".

7.  Set a list of tags to include or exclude. Note that syncing automation execution environments with a large number of tags is time consuming and uses a lot of disk space.

### Automation execution environments precedence

Identify and control the exact automation execution environment applied to your jobs by tracing the precedence hierarchy, ensuring you can troubleshoot environment mismatches or configure accurate defaults across your templates, projects, and organizations.

Project updates always use the control plane automation execution environments by default.

However, jobs use the first available automation execution environments as follows:

1. The `execution_environment` defined on the template (job template or inventory source) that created the job.
2. The `execution_environment` defined on the project that the job uses.
3. The `execution_environment` defined on the organization of the job.
4. The `execution_environment` defined on the organization of the inventory the job uses.
5. The current Global default execution environment setting configurable at `api/v2/settings/system/`
6. Any image from the `GLOBAL_JOB_EXECUTION_ENVIRONMENTS` setting.
7. Any other global execution environment. Note:
      Where an `execution_environment` is not available, the `Default execution environment` can be used. However, you must select this, as the system does not automatically provide a default environment.

    If more than one execution environment fits a criteria (applies for 6 and 7), the most recently created one is used.

When the "Default Execution Environment" is not used for a job, double-check the following:

1. Whether a different execution environment has been defined for the template, project, or organization of the job.

2. If the **Global default execution environment** in Settings> (and then)Automation execution> (and then)System specifies a different execution environment. Note:
  This setting is not configured by default.

3. Check the order of the `GLOBAL_JOB_EXECUTION_ENVIRONMENTS` in `/etc/tower/conf.d/execution_environments.py`. `Default Execution Environment` should be the first item in the array.

4. Check the order of the execution environments defined in the database by running the following command as root on the Ansible Controller node to output the `main_executionenvironment` table:

```
# echo "select id, name, created from main_executionenvironment where organization_id is null and managed = False order by created desc;" | awx-manage dbshell
```
     To ensure that the Default Execution Environment is used regardless of the `GLOBAL_JOB_EXECUTION_ENVIRONMENTS` setting and database order, set the Global default execution environment in Settings> (and then)Automation execution> (and then)System to Default Execution Environment.
