# Install the Ansible automation portal Helm chart
## Verify the installation

Verify the Helm chart installation from the OpenShift Container Platform web console.

### Procedure

1.  In a browser, log in to your OpenShift instance.
2.  In the Developer view, navigate to the Topology view for the namespace where you deployed the Helm chart.
The deployment appears with the label `D` on the icon. The name of the deployment is `<installation-name>-backstage`, for example `<my-self-service-automation-portal-backstage>`.

While it is deploying, the icon is light blue. The color changes to dark blue when deployment is complete.

*Figure 1. OpenShift deployment topology view*
![Deployment on OpenShift console](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/self-service-verify-helm-install.png)
