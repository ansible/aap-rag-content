# Chapter 7. Enabling custom support URL

Update the Helm configuration to redirect the default support link to your organization’s specific support resources.

**Prerequisites**

- You have administrative access to the OpenShift Container Platform console.
- The self-service automation portal is installed in an OpenShift project.

**Procedure**

1. Log in to the OpenShift Container Platform console.

2. In the **Developer** perspective, navigate to **Helm**.

3. Click the **More actions** icon for your self-service automation portal Helm release and select **Upgrade**.

4. Select **YAML view**.

5. Add the `CUSTOMER_SUPPORT_URL` environment variable to the `extraEnvVars` section:

redhat-developer-hub:
upstream:
backstage:
extraEnvVars:
- name: CUSTOMER_SUPPORT_URL
value: https://your-support-portal.example.com

6. Click Upgrade.

**Verification**

1. Log in to the self-service automation portal.
2. Hover over the **Support** link in the upper right of the UI (next to the **Create** icon) and verify it points to your custom URL.

