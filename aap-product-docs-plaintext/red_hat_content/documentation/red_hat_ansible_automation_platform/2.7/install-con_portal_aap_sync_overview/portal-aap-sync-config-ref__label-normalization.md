# Understanding Ansible Automation Platform synchronization
## Ansible Automation Platform synchronization configuration reference
### Ansible Automation Platform label normalization

Before filtering is applied, Ansible Automation Platform Labels are normalized by applying the following transformations:

- Convert the label to lowercase (for example, "CaC" becomes "cac")
- Replace invalid characters
- Collapse multiple hyphens into a single hyphen (for example, "app--dev" becomes "app-dev")
- Remove leading and trailing hyphens (for example, "--tag--" becomes "tag")

