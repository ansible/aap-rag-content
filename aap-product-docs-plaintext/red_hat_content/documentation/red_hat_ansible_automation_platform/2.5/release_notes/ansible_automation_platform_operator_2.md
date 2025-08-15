# 10. Patch releases
## 10.2. Ansible Automation Platform patch release July 2, 2025
### 10.2.5. Ansible Automation Platform Operator




#### 10.2.5.1. Enhancements




- Annotation can now be added to the route by specifying **spec.route_annotations** on the Ansible Automation Platform and automation controller custom resources.(AAP-45952)
- New installations of Red Hat Ansible Lightspeed using the Ansible Automation Platform Custom Resource will automatically integrate with Ansible Automation Platform’s **OAuth** mechanism. The `    auth_config_secret_name` setting is optional.(AAP-45686)


#### 10.2.5.2. Bug fixes




- Fixed an issue where the `    jquery` version included in the redirect page did not match the version from the rest framework directory.(AAP-47160)
- Fixed an issue where the ingress class name could not be configured on the automation hub CR.(AAP-47054)
- Fixed an issue where there was a missing resources limit on automation hub API `    init` containers.(AAP-47053)
- Fixed an issue where the resources limit on worker pods could not be configured.(AAP-47045)
- Fixed an issue where there was no `    readinessProbe` configuration in the PostgreSQL `    statefulset` definition.(AAP-47043)


