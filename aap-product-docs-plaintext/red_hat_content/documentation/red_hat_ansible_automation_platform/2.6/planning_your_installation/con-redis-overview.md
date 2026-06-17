# 3. Caching and queueing system
## 3.1. Overview of the Redis cache and queueing system

Redis is an open source, in-memory, NoSQL key/value store used primarily as an application cache and lightweight message broker, which stores event queues, session data, and tokens to deliver improved performance, reliability, and data security.

platform gateway and Event-Driven Ansible use Centralized Redis. Automation controller and automation hub have their own instances of Redis.

This cache and queue system stores data in memory, rather than on a disk or solid-state drive (SSD), which helps deliver speed, reliability, and performance. Secure communication with the cache and queue system through Transport Layer Security (TLS) encryption and authentication protects your data.

**Table 3.1. Data types cached by Centralized Redis**

| Component |
| --- |
| <br>  Data types cached |
| <br>  Platform gateway |
| <br>  Settings, Session Information, JSON Web Tokens |
| <br>  Event-Driven Ansible server |
| <br>  Event queues |

Note

The data in Redis from the platform gateway and Event-Driven Ansible are partitioned. Neither service can access the other service’s data.

