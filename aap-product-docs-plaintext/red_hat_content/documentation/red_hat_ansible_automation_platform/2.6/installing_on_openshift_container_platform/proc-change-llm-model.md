# 6. Deploying the Ansible Lightspeed intelligent assistant on OpenShift Container Platform
## 6.2. Deploying the Ansible Lightspeed intelligent assistant
### 6.2.3. Changing your LLM model




If you have already deployed Ansible Lightspeed intelligent assistant but want to change your LLM model, you can create a new chatbot configuration secret for the new LLM model.

Alternatively, if you want to use the same chatbot configuration secret, you must delete and redeploy the Ansible Lightspeed intelligent assistant.

**Procedure**

- To create and use a new chatbot configuration secret:


1.  [Create a new chatbot configuration secret](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/installing_on_openshift_container_platform/index#proc-create-chatbot-config-secret_deploying-chatbot-operator) with a different name for the new LLM model.
1.  [Update the YAML file of the Ansible Automation Platform operator](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/installing_on_openshift_container_platform/index#proc-update-aap-operator-chatbot_deploying-chatbot-operator) with the new chatbot configuration secret name.

The Ansible Automation Platform operator detects the new configuration and redeploys the Ansible Lightspeed intelligent assistant.


1. Verify that the chat interface service is running successfully. See the verification steps mentioned in the topic [Update the YAML file of the Ansible Automation Platform operator](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/installing_on_openshift_container_platform/index#proc-update-aap-operator-chatbot_deploying-chatbot-operator) .

Important
Do not update the existing chatbot configuration secret with the new LLM model, as the reconciliation logic does not check the updates made to the secret.





- To use the same chatbot secret by deleting and redeploying the Ansible Lightspeed intelligent assistant:


1. Disable the Ansible Lightspeed operator instance:


1. Navigate toOperators→Installed Operators.
1. From the list of installed operators, select **Ansible Automation Platform** .
1. Locate and select the Ansible Automation Platform custom resource.
1. Select the **YAML** tab and under the `            spec:` section for `            lightspeed` category, specify `            disabled:true` .
1. Click **Save** .

1. Delete the Ansible Lightspeed operator instance:


1. Navigate toOperators→Installed Operators.
1. From the list of installed operators, select **Ansible Lightspeed** and delete the operator.

1. Re-enable the Ansible Automation Platform instance:


1. Navigate toOperators→Installed Operators.
1. From the list of installed operators, select **Ansible Automation Platform** .
1. Locate and select the Ansible Automation Platform custom resource.
1. Select the **YAML** tab and under the `            spec:` section for `            lightspeed` category, specify `            disabled:false` .
1. Click **Save** .




