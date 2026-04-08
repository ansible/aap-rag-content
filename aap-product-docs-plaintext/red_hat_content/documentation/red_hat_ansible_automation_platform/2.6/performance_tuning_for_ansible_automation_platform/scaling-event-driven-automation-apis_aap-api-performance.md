# 3. API service performance
## 3.5. Considerations for scaling the Event-Driven Ansible APIs




Scaling Event-Driven Ansible involves considerations for each of its service types:

- API and WebSocket service
- EventStream service


API requests routed to `/api/eda` and `/api/eda-event-stream` are handled by two separate `Gunicorn` deployments. In OpenShift Container Platform, these services must be scaled independently. For VM-based installation and container-based installation, you can scale these services together by increasing the number of hybrid nodes.

