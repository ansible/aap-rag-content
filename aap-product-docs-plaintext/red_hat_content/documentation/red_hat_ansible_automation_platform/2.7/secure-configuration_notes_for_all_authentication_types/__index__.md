# Configuration notes for all authentication types

Managing authentication configuration includes updating callback URLs for OAuth and SSO authenticators and configuring timeout values for password-based authenticators.

Address these configuration requirements after setting up authenticators to maintain proper integration with external identity providers.

Managing authentication configuration helps you to:

- **Maintain OAuth and SSO authentication in Ansible Automation Platform**: Update callback URLs in your identity providers to redirect authentication flows from automation controller to platform gateway.
- **Prevent authentication request failures**: Configure layered timeout values for password-based authenticators to ensure each upstream timeout exceeds the sum of its downstream timeouts.
- **Align timeout values with your environment**: Set authenticator-specific timeout values that match the performance characteristics of your external authentication servers.

