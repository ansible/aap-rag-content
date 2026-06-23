# Execution environment definition components
## Predefined execution environment templates

Predefined templates accelerate environment setup for common use cases. AAP administrators manage which templates are available and can control access with RBAC.

| Template                  | Description                                                                                                                                                | Use cases                                                                                                                                                 |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Start from scratch**    | A blank-slate template for creating custom execution environments (loaded by default).                                                                     | Use this template when you require complete control over the base image and dependencies to build a highly customized or minimized execution environment. |
| **Networking Automation** | A template optimized for network device interaction with pre-selected networking collections (included in Helm chart but commented out by default).        | Use this template when your automation primarily interacts with switches, routers, firewalls, and other network infrastructure.                           |
| **Cloud Automation**      | A template optimized for deploying and managing cloud resources with pre-selected cloud collections (included in Helm chart but commented out by default). | Use this template when your automation targets provisioning, configuration, and management of cloud services.                                             |


Note:

Networking Automation and Cloud Automation templates require their referenced collections to be discoverable from a configured content source.
