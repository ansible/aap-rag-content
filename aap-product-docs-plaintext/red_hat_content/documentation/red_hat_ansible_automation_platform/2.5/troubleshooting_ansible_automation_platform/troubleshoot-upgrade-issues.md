# 9. Upgrading
## 9.1. Issue - automation controller API connection fails after upgrade with load balancer




When upgrading from Ansible Automation Platform 2.4 to 2.5, the upgrade completes successfully. However, connections to the platform gateway URL fail if you are using automation controller behind a load balancer.

You see this error message in the logs:

`Error connecting to Controller API`

**Procedure**

1. To resolve this issue, perform the following tasks for all controller hosts:


1. For each controller host, add the platform gateway URL as a trusted source in the `        CSRF_TRUSTED_ORIGIN` setting in the **settings.py** file.

For example, if you configured the platform gateway URL as `        https://www.example.com` , you must add that URL in the **settings.py** file too as shown:


```
CSRF_TRUSTED_ORIGINS = ['https://appX.example.com:8443','https://www.example.com']
```


1. Restart each controller host by using the `        automation-controller-service restart` command so that the URL changes are implemented. For the procedure, see [Start, stop, and restart automation controller](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/configuring_automation_execution/controller-start-stop-controller) in _Configuring automation execution_ .




<span id="idm140186438142192"></span>
