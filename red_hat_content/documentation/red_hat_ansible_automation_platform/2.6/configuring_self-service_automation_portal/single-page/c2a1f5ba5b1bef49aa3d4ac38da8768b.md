+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/html-single/configuring_self-service_automation_portal/index"
title = "Configuring self-service automation portal - Red Hat Ansible Automation Platform 2.6"

[extra]
category = "Self-service automation portal"
category_description = ""
document_kind = "documentation"
modified = "2026-02-27T14:35:44.000Z"
multi_page_path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/html/configuring_self-service_automation_portal/index/"
name = "Configuring self-service automation portal"
page_slug = "configuring_self-service_automation_portal"
product = "Red Hat Ansible Automation Platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/configuring_self-service_automation_portal/index"
type = "single-page"
+++


<span id="idm139788852998224"></span>
Red Hat Ansible Automation Platform2.6
## Configure self-service automation portal


Red Hat Customer Content Services

 [Legal Notice](#idm139788858142464) 
 **Abstract** 

This guide describes how to configure self-service automation portal so that users can run automation.




---

# Preface




Configure synchronization with Red Hat Ansible Automation Platform to securely expose core resources to the self-service portal. This process imports Ansible Automation Platform Organizations, Users, Teams, and Job Templates, making these resources readily discoverable.

# Providing feedback on Red Hat documentation




If you have a suggestion to improve this documentation, or find an error, you can contact technical support at [https://access.redhat.com](https://access.redhat.com) to open a request.

# Chapter 1. Understanding Ansible Automation Platform synchronization




The synchronization feature imports Organizations, Users, Teams, and Job Templates from Ansible Automation Platform into the self-service automation portal. This process makes the Ansible Automation Platform entities securely discoverable and accessible to portal users.

## 1.1. Overview




Self-service automation portal synchronizes two types of data from Ansible Automation Platform:

- Organizations, Users, and Teams: Identity and organizational structure data
- Job Templates: Executable automation templates


Both synchronizations run on a scheduled basis and can be manually triggered by Ansible Automation Platform Administrators in the portal UI.

## 1.2. How it works




1. The self-service automation portal connects to your Ansible Automation Platform instance using configured credentials.
1. The self-service automation portal fetches data based on the configured Ansible Automation Platform Organization and filter criteria.
1. The self-service automation portal converts Ansible Automation Platform entities into portal entities and displays them in the UI.
1. Synchronization runs on a configurable schedule (for example, every 60 minutes).
1. Users access and launch resources based on their existing Ansible Automation Platform permissions.


# Chapter 2. Ansible Automation Platform synchronization configuration reference




Definitions for all required and optional configuration parameters for the Ansible Automation Platform synchronization feature, including data types, filter options, and label normalization logic. Use this information to configure synchronization settings in the Helm values file.

## 2.1. Required synchronization settings




These parameters **must** be included in the `catalog.providers.rhaap` section of your Helm values file to enable identity synchronization.

| Option | Type | Requirement | Default | Description |
| --- | --- | --- | --- | --- |
|  `orgs` |  `string` |  **Must** be provided | - | The Ansible Automation Platform Organization to synchronize from. The configuration supports only one Ansible Automation Platform Organization. |
|  `sync.orgsUsersTeams.schedule.frequency` |  `object` |  **Must** be provided | - | Defines how often the identity data (Organizations, Users, and Teams) synchronization runs (for example, `{ minutes: 60 }` ). |
|  `sync.orgsUsersTeams.schedule.timeout` |  `object` |  **Must** be provided | - | The maximum duration for identity synchronization before a timeout error occurs (for example, `{ minutes: 15 }` ). |


## 2.2. Optional Job Template synchronization settings




These parameters apply specifically to Job Template synchronization. If synchronization is enabled, the schedule and timeout settings **must** be provided.

| Option | Type | Requirement | Default | Description |
| --- | --- | --- | --- | --- |
|  `sync.jobTemplates.enabled` |  `boolean` |  **Must** be provided |  `true` | Set to `true` to enable Job Template synchronization, or `false` to disable it. |
|  `sync.jobTemplates.surveyEnabled` |  `boolean` | Optional | - | Filters Job Templates based on whether an Ansible Automation Platform Survey is enabled. See the **Filter Options** section for details. |
|  `sync.jobTemplates.labels` |  `array` | Optional |  `[]` | Filters Job Templates based on specific Ansible Automation Platform Labels. See the **Filter Options** section for details. |
|  `sync.jobTemplates.schedule.frequency` |  `object` |  **Must** be provided if template sync is enabled | - | Defines how often the Job Template synchronization runs (for example, `{ minutes: 60 }` ). |
|  `sync.jobTemplates.schedule.timeout` |  `object` |  **Must** be provided if template sync is enabled | - | The maximum duration for Job Template synchronization before a timeout error occurs (for example, `{ minutes: 15 }` ). |


## 2.3. Filter Options




The following filter options apply only to Job Template synchronization.

The `surveyEnabled` filter accepts one of the following values:

- Omitted: Sync **all** Job Templates, regardless of their Ansible Automation Platform Survey status.
-  `    true` : Sync **only** Job Templates that have Ansible Automation Platform Surveys enabled.
-  `    false` : Sync **only** Job Templates that do **not** have Ansible Automation Platform Surveys enabled.


The `labels` filter accepts an array of strings:

-  `    []` (empty array) or omitted: Sync **all** Job Templates, regardless of associated Ansible Automation Platform Labels.
- ["label1", "label2"]: Sync **only** Job Templates that have **any** of the specified Ansible Automation Platform Labels ( **OR** logic).
- Label matching is case-insensitive.


## 2.4. Ansible Automation Platform label normalization




Before filtering is applied, Ansible Automation Platform Labels are normalized by applying the following transformations:

- Convert the label to lowercase (for example, "CaC" becomes "cac")
- Replace invalid characters
- Collapse multiple hyphens into a single hyphen (for example, "app—​dev" becomes "app-dev")
- Remove leading and trailing hyphens (for example, "--tag--" becomes "tag")


# Chapter 3. Ansible Automation Platform synchronization configuration examples




These configuration examples provide complete, tested YAML blocks for common synchronization scenarios, such as minimal setup or filtered synchronization. Use the examples to quickly implement and validate settings in your Helm values file.

## 3.1. Minimal configuration




Synchronizes all Organizations, Users, Teams, and Job Templates using the using the default 60-minute frequency and 15-minute timeout.

```
catalog:
  providers:
    rhaap:
      '{{- include "catalog.providers.env" . }}':
        orgs: Default
        sync:
          orgsUsersTeams:
            schedule:
              frequency: { minutes: 60 }
              timeout: { minutes: 15 }
          jobTemplates:
            enabled: true
            schedule:
              frequency: { minutes: 60 }
              timeout: { minutes: 15 }
```

## 3.2. Filter by survey status




Synchronize identity data, but filter Job Templates to include only those that have Ansible Automation Platform Surveys **enabled** .

To sync Job Templates without Ansible Automation Platform Surveys, set `surveyEnabled:` to `false` .

```
catalog:
  providers:
    rhaap:
      development:
        orgs: Default
        sync:
          orgsUsersTeams:
            schedule:
              frequency: { minutes: 60 }
              timeout: { minutes: 15 }
          jobTemplates:
            enabled: true
            surveyEnabled: true
            schedule:
              frequency: { minutes: 60 }
              timeout: { minutes: 15 }
```

## 3.3. Filter by labels




Synchronize Job Templates that match **ANY** of the specified Ansible Automation Platform Labels: `portal` , `self-service` , or `production` . The configuration uses **OR** logic for labels.

```
catalog:
  providers:
    rhaap:
      development:
        orgs: Default
        sync:
          orgsUsersTeams:
            schedule:
              frequency: { minutes: 60 }
              timeout: { minutes: 15 }
          jobTemplates:
            enabled: true
            labels:
              - portal
              - self-service
              - production
            schedule:
              frequency: { minutes: 60 }
              timeout: { minutes: 15 }
```

## 3.4. Exclude by labels




To prevent templates from syncing into Portal with specific labels, use the `excludeLabels` parameter in your template configuration or search query.

You must format excluded labels as an array (for example, `excludeLabels: ["test", "deprecated"]` ).

```
catalog:
  providers:
    rhaap:
      development:
        orgs: Default
        sync:
          orgsUsersTeams:
            schedule:
              frequency: { minutes: 60 }
              timeout: { minutes: 15 }
          jobTemplates:
            enabled: true
            labels:
              - portal
              - self-service
              - production
            excludeLabels:
              - "test"
              - "example"
            schedule:
              frequency: { minutes: 60 }
              timeout: { minutes: 15 }
```

## 3.5. Combine filters for production




Combine survey status and label filters:

```
catalog:
  providers:
    rhaap:
      production:
        orgs: Default
        sync:
          orgsUsersTeams:
            schedule:
              frequency: { hours: 1 }
              timeout: { minutes: 15 }
          jobTemplates:
            enabled: true
            surveyEnabled: true
            labels:
              - portal
              - self-service
            schedule:
              frequency: { hours: 1 }
              timeout: { minutes: 15 }
```

This configuration syncs:

- All Users, Teams, and Organizations from the "Default" organization
- Job Templates that belong to "Default" organization AND have Ansible Automation Platform Surveys enabled **AND** have Ansible Automation Platform Labels "portal" **OR** "self-service"


## 3.6. Custom sync frequencies




Fast synchronization (development):

```
catalog:
  providers:
    rhaap:
      development:
        orgs: Default
        sync:
          orgsUsersTeams:
            schedule:
              frequency: { minutes: 5 }
              timeout: { seconds: 30 }
          jobTemplates:
            enabled: true
            schedule:
              frequency: { minutes: 5 }
              timeout: { seconds: 30 }
```

Standard synchronization:

```
catalog:
  providers:
    rhaap:
      development:
        orgs: Default
        sync:
          orgsUsersTeams:
            schedule:
              frequency: { hours: 1 }
              timeout: { minutes: 15 }
          jobTemplates:
            enabled: true
            schedule:
              frequency: { hours: 1 }
              timeout: { minutes: 15 }
```

Slow synchronization:

```
catalog:
  providers:
    rhaap:
      development:
        orgs: Default
        sync:
          orgsUsersTeams:
            schedule:
              frequency: { hours: 4 }
              timeout: { minutes: 30 }
          jobTemplates:
            enabled: true
            schedule:
              frequency: { hours: 4 }
              timeout: { minutes: 30 }
```

## 3.7. Disable sync frequencies




Sync identity data less frequently than Job Templates:

```
catalog:
  providers:
    rhaap:
      production:
        orgs: Default
        sync:
          orgsUsersTeams:
            schedule:
              frequency: { hours: 4 }
              timeout: { minutes: 15 }
          jobTemplates:
            enabled: true
            schedule:
              frequency: { minutes: 30 }
              timeout: { minutes: 10 }
```

## 3.8. Disable Job Template sync




Set `enabled: false` to temporarily disable Job Template synchronization while maintaining identity sync.

```
catalog:
  providers:
    rhaap:
      development:
        orgs: Default
        sync:
          orgsUsersTeams:
            schedule:
              frequency: { minutes: 60 }
              timeout: { minutes: 15 }
          jobTemplates:
            enabled: false
            schedule:
              frequency: { minutes: 60 }
              timeout: { minutes: 15 }
```

## 3.9. Production configuration example




Complete production configuration with filters:

```
catalog:
  providers:
    rhaap:
      production:
        orgs: Default
        sync:
          orgsUsersTeams:
            schedule:
              frequency: { hours: 1 }
              timeout: { minutes: 15 }
          jobTemplates:
            enabled: true
            surveyEnabled: true
            labels:
              - production
              - self-service
            schedule:
              frequency: { hours: 1 }
              timeout: { minutes: 15 }
```

# Chapter 4. Configuring template RBAC and display logic




Template definitions in the YAML file control where templates appear in the self-service automation portal and how to manage permissions.

Note
Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/) .



## 4.1. Role-based access control (RBAC)




The template type determines where you must configure user permissions.

-  **Auto-generated templates** : Permissions synchronize from Ansible Automation Platform. Users must have permissions on the underlying Ansible Automation Platform job template. For more information, see [Setting up initial RBAC rules in self-service automation portal](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/installing_self-service_automation_portal/index#self-service-initial-rbac-setup_self-service-accessing-deployment) .
-  **Custom templates** : You must explicitly configure permissions within the self-service automation portal. Users must also have permission to run the associated job templates in Ansible Automation Platform. For more information see, [Setting up RBAC for custom self-service templates](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_self-service_automation_portal/index#self-service-set-up-rbac_self-service-rbac) .


## 4.2. Backstage software template display logic (spec.type)




The `spec.type` value in the template YAML determines which portal page displays the template.

-  **No spec.type defined** : The template appears on the Ansible Automation Platform templates page for all users.
-  **spec.type: execution-environment** : The template appears only on the **EE definition files** page.


## 4.3. Example: Auto-generated template




The following YAML example uses the `spec.type` field to restrict the template view to the **EE definition files** page.

```
apiVersion: scaffolder.backstage.io/v1beta3
kind: Template
metadata:
  name: ansible-execution-environment-template
  title: EE template
  description: Ansible Execution Environment Template
  tags:
    - ansible
    - execution-environment
    # ...
spec:
  type: execution-environment  # Restricts the template view to the Execution Environment page.
  parameters:
    # ...
```

# Chapter 5. Troubleshooting Ansible Automation Platform synchronization




Review common issues, symptoms, and solutions if synchronization does not function as expected.

## 5.1. No Job Templates appearing in portal




 **Issue:** Expected Job Templates are missing from the portal interface.

 **Solutions:** 

- Verify the `    surveyEnabled` setting in your Helm values file matches the status of your Job Templates.
- Confirm the `    labels` filter includes the correct, approved Ansible Automation Platform Label names.
- Try temporarily removing filters to confirm if the Job Templates appear without restrictions.
- Verify the Ansible Automation Platform Organization name spelling is exact (it is case-sensitive).
- Check Ansible Automation Platform connectivity and the configured token permissions.


## 5.2. No Users or Teams appearing in portal




 **Issue:** Expected users or teams are missing from the portal interface.

 **Solutions:** 

- Check Ansible Automation Platform connectivity and the configured token permissions.
- Verify the Ansible Automation Platform Organization name matches exactly.
- Review the configured synchronization schedule and check system logs.
- Ensure users have the proper organization or team memberships within Ansible Automation Platform.


## 5.3. Slow synchronization




 **Issue:** Synchronization takes too long to complete or times out.

 **Symptoms:** 

- Timeouts during synchronization.
- Timeout errors appear in the logs.


 **Solutions:** 

- Increase the `    timeout` value in the synchronization schedule.
- Reduce the synchronization `    frequency` (sync less often).
- Add more specific filters to the Job Templates configuration to reduce the overall count of entities processed.
- For large organizations, increase the `    timeout` specifically for the identity sync ( `    orgsUsersTeams` ).


## 5.4. Wrong Ansible Automation Platform organization




 **Issue:** The portal displays unexpected Job Templates, users, or teams.

 **Symptoms:** 

- Expected Job Templates do not appear.
- Incorrect templates appear.
- Users or teams are missing, or the wrong ones are present.


 **Solutions:** 

- Verify the Ansible Automation Platform Organization name spelling is exact (it is case-sensitive).
- Check the organization names in Ansible Automation Platform itself.
- Ensure the configured organization exists in Ansible Automation Platform.


# Chapter 6. Manually triggering synchronization




Ansible Automation Platform administrators can manually trigger synchronization from the portal UI.

 **Procedure** 

1. Log in to self-service automation portal as an Ansible Automation Platform Administrator.
1. Navigate to the **Synchronization management** page.
1. ClickManual syncfor Organizations or Job Templates.
1. Monitor the sync progress in the UI.


 **Verification** 

Verify that the synchronization is listed as **Successful** on the **Synchronization management** page.


# Chapter 7. Enabling custom support URL




Update the Helm configuration to redirect the default support link to your organization’s specific support resources.

 **Prerequisites** 

- You have administrative access to the OpenShift Container Platform console.
- The self-service automation portal is installed in an OpenShift project.


 **Procedure** 

1. Log in to the OpenShift Container Platform console.
1. In the **Developer** perspective, navigate to **Helm** .
1. Click the **More actions** icon for your self-service automation portal Helm release and select **Upgrade** .
1. Select **YAML view** .
1. Add the `    CUSTOMER_SUPPORT_URL` environment variable to the `    extraEnvVars` section:
    
    
    ```
    redhat-developer-hub:      upstream:        backstage:          extraEnvVars:            - name: CUSTOMER_SUPPORT_URL              value: https://your-support-portal.example.com
    ```
    
    
1. ClickUpgrade.


 **Verification** 

1. Log in to the self-service automation portal.
1. Hover over the **Support** link in the upper right of the UI (next to the **Create** icon) and verify it points to your custom URL.


# Chapter 8. Enabling feedback to Red Hat




Enable the optional feedback form to allow users to submit suggestions and general feedback directly through the portal interface.

 **Prerequisites** 

- You have administrative access to the OpenShift Container Platform console.
- The self-service automation portal is installed in an OpenShift project.


 **Procedure** 

1. Log in to the OpenShift Container Platform console.
1. In the **Developer** perspective, navigate to **Helm** .
1. Click the **More actions** icon for your self-service automation portal Helm release and select **Upgrade** .
1. Select **YAML view** .
1. Locate the `    ansible` section and set the `    feedback.enabled` value to `    true` :
    
    
    ```
    ansible:      feedback:        enabled: true
    ```
    
    
1. ClickUpgrade


 **Verification** 

1. Log in to the self-service automation portal.
1. Confirm that the Feedback button is visible in the bottom-left corner of the console.



<span id="idm139788858142464"></span>
# Legal Notice

Copyright© Red Hat.
Except as otherwise noted below, the text of and illustrations in this documentation are licensed by Red Hat under the Creative Commons Attribution–Share Alike 3.0 Unported license . If you distribute this document or an adaptation of it, you must provide the URL for the original version.
Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.
Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of Red Hat, LLC. or its subsidiaries in the United States and other countries.
Linux® is the registered trademark of Linus Torvalds in the United States and other countries.
XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its subsidiaries in the United States and other countries.
TheOpenStack® Word Mark and OpenStack logo are trademarks or registered trademarks of the Linux Foundation, used under license.
All other trademarks are the property of their respective owners.





