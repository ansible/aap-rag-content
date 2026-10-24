# Install and configure the Ansible VS Code extension
## Configure the Ansible VS Code extension for a containerized deployment
### Configure a wildcard OAuth redirect URI for OpenShift Dev Spaces

When developers use Ansible Lightspeed from OpenShift Dev Spaces in an air-gapped environment, each Dev Spaces workspace generates a unique callback URL. Instead of registering each workspace URL individually, you can register a single wildcard OAuth redirect URI that covers all workspaces.

#### Before you begin

- Ansible Lightspeed is deployed on your Ansible Automation Platform environment.
- OpenShift Dev Spaces is installed and configured for your developers.
- You have administrator access to the Ansible Lightspeed Django admin interface or the `wisdom-manage` CLI.

#### About this task

On-prem Ansible Lightspeed includes a custom OAuth application model (`wildcard_oauth2.Application`) that supports glob wildcards in both the host and path components of a redirect URI. This capability is available in Ansible Automation Platform 2.6 and later.

#### Procedure

1. Identify the redirect URI pattern for your Dev Spaces environment.
Each Dev Spaces workspace generates a callback URL in the following format:

```
https://<devspaces-host>/<user>/<workspace>/<port>/<endpoint>/callback
```

To find the exact path depth, capture the `redirect_uri` parameter from a failing `/o/authorize/` request in your browser's developer tools or server logs. Count the number of path segments between the host and `/callback`.

2. Construct the wildcard redirect URI.
Replace each dynamic path segment with `*`. For example, if the callback URL has four dynamic segments:

```
https://<devspaces-host>/*/*/*/*/callback
```

Important:
Each `*` matches exactly one path segment and does not match across `/` separators. The number of `*` segments in your wildcard pattern must match the actual number of dynamic path segments in the Dev Spaces callback URL. Wildcards in the hostname are permitted only within subdomain labels and cannot be used in the primary domain name or top-level domain. If the segment count does not match or the hostname pattern is invalid, authentication fails. For more information, see the Security considerations section.

3. Open the Ansible Lightspeed Django admin interface.
Navigate to OAuth2 Provider> (and then)Applications and select the VS Code Lightspeed OAuth Application.

Alternatively, use the `wisdom-manage` CLI to update the application.

4. Add the wildcard redirect URI to the application.
In the Redirect uris field, add the wildcard URI on a new line alongside any existing redirect URIs, such as `vscode://redhat.ansible` entries. For example:

```
vscode://redhat.ansible
https://devspaces.example.com/*/*/*/*/callback
```

5. Save the application.

#### Results

To verify the configuration, open a Dev Spaces workspace, launch the Ansible extension, and sign in to Lightspeed. The OAuth authorization-code flow should complete without requiring individual workspace registration.

#### What to do next

**Security considerations**

The wildcard pattern is anchored to the registered URI. This means:

- Suffix-spoof hosts (for example, `devspaces.example.com.attacker.io`) and off-domain hosts are rejected.
- Only URIs that match the exact pattern, including the host and path depth, are accepted.
- Wildcards (`*`) are permitted only within subdomain labels of a hostname. They cannot be used in the primary domain name or the top-level domain (the last two labels).   * Valid: `*.example.com`, `sub*.example.com`, `*.*.example.com`
* Invalid: `*.com`, `*.example.*`, `subdomain.*.com`
- Wildcard patterns in redirect network locations do not match IP addresses. For example, `http://*.0.1/...` does not match `123.123.0.1`.

To minimize risk, scope the host label as tightly as possible. Do not use wildcards in the domain portion of the URI.

