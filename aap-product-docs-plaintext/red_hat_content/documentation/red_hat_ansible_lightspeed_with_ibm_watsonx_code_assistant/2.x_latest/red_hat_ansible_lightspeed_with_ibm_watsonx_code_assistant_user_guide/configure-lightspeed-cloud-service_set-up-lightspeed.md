# 4. Setting up Red Hat Ansible Lightspeed for your organization
## 4.2. Setting up Red Hat Ansible Lightspeed cloud service

As a Red Hat customer portal administrator, you must configure Red Hat Ansible Lightspeed cloud service to connect to your IBM watsonx Code Assistant instance.

Note

The IBM Cloud service instance of IBM watsonx Code Assistant is available in the following data centers:

- Dallas (`us-south`)
- Frankfurt (`eu-de`)
- Sydney (`au-syd`) (Essentials plan only)

Ansible Lightspeed cloud deployments are configured to connect exclusively to the US (Dallas) IBM data center. Attempts to connect from non-US data centers will result in connection failure. If you want to use a non-Dallas IBM data center, then you must set up Ansible Lightspeed in [hybrid deployment model](#overview-lightspeed-onpremise_configuring-lightspeed-onpremise "4.3.1.&nbsp;Overview"). For more information about IBM’s supported data centers, see the topic [Setting up your watsonx Code Assistant for Red Hat Ansible Lightspeed service](https://cloud.ibm.com/docs/watsonx-code-assistant) in *IBM watsonx Code Assistant* documentation.

