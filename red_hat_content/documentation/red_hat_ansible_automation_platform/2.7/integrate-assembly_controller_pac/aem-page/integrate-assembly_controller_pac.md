+++
title = "Implement policy enforcement - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/integrate-assembly_controller_pac"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/integrate-integrate_with_the_external_policy_engine_open_policy_agent__opa_/", "Integrate with the external policy engine Open Policy Agent (OPA)"]]
category = "Integrate"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/integrate-assembly_controller_pac/aem-page/integrate-assembly_controller_pac.html"
last_crumb = "Implement policy enforcement"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Implement policy enforcement"
oversized = "false"
page_slug = "integrate-assembly_controller_pac"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/integrate-assembly_controller_pac"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/integrate-assembly_controller_pac/toc/toc.json"
type = "aem-page"
+++

# Implement policy enforcement

Policy enforcement at automation runtime is a feature that uses encoded rules to define, manage, and enforce policies that govern how your users interact with your Ansible Automation Platform instance. Policy enforcement automates policy management, improving security, compliance, and efficiency.

Open Policy Agent, or OPA, is a policy engine that offloads policy decisions from your Ansible instance. When it is triggered, the policy enforcement feature connects to OPA to retrieve policies specified in your configuration, and applies policy rules to your automation content. If OPA detects a policy violation, it will stop the action and give your user information about the policy violation. For more information, see *Open Policy Agent* in the Related Links section.

 **Prerequisites**

Before you can implement policy enforcement in your Ansible Automation Platform instance, you must have:

- Access to an OPA server that is reachable from your Ansible Automation Platform deployment.
- Configured Ansible Automation Platform with settings required for authenticating to your OPA server.
- Some familiarity with OPA and the Rego language, which is the language policies are written in.


For policy enforcement to work correctly, you must both configure the OPA server in your policy settings, and associate a specific policy with a particular resource. For example, a particular organization, inventory, or job template.

Note:

OPA API V1 is the only version currently supported in Ansible Automation Platform.

## Configure policy enforcement settings

You can specify how your Ansible Automation Platform instance interacts with OPA by modifying your global settings.

### Before you begin

- To configure policy enforcement, you must have administrative privileges.


Note:

If you do not configure the OPA server in your policy settings, policy evaluation will not occur when you run the job.

### Procedure

1.  From the navigation panel, select Settings> (and then)Automation Execution> (and then)Policy.
2.  Click **Edit policy settings**.
3.  On the Policy Settings page, fill out the following fields:
  

OPA Server hostname
Enter the name of the host that connects to the OPA service.

OPA server port
Enter the port that connects to the OPA service.

OPA authentication type
Select the OPA authentication type.

OPA custom authentication header
Enter a custom header to append to request headers for OPA authentication.

OPA request timeout
Enter the number of seconds until the connection times out.

OPA request retry count
Enter a figure for the number of times a request can attempt to connect to the OPA service before failing.

4.  Depending on your authentication type, you might need to fill out the following fields.   1.  If you selected Token as your authentication type:
  

OPA authentication token
Enter the OPA authentication token.

  2.  If you selected Certificate as your authentication type:
  

OPA client certificate content
Enter content of the CA certificate for mTLS authentication.

OPA client key content
Enter the client key for mTLS authentication.

OPA CA certificate content
Enter the content of the CA certificate for mTLS authentication.

5.  Beneath the heading labeled **Options**:
  

Use SSL for OPA connection
Check this box to enable an SSL/TLS connection to the OPA service.

6.  Click Save policy settings.

## Understand OPA packages and rules

An OPA policy is organized in packages, which are namespaced collections of rules. The basic structure of an OPA policy looks like this:

```rego
package aap_policy_examples  # Package name

import rego.v1  # Import required for Rego v1 syntax

# Rules define the policy logic
allowed := {
    "allowed": true,
    "violations": []
}
```
The key components of the rule’s structure are:

Package declaration
This defines the namespace for your policy.

Rules
This defines the policy’s logic and the decision that it returns.

These components together form the OPA policy name, with the format `[package]/[rule]`. Enter the OPA policy name when you configure enforcement points.
