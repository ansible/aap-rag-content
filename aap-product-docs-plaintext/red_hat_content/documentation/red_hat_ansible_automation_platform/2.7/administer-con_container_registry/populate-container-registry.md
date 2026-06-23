# Manage containers in your private automation hub
## Populate your private automation hub container registry

The automation hub remote registry is used for storing and managing automation execution environments.

When you have built or sourced an execution environment, you can push that execution environment to the registry portion of private automation hub to create a container repository. Then, you can grant your team access to the container repository, and customize the repository with a README, relevant links and other information for your team's use.

The workflow is as follows:

1.      Pull an execution environment from an external registry (like registry.redhat.io) to your local machine.

2.      Tag the image locally for your private automation hub registry.

3.      Push the image to your private automation hub.

4.      Configure access permissions and documentation (such as READMEs) within private automation hub so your teams can use the image.

Important:

As of **April 1st, 2025**, `quay.io` is adding three additional endpoints. As a result, you must adjust the allow/block lists within your firewall systems lists to include the following endpoints:

-  `cdn04.quay.io`
-  `cdn05.quay.io`
-  `cdn06.quay.io`


To avoid problems pulling container images, customers must allow outbound TCP connections (ports 80 and 443) to the following hostnames:

-  `cdn.quay.io`
-  `cdn01.quay.io`
-  `cdn02.quay.io`
-  `cdn03.quay.io`
-  `cdn04.quay.io`
-  `cdn05.quay.io`
-  `cdn06.quay.io`


This change should be made to any firewall configuration that specifically enables outbound connections to `registry.redhat.io` or `registry.access.redhat.com`.

Use the hostnames instead of IP addresses when configuring firewall rules.

After making this change, you can continue to pull images from `registry.redhat.io` or `registry.access.redhat.com`. You do not require a `quay.io` login, or need to interact with the `quay.io` registry directly in any way to continue pulling Red Hat container images.

