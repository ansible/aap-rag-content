# 7. Red Hat Ansible Automation Platform Service on AWS Private Link Connectivity
## 7.3. Enabling AWS PrivateLink connectivity




To enable private link connectivity, submit a customer support ticket and the Red Hat team will assist you with next steps.

Note
You must create two support tickets for bi-directional connectivity: one support case for enabling AWS PrivateLink connectivity into the control plane and another one for enabling AWS PrivateLink connectivity out of the control plane.



**Procedure**

1. Navigate to [Customer support](https://access.redhat.com/support/cases/#/case/new/get-support?caseCreate=true&product=Red%20Hat%20Ansible%20Automation%20Platform%20On%20Clouds&version=AWS%20-%20Managed%20Service&seSessionId=db3c1163-09b0-4076-b27f-0ce89eb2b9e7) . The fields auto-fill, however confirm:


1. The **Account** field displays your customer account
1. The **Owner** field displays your login
1. The **Product** field displays **Red Hat Ansible Automation Platform On Clouds**
1. The **Version** field displays **AWS - Managed Service**

1. Select **Configuration** for the **What can we help you with?** section.
1. ClickContinue.
1. Use the values in the following templates to copy values into the **Title** and **Describe your problem** sections of the support request.


```
Title:    Ansible Automation Platform Service on AWS PrivateLink Template        Describe your problem:    Enable AWS PrivateLink connectivity from control plane to customer's network        Endpoint Service references are for the Endpoint Service created in the customer's VPC.        Endpoint Service name: &lt;enter here&gt;    Endpoint Service AWS region: &lt;enter here&gt;    Endpoint Service ports or port ranges: &lt;enter here&gt;        If you have multiple endpoint services, provide the values above for each endpoint service.
```


```
Title:    Ansible Automation Platform Service on AWS PrivateLink Template        Describe your problem:    Enable AWS PrivateLink connectivity from customer's network to control plane        Customer AWS account ID: &lt;enter here&gt;    Endpoint AWS region(s): &lt;enter here&gt;    URL of your AAP deployment: &lt;enter here&gt;    The existing endpoint provided for the initial region (if a PrivateLink has already been configured): &lt;enter here&gt;        If you want to setup PrivateLink for additional regions, you must send the above values for those regions.            After Red Hat has configured the control plane Endpoint Service allowed principal and supported regions, a response will be added to your support ticket to create your Endpoint and share the Endpoint Service name, which you can find at https://console.redhat.com/ansible/service.
```


1. ClickContinue.



<span id="idm139696182053424"></span>
