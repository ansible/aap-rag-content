# 3. API service performance
## 3.4. Considerations for scaling the automation controller API service
### 3.4.2. Scaling strategies by deployment type




Consider the following strategies to scale the automation controller API service:

- OpenShift Container Platform: Adjust the `    web_replicas` attribute on the `    AutomationController` CR. Scaling the `    replicas` attribute scales task and web replicas.
- VM-based installation and container-based installation: Scale control or hybrid nodes, increasing the ability to control additional automation jobs.


