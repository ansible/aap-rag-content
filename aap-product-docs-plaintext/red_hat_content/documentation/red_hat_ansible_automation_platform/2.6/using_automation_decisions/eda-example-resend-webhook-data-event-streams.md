# 14. Event-Driven Ansible user scenarios
## 14.1. Simplified Event Routing using GitHub event streams
### 14.1.7. Resend webhook data from your event stream type

Resending webhook data allows for efficient testing of new event routing configurations. This process verifies that the event stream successfully triggers the rulebook activation using existing payloads, eliminating the need to manually recreate events.

**Procedure**

1. Go back to the **GitHub Webhook / Manage webhook** page.
2. Click the **Recent Deliveries** tab.
3. Click the ellipsis.
4. Click Redeliver. A **Redeliver payload?** window is displayed with a delivery message.
5. Click **Yes, redeliver this payload**.
6. Return to the Ansible Automation Platform to check your rule audit.

