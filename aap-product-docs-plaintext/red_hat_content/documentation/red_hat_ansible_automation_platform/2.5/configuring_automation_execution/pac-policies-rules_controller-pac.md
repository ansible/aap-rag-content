# 7. Implementing policy enforcement
## 7.3. Understanding OPA packages and rules




An OPA policy is organized in packages, which are namespaced collections of rules. The basic structure of an OPA policy looks like this:

```
package aap_policy_examples  # Package name

import rego.v1  # Import required for Rego v1 syntax

# Rules define the policy logic
allowed := {
"allowed": true,
"violations": []
}
```

The key components of the rule’s structure are:

These components together comprise the OPA policy name, which is formatted as `[package]/[rule]` . You will enter the OPA policy name when you configure enforcement points.

