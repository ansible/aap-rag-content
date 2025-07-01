# 9. Upgrading
## 9.1. Issue - When upgrading from Ansible Automation Platform 2.4 to 2.5, connections to the automation controller API fail if the automation controller is behind a load balancer




When upgrading Ansible Automation Platform 2.4 to 2.5, the upgrade is completed; however, connections to the platform gateway URL fail on the platform gateway UI if you are using the automation controller behind a load balancer. The following error message is displayed:

`Error connecting to Controller API`

To resolve this issue, perform the following tasks for all controller hosts:

1. For each controller host, add the platform gateway URL as a trusted source in the `    CSRF_TRUSTED_ORIGIN` setting in the **settings.py** file.

For example, if you configured the platform gateway URL as `    <a class="link" href="https://www.example.com">https://www.example.com</a>` , you must add that URL in the **settings.py** file too as shown below:


```
CSRF_TRUSTED_ORIGINS = ['https://appX.example.com:8443','https://www.example.com']
```


1. Restart each controller host by using the `    automation-controller-service restart` command so that the URL changes are implemented. For the procedure, see [Start, stop, and restart automation controller](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/configuring_automation_execution/controller-start-stop-controller) in _Configuring automation execution_ .



<span id="idm140276128147104"></span>
