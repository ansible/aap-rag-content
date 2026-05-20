# 9. Patch releases
## 9.9. Ansible Automation Platform patch release October 28, 2025
### 9.9.9. Event-Driven Ansible

#### 9.9.9.1. Features

- Changes in the deployment and nginx configuration now allow for gunicorn and daphne to bind to :: as well, essentially allowing for seamlessly binding to IPv4 and IPv6 (dual-stack) addresses, while also enabling the operator to run in single-stack IPv6 or IPv4 scenarios.(AAP-56192)

