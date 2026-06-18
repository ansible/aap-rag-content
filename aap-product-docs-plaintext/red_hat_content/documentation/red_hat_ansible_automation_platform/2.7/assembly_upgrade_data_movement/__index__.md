# Identity and access management migration during upgrade

When upgrading from a version of Ansible Automation Platform that predates the platform gateway, Identity Access Management (IAM) data, including users, teams, organizations, their memberships, and associated roles, is migrated from automation controller and automation hub to platform gateway.

This migration establishes automation controller as the primary source of IAM data for platform gateway, ensuring continuity of user memberships and appropriate platform-level role assignments.

Note:

If your current version is more than one minor release behind the target version, upgrade directly to the target version rather than performing intermediate upgrades. A direct upgrade is less complex.
