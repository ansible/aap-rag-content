# 1. Terraform integration
## 1.1. About the Terraform integration
### 1.1.1. Introduction




Many organizations find themselves using both Ansible Automation Platform and Terraform, recognizing that these two open-source IT tools can work in harmony to create an improved experience for developers and operations teams. While Terraform excels at Infrastructure as Code (IaC) for provisioning and de-provisioning cloud resources, Ansible Automation Platform is a versatile, all-purpose automation solution ideal for configuration management, application deployment, and orchestrating complex IT workflows across diverse domains.

This integration directly addresses common challenges such as managing disparate automation tools, ensuring consistent configuration across hybrid cloud environments and accelerating deployment cycles. By bringing together Terraform’s declarative approach to infrastructure provisioning with Ansible Automation Platform’s procedural approach to configuration and orchestration, users can achieve:

-  **Optimized costs:** Reduce cloud waste, minimize manual processes, and combat tool sprawl. This integration can lead to a significant reduction in infrastructure costs and a high return on investment.
-  **Reduced risk:** Lower the risk of breaches, enforce policies, and significantly decrease unplanned downtime. The ability to review Terraform plan output before applying it in a workflow, with approval steps, enhances security and compliance.
-  **Faster time to value:** Boost developer productivity and deploy new compute resources more rapidly, leading to a faster time to market. This is achieved through unified lifecycle management and automation for Day 0 (provisioning), Day 1 (configuration), and Day 2 (ongoing management) operations.


This integration supports various implementation workflows to support diverse needs:

-  **Ansible-initiated workflow:** Ansible Automation Platform can directly call Terraform for provisioning within comprehensive, end-to-end automation workflows. This allows Ansible Automation Platform users to leverage Terraform’s provisioning capabilities while maintaining Ansible Automation Platform as their primary platform for configuration and lifecycle management.
-  **Terraform community-initiated workflow:** Community-edition users can migrate to Terraform Enterprise or HCP Terraform, and then integrate the Ansible Automation Platform capabilities.
-  **Terraform-initiated workflow:** For existing Terraform users, Terraform can directly call Ansible Automation Platform at the end of provisioning for a more seamless and secure workflow. This enables Terraform users to enhance their immutable infrastructure automation with Ansible Automation Platform Day 2 automation capabilities and manage infrastructure updates and lifecycle events.


By enabling direct calls between Ansible Automation Platform and Terraform, organizations can unlock time to value by creating combined workflows, reduce risk through enhanced product integrations, and enhance Infrastructure-as-Code with Ansible Automation Platform content and practices. This allows for unified lifecycle management, enabling tasks from initial provisioning and configuration to ongoing health checks, incident response, patching, and infrastructure optimization.

