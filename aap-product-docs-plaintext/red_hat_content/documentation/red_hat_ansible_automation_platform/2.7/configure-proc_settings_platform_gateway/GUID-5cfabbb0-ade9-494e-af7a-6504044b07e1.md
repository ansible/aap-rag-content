# Platform gateway
## Configure system settings

Establish core automation controller operations by configuring proxy trusts, telemetry integration, default execution environments, and administrator permissions to ensure your platform integrates securely with your network infrastructure.

### Procedure

1.  Navigate to Settings> (and then)Automation Execution> (and then)System.
2.  Click Edit.
3.  Configure the necessary options to achieve your administrative goals:


Ensure services generate correct links
Define the Base URL of the service so external integrations (like notifications) can accurately point back to the controller.

Secure reverse proxy connections
If your controller sits behind a load balancer or reverse proxy, configure the Proxy IP allowed list to restrict which IPs are trusted for custom `REMOTE_HOST_HEADERS`.  Note:
Leaving this empty trusts these headers unconditionally.

Ensure accurate IP identification behind a proxy
Configure Remote Host Headers to specify which HTTP headers (e.g., `HTTP_X_FORWARDED_FOR`) the system uses to identify remote hostnames.  Important:
When you need to establish a hard directive for your infrastructure, define your settings within a server file (such as Python or YAML) or an environment variable. The platform treats these server-level files as the official source of truth. If you use this method, UI fields like **Remote Host Headers** become read-only to prevent interface changes from overriding your established configurations.

Synchronize with Red Hat services
Input your Red Hat Client ID and Client Secret for both Analytics and Subscriptions to enable telemetry, retrieve subscription data, and access content.

Establish a fallback runtime environment
Define a Global default execution environment to ensure jobs can run even if a specific job template lacks an assigned environment.

Utilize legacy Python environments
Specify Custom virtual environment paths (one per line) to instruct the controller where to find locally managed environments.

Manage telemetry reporting
Toggle Gather data for Automation Analytics to enable or disable telemetry. If enabled, control the reporting frequency using the Automation Analytics Gather Interval and verify the destination through the Automation Analytics upload URL.

Control managed node licensing
Define your subscription usage model to determine how hosts are counted. Choose whether to track historical unique nodes (allowing deletion of unused nodes) or operate with no subscription tracking for host metrics.

Maintain an audit trail
Toggle Enable Activity Stream and Enable Activity Stream for Inventory Sync to capture detailed logs of system changes and inventory updates.

Delegate or restrict administrator permissions
Use All Users Visible to Organization Admins and Organization Admins Can Manage Users and Teams to dictate cross-organization visibility and user creation rights.  Tip:
Disable the management toggle if your users are centrally managed using LDAP.

4.  Click Save to apply your configurations.

