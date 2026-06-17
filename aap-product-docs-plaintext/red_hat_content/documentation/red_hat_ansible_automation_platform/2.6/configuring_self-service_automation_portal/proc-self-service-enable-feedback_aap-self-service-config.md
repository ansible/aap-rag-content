# Chapter 8. Enabling feedback to Red Hat

Enable the optional feedback form to allow users to submit suggestions and general feedback directly through the portal interface.

**Prerequisites**

- You have administrative access to the OpenShift Container Platform console.
- The self-service automation portal is installed in an OpenShift project.

**Procedure**

1. Log in to the OpenShift Container Platform console.

2. In the **Developer** perspective, navigate to **Helm**.

3. Click the **More actions** icon for your self-service automation portal Helm release and select **Upgrade**.

4. Select **YAML view**.

5. Locate the `ansible` section and set the `feedback.enabled` value to `true`:

ansible:
feedback:
enabled: true

6. Click Upgrade

**Verification**

1. Log in to the self-service automation portal.
2. Confirm that the Feedback button is visible in the bottom-left corner of the console.

