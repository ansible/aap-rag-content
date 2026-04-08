# 3. Caching and queueing system
## 3.1. Overview of the Redis cache and queueing system




Redis is an open source, in-memory, NoSQL key/value store used primarily as an application cache and lightweight message broker, which stores event queues, session data, and tokens to deliver improved performance, reliability, and data security.

platform gateway and Event-Driven Ansible use Centralized Redis. Automation controller and automation hub have their own instances of Redis.

This cache and queue system stores data in memory, rather than on a disk or solid-state drive (SSD), which helps deliver speed, reliability, and performance. Secure communication with the cache and queue system through Transport Layer Security (TLS) encryption and authentication protects your data.


<span id="idm139629090157872"></span>
**Table 3.1. Data types cached by Centralized Redis**

| Component |
| --- |
| Data types cached |
| Platform gateway |
| Settings, Session Information, JSON Web Tokens |
| Event-Driven Ansible server |
| Event queues |




Note
The data in Redis from the platform gateway and Event-Driven Ansible are partitioned. Neither service can access the other service’s data.



