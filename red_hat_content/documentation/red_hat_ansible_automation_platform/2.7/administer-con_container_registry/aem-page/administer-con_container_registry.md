+++
title = "Manage containers in your private automation hub - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-con_container_registry"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-con_container_registry/", "Manage containers in your private automation hub"]]
category = "Administer"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/administer-con_container_registry/aem-page/administer-con_container_registry.html"
last_crumb = "Manage containers in your private automation hub"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Manage containers in your private automation hub"
oversized = "false"
page_slug = "administer-con_container_registry"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/administer-con_container_registry"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/administer-con_container_registry/toc/toc.json"
type = "aem-page"
+++

# Manage containers in your private automation hub

Private automation hub functions as an internal container registry for your organization. It allows you to store, manage, and govern the container images, or automation execution environments, that your teams use to run automation.

Private automation hub functions as an internal container registry for your organization. It allows you to store, manage, and govern the container images, or automation execution environments, that your teams use to run automation.

To effectively manage these containers, first learn the difference between the two types of registries in your workflow:

- External registries (the source): Public or third-party registries where you source your initial images. Common examples include the Red Hat Ecosystem Catalog (registry.redhat.io) or Quay.io. You can pull images from these registries to your local environment.
- Private automation hub registry, or your remote registry (the destination): Your internal, secure registry hosted on private automation hub. You push your curated and approved images here. Your Ansible Automation Platform infrastructure then pulls these images from private automation hub to execute jobs.

## Populate your private automation hub container registry

The automation hub remote registry is used for storing and managing automation execution environments.

When you have built or sourced an execution environment, you can push that execution environment to the registry portion of private automation hub to create a container repository. Then, you can grant your team access to the container repository, and customize the repository with a README, relevant links and other information for your team's use.

The workflow is as follows:

1.      Pull an execution environment from an external registry (like registry.redhat.io) to your local machine.

2.      Tag the image locally for your private automation hub registry.

3.      Push the image to your private automation hub.

4.      Configure access permissions and documentation (such as READMEs) within private automation hub so your teams can use the image.

Important:

As of **April 1st, 2025**, `quay.io` is adding three additional endpoints. As a result, you must adjust the allow/block lists within your firewall systems lists to include the following endpoints:

-  `cdn04.quay.io`
-  `cdn05.quay.io`
-  `cdn06.quay.io`


To avoid problems pulling container images, customers must allow outbound TCP connections (ports 80 and 443) to the following hostnames:

-  `cdn.quay.io`
-  `cdn01.quay.io`
-  `cdn02.quay.io`
-  `cdn03.quay.io`
-  `cdn04.quay.io`
-  `cdn05.quay.io`
-  `cdn06.quay.io`


This change should be made to any firewall configuration that specifically enables outbound connections to `registry.redhat.io` or `registry.access.redhat.com`.

Use the hostnames instead of IP addresses when configuring firewall rules.

After making this change, you can continue to pull images from `registry.redhat.io` or `registry.access.redhat.com`. You do not require a `quay.io` login, or need to interact with the `quay.io` registry directly in any way to continue pulling Red Hat container images.

## Pull execution environments for use in automation hub

Before you can push execution environments to your private automation hub, you must first pull them from an existing registry and tag them for use.

### Before you begin

- You have permissions to pull automation execution environments from `registry.redhat.io`.

### About this task

The following example details how to pull an execution environment from the Red Hat Ecosystem Catalog (`registry.redhat.io`).

### Procedure

1.  Log in to Podman with your `registry.redhat.io` credentials:
  

```
$ podman login registry.redhat.io
```

2.  Pull an execution environment:
  

```
$ podman pull registry.redhat.io/<ee_name>:<tag>
```

### Results

To verify that the execution environment you pulled is contained in the list, take these steps:

1. List the images in local storage:

```
$ podman images
```

2. Check the execution environment name, and verify that the tag is correct.

## Tag container images

Tag automation execution environments to add an additional name to automation execution environments stored in your automation hub container repository. If no tag is added to an automation execution environment, automation hub defaults to `latest` for the name.

### Before you begin

- You have **change automation execution environment tags** permissions.

### Procedure

1.  From the navigation panel, select Automation Content> (and then)Execution Environments.
2.  Select your automation execution environments.
3.  Click the **Images** tab.
4.  Click the More Actions icon **⋮**, and click Manage tags.
5.  Add a new tag in the text field and click Add.
6.  Optional: Remove **current tags** by clicking x on any of the tags for that image.

### Results

