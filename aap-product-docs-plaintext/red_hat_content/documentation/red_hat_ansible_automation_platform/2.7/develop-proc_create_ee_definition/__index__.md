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

