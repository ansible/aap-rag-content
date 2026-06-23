# Use automation controller credentials in a playbook
## Use 'delegate_to' and any lookup variable

```
- command: somecommand
environment:
USERNAME: '{{ lookup("env", "USERNAME") }}'
PASSWORD: '{{ lookup("env", "PASSWORD") }}'
delegate_to: somehost
```
