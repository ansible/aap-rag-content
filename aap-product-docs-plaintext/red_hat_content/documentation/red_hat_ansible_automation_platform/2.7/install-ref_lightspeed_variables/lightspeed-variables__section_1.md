# Red Hat Ansible Lightspeed variables
## Bring your own Knowledge for automation intelligent assistant variables

Inventory file variables for the automation intelligent assistant with BYOK.

| Parameter                                  | Description                                                                                                                  | Default value |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `lightspeed_chatbot_byok_image`            | The full registry path to your RAG image. For example,`lightspeed_chatbot_byok_image: quay.io/my-custom-image/my-rag`        | n/a           |
| `lightspeed_chatbot_byok_score_multiplier` | The score multiplier for BYOK content priority. It adjusts how heavily the AI weighs your custom data versus base knowledge. | `1.2`         |
