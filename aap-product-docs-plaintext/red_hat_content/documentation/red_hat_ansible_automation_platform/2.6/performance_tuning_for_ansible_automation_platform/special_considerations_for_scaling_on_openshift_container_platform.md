# 3. API service performance
## 3.4. Considerations for scaling the automation controller API service
### 3.4.4. Special considerations for scaling on OpenShift Container Platform




It is particularly important that the service is horizontally scaled sufficiently in OpenShift Container Platform, because if more than 100 requests are backlogged, then these requests are then dropped by uWSGI. This results in clients receiving a timeout for dropped requests. The following log text provides the corresponding error for this event:

```
*** uWSGI listen queue of socket ":8000" (fd: 3) full !!! (101/100) ***
```

This error occurs due to a limitation of uWSGI tying its backlog length to the kernel parameter `somaxconn` . It is possible to raise this kernel parameter in OpenShift Container Platform, but doing so requires allowing “unsafe sysctls”.

