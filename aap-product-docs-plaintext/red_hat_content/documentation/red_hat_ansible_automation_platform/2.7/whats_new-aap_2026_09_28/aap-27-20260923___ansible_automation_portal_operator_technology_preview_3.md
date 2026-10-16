# Ansible Automation Platform 2.7 patch release September 28, 2026 (portal-2.2.8)
## Ansible automation portal operator Technology Preview

- Operator configuration UI and API labels updated from Backstage terminology to Ansible automation portal language. (AAP-92046)
- Managed Backstage custom resource naming corrected so RHDH resources use `backstage-<cr-name>` instead of `backstage-<cr-name>-backstage`. (AAP-93825)
* Existing installs must manually delete the old Backstage CR after upgrade: `oc delete backstage <name>-backstage -n <namespace>`
- `spec.plugins.selfService`, `spec.plugins.rbac`, and `spec.plugins.scaffolder` removed from the CRD; these plugins are always on. To disable a plugin, use `spec.plugins.overrides`. (AAP-93825)
- `spec.devtools` and `spec.plugins.ghcrRegistry` hidden from the operator form; both remain settable via YAML. (AAP-93825)
- Lightspeed plugin option removed from the AutomationPortal operator form; `spec.plugins.lightspeed.enabled` remains valid in YAML for advanced use. (AAP-92058)

