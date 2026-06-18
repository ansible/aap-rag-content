# Ansible plug-ins for Red Hat Developer Hub

Ansible plug-ins for Red Hat Developer Hub deliver an Ansible-first user experience that simplifies the automation experience for Ansible users of all skill levels.

The Ansible plug-ins provide:

- A customized home page and navigation tailored to Ansible users.
- Software templates for creating Ansible playbook and collection projects that follow best practices.
- Curated Ansible learning paths to help users new to Ansible.
- Links to supported development environments and tools with opinionated configurations.


The `automation-portal` OCI bundle includes the following plug-ins:

*Table 1. Ansible plug\-ins for Red Hat Developer Hub*

| Plug-in                                                    | Type     | Purpose                                                                 |
| ---------------------------------------------------------- | -------- | ----------------------------------------------------------------------- |
| `ansible-plugin-backstage-rhaap`                           | Frontend | Ansible landing page, navigation, and UI components                     |
| `ansible-plugin-backstage-self-service`                    | Frontend | Scaffolder field extensions for AAP token and resource picker           |
| `ansible-plugin-scaffolder-backend-module-backstage-rhaap` | Backend  | Scaffolder actions for creating Ansible content                         |
| `ansible-backstage-plugin-catalog-backend-module-rhaap`    | Backend  | Catalog entity provider for syncing AAP organizations, users, and teams |
