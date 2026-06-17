# 3. Working with templates
## 3.2. Understanding auto-generated templates

self-service automation portal automatically generates templates from Ansible Automation Platform Job Templates. Each Ansible Automation Platform Job Template with the appropriate configuration becomes a template that users can execute from self-service automation portal.

Note

Templates in self-service automation portal use [Backstage Software Templates](https://backstage.io/docs/features/software-templates/writing-templates) as the underlying technology. For details on supported usage, see the [self-service automation portal support policy](https://access.redhat.com/page/ansible-automation-platform-self-service-automation-portal-support-policy).

Auto-generated templates include:

- Form fields generated from Ansible Automation Platform Job Template Surveys and "Prompt on Launch" options.
- Metadata (name, description, labels) mapped from Ansible Automation Platform Job Template properties.
- A single step that launches the Ansible Automation Platform Job Template using the `rhaap:launch-job-template` action.
- Output that displays the job execution results to the user.

Users only see and execute templates for Ansible Automation Platform Job Templates they have Job Template Execute permission in Ansible Automation Platform.

