# 5. Red Hat Ansible Automation Platform Service on AWS Service Definition
## 5.5. Multi-Region Active/Passive infrastructure
### 5.5.2. Failure domains and events requiring failover

The following are operational issues that indicate when a disruption qualifies for a failover:

#### 5.5.2.1. Regional outages

A regional outage constitutes a complete AWS infrastructure failure impacting your primary deployment region.

This includes:

- **Data center isolation**: A total loss of external network routing capabilities and API access to the underlying AWS availability zones, rendering the infrastructure entirely unreachable.
- **Absolute loss of availability zones**: Concurrent physical or logical failures of all hosting zones within the specified AWS region.

##### 5.5.2.1.1. Service outages

A service outage is defined as functional degradation to the Ansible Automation Platform service, despite stable cloud hosting infrastructure.

Indicators include:

- **Total loss of responsiveness**: Complete inability to access or authenticate through user interfaces (UIs) or programmatic endpoints (APIs).

