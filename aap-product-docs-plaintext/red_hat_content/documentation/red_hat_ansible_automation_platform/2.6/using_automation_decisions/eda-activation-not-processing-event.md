# 8. Rulebook activations troubleshooting
## 8.4. Events are not being processed by rulebook activation




Troubleshoot why a running rulebook activation is failing to process events, focusing on common causes like source definition mismatches or internal processing errors.

**Procedure**

1.  **Check the rulebook source:** Review the source plugin defined in your rulebook YAML (for example, ansible.eda.webhook, ansible.eda.kafka).
1.  **Verify event input:** Confirm that the events you are sending to Event-Driven Ansible controller are compatible with the source plugin defined in the rulebook. If the rulebook expects a Kafka message, it cannot process a generic webhook event.
1.  **Confirm activation mapping:** If you are using event streams, ensure the correct event stream is mapped to the rulebook during the activation setup. A mismatch here will result in the activation receiving no data.


