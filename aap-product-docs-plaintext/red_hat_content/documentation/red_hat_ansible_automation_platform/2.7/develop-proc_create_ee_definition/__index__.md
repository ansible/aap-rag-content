# Create an execution environment definition using the UI wizard

Use the execution environment builder wizard in Ansible automation portal to create a custom execution environment definition by selecting a template, base image, collections, and dependencies.

## Before you begin

- You have access to Ansible automation portal with the `ansible.execution-environments.view` permission granted.
- Your AAP administrator has configured and synced content sources.

## About this task

Navigate to **Execution Environments > Create** and select a template. The wizard walks you through base image selection, collections, dependencies, and build steps.

AAP administrators manage which templates are available and can control access with RBAC. The following built-in templates are available:

- **Start from scratch** -- minimal starting point for custom definitions (loaded by default).
- **Networking Automation** -- pre-selected networking collections (included in Helm chart but commented out by default; requires collections to be discoverable from a configured content source).
- **Cloud Automation** -- pre-selected cloud collections (included in Helm chart but commented out by default; requires collections to be discoverable from a configured content source).


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

- Your AAP administrator has configured GitHub or GitLab OAuth. See [Configure a GitHub OAuth App for saving definitions](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_configure_github_oauth_ee_builder "Configure a GitHub OAuth App so that users can save execution environment definition files to a GitHub repository and trigger automated image builds.") or [Set up GitLab integration](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_configure_gitlab_ee_builder "Configure GitLab content discovery and OAuth so that execution environment builder can scan GitLab groups for Ansible collections and save definition files.").
- For automated builds: your AAP administrator has configured GitHub repository secrets.

### About this task

When you select **Publish to a Git repository** in the wizard, the definition files are saved to a GitHub or GitLab repository and can optionally trigger an automated container image build.

Note:

Automated image builds are available for GitHub only in this release. GitLab CI support is planned for a future release.

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
- `ee-build.yml` (GitHub only) -- GitHub Actions workflow for automated builds.


After saving, check the build status directly from the GitHub Actions tab on the target repository.

Note:

If the target repository does not exist, it is created automatically. If it exists, a pull request is created instead.

## Use a custom registry or self-signed certificates

Adjust the execution environment build configuration when targeting a private or internal container registry that uses custom URLs or self-signed certificates.

### Before you begin

- Your AAP administrator has configured templates and internal content sources. See [Host execution environment wizard templates in a private Git repository](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_host_templates_private_repo "Copy the EE Builder wizard templates from the public Ansible GitHub repository to a private repository for use in private or air-gapped environments.").
- You have access to an internal container registry.

### Procedure

1.  In the wizard, select **Custom Registry** instead of private automation hub and enter your internal registry URL.
2.  Clear the **Verify TLS certificates** checkbox if your internal registry uses self-signed certificates.
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

## Execution environment builder custom UI components

Custom UI components are available for use in software templates to provide specialized form fields for creating and configuring execution environment definitions in Ansible automation portal.

To use a component in your template, set the `ui:field` property on a parameter:

```yaml
parameters:
myField:
type: string
ui:field: BaseImagePicker
```

### BaseImagePicker

Displays a selection of pre-configured base container images for execution environment definitions. Includes an option to specify a custom image.

| Property    | Description                                                             |
| ----------- | ----------------------------------------------------------------------- |
| `ui:field`  | `BaseImagePicker`                                                       |
| `enum`      | Array of base image references, plus `custom` for a custom image entry. |
| `enumNames` | Display labels for each base image option.                              |


**Example:**

```yaml
baseImage:
title: Base image
type: string
ui:field: BaseImagePicker
enum:
- registry.redhat.io/ansible-automation-platform/ee-minimal-rhel9:2.18
- custom
enumNames:
- Red Hat Ansible Minimal EE - Ansible Core 2.18 (RHEL 9)
- Custom Image
```

### CollectionsPicker

