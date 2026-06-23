# Implement policy enforcement
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
