# Use custom actions and UI components in Backstage Software Templates
## Overview

Learn how Backstage Software Templates relate to the Ansible automation portal and how custom templates execute automation jobs in Ansible Automation Platform.

### Understanding software templates in the automation portal

The Ansible automation portal uses Backstage Software Templates as the foundation for its self-service catalog. A software template is a YAML document stored in a Git repository (GitHub or GitLab) that defines an interactive web form and an automated workflow.

When an automation creator registers a custom software template in the portal, end users can launch it to execute jobs in Ansible Automation Platform without needing direct access to automation controller or familiarity with Ansible playbooks.

### Anatomy of a portal software template

A custom software template consists of four main sections:

- **Metadata:** Identifies the template in the portal catalog, including its display name, title, description, and source taxonomy.
- **Spec:** Declares the template type (`spec.type: automation-template`) and ownership.
- **Parameters:** Defines the input form that users complete in the portal UI before execution, such as target hosts, environment choices, or application versions.
- **Steps:** Defines the sequence of actions executed when the user submits the form, including calling custom `rhaap:*` actions to launch jobs or create resources.

### Upstream Backstage documentation versus portal differences

The Ansible automation portal is built on a Red Hat Developer Hub base image. While upstream Backstage template syntax provides the foundation, specific conventions apply to the portal:

| Template area         | Upstream Backstage convention                                       | Ansible automation portal convention                                                                                                                                   |
| --------------------- | ------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Entity type**       | `spec.type: service` or`website`                                    | **Must** use`spec.type: automation-template`.                                                                                                                          |
| **Source annotation** | Not used or generic SCM annotations                                 | Include`ansible.com/template-source: scm` so custom templates appear correctly in the portal source filter.                                                            |
| **Authentication**    | Parameters prompt for tokens or use generic secrets                 | The portal automatically injects the user's OAuth token on submit. Steps**must** reference`token: ${{ secrets.aapToken }}`. Do not define a token field in parameters. |
| **Custom actions**    | Upstream scaffolder actions (e.g.`fetch:template`,`publish:github`) | Portal includes native`rhaap:*` actions (such as`rhaap:launch-job-template`) to interact directly with Ansible Automation Platform.                                    |

Important:

Red Hat does not support the use of the Red Hat Developer Hub image for standalone purposes outside the scope of the Ansible Automation Platform self-service automation portal functionality.

