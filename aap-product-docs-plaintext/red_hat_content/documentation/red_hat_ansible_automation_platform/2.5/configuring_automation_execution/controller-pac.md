# Chapter 7. Implementing policy enforcement




Policy enforcement at automation runtime is a feature that uses encoded rules to define, manage, and enforce policies that govern how your users interact with your Ansible Automation Platform instance. Policy enforcement automates policy management, improving security, compliance, and efficiency.

OPA, or [Open Policy Agent](https://www.openpolicyagent.org/docs/latest/) , is a policy engine that offloads policy decisions from your Ansible instance. When it is triggered, the policy enforcement feature connects to OPA to retrieve policies specified in your configuration, and applies policy rules to your automation content. If OPA detects a policy violation, it will stop the action and give your user information about the policy violation.

**Prerequisites**

Before you can implement policy enforcement in your Ansible Automation Platform instance, you must have:


- An Ansible Automation Platform 2.5 deployment with the `    FEATURE_POLICY_AS_CODE_ENABLED` feature flag set to `    TRUE` .
- Access to an OPA server that is reachable from your Ansible Automation Platform deployment.
- Configured Ansible Automation Platform with settings required for authenticating to your OPA server.
- Some familiarity with OPA and the Rego language, which is the language policies are written in.


For policy enforcement to work correctly, you must both configure the OPA server in your policy settings, and associate a specific policy with a particular resource (for example, a particular organization, inventory, or job template).

Note
OPA API V1 is the only version currently supported in Ansible Automation Platform.



