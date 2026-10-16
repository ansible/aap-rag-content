+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_organizations"
template = "docs/aem-title.html"
title = "Structure groups and resources with organizations - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_managing_access/", "Manage access with role-based access control"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_organizations/aem-page/secure-assembly_controller_organizations.html"
last_crumb = "Structure groups and resources with organizations"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Structure groups and resources with organizations"
oversized = "false"
page_slug = "secure-assembly_controller_organizations"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_organizations"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_organizations/toc/toc.json"
type = "aem-page"
+++

# Structure groups and resources with organizations

Administrators use organizations to group resources. Assigning a user or team to an organization grants access to its resources. Team membership and organization membership are managed independently.

Adding a user to a team within an organization does not automatically make the user a member of that organization. To give a user full access to organization-level resources, you must add the user to both the team and the organization separately.

Important:

If you use external authentication such as LDAP or SAML to map users to teams, you must also create separate mappings for the corresponding organizations. Users do not inherit organization membership through team membership*.*

After you have created an organization, Ansible Automation Platform displays the organization details. You can then manage resources such as access and execution environments for the organization.

Ansible Automation Platform automatically creates a default organization. If you have a self-support level license, you have only the default organization available and must not delete it.
