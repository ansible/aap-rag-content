# Set up permissions for custom self-service templates
## Verify RBAC

This procedure describes how to verify that the role you set up is working correctly.

### Procedure

1.  Verify that users with permissions can use a template:
1.  Log in to Ansible automation portal as a user who is a member of a team that has been enabled to use a role.
2.  Verify that RBAC is applied and that the user can use the templates that you enabled for the role.
2.  Log out of Ansible automation portal.
3.  Verify that users without permissions can not see or use a template:
1.  Log in to Ansible automation portal as a user who is not a member of the new team that has been enabled to use the role.
2.  Verify that RBAC is applied and that the user cannot use the templates that you enabled for the role.
4.  Log out of Ansible automation portal.

