# Structure groups and resources with organizations

Administrators use organizations to group resources. Assigning a user or team to an organization grants access to its resources. Team membership and organization membership are managed independently.

Adding a user to a team within an organization does not automatically make the user a member of that organization. To give a user full access to organization-level resources, you must add the user to both the team and the organization separately.

Important:

If you use external authentication such as LDAP or SAML to map users to teams, you must also create separate mappings for the corresponding organizations. Users do not inherit organization membership through team membership*.*

After you have created an organization, Ansible Automation Platform displays the organization details. You can then manage resources such as access and execution environments for the organization.

Ansible Automation Platform automatically creates a default organization. If you have a self-support level license, you have only the default organization available and must not delete it.
