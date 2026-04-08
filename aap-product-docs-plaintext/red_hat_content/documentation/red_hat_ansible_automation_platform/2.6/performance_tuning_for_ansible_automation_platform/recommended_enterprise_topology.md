# 2. Scaling the tested deployment models
## 2.4. Motivations for migrating to an enterprise topology
### 2.4.3. Recommended enterprise topology




To maximize flexibility, resilience, and scalability, migrate to the OpenShift Container Platform-based enterprise topology. This migration includes integration with an externally managed, enterprise-grade PostgreSQL database. operator-based installation offers greater flexibility to scale individual services and adapt the deployment to specific requirements. They also enhance the ability to scale the deployment up and down with reduced downtime and customize workload placement with labels, taints, tolerations, and topology constraints. operator-based installation also benefits from resilience features, such as automatic service recreation if underlying worker nodes experience failure or resource exhaustion.

