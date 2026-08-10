+++
title = "Create an execution environment definition using the UI wizard - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_create_ee_definition"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-build_execution_environments_with_the_automation_portal/", "Build execution environments with automation portal"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-proc_create_ee_definition/aem-page/develop-proc_create_ee_definition.html"
last_crumb = "Create an execution environment definition using the UI wizard"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Create an execution environment definition using the UI wizard"
oversized = "false"
page_slug = "develop-proc_create_ee_definition"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-proc_create_ee_definition"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-proc_create_ee_definition/toc/toc.json"
type = "aem-page"
+++

# Create an execution environment definition using the UI wizard

Use the execution environment builder wizard in Ansible automation portal to create a custom execution environment definition by selecting a template, base image, collections, and dependencies.

## Before you begin

- You have access to Ansible automation portal with the `ansible.execution-environments.view` permission granted.
- Your AAP administrator has configured and synced content sources.

## About this task

Navigate to **Execution Environments > Create** and select a template. The wizard walks you through base image selection, collections, dependencies, and build steps.

AAP administrators manage which templates are available and can control access with RBAC. The following built-in templates are available:

- **Start from scratch** -- minimal starting point for custom definitions (loaded by default).
- **Networking Automation** -- pre-selected networking collections (requires collections to be discoverable from a configured content source).
- **Cloud Automation** -- pre-selected cloud collections (requires collections to be discoverable from a configured content source).

Custom templates created by your AAP administrator also appear on this page. See [Create standardized EE templates for teams](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_create_team_templates "Create pre-configured EE templates so that your teams start from a known-good baseline without choosing every dependency from scratch.") for details.

## Procedure

1.  Navigate to **Execution Environments > Create**.
2.  Select a template.
3.  Choose a base image appropriate for your environment.
4.  In the collections picker, select the Ansible collections your execution environment requires.
5.  Optional: Add Python requirements and system packages.
6.  Optional: Add custom build steps at specific phases (prepend or append to base, galaxy, builder, or final stages).
7.  Name the definition and add a descriptive tag.
      The wizard uses `spec.type: execution-environment` to tag the definition. This tag is optional but recommended to make definitions searchable and filterable in the catalog.

8.  Choose to select **Publish to a Git repository** to save definition files to a repository, or leave the checkbox cleared to register in the catalog and download files locally.

## Results

The generated execution environment definition includes:

- `<ee-name>.yml` -- the EE definition with all dependencies (collections, Python packages, system packages) declared inline. The file name matches the name you entered in the form.
- `ansible.cfg` -- galaxy server configuration (auto-generated from configured collection sources).
- `<ee-name>-template.yaml` -- a reusable template for sharing your configuration.

## What to do next

Note:

Collections available in the picker come from configured content sources. If a collection is missing, ask your AAP administrator to verify the content source configuration and sync status.

## Save definition files to a Git repository and build

Save execution environment definition files to a GitHub or GitLab repository and optionally trigger an automated container image build.

### Before you begin

- Your AAP administrator has configured GitHub or GitLab OAuth. See [Configure a GitHub OAuth App for saving definitions](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_configure_github_oauth_ee_builder "Configure a GitHub OAuth App so that users can save execution environment definition files to a GitHub repository and trigger automated image builds.") or [Configure a GitLab OAuth App for saving definitions](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_configure_gitlab_ee_builder "Configure a GitLab OAuth App so that users can save execution environment definition files to a GitLab repository.").
- For automated builds: your AAP administrator has configured GitHub repository secrets or GitLab CI/CD variables.

### About this task

When you select **Publish to a Git repository** in the wizard, the definition files are saved to a GitHub or GitLab repository and can optionally trigger an automated container image build.

### Procedure

1.  In the final step of the wizard, select **Publish to a Git repository**.
2.  Authenticate with your Git provider through OAuth when prompted.
3.  Select the target repository or allow the wizard to create a new one.
4.  Optional: Select **Build Execution Environment** to trigger an automated image build after saving.
5.  Configure the target registry (private automation hub or custom), image name, tag, and TLS settings.
6.  Click **Create**.

### Results

The following files are saved to the repository:

- `<ee-name>.yml` -- EE definition with all dependencies inline. The file name matches the name you entered in the form.
- `<ee-name>-template.yaml` -- reusable template file that administrators can register in the catalog.
- `ansible.cfg` -- galaxy server configuration.
- `ee-build.yml` (GitHub) or `.gitlab-ci.yml` (GitLab) -- CI/CD pipeline workflow for automated builds.

After saving, check the build status from the GitHub Actions tab or the GitLab CI/CD Pipelines page on the target repository.

Note:

If the target repository does not exist, it is created automatically. If it exists, a pull request is created instead.

## Use a custom registry or self-signed certificates

Adjust the execution environment build configuration when targeting a private or internal container registry that uses custom URLs or self-signed certificates.

### Before you begin

- Your AAP administrator has configured templates and internal content sources. See [Host execution environment wizard templates in a private Git repository](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_host_templates_private_repo "Copy the EE Builder wizard templates from the public Ansible GitHub repository to a private repository for use in private or air-gapped environments.").
- You have access to an internal container registry.

### Procedure

1.  In the wizard, select **Custom Registry** instead of private automation hub and enter your internal registry URL.
2.  Clear the **Verify TLS certificates** checkbox if your internal registry uses self-signed certificates that are not trusted by the GitHub Actions runner or GitLab Runner executing the build.
3.  Select a base image from your internal registry instead of the default `registry.redhat.io` images.

## Download definition files without saving to a repository

Create an execution environment definition and download the generated files as a `.tar` archive instead of saving them to a Git repository.

### Procedure

1.  In the wizard, clear the **Publish to a Git repository** checkbox.
2.  Complete the remaining steps and click **Create**.
3.  After creation, click **Download EE files** to download a `.tar` archive containing all generated files.

### Results

The execution environment definition is registered in the catalog. The archive includes `<ee-name>.yml` (with all dependencies declared inline), `<ee-name>-template.yaml`, `ansible.cfg`, and an optional readme.

## Import an existing execution environment definition

Import a previously generated execution environment template to make it available for other users to create definitions with the same defaults.

### Before you begin

- You have the AAP Administrator role.
- You have a `<ee-name>-template.yaml` file hosted in a Git repository or available as a URL.

### About this task

Important:

Importing templates requires AAP administrator access. Only users with the AAP Administrator role can import templates.

### Procedure

1.  Navigate to **Execution Environments > Create**.
2.  Open the kebab menu and select **Import Template**.
3.  Paste the template URL and click **Analyze**.
4.  Click **Import**.

### Results

The imported template appears on the **Create** tab. Launch the template to verify the wizard pre-populates the expected collections and configuration.
