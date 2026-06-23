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
