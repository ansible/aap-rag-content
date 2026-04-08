# 5. Advanced containerized deployment
## 5.7. Configuring custom TLS certificates
### 5.7.4. Redis certificate considerations




When using custom TLS certificates for Redis-related services, consider the following for mutual TLS (mTLS) communication if specifying Extended Key Usage (EKU):

- The Redis server certificate ( `    redis_tls_cert` ) should include the `    serverAuth` (web server authentication) and `    clientAuth` (client authentication) EKU.
- The Redis client certificates ( `    gateway_redis_tls_cert` , `    eda_redis_tls_cert` ) should include the `    clientAuth` (client authentication) EKU.


