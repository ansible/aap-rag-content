# Set up Red Hat Ansible Lightspeed on-premise deployment

As an administrator, you can deploy Ansible Lightspeed on-premise and connect it to IBM watsonx Code Assistant. Once the deployment is complete, you can use the Ansible Lightspeed service through the Ansible Visual Studio (VS) Code extension.

Note:

- Red Hat Ansible Lightspeed on-premise deployments are supported on Red Hat Ansible Automation Platform version 2.4 and later.
- The IBM Cloud service instance of IBM watsonx Code Assistant is available in the following data centers:
* Dallas (`us-south`)
* Frankfurt (`eu-de`)
* Sydney (`au-syd`) (Essentials plan only)


Ansible Lightspeed cloud deployments are configured to connect exclusively to the US (Dallas) IBM data center. Attempts to connect from non-US data centers will result in connection failure. If you want to use a non-Dallas IBM data center, then you must set up Ansible Lightspeed in hybrid deployment model. For more information about IBM’s supported data centers, see the topic Setting up your watsonx Code Assistant for Red Hat Ansible Lightspeed service in *IBM watsonx Code Assistant* documentation.

