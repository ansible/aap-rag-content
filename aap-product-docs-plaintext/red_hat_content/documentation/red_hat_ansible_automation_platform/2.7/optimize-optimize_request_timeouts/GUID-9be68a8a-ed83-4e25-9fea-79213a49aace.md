# Optimize request timeouts
## Increase the OpenShift Route timeout

High-volume API operations can exceed the default 30-second OpenShift Route timeout. To resolve HTTP 504 or 503 errors, you must increase `client_request_timeout` in the `AnsibleAutomationPlatform` custom resource..

