# Configure JWT_Algorithms manually

To resolve the authentication failure, manually provide the list of supported algorithms in the platform gateway configuration.

## Procedure

1.  From the navigation panel, select Access Management> (and then)Authentication Methods.
2.  Select your OIDC authenticator from the list.
3.  Click Edit authentication and locate the **OIDC JWT Algorithm(s)** field.
4.  Enter the list of supported algorithms as a YAML list or a JSON array. These algorithms are typically available from your IdP’s OpenID Connect (OIDC) discovery endpoint.  **Example**

```
[
"PS384",
"ES384",
"RS384",
"HS256",
"HS512",
"ES256",
"RS256",
"HS384",
"ES512",
"PS256",
"PS512",
"RS512"
]
```

5.  Save your changes. The system uses these specified algorithms for token verification, resolving any authentication failures related to their absence.
