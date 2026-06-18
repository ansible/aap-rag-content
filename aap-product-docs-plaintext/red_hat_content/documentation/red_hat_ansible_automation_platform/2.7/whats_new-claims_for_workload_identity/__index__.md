# Claims for workload identity

Ansible Automation Platform uses OpenID Connect (OIDC) and short-lived JSON Web Tokens (JWTs) with digitally signed claims to verify identity across systems. Understanding this claims structure allows you to create secure access control policies.

## Example claims

The example shows a JWT payload including standard and custom claim definitions describing an automation controller job.

```
{
"jti": "12345678-90ab-cdef-0808-aabbccddeeff",
"iss": "https://app.ansible.com/o",
"aud": "https://vault.example.com:8200",
"iat": 1234567890,
"exp": 1234567890,
"sub":
"workload_type:aap_controller_automation_job:organization:my-org:job_template:my-template",
"aap_controller_job_id": "42"
"aap_controller_job_name": "Deploy Web Server"
"aap_controller_job_type": "run"
"aap_controller_launch_type": "manual"
"aap_controller_playbook_name": "deploy.yml"
"aap_controller_launched_by_name": "alice"
"aap_controller_launched_by_id": "7"
"aap_controller_organization_name": "Default"
"aap_controller_organization_id": "1"
"aap_controller_inventory_name": "Production Inventory"
"aap_controller_inventory_id": "5"
"aap_controller_execution_environment_name": "Default EE"
"aap_controller_execution_environment_id": "3"
"aap_controller_project_name": "Infrastructure Project"
"aap_controller_project_id": "17"
"aap_controller_job_template_name": "Deploy Template"
"aap_controller_job_template_id": "21"
"aap_controller_unified_job_template_name": "Unified Deploy Template"
"aap_controller_unified_job_template_id": "55"
"aap_controller_instance_group_name": "Group 1"
"aap_controller_instance_group_id": "9"
}
```

## Standard Claims

The following table shows the standard JWT claims.

| Claim                | Value                                                                                                                                                                                                                               |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **j**(J**ti** WT ID) | A unique identifier for each JWT.                                                                                                                                                                                                   |
| **iss** (issuer)     | The URL of the Ansible Automation Platform OIDC provider (for example, `https://aap.example.com/o`).                                                                                                                                |
| **iat** (issued at)  | UNIX timestamp when the JWT was issued.                                                                                                                                                                                             |
| **aud** (audience)   | The intended recipient of the JWT, such as a HashiCorp Vault instance. This is set to the value of the Vault Server URL.                                                                                                            |
| **exp** (expiration) | UNIX timestamp that determines when the token expires. This is calculated based on the job’s configured timeout. The platform fallback defaults to 5 minutes (plus 1 minute for clock skew), and is configurable by administrators. |
| **sub** (subject)    | Uniquely identifies the automation workload. It follows the format: `workload_type:aap_controller_automation_job:organization:<org>:job_template:<template>`.                                                                       |

## Custom claims

The following table shows the Ansible Automation Platform custom claims that are included in JWT issued by Ansible Automation Platform.

These claims provide granular workload metadata, including organization, project, and inventory details. Custom claims are grouped into scope definitions. The platform currently defines an aap_controller_automation_job scope, which includes the following claims that describe an AAP Automation Controller Job workload.

| Claim                                       | Value                                                                               |
| ------------------------------------------- | ----------------------------------------------------------------------------------- |
| `aap_controller_job_id`                     | Unique identifier of the controller job.                                            |
| `aap_controller_job_name`                   | Name of the job template or project sync job being executed.                        |
| `aap_controller_job_type`                   | Type of job being performed, such as `run` or `cleanup`.                            |
| `aap_controller_launch_type`                | How the job was initiated, such as `manual`, `scheduled`, `webhook`, or `workflow`. |
| `aap_controller_playbook_name`              | Name of the playbook being executed in the job.                                     |
| `aap_controller_launched_by_name`           | Username or system entity name that initiated the job run.                          |
| `aap_controller_launched_by_id`             | Unique identifier of the user or entity that launched the job.                      |
| `aap_controller_organization_name`          | Name of the organization.                                                           |
| `aap_controller_organization_id`            | Unique identifier of the organization.                                              |
| `aap_controller_inventory_name`             | Name of the inventory used in the job.                                              |
| `aap_controller_inventory_id`               | Unique identifier of the inventory used in the job.                                 |
| `aap_controller_execution_environment_name` | Name of the execution environment used in the job.                                  |
| `aap_controller_execution_environment_id`   | Unique identifier of the execution environment used in the job.                     |
| `aap_controller_project_name`               | Name of the project used in the job.                                                |
| `aap_controller_project_id`                 | Unique identifier of the project used in the job.                                   |
| `aap_controller_job_template_name`          | Name of the job template used to launch the job.                                    |
| `aap_controller_job_template_id`            | Unique identifier of the job template used.                                         |
| `aap_controller_unified_job_template_name`  | Name of the unified job template used to launch the job.                            |
| `aap_controller_unified_job_template_id`    | Unique identifier of the unified job template.                                      |
| `aap_controller_instance_group_name`        | Name of the instance group used in the job.                                         |
| `aap_controller_instance_group_id`          | Unique identifier of the instance group used in the job.                            |
