# 8. Fixed issues
## 8.3. Event-Driven Ansible




- Fixed a bug where the Swagger API docs URL returned 404 error with trailing slash. (AAP-27417)
- Fixed a bug where logs contained stack trace errors inappropriately. (AAP-23605)
- Fixed a bug where the API returned error 500 instead of error 400 when a foreign key ID did not exist. (AAP-23105)
- Fix a bug where the Git hash of a project could be empty. (AAP-21641)
- Fixed a bug where an activation could fail at the start time due to authentication errors with Podman. (AAP-21067)
- Fixed a bug where a project could not get imported if it contained a malformed rulebook. (AAP-20868)
- Added **EDA_CSRF_TRUSTED_ORIGINS** , which can be set by user input or defined based on the allowed hostnames provided or determined by the installer as a default. (AAP-19319)
- Redirected all Event-Driven Ansible traffic to `    /eda/` following UI changes that require the redirect. (AAP-18989)
- Fixed target database for Event-Driven automation restore from backup. (AAP-17918)
- Fixed the automation controller URL check when installing Event-Driven Ansible without a controller. (AAP-17249)
- Fixed a bug when the membership operator failed in a condition applied to a previously saved event. (AAP-16663)
- Fixed Event-Driven Ansible nginx configuration for custom HTTPS port. (AAP-16000)
- Instead of the target service only, all Event-Driven Ansible services are enabled after installation is completed. The Event-Driven Ansible services will always start after the setup is complete. (AAP-15889)


