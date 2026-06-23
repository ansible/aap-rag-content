# Deploy the automation intelligent assistant
## Change your LLM model

If you have already deployed Ansible Lightspeed intelligent assistant but want to change your LLM model, you can create a new chatbot configuration secret for the new LLM model.

### About this task

Alternatively, if you want to use the same chatbot configuration secret, you must delete and redeploy the Ansible Lightspeed intelligent assistant.

### Procedure

-  To create and use a new chatbot configuration secret:
1.  [Create a new chatbot configuration secret](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_operator_install_operator "As a system administrator, you can use Ansible Automation Platform Operator to deploy new Ansible Automation Platform instances in your OpenShift environment.") with a different name for the new LLM model.
2.  [Update the YAML file of the Ansible Automation Platform operator](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_operator_install_operator "As a system administrator, you can use Ansible Automation Platform Operator to deploy new Ansible Automation Platform instances in your OpenShift environment.") with the new chatbot configuration secret name. The Ansible Automation Platform operator detects the new configuration and redeploys the Ansible Lightspeed intelligent assistant.

3.  Verify that the chat interface service is running successfully. See the verification steps mentioned in the topic [Update the YAML file of the Ansible Automation Platform operator](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_operator_install_operator "As a system administrator, you can use Ansible Automation Platform Operator to deploy new Ansible Automation Platform instances in your OpenShift environment.").  Important:
Do not update the existing chatbot configuration secret with the new LLM model, as the reconciliation logic does not check the updates made to the secret.

-  To use the same chatbot secret by deleting and redeploying the Ansible Lightspeed intelligent assistant:
1.  Disable the Ansible Lightspeed operator instance:

1. Navigate to Operators> (and then)Installed Operators.
2. From the list of installed operators, select **Ansible Automation Platform**.
3. Locate and select the Ansible Automation Platform custom resource.
4. Select the **YAML** tab and under the `spec:` section for `lightspeed` category, specify `disabled:true`.
5. Click **Save**.

2.  Delete the Ansible Lightspeed operator instance:

1. Navigate to Operators> (and then)Installed Operators.
2. From the list of installed operators, select **Ansible Lightspeed** and delete the operator.

3.  Re-enable the Ansible Automation Platform instance:

1. Navigate to Operators> (and then)Installed Operators.
2. From the list of installed operators, select **Ansible Automation Platform**.
3. Locate and select the Ansible Automation Platform custom resource.
4. Select the **YAML** tab and under the `spec:` section for `lightspeed` category, specify `disabled:false`.
5. Click **Save**.
