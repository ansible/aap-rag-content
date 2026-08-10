# Add and launch custom self-service templates

Custom self-service templates are stored as YAML files in repositories in GitHub or Gitlab. When a user launches a software template from Ansible automation portal, they must fill in a form with the values needed to run the associated job template in Ansible Automation Platform.

Custom self-service templates are YAML files stored in GitHub or GitLab repositories. Each template defines a user form and one or more `rhaap:*` action steps that execute automation in Ansible Automation Platform.

In the `steps` section, reference the authentication token as `${{ secrets.aapToken }}`. Ansible automation portal automatically injects this token when a user submits the form. Do not include `token` in the `parameters.required` list.

Business inputs such as software names, versions, or inventory selections belong in the `parameters` section. The `values.template` field must match the exact name of the job template in Ansible Automation Platform.

The following example shows a custom template that lets users select a software package and version, then launches the corresponding job template in Ansible Automation Platform:

```
apiVersion: scaffolder.backstage.io/v1beta3
kind: Template
metadata:
name: software-installation
title: Software Installation
description: Install software via an AAP job template from the Automation Portal
spec:
owner: group:default/team-platform
type: service

parameters:
- title: Software
required:
- SoftwareName
- Softwareversion
properties:
SoftwareName:
type: string
title: Software name
enum:
- Postgresql
- Nginx
- Grafana

dependencies:
SoftwareName:
oneOf:
- properties:
SoftwareName:
const: Postgresql
Softwareversion:
type: string
title: Choose a version
enum:
- v13
- v14
- v16
required:
- Softwareversion

- properties:
SoftwareName:
const: Nginx
Softwareversion:
type: string
title: Choose a version
enum:
- v2.4
- v2.5
- v2.6
required:
- Softwareversion

- properties:
SoftwareName:
const: Grafana
Softwareversion:
type: string
title: Choose a version
enum:
- v2
- v3
- v4
required:
- Softwareversion

steps:
- id: launch-job
name: Launch AAP job template
action: rhaap:launch-job-template
input:
token: ${{ secrets.aapToken }}
values:
template: test job
extraVariables:
software_name: ${{ parameters.SoftwareName }}
software_version: ${{ parameters.Softwareversion }}
```

Important:

Starting in Ansible Backstage Plugins v2.2.0, the portal no longer passes the OAuth token in template form values. Templates that use `${{ parameters.token }}` in `rhaap:*` action steps will fail with a `Could not create entity` error. Always use `${{ secrets.aapToken }}` to access the real OAuth token.

