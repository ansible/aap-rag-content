# 3. API service performance
## 3.4. Considerations for scaling the automation controller API service
### 3.4.3. Database connection and architecture considerations




On OpenShift Container Platform, each web replica consumes database connections for WSGI web service workers and various background services facilitating task communication and WebSockets. The number of database connections used by the WSGI web server on VM-based installation and container-based installation scales with the machine’s CPU count. Additionally, control and hybrid nodes manage the Dispatcher (tasking system) and the Callback Receiver (job event processing worker pool). These worker pools scale with CPU availability and necessitate database connections.

Provisioning additional control nodes demands more database connections than solely scaling out the web deployment on OpenShift Container Platform. This demand occurs because containerized and RPM control node scaling also expands the tasking system, which operates as a distinct deployment on OpenShift Container Platform. This separation of services on OpenShift Container Platform deployments is an important distinction that allows administrators to more finely tune the deployment and conserve limited resources, such as database connections.

