# 4. Execution environments
## 4.1. Issue - Cannot select the "Use in Controller" option for execution environment image on private automation hub




You cannot use the **Use in Controller** option for an execution environment image on private automation hub. You also receive the error message: “No Controllers available”.

To resolve this issue, connect automation controller to your private automation hub instance.

**Procedure**

1. Change the `    /etc/pulp/settings.py` file on private automation hub and add one of the following parameters depending on your configuration:


- Single controller


```
CONNECTED_ANSIBLE_CONTROLLERS = ['<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">&lt;https://my.controller.node&gt;</span></em></span>']
```


- Many controllers behind a load balancer


```
CONNECTED_ANSIBLE_CONTROLLERS = ['<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">&lt;https://my.controller.loadbalancer&gt;</span></em></span>']
```


- Many controllers without a load balancer


```
CONNECTED_ANSIBLE_CONTROLLERS = ['<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">&lt;https://my.controller.node1&gt;</span></em></span>', '<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">&lt;https://my.controller2.node2&gt;</span></em></span>']
```



1. Stop all of the private automation hub services:


```
# systemctl stop pulpcore.service pulpcore-api.service pulpcore-content.service pulpcore-worker@1.service pulpcore-worker@2.service nginx.service redis.service
```


1. Restart all of the private automation hub services:


```
# systemctl start pulpcore.service pulpcore-api.service pulpcore-content.service pulpcore-worker@1.service pulpcore-worker@2.service nginx.service redis.service
```

**Verification**


- Verify that you can now use the **Use in Controller** option in private automation hub.



