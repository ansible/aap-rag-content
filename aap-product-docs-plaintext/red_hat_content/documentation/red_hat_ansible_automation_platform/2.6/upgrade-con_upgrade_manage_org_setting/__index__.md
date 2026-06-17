# The `MANAGE_ORGANIZATION_AUTH` setting

The automation controller setting previously called **Organization Admins Can Manage Users and Teams** in the UI (or `MANAGE_ORGANIZATION_AUTH` in the API) controls whether an organization administrator can create users and teams.

This setting now exists in both platform gateway and automation controller in Ansible Automation Platform 2.6. During an upgrade the value from automation controller is imported into the platform gateway server. If you decide to change the value of this setting ensure that you change it to the same values in both the platform gateway and automation controller.

Important:

For environments with automation running directly against automation controller, maintain a consistent value for `MANAGE_ORGANIZATION_AUTH` across both automation controller and platform gateway to avoid unexpected behavior.
