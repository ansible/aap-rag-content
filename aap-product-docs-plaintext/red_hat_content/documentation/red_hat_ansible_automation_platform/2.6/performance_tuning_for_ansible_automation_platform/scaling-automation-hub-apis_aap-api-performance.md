# 3. API service performance
## 3.6. Considerations for scaling the automation hub APIs




Scaling automation hub involves considerations for each of its service types:

- API service: manages `    HTTP` requests through the API
- Pulp workers service: manages syncs and content uploads
- Content service: manages content delivery after content has been processed and stored


Separate `Gunicorn` deployments back these services and handle different types of requests. In OpenShift Container Platform, these services must be scaled independently. In VM-based installation and container-based installation, a standard automation hub node hosts all services, and scaling is achieved by adding more nodes.

