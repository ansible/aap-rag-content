# Ansible Automation Platform 2.7 patch release June 17, 2026
## Controller

- Fixed an issue where Execution Nodes were incorrectly included in the Control Plane. (AAP-78341)
- Fixed an issue where jobs would remain in Waiting indefinitely if the assigned controller node instance was deprovisioned. (AAP-78097)
- Fixed an issue where the Azure Key Vault credential plugin failed with a TypeError because the cloud_name field was not accepted by the backend function, a regression introduced when explicit typed parameters replaced **kwargs. (AAP-77748)
- Fixed an issue where setting an rrule interval to 0 caused the dispatcher to hang. (AAP-77568)
- Fixed an issue where the request_timeout field on the Ansible Automation Platform credential was not working correctly. (AAP-77341)
- Fixed an issue where populate_workload_identity_tokens() did not accept an additional list of credentials, causing workload identity token injection to fail for inventory update cloud credentials. (AAP-75205)
- Fixed an issue where workflow node updates failed when the Job Template had labels without "Prompt on Launch" enabled, because the serializer re-validated all persisted prompt state on every update instead of only the fields included in the request. (AAP-75202)
- Fixed an issue where as_user() failed to switch the authenticated user when requests went through the AAP gateway because the gateway_sessionid cookie was not checked as a fallback. (AAP-75199)
- Fixed an issue where the Thycotic Secret Server (Delinea) credential plugin failed with an HTTP 500 error when resolving credentials from Delinea Platform URLs. (AAP-75198)
- Fixed an issue where fact cache queries were expensive, degrading performance. (AAP-74523)
- Fixed an issue where awxkit failed with ModuleNotFoundError for the packaging module because install_requires listed setuptools instead of packaging after the Python 3.12 upgrade. (AAP-74277)
- Fixed an issue where analytics API requests did not respect proxy environment variables, causing DNS resolution failures in proxy environments. (AAP-73163)
- Fixed an issue where the GET /api/v2/hosts/ endpoint had slow response times at scale due to loading the large ansible_facts JSON column and an unnecessary database table JOIN in RBAC permission evaluation queries. (AAP-73161)
- Fixed an issue where schedules could not parse a valid RRULE with certain BYHOUR constraints. (AAP-72482)

