# Ansible Automation Platform 2.7 patch release August 4, 2026 (2.7.4)
## Ansible Lightspeed / MCP Server

- Add OAuth Protected Resource Metadata (RFC 9728) (AAP-81961)

## **Metrics Service**

- Added support for collecting data relating to indirect node counts once the feature flag is enabled. (AAP-80160, AAP-80159)

## Enhancements

## Automation Platform Gateway

- The resource migration performed during platform startup (`migrate_service_data`) now uses bulk processing, significantly reducing migration time for large deployments. (AAP-84084)
- The `migrate_service_data` management command role imports have been optimized to run faster. (AAP-80781)
- Role assignment migration in migrate_service_data now uses a database backed PK (primary key) cursor instead of re-fetching and processing all assignments on every run. (AAP-79711)
- `migrate_service_data` management command now emits status logs every 5% and has an optional --log-file parameter that can be used to write structured logs to a file. (AAP-79710)
- Added gateway-manage rotate_secret_key command to re-encrypt all gateway database secrets under a new `SECRET_KEY`, with --dry-run and --use-custom-key support. (AAP-77152)
- Adds the ability to configure a maximum additional concurrent login session (above 1) limit via the setting `MAX_EXTRA_SESSIONS_PER_USER` (AAP-76832)

## Metrics Service and Automation Dashboard

- Restricting the endpoints to admin and system auditor (AAP-83875)

## **Automation Platform UI**

- Cached jobEventToRows results to avoid redundant computation and improve performance. (AAP-83461)
- Tooltip language updated for Schedule Rules (AAP-83112)
- Messages updated on Empty State pages (AAP-81386)

## **Automation Platform Gateway / Platform Operator**

- The Envoy proxy container now has its own configurable resource section (spec.proxy) separate from the API container. A new spec.proxy.concurrency field controls the number of Envoy worker threads via --concurrency, preventing unbounded thread spawning on large nodes. The proxy container also gets its own resource_requirements and security_context fields. Default CPU limit is set to 256 cores and memory request to 750Mi. (AAP-79993)

## **Containerized installer**

- The containerized installer now displays the progress log file location before starting a merge organization operation, so administrators can monitor long-running migrations. (AAP-80777)
- Add `MCP_SERVER_URL` environment variable (AAP-81958)

## **Automation Controller**

- Replaced a 4-way OR in `UnifiedJobAccess.filtered_queryset()` with UNION ALL. The OR forced PostgreSQL to evaluate all four RBAC branches in a single query plan, preventing branch-specific index optimization. Includes preventive pagination optimization to avoid the same COUNT regression fixed in AAP-83773. (AAP-83610)
- Replaced per-organization correlated subqueries for user and admin counts with a single conditional-aggregation query. The original pattern executed two subqueries per organization row, making DB load proportional to the number of organizations. (AAP-83344)
- Fixed a LEFT JOIN fan-out in the user list RBAC query that traversed through RBAC role evaluation tables. The join pattern caused massive row multiplication proportional to the number of RBAC role assignments. Replaced with semi-join subqueries that short-circuit on first match. (AAP-83190)
- Fixed high latency on the User Access tab caused by N+1 serialization. Replaced with an EXISTS semi-join pattern that significantly reduces query count and response time. (AAP-82626)

## **Django-ansible-base**

- Optimized the `roleuserassignment_select_all_roles` query used by the RBAC visible-items check. The original query pattern was one of the highest contributors to total DB time at scale. (AAP-81869)
- Service-index role assignment endpoints now support service-scoped filtering, reducing sync traffic by ~67% in multi-service deployments. (AAP-80775)

## **Event-Driven Ansible**

- Reduces log noise caused by connect and disconnection of database connections. (AAP-76990)

## Execution environments

Collection updates:

| Collection         | Version change              |
| ------------------ | --------------------------- |
| ansible.controller | 4.8.3 → 4.8.4               |
| ansible.platform   | 2.7.20260615 → 2.7.20260630 |

(AAP-83574)

## **Ansible Lightspeed / MCP Server**

- Add revocation_endpoint and PKCE metadata to OIDC discovery (AAP-82011)

## **Ansible Lightspeed**

- Improved security. (AAP-81280)

## **MCP Server**

