# 3. Manage containers in private automation hub
## 3.3. Populating your private automation hub container registry




By default, private automation hub does not include automation execution environments. To populate your container registry, you must push an execution environment to it.

You must follow a specific workflow to populate your private automation hub remote registry:

- Pull automation execution environments from the Red Hat Ecosystem Catalog (registry.redhat.io)
- Tag them
- Push them to your private automation hub remote registry


Important
As of **April 1st, 2025** , `quay.io` is adding three additional endpoints. As a result, customers must adjust the allow/block lists within their firewall systems lists to include the following endpoints:

-  `    cdn04.quay.io`
-  `    cdn05.quay.io`
-  `    cdn06.quay.io`


To avoid problems pulling container images, customers must allow outbound TCP connections (ports 80 and 443) to the following hostnames:

-  `    cdn.quay.io`
-  `    cdn01.quay.io`
-  `    cdn02.quay.io`
-  `    cdn03.quay.io`
-  `    cdn04.quay.io`
-  `    cdn05.quay.io`
-  `    cdn06.quay.io`


This change should be made to any firewall configuration that specifically enables outbound connections to `registry.redhat.io` or `registry.access.redhat.com` .

Use the hostnames instead of IP addresses when configuring firewall rules.

After making this change, you can continue to pull images from `registry.redhat.io` or `registry.access.redhat.com` . You do not require a `quay.io` login, or need to interact with the `quay.io` registry directly in any way to continue pulling Red Hat container images.

For more information, see [Firewall changes for container image pulls 2024/2025](https://access.redhat.com/articles/7084334) .

Ensure that the [Network ports and protocols](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/planning_your_installation/ref-network-ports-protocols_planning) listed in _Table 6.4. Execution Environments (EE)_ are available to avoid problems pulling container images.



