# Optimize request timeouts

Ansible Automation Platform on OpenShift Container Platform manages request timeouts through a synchronized, cascading architecture. This structure ensures that if a high-level service (the Gateway) reaches a timeout limit, all dependent internal processes terminate.

placeholder

