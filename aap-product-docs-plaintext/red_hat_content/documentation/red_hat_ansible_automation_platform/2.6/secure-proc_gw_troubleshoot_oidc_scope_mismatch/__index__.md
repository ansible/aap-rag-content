# Troubleshoot Generic OIDC scope mismatches

Authentication fails when the Identity Provider (IdP) does not support the default scopes automatically appended by the system.

## About this task

To prevent the system from appending this default scope, you must add a setting to your authenticator configuration.

## Procedure

1.  From the navigation panel, select Access Management> (and then)Authentication Methods.
2.  Select your OIDC authenticator from the list.
3.  Click Edit authentication.
4.  In the **Additional Authenticator Fields** section, add the following attribute and value. This input box supports either YAML or JSON. Ensure you add this key-value pair on a new line if there are other fields present:


```yaml
IGNORE_DEFAULT_SCOPE: True
```

5.  Save your changes. The authenticator now only uses the scopes you explicitly defined, resolving any authentication failures related to unsupported scopes.
