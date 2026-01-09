# 7. Target environment
## 7.1. Container-based Ansible Automation Platform
### 7.1.4. Validating the target environment




After completing the migration, validate that all components in your target environment function correctly.

**Procedure**

1. Verify all migrated components function correctly.


1. Platform gateway: Access the Ansible Automation Platform URL at `        https://&lt;gateway_hostname&gt;/` and verify that the dashboard loads correctly. Check that the platform gateway service is running and connected to automation controller.
1. Automation controller: Under **Automation Execution** , check that projects, inventories, and job templates are present and configured.
1. Automation hub: Under **Automation Content** , verify that collections, namespaces, and their contents are visible.
1. Event-Driven Ansible (if applicable): Under **Automation Execution Decisions** , verify that rule audits, rulebook activations, and projects are accessible.
1. For each component, check the logs to ensure there are no startup errors or warnings:


```
podman logs &lt;container_name&gt;
```



1. Test workflows and automation processes.


1. Run job templates: Run several key job templates, including those with dependencies on various credential types.
1. Test workflow templates: Run workflow templates to ensure that workflow nodes run in the correct order and that the workflow completes successfully.
1. Verify execution environments: Ensure that jobs run in the appropriate execution environments and can access required dependencies.
1. Check job artifacts: Verify that job artifacts are properly stored and accessible.
1. Validate job scheduling: Test scheduled jobs to ensure they run at the expected times.

1. Validate user access and permissions.


1. User authentication: Test login functionality with various user accounts to ensure authentication works correctly.
1. Role-based access controls: Verify that users have appropriate permissions for organizations, projects, inventories, and job templates.
1. Team memberships: Confirm that team memberships and team-based permissions are intact.
1. API access: Test API tokens and ensure that API access is functioning properly.
1. SSO integration (if applicable): Verify that Single Sign-On authentication is working correctly.

1. Confirm content synchronization and availability.


1. Collection synchronization: Check that you can synchronize collections from a remote.
1. Collection Upload: Check that you can upload collections.
1. Collection repositories: Verify that automation hub makes collections available and that execution environments can use them.
1. Project synchronization: Check that projects can sync content from source control repositories.
1. External content sources: Test synchronization from automation hub and Ansible Galaxy (if configured).
1. Execution environment availability: Confirm that all required execution environments exist and that execution nodes can access them.
1. Content dependencies: Verify that the system correctly resolves content dependencies when running jobs.



**Additional resources**

-  [Troubleshooting containerized Ansible Automation Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/troubleshooting-containerized-ansible-automation-platform)


