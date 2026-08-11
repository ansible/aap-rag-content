# CVE - Bug Fixes
## Bug fixes

- Ansible automation portal
* **Survey and form rendering improvements**: Nested survey parameters, conditional form schemas, and password fields now render correctly. Survey passwords are written as secrets.

- Controller
* Fixed an issue where OIDC workload identity tokens were not applied to cloud credentials during inventory sync, because `populate_workload_identity_tokens()` did not include the cloud credential when called from `RunInventoryUpdate`. (AAP-75205)
* Fixed an issue where workflow node updates failed when the Job Template had labels without "Prompt on Launch" enabled, causing API or UI updates to prompt fields to return "Field is not configured to prompt on launch." The serializer now validates only the prompt fields included in the request rather than re-validating all persisted prompt state. (AAP-75202)
* Fixed an issue where `awxkit as_user()` failed to switch the authenticated user when requests were routed through the AAP gateway, because the gateway uses `gateway_sessionid` instead of `sessionid`. A fallback now checks `gateway_sessionid` when no cookie matches `session_cookie_name`. (AAP-75199)
* Fixed an issue where the Thycotic Secret Server (Delinea) credential plugin failed with an HTTP 500 error when resolving credentials from Delinea Platform URLs due to an older version of `python-tss-sdk`. (AAP-75198)
* Fixed an issue where at CLI failed on clean install with ModuleNotFoundError: No module named 'packaging' because setup.py listed setuptools instead of packaging as a runtime dependency after the Python 3.12 upgrade. (AAP-74277)
* Fixed an issue where schedules could not parse a valid RRULE with certain BYHOUR constraints. (AAP-72482)
- Django-ansible-base
* Fixed an issue where an authenticator map of type "allow" could not recover access once it had been set to false by an earlier deny-all rule. (AAP-75209)
* Fixed an issue where an authenticator map of type "allow" could not recover access once it had been set to false by an earlier deny-all rule. (AAP-75207)
- Hub
* Fixed an issue where Automation Hub pods experienced sustained high memory usage under idle conditions because health probes caused progressive memory growth in pulpcore worker processes, approaching configured memory limits and triggering unnecessary HPA scaling events. (AAP-68883)
- Lightspeed
* Fixed an issue where the containerized installer did not show the image used for Ansible Lightspeed chatbot BYOK configuration. (AAP-73534)
* Fixed an issue where the containerized installer did not show the image used for Ansible Lightspeed chatbot BYOK configuration. (AAP-72986)
- Platform operator
* Fixed an issue where a cluster-scoped operator could not resolve PostgreSQL database connections when components were installed in other namespaces. (AAP-75065)
- ansible.platform collection
* Fixed broken idempotency for redirect_uris and organization fields in the application module. Previously, redirect_uris was compared as a list against the API's space-separated string, and organization was compared as a name against the API's integer foreign key, causing false drift detection.
* Fixed a deletion bug in role_team_assignment where assignments were not correctly removed when state: absent was specified.
* The role_user_assignment module now raises a clear error when the specified role_definition or user does not exist on the gateway.
* Fixed false idempotency failures in the service_key module caused by the API returning $encrypted$ for secret on GET responses.
* Fixed task-level environment: variables (for example, SSL_CERT_FILE, REQUESTS_CA_BUNDLE, proxy settings) not being forwarded to the manager subprocess when using connection: ansible.platform.http.
* Fixed malformed URLs in the ansible.platform.gateway_api lookup plugin caused by scheme and hostname not being stripped from the URL builder.
* Restored async: / poll: 0 parallelism for all ansible.platform action plugins. The fork-based async mechanism that infra.aap_configuration gateway roles depend on was broken during the action plugin rewrite.
* Fixed empty-string handling for aap_request_timeout / gateway_request_timeout. The AAP built-in credential type injects an empty string when the field is not configured, which previously caused validation to fail. Empty strings are now stripped and the 10-second default is used.
* Fixed aap_validate_certs alias resolution. When aap_validate_certs: false was set via module_defaults or group, it was silently ignored. The parameter is now resolved correctly so that false is honored.
* Fixed pagination in the gateway_api lookup / search_api for relative next URLs. AAP returns the next link as a relative path which is now resolved against base_url with urljoin.
* Fixed the gateway_api lookup / search_api to support the Galaxy/Hub pagination envelope. Hub list responses use a different response shape than DRF, and return_all now handles both envelopes so /api/galaxy/ endpoints no longer silently return only the first page.