- Click the **Activity** tab and review the latest changes.

## Pull and sync images from automation hub to your local system

Pull Ansible Automation Platform execution environments from the automation hub registry to your local machine. Use the provided `podman pull` command for the `latest` version in the repository, or specify a tag to copy a specific execution environment.

## Pull an image

Use the user interface to pull an execution environment from your private automation hub remote registry to make a copy to your local machine.

### Before you begin

- You must have permission to view and pull from a private container repository.
- If you are pulling automation execution environments from a password or token-protected registry, [create a credential](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-manage_execution_environments_in_private_automation_hub#GUID-c616972e-1012-4d50-a64b-dc38f0d5105b "When you set up your container repository, you can add a description, include a README, add teams that can access the repository, and tag automation execution environments.") first.

### Procedure

1.  From the navigation panel, select Automation Content> (and then)Execution Environments.
2.  Select your execution environment.
3.  In the **Pull this image** entry, click Copy to clipboard.
4.  Paste and run the command in your terminal.

### Results

- Run `podman images` to view images on your local machine.

## Sync images from a container registry

You can pull automation execution environments from the private automation hub remote registry to sync an image to your local machine. To sync an execution environment from a remote registry, you must first configure a remote registry.

### Before you begin

You must have permission to view and pull from a private container repository.

### Procedure

1.  From the navigation panel, select Automation Content> (and then)Execution Environments.
2.  Add `<https://registry.redhat.io>` to the registry.
3.  Add any required credentials to authenticate. Note:
      Some remote registries are aggressive with rate limiting. Set a rate limit under **Advanced Options**.

4.  From the navigation panel, select Automation Content> (and then)Execution Environments.
5.  Click Create execution environment in the page header.
6.  Select the registry you want to pull from. The **Name** field displays the name of the automation execution environments displayed on your local registry. Note:
      The **Upstream name** field is the name of the image on the remote server. For example, if the upstream name is set to "alpine" and the **Name** field is "local/alpine", the alpine image is downloaded from the remote and renamed to "local/alpine".

7.  Set a list of tags to include or exclude. Note that syncing automation execution environments with a large number of tags is time consuming and uses a lot of disk space.

## Create a credential

To pull automation execution environments images from a password or token-protected registry, you must create a credential.

### About this task

In earlier versions of Ansible Automation Platform, you were required to deploy a registry to store execution environment images. On Ansible Automation Platform 2.0 and later, the system operates as if you already have a remote registry up and running. To store execution environment images, add the credentials of only your selected remote registries.

### Procedure

1.  Log in to Ansible Automation Platform.
2.  From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Credentials.
3.  Click Create credential to create a new credential.
4.  Enter an authorization **Name**, **Description**, and **Organization**.
5.  In the **Credential Type** drop-down, select **Container Registry**.
6.  Enter the **Authentication URL**. This is the remote registry address.
7.  Enter the **Username** and **Password or Token** required to log in to the remote registry.
8.  Optional: To enable SSL verification, select **Verify SSL**.
9.  Click Create credential.

## Remote registry team permissions

Configure team access to container repositories in private automation hub to control who can access and manage execution environments.

New teams do not have any assigned permissions by default. You must add permissions when first creating a team or edit an existing team to add or remove permissions.

The following table lists permissions you can grant to teams to ensure they have the correct level of access and privileges to your remote registries.

*Table 1. Team permissions for managing containers in private automation hub*

| Permission name                            | Description                                                          |
| ------------------------------------------ | -------------------------------------------------------------------- |
| <br>Create new containers                  | <br>Users can create new containers                                  |
| <br>Change container namespace permissions | <br>Users can change permissions on the container repository         |
| <br>Change container                       | <br>Users can change information on a container                      |
| <br>Change execution environment tags      | <br>Users can modify execution environment tags                      |
| <br>Push to existing container             | <br>Users can push an execution environment to an existing container |

## Add a README to your container repository

Add a README to your container repository to provide instructions to your users on how to work with the container. Automation hub container repositories support Markdown for creating a README. By default, the README is empty.

### Before you begin

- You have permissions to change containers.

### Procedure

1.  Log in to Ansible Automation Platform.
2.  From the navigation panel, select Automation Content> (and then)Execution Environments.
3.  Select your execution environment.
4.  On the **Detail** tab, click Add.
5.  In the **Raw Markdown** text field, enter your README text in Markdown.
6.  Click Save when you are finished.

### What to do next

After you add a README, you can edit it at any time by clicking Edit and repeating steps 4 and 5.
