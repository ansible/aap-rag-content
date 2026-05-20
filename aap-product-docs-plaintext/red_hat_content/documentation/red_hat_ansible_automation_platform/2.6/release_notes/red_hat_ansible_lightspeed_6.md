# 9. Patch releases
## 9.7. Ansible Automation Platform patch release November 19, 2025
### 9.7.3. Red Hat Ansible Lightspeed

#### 9.7.3.1. Features

- Added support for 3rd party model providers OpenAI.(AAP-58291)
- Added support for 3rd party model providers Azure.(AAP-58290)

#### 9.7.3.2. Enhancements

- Upgraded Lightspeed Core Stack to 0.3.0.(AAP-55681)
- Added ALIA support `lightspeed-stack` 0.3.0 and `llama-stack` 0.2.22.(AAP-58136)
- Upgraded Ansible Lightspeed intelligent assistant to `Lightspeed-core` 0.3.0.(AAP-56629)
- Added ALIA support for Azure provider.(AAP-56511)
- Added ALIA support for OpenAI provider.(AAP-56509)
- Made changes required to support `llama-stack` 0.2.22.(AAP-58361)

#### 9.7.3.3. Bug Fixes

- Fixes an issue where the Red Hat Ansible Lightspeed assistant returned raw `tool_call` JSON instead of natural language answers due to improper processing in Ansible Automation Platform 2.6 with granite-3.3-8b. This compromised user experience by exposing internal details.(AAP-57513)
- Fixed an issue where the user would be scrolled to the bottom of the chat history if they clicked **thumbs up/thumbs down** on a previous message.(AAP-58438)
- Fixed an issue where during the upgrade of `chatbot-api`, the new one is stuck in pending state waiting until PVC is removed.(AAP-57376)

#### 9.7.3.4. Known Issues

- If you are using an IBM Granite 3.3 AI model series in your Ansible Lightspeed intelligent assistant deployment, there may be a delay of ~1 minute in receiving a chat response. As a workaround, restart the chat session.(AAP-58186)

