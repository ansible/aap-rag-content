# 10. Patch releases
## 10.8. Ansible Automation Platform patch release May 7, 2025
### 10.8.3. Features




#### 10.8.3.1. Ansible Automation Platform




- Added an enhanced log viewer for rulebook activation instances similar to the job output logger.(AAP-43337)


#### 10.8.3.2. Container-based Ansible Automation Platform




- Implemented a playbook to collect sos reports using the inventory file.(AAP-42606)


#### 10.8.3.3. Event-Driven Ansible




- Event-Driven Ansible now submits analytics data.(AAP-40881)
- Enabled Event-Driven Ansible analytics data to be uploaded to the cloud. This feature is guarded by a feature flag.(AAP-42468)
- Added a log tracking id to each log message labelled as `    [tid: uuid-pattern]` .(AAP-42270)
- Improved the user experience of managing rulebook activations in Event-Driven Ansible by introducing an edit capability.(AAP-33067)
- The following datapoints Event-Driven Ansible now collects for analytics for MVP:


- Eventsources used in Event-Driven Ansible.
- Eventstreams used in Event-Driven Ansible.
- Version of Event-Driven Ansible installed.
- Installation type (container/OCP/VM).
- Platform organizations in Event-Driven Ansible.
- Which automation controller job template was launched from a rulebook activation.(AAP-31458)

- Event-Driven Ansible `    gather_analytics` command now runs on schedule as an internal task.(AAP-30063)
- Event-Driven Ansible now writes analytics data collector that sends payloads to **console.redhat.com** .(AAP-30055)
- Add `    x-request-id` to each log message labelled as `    [rid:uuid-pattern]` .(AAP-42269)


