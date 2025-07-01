# Chapter 2. Installing the Ansible plug-ins with a Helm chart on OpenShift Container Platform




The following procedures describe how to install Ansible plug-ins in Red Hat Developer Hub instances on Red Hat OpenShift Container Platform using a Helm chart.

The workflow is as follows:

1. Download the Ansible plug-ins files.
1. Create a plug-in registry in your OpenShift cluster to host the Ansible plug-ins.
1. Add the plug-ins to the Helm chart.
1. Create a custom ConfigMap.
1. Add your custom ConfigMap to your Helm chart.
1. Edit your custom ConfigMap and Helm chart according to the required and optional configuration procedures.

Note
You can save changes to your Helm and ConfigMap after each update to your configuration. You do not have to make all the changes to these files in a single session.