- Gateway root /.well-known non existent paths return http status 404 (AAP-82012)

## **Metrics Service and Automation Dashboard**

- Fixed chart hover elements (AAP-83659)
- Automation Dashboard now aligns its retention with Controller (AAP-83686)
- Payload recording operator vs containerized (AAP-83331)

## **Platform Operator**

- Show a message in the operator that displays a command that can be executed to watch the logs and the migration process (AAP-79713)
- Add MCP_SERVER_URL environment variable (AAP-81960)

## CVE

- **Automation gateway**
* [CVE-2026-18141](http://access.redhat.com/security/cve/CVE-2026-18141) – Authentication bypass in Event-Driven Ansible via forged HTTP header in:
+ `gateway-rhel9`. AAP-84770
* [CVE-2026-48526](http://access.redhat.com/security/cve/CVE-2026-48526) – PyJWT authentication bypass due to forged JSON Web Tokens in:
+ `gateway-rhel9`. AAP-78035
- **Automation Platform UI**
* [CVE-2026-13149](http://access.redhat.com/security/cve/CVE-2026-13149) – Brace-expansion denial of service due to exponential-time complexity in:
+ `gateway-rhel9`. AAP-82747
- **Automation controller**
* [CVE-2026-48526](http://access.redhat.com/security/cve/CVE-2026-48526) – PyJWT authentication bypass due to forged JSON Web Tokens in:
+ `controller-rhel9`. AAP-78036
- **Event-Driven Ansible**
* [CVE-2026-12383](http://access.redhat.com/security/cve/CVE-2026-12383) – ExternalEventStreamViewSet trusts Subject header without validation and leaks expected DN in:
+ `eda-controller-rhel9`. AAP-79215
* [CVE-2026-11332](http://access.redhat.com/security/cve/CVE-2026-11332) – Argument injection in ansible-galaxy role install leads to arbitrary code execution in:
+ `eda-controller-rhel9`. AAP-82652
+ `de-minimal-rhel9`. AAP-82650
+ `de-supported-rhel9`. AAP-82649
* [CVE-2026-44545](http://access.redhat.com/security/cve/CVE-2026-44545) – Daphne denial of service via excessive WebSocket message size in:
+ `eda-controller-rhel9`. AAP-82619
- Automation hub
* [CVE-2026-34993](http://access.redhat.com/security/cve/CVE-2026-34993) – AIOHTTP arbitrary code execution via untrusted input to CookieJar.load() in:
+ `hub-rhel9`. AAP-83362
* [CVE-2026-59197](http://access.redhat.com/security/cve/CVE-2026-59197) – Pillow native heap out-of-bounds write in:
+ `hub-rhel9`. AAP-83292
* [CVE-2026-54060](http://access.redhat.com/security/cve/CVE-2026-54060) – Pillow denial of service via excessive memory allocation when processing font files in:
+ `hub-rhel9`. AAP-82203
* [CVE-2026-55380](http://access.redhat.com/security/cve/CVE-2026-55380) – Pillow denial of service via crafted GD 2.x image file in:
+ `hub-rhel9`. AAP-82186
* [CVE-2026-55379](http://access.redhat.com/security/cve/CVE-2026-55379) – Pillow denial of service via crafted BDF font file in:
+ `hub-rhel9`. AAP-82164
- Ansible Lightspeed
* [CVE-2026-59886](http://access.redhat.com/security/cve/CVE-2026-59886) – pyasn1 denial of service via crafted ASN.1 REAL values in:
+ `lightspeed-chatbot-rhel9`. AAP-83749
* [CVE-2026-34993](http://access.redhat.com/security/cve/CVE-2026-34993) – AIOHTTP arbitrary code execution via untrusted input to CookieJar.load() in:
+ `lightspeed-chatbot-rhel9`. AAP-83363
* [CVE-2026-59197](http://access.redhat.com/security/cve/CVE-2026-59197) – Pillow native heap out-of-bounds write in:
+ `lightspeed-chatbot-rhel9`. AAP-83293
* [CVE-2026-54058](http://access.redhat.com/security/cve/CVE-2026-54058) – Pillow memory disclosure or denial of service via crafted McIdas AREA image in:
+ `lightspeed-chatbot-rhel9`. AAP-83278
* [CVE-2026-11332](http://access.redhat.com/security/cve/CVE-2026-11332) – Argument injection in ansible-galaxy role install leads to arbitrary code execution in:
+ `lightspeed-rhel9`. AAP-82659
* [CVE-2026-44545](http://access.redhat.com/security/cve/CVE-2026-44545) – Daphne denial of service via excessive WebSocket message size in:
+ `lightspeed-rhel9`. AAP-82617
* [CVE-2026-59939](http://access.redhat.com/security/cve/CVE-2026-59939) – httplib2 denial of service via unbounded decompression of HTTP response bodies in:
+ `lightspeed-rhel9`. AAP-82571
* [CVE-2026-54060](http://access.redhat.com/security/cve/CVE-2026-54060) – Pillow denial of service via excessive memory allocation when processing font files in:
+ `lightspeed-chatbot-rhel9`. AAP-82204
* [CVE-2026-55380](http://access.redhat.com/security/cve/CVE-2026-55380) – Pillow denial of service via crafted GD 2.x image file in:
+ `lightspeed-chatbot-rhel9`. AAP-82183
* [CVE-2026-55379](http://access.redhat.com/security/cve/CVE-2026-55379) – Pillow denial of service via crafted BDF font file in:
+ `lightspeed-chatbot-rhel9`. AAP-82162
* [CVE-2026-54283](http://access.redhat.com/security/cve/CVE-2026-54283) – Starlette request.form() limits silently ignored for application/x-www-form-urlencoded enabling DoS in:
+ `lightspeed-chatbot-rhel9`. AAP-81671
* [CVE-2026-48990](http://access.redhat.com/security/cve/CVE-2026-48990) – joserfc resource exhaustion via oversized JSON Web Signature payloads in:
+ `lightspeed-chatbot-rhel9`. AAP-79754
- Receptor
* [CVE-2026-40898](http://access.redhat.com/security/cve/CVE-2026-40898) – quic-go denial of service via excessive memory allocation in HTTP/3 trailers in:
+ `receptor-rhel9`. AAP-82604
+ `receptor`. AAP-82603

## Bug fixes

## Automation gateway

- Fixed an issue where gateway did not include pins for DAB libraries; bumped pyasn1 library version. (AAP-84511)
- Fixed an issue where a performance bottleneck caused SAML and OIDC logins to take 60-120+ seconds or time out when more than 300 authenticator maps were configured. The claims processing algorithm now scales linearly with the number of user attribute values and map triggers. (AAP-83458)
- Fixed an issue where PATCH/PUT to service_clusters returned 403 Forbidden when the gateway route had enable_gateway_auth=False. (AAP-83439)
- Fixed an issue where the service client crashed on services without a service_index_path value. (AAP-82284)
- Fixed an issue where migrate_service_data used single-resource GETs instead of bulk paginated list fetches, causing poor performance. (AAP-79709)
- Fixed an issue where migrate_service_data count validation failed due to concurrent changes during pagination. (AAP-79708)
- Fixed an issue where gateway pods crashlooped during database outages by adding a connect timeout to the ping endpoint's health check query. (AAP-78933)
- Fixed an issue where migrate_service_data performed full resource enumeration when data was already synchronized, reducing runtime from hours to seconds. (AAP-78250)
- Fixed an issue where migrate_service_data failed all role assignments when a single downstream service was unreachable. (AAP-77949)
- Fixed an issue where loading users in the Access Management UI with more than 50 users per page could result in a "Service Unavailable" error. (AAP-75015)
- Fixed an issue where organization admins were unable to view, modify, or remove permissions on teams outside of their organization. (AAP-72503)

## Automation Platform Gateway / Django-ansible-base

- Fixed an issue where organization administrators could assign permissions to users from other organizations on resources within their own organization, but could not view, modify, or remove those permissions afterward. Organization administrators can now fully manage permissions for users outside their organization on resources within their organizational scope. (AAP-83807)
- Fixed an issue where the user list API endpoint experienced slow response times due to redundant database queries when loading users. This has been fixed by optimizing query patterns to eliminate N+1 queries. (AAP-75267)

## Automation Platform Gateway / Automation Dashboard

- Fixed an issue where Metrics Service could not correctly register with Gateway. (AAP-83448)
- Fixed an issue where the migration command did not enable metrics service RBAC service ID support. (AAP-82992)

## Metrics Service and Automation Dashboard

- Fixed an issue where the API response was incorrect. (AAP-83881)
- Fixed an issue where Unicode characters in query parameters caused 500 Internal Server Error on metrics endpoints. (AAP-83877)
- Fixed an issue where system tasks with can_modify=false could still be modified via PATCH. (AAP-83873)

## Automation Platform UI

- Fixed an issue where form select dropdowns did not consistently include typeahead search filtering, affecting survey single-select questions and other dropdowns. (AAP-83951)
- Fixed an issue where the job list page experienced high latency under heavy WebSocket traffic. Batched triggered fetches with id__in filtering instead of refetching the full list on each event. (AAP-83242)
- Fixed an issue where setting the default value of a survey question to 0 for integer (or 0.0 for float) answer types was silently ignored. The UI now correctly submits 0 as a valid default value. (AAP-83207)

## **Automation Platform UI / Automation Hub**

- Fixed an issue where collection versions in Automation Content were sorted as plain strings (e.g., 4.7.10 before 4.7.5) instead of proper semantic version order. The version list now defaults to descending semver order with the latest version displayed first. (AAP-83918)

## **Automation Controller**

- Fixed an issue where Controller failed to load subscriptions when using Satellite (REDHAT_CANDLEPIN_HOST) because validate_rh() only used it as a fallback when rhsm.conf was missing, and get_satellite_subs() ignored REDHAT_CANDLEPIN_VERIFY. (AAP-84439)
- Fixed an issue where the task manager assigned all burst jobs to a single controller node when capacity was tied by adding least-connections tie-breaking. (AAP-83717)
- Fixed an issue where large fields in the unified_jobs list caused slowness. Added query param to skip large fields. (AAP-82685)

## Automation Controller / Django-ansible-base

- Fixed an issue where specialized Organization *Admin roles were missing shared.member_organization permission, causing create operations to fail with 403. (AAP-83958)
- Fixed an issue where all team access endpoints returned 500 Internal Server Error because the Team model was missing an encrypted_fields attribute required by the DAB serializer. (AAP-82775)

## Django-ansible-base

- Fixed an issue where resource sync crashed when the RBAC API returned null results during role assignment pagination. (AAP-83265)
- Fixed an issue where OIDC authenticator maps did not evaluate attribute-based triggers, preventing automatic role and organization assignment during login. (AAP-80188)
- Fixed an issue where SAML authenticator maps failed to assign roles and organization memberships when using attribute-based triggers. (AAP-80185)

## Event-Driven Ansible

- Fixed an issue where a test credential tied to a decision environment sync was failing. (AAP-83308)
- Fixed an issue with the rotate_db_encryption_key management command. (AAP-82500)

## Ansible Lightspeed

- Fixed an issue where the AAP chatbot returned a 403 CSRF error after VS Code extension OAuth login in same browser. (AAP-82827)

## Metrics Service and Automation Dashboard

- Fixed an issue where Swagger UI was broken and feature_flags redirect was invalid due to missing service prefix from generated URLs. (AAP-83879)
- Fixed an issue where the Prometheus endpoint trailing slash returned 404 due to incorrect mounting. (AAP-83869)

## Platform Operator

- Fixed an issue where unnecessary file permission changes in the database backup task caused failures on storage backends enforcing POSIX identity, such as AWS EFS with access points (galaxy-operator). (AAP-84423)
- Fixed an issue where unnecessary file permission changes in the database backup task caused failures on storage backends enforcing POSIX identity, such as AWS EFS with access points (eda-server-operator). (AAP-84420)
- Fixed an issue where unnecessary file permission changes in the database backup task caused failures on storage backends enforcing POSIX identity, such as AWS EFS with access points (aap-gateway-operator). (AAP-84417)
- Fixed an issue where the gateway operator propagated the NO_PROXY environment variable to operand containers verbatim without including internal service exclusions, causing internal traffic to be routed through the corporate proxy and resulting in authentication failures on proxy-configured clusters. The operator now automatically augments NO_PROXY with the required internal cluster service exclusions. (AAP-83822)
