# Optimize request timeouts
## Increase the OpenShift Route timeout
### Results

Confirm that the `haproxy.router.openshift.io/timeout` annotation in the **Route** reflects the new value.

- Navigate to **Networking → Routes** in the OpenShift console. Select the route for your **Ansible Automation Platform** instance.

- Verify the **Annotations** section contains the updated timeout value.
