# Chapter 3. Caching and queueing system




In Ansible Automation Platform 2.5, [Redis (REmote DIctionary Server)](https://redis.io/) is used as the caching and queueing system. Redis is an open source, in-memory, NoSQL key/value store that is used primarily as an application cache, quick-response database and lightweight message broker.

Centralized Redis is provided for the platform gateway and Event-Driven Ansible and shared between those components. Automation controller and automation hub have their own instances of Redis.

This cache and queue system stores data in memory, rather than on a disk or solid-state drive (SSD), which helps deliver speed, reliability, and performance. In Ansible Automation Platform, the system caches the following types of data for the various services in Ansible Automation Platform:


<span id="idm140401810126832"></span>
**Table 3.1. Data types cached by Centralized Redis**

| Automation controller | Event-Driven Ansible server | Automation hub | Platform gateway |
| --- | --- | --- | --- |
| N/A automation controller does not use shared Redis in Ansible Automation Platform 2.5 | Event queues | N/A automation hub does not use shared Redis in Ansible Automation Platform 2.5 | Settings, Session Information, JSON Web Tokens |




This data can contain sensitive Personal Identifiable Information (PII). Your data is protected through secure communication with the cache and queue system through both Transport Layer Security (TLS) encryption and authentication.

Note
The data in Redis from both the platform gateway and Event-Driven Ansible are partitioned; therefore, neither service can access the other’s data.



