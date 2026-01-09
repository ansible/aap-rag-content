# 11. Performance tuning for Event-Driven Ansible controller
## 11.3. System level monitoring for Event-Driven Ansible controller




After characterizing your workload to determine how many rulebook activations you are running in parallel and how many events you are receiving at any given point, conduct system-level monitoring to ensure the host environment can sustain the resource demands of the event-driven workload.

Using system level monitoring to review information about Event-Driven Ansible’s performance over time helps when diagnosing problems or when considering capacity for future growth.

System level monitoring includes the following information:

- Disk I/O
- RAM utilization
- CPU utilization
- Network traffic


Higher CPU, RAM, or Disk utilization can affect the overall performance of Event-Driven Ansible controller.

For example, a high utilization of any of these system level resources indicates that either the Event-Driven Ansible controller is running too many rulebook activations, or some of the individual rulebook activations are using a high volume of resources. In this case, you must increase your system level resources to support your workload.

