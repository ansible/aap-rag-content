# 3. API service performance
## 3.6. Considerations for scaling the automation hub APIs
### 3.6.2. Automation hub Pulp worker and content services




The Pulp worker and content services manage all operations related to content syncs, uploads and downloads. Key performance indicators for the Pulp worker and content services include:

- High Content sync rates: Frequent or large synchronization operations from external repositories demanding significant pulp-content worker processing.
- High Content upload or download rates: Frequent pushing or pulling of automation execution environments by automation controller, Event-Driven Ansible, or large Collection uploads or downloads by automation clients.
- Disk I/O bottlenecks: Performance issues related to read/write operations on the underlying content storage ( `    /var/lib/pulp` ), often shown as high disk I/O wait times.
- Pulp worker saturation: High CPU utilization or queuing within pulp processes, indicating an inability to keep up with content processing and serving.


To scale your Pulp worker and content services, consider the following scaling strategies:

- In OpenShift Container Platform: Scale the deployment of these services by increasing the `    hub.content.replicas` and `    hub.worker.replicas` attributes on the `    AnsibleAutomationPlatform` Custom Resource.
- For VM-based installation or container-based installation: Horizontally scale all services by adding more automation hub nodes.



<span id="idm139687041685328"></span>
