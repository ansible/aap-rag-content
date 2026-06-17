# Enable a custom support URL

Update the Helm configuration to redirect the default support link to your organization's specific support resources.

## Before you begin

- You have administrative access to the OpenShift Container Platform console.
- Ansible automation portal is installed in an OpenShift project.

## Procedure

1.  Log in to the OpenShift Container Platform console.
2.  In the Developer perspective, navigate to Helm.
3.  Click the More actions icon for your Ansible automation portal Helm release and select Upgrade.
4.  Select YAML view.
5.  Add the `CUSTOMER_SUPPORT_URL` environment variable to the `extraEnvVars` section:


```
redhat-developer-hub:
upstream:
backstage:
extraEnvVars:
- name: CUSTOMER_SUPPORT_URL
value: https://your-support-portal.example.com
```

6.  Click Upgrade.

## What to do next

To verify the configuration, log in to Ansible automation portal. Hover over the Support link in the upper right of the UI (next to the Create icon) and verify it points to your custom URL.