Provides an interactive interface for selecting Ansible collections to include in an execution environment. Supports searching and adding collections from private automation hub, Galaxy, and SCM repositories. Includes version selection and source management.

| Property   | Description                                                                                  |
| ---------- | -------------------------------------------------------------------------------------------- |
| `ui:field` | `CollectionsPicker`                                                                          |
| `type`     | `array` (returns an array of collection objects with `name`, `version`, and `source` fields) |

### PackagesPicker

Enables adding Python packages or system packages to an execution environment definition. Supports direct entry and bulk addition through comma-separated values.

| Property   | Description                                        |
| ---------- | -------------------------------------------------- |
| `ui:field` | `PackagesPicker`                                   |
| `type`     | `array` (returns an array of package name strings) |

### FileUploadPicker

Provides a file upload interface for importing requirements files, such as `requirements.txt` for Python packages or `bindep.txt` for system packages. The file content is parsed and merged with manually entered values.

| Property   | Description                                     |
| ---------- | ----------------------------------------------- |
| `ui:field` | `FileUploadPicker`                              |
| `type`     | `string` (returns the file content as a string) |

### EEFileNamePicker

A text input field for specifying the execution environment definition name. Validates the name against existing EE definitions in the catalog to prevent duplicates and enforces naming conventions.

| Property   | Description        |
| ---------- | ------------------ |
| `ui:field` | `EEFileNamePicker` |
| `type`     | `string`           |

### EETagsPicker

Provides an interface for adding discovery tags to an execution environment definition. Tags help users find and categorize EE definitions in the catalog.

| Property   | Description                               |
| ---------- | ----------------------------------------- |
| `ui:field` | `EETagsPicker`                            |
| `type`     | `array` (returns an array of tag strings) |

### MCPServersPicker

Displays available Model Context Protocol (MCP) servers as selectable cards. Users can select which MCP servers to integrate with their execution environment.

| Property            | Description                                                          |
| ------------------- | -------------------------------------------------------------------- |
| `ui:field`          | `MCPServersPicker`                                                   |
| `type`              | `array` (returns an array of selected MCP server identifier strings) |
| `schema.items.enum` | Array of available MCP server identifiers.                           |

### ScmSelector

Provides a source control management (SCM) provider selector with built-in authentication. Users select a configured GitHub or GitLab instance, then authenticate through the SCM provider OAuth flow. The component validates credentials and displays connection status.

| Property                                       | Description                                                                                                   |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `ui:field`                                     | `ScmSelector`                                                                                                 |
| `type`                                         | `string` (returns the selected SCM provider identifier)                                                       |
| `ui:options.providers`                         | Array of provider configuration objects with `label`, `provider` (`github` or `gitlab`), and optional `host`. |
| `ui:options.requestUserCredentials.secretsKey` | Key used to store the authenticated SCM token in template secrets.                                            |

### AdditionalBuildStepsPicker

Provides an interface for specifying custom build steps to include in the execution environment build process. Supports multiple build phases with command entry.

| Property   | Description                                                                            |
| ---------- | -------------------------------------------------------------------------------------- |
| `ui:field` | `AdditionalBuildStepsPicker`                                                           |
| `type`     | `array` (returns an array of build step objects with `stepType` and `commands` fields) |


**Available build step phases:**

| Phase             | Description                                                   |
| ----------------- | ------------------------------------------------------------- |
| `prepend_base`    | Commands to run before base image dependencies are installed. |
| `append_base`     | Commands to run after base image dependencies are installed.  |
| `prepend_galaxy`  | Commands to run before Galaxy collections are installed.      |
| `append_galaxy`   | Commands to run after Galaxy collections are installed.       |
| `prepend_builder` | Commands to run before builder dependencies are installed.    |
| `append_builder`  | Commands to run after builder dependencies are installed.     |
| `prepend_final`   | Commands to run before the final image stage.                 |
| `append_final`    | Commands to run after the final image stage.                  |
