+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/get_started-con_gs_execution_env"
title = "Create automation runtimes with execution and decision environments - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/get_started-assembly_gs_auto_dev/", "Get started as an automation developer"]]
category = "Get started"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/get_started-con_gs_execution_env/aem-page/get_started-con_gs_execution_env.html"
last_crumb = "Create automation runtimes with execution and decision environments"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Create automation runtimes with execution and decision environments"
oversized = "false"
page_slug = "get_started-con_gs_execution_env"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/get_started-con_gs_execution_env"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/get_started-con_gs_execution_env/toc/toc.json"
type = "aem-page"
+++

# Create automation runtimes with execution and decision environments

All automation in Red Hat Ansible Automation Platform runs on container images called automation execution environments.

Automation execution environments are consistent and shareable container images that serve as Ansible control nodes. Automation execution environments reduce the challenge of sharing Ansible content that has external dependencies.

If automation content is similar to a script that a developer has written, an automation execution environment is like a replica of that developer’s environment, thereby enabling you to reproduce and scale that automation content. In this way, execution environments make it easier for you to implement automation in a range of environments.

Automation execution environments contain:

- Ansible Core
- Ansible Runner
- Ansible Collections
- Python libraries
- System dependencies
- Custom user needs


You can either use the default base execution environment included in your Ansible Automation Platform subscription, or you can define and create an automation execution environment using Ansible Builder.

## Use the base automation execution environment

Ansible Automation Platform provides access to some base automation execution environments. You can use a base execution environment as a starting point for creating a customized execution environment.

### Before you begin

- You have a valid Red Hat Ansible Automation Platform subscription.

### About this task

Ansible Automation Platform includes the following execution environments:

- `Minimal` - Includes the latest Ansible-core 2.15 release along with Ansible Runner, but does not include collections or other content
- `EE Supported` - Minimal, plus all Red Hat-supported collections and dependencies


Base images included with Ansible Automation Platform are hosted on the Red Hat Ecosystem Catalog (`registry.redhat.io`).

### Procedure

1.  Log in to `registry.redhat.io`.

```bash
$ podman login registry.redhat.io
```

2.  Pull the base images from the registry:
  

```bash
$ podman pull registry.redhat.io/aap/<image name>
```

## Add an execution environment to a job template

After you have built an execution environment, use it to run jobs. To do so, first associate the execution environment with a job template.

### Before you begin

- An execution environment created using `ansible-builder` as described in [Define, create, and build execution environments](/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-define__create__and_build_execution_environments "Run automation consistently across nodes with execution environments, which are container images that contain everything you need to run your automation.").
- Organization administrator privileges (if the execution environment is associated with an organization).
- A credential with a username, host, and password (if assigned to the execution environment).

### About this task

Use the following procedure to add an execution environment to a job template.

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Execution Environments.
2.  Click Create execution environment to create an execution environment.
3.  Enter the appropriate details into the following fields:
  1.  **Name** (required): Enter a name for the execution environment.
  2.  **Image** (required): Enter the image name. The image name requires its full location (repository), the registry, image name, and version tag, as in the following example: `quay.io/ansible/awx-ee:latestrepo/project/image-name:tag`
  3.  Optional: **Pull**: Choose the type of pull when running jobs:

    1. **Always pull container before running**: Pulls the latest image file for the container.
    2. **Only pull the image if not present before running**: Only pulls the latest image if none are specified.
    3. **Never pull container before running**: Never pull the latest version of the container image. Note:
      If you do not set a type for pull, the value defaults to **Only pull the image if not present before running**.

  4.  Optional: **Description**: Enter an optional description.
  5.  Optional: **Organization**: Assign the organization to specifically use this execution environment. To make the execution environment available for use across multiple organizations, leave this field blank.
  6.  **Registry credential**: If the image has a protected container registry, provide the credential to access it.
4.  Click Create execution environment. Your newly added execution environment is ready to be used in a job template.
5.  To add an execution environment to a job template, navigate to Automation Execution> (and then)Templates and select your template.   1.  Click Edit template and specify your execution environment in the field labeled **execution environment**.

### Results

After you add an execution environment to a job template, the template is listed in the **Templates** tab in your execution environment details.

## About container registries

If you have many automation execution environments that you want to support, you can store them in a container registry linked to your private automation hub.

For more information, see [Populating your private automation hub container registry](/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-con_container_registry#populate-container-registry "The automation hub remote registry is used for storing and managing automation execution environments.").

## Build and use a decision environment

Event-Driven Ansible includes an ansible.eda collection, which contains sample sources, event filters and rulebooks. All the collections, ansible rulebooks and their dependencies use a decision environment, which is an image that can be run on either Podman or Kubernetes.

In decision environments, sources, which are typically Python code, are distributed through ansible-collections. They inject external events into a rulebook for processing. The rulebook consists of the following:

- The python interpreter
- Java Runtime Environment for Drools rule engine
- ansible-rulebook python package
- ansible.eda collection


You can use the base decision environment and build your own customized Decision Environments with additional collections and collection dependencies. You can build a decision environment using a Dockerfile or optionally you can deploy your CA certificate into the image.

## Set up a new decision environment

The following steps describe how to import a decision environment into the platform.

### Before you begin

- You have set up any necessary credentials. For more information, see [Setting up credentials](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-proc_eda_set_up_credential#eda-set-up-credential "Create a credential to securely store sensitive data (like tokens and passwords) required for rulebook activations to connect to source plugins or private registries.").
- You have pushed a decision environment image to an image repository or you chose to use the image `de-supported` provided at [registry.redhat.io](http://registry.redhat.io/).

### About this task

### Procedure

1.  Navigate to Automation Decisions> (and then)Decision Environments.
2.  Click Create decision environment.
3.  Enter the following:
  

Name
Insert the name.

Description
This field is optional.

Image
This is the full image location, including the container registry, image name, and version tag.

Credential
This field is optional. This is the token needed to use the decision environment image.

4.  Select Create decision environment.

### Results

Your decision environment is now created and can be managed on the **Decision Environments** page.

After saving the new decision environment, the decision environment’s details page is displayed. From there or the **Decision Environments** list view, you can edit or delete it.
