# 7. Target environment
## 7.1. Container-based Ansible Automation Platform
### 7.1.4. Validating the target environment




After completing the migration, validate your target environment to ensure all components are functional and operating as expected.

**Procedure**

1. Verify all migrated components are functional.

To ensure that all components have been successfully migrated, verify that each component is operational and accessible:


1. Platform gateway: Access the Ansible Automation Platform URL at `        <a class="link" href="https://<gateway_hostname>/">https://&lt;gateway_hostname&gt;/</a>` and verify that the dashboard loads correctly. Check that the platform gateway service is running and properly connected to automation controller.
1. Automation controller: Under **Automation Execution** , check that projects, inventories, and job templates are present and properly configured.
1. Automation hub: Under **Automation Content** , verify that collections, namespaces, and their contents are visible.
1. Event-Driven Ansible (if applicable): Under **Automation Execution Decisions** , verify that rule audits, rulebook activations, and projects are accessible.

For each component, check the logs to ensure there are no startup errors or warnings:


```
podman logs &lt;container_name&gt;
```



1. Test workflows and automation processes.

After you have confirmed that all components are functional, test critical automation workflows to ensure they operate correctly in the containerized environment:


1. Run job templates: Run several key job templates, including those with dependencies on various credential types.
1. Test workflow templates: Run workflow templates to ensure that workflow nodes run in the correct order and that the workflow completes successfully.
1. Verify execution environments: Ensure that jobs run in the appropriate execution environments and can access required dependencies.
1. Check job artifacts: Verify that job artifacts are properly stored and accessible.
1. Validate job scheduling: Test scheduled jobs to ensure they run at the expected times.

1. Validate user access and permissions.

Confirm that user accounts, teams, and roles were correctly migrated:


1. User authentication: Test login functionality with various user accounts to ensure authentication works correctly.
1. Role-based access controls: Verify that users have appropriate permissions for organizations, projects, inventories, and job templates.
1. Team memberships: Confirm that team memberships and team-based permissions are intact.
1. API access: Test API tokens and ensure that API access is functioning properly.
1. SSO integration (if applicable): Verify that Single Sign-On authentication is working correctly.

1. Confirm content synchronization and availability.

Ensure that all content sources are properly configured and accessible:


- Collection synchronization: Check that you can synchronize collections from a remote.
- Collection Upload: Check that you can upload collections.
- Collection repositories: Verify that collections are available in automation hub and can be used in execution environments.
- Project synchronization: Check that projects can sync content from source control repositories.
- External content sources: Test synchronization from automation hub and Ansible Galaxy (if configured).
- Execution environment availability: Confirm that all required execution environments are available and can be accessed by the execution nodes.
- Content dependencies: Verify that content dependencies are correctly resolved when running jobs.



**Additional resources**

-  [Troubleshooting containerized Ansible Automation Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation/troubleshooting-containerized-ansible-automation-platform)


