# Troubleshoot failed event-driven automation triggers
## Troubleshoot event streams that fail to send events

Diagnose issues where an event stream is receiving data but failing to forward it, ensuring proper connectivity and correct credential setup.

### Procedure

Try the following options to resolve this. 1.  Ensure that each of your event streams in Event-Driven Ansible controller is *not* in **Test** mode . This means activations would not receive the events.
2.  Verify that the origin service is sending the request properly.
3.  Check that the network connection to your platform gateway instance is stable. If you have set up event streams, this is the entry of the event stream request from the sender.
4.  Verify that the proxy in the platform gateway is running.
5.  Confirm that the event stream worker is up and running, and able to process the request.
6.  Verify that your credential is correctly set up in the event stream.
7.  Confirm that the request complies with the authentication mechanism determined by the set credential (for example, basic must contain a header with the credentials or HMAC must contain the signature of the content in a header, and similar). Note:
The credentials might have been changed in Event-Driven Ansible controller, but not updated in the origin service.

8.  Verify that the rulebook that is running in the activation reacts to these events. This would indicate that you wrote down the event source *and* added actions that consume the events coming in. Otherwise, the event does reach the activation but there is nothing to activate it.
9.  If you are using self-signed certificates, you might want to disable certificate validation when sending webhooks from vendors. Most of the vendors have an option to disable certificate validation for testing or non-production environments.
