# 6. Red Hat Ansible Automation Platform best practices
## 6.1. Configure automation to use instance groups




Red Hat Ansible Automation Platform Service on AWS requires that customers implement their own automation execution plane.

Job templates must use a customer-configured instance or container group to run. If omitted, job runs can seem non-functional and eventually time out due to automation execution failure. Each job template must be assigned to a customer-configured instance group to function.

