# Ansible Automation Platform 2.7 patch release June 17, 2026
## Platform-operator

- Fixed an issue where Hub nginx and gunicorn timeout values were not derived from the gateway client_request_timeout annotation, causing 502 errors during long-running operations such as content uploads and Collections as Code workflows. (AAP-78055)
- Fixed an issue where the gateway operator failed to reconcile after HA/DR failback due to a stale OAuth2 token that was not properly validated or regenerated. (AAP-77512)
- Fixed an issue where the Lightspeed status URL was not reported when using ingress or none as the ingress type, which could cause the gateway operator to wait indefinitely for Lightspeed readiness. (AAP-76781)
