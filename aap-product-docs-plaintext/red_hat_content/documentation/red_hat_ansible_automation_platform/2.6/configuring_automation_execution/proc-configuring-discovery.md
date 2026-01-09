# 3. Performance tuning for automation controller
## 3.1. WebSocket configuration for automation controller
### 3.1.1. Configuring automatic discovery of other automation controller nodes




You can configure WebsSocket connections to enable automation controller to automatically handle discovery of other automation controller nodes through the Instance record in the database.

1. Edit automation controller WebSocket information for port and protocol, and confirm whether to verify certificates with `    True` or `    False` when establishing the WebSocket connections:


```
BROADCAST_WEBSOCKET_PROTOCOL = 'http'    BROADCAST_WEBSOCKET_PORT = 80    BROADCAST_WEBSOCKET_VERIFY_CERT = False
```


1. Restart automation controller with the following command:


```
$ automation-controller-service restart
```




