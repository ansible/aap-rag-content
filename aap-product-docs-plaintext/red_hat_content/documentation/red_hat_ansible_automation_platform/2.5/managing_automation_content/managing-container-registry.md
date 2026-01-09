# 3. Manage containers in private automation hub
## 3.1. Managing your private automation hub registry




You do not build container images directly inside private automation hub. Instead, use the following workflow to populate and manage your registry.

**Procedure**

1. Pull an execution environment from an external registry (like registry.redhat.io) to your local machine.
1. Tag the image locally for your private automation hub registry.
1. Push the image to your private automation hub.
1. Configure access permissions and documentation (such as READMEs) within private automation hub so your teams can use the image.


