# 6. Job templates
## 6.20. Provisioning Callbacks
### 6.20.3. Passing extra variables to Provisioning Callbacks




You can pass `extra_vars` in Provisioning Callbacks the same way you can in a regular job template. To pass `extra_vars` , the data sent must be part of the body of the POST as application or JSON, as the content type.

**Procedure**

- Pass extra variables by using one of these methods:


- Use the following JSON format as an example when adding your own `        extra_vars` to be passed:


```
'{"extra_vars": {"variable1":"value1","variable2":"value2",...}}'
```


- Pass extra variables to the job template call using `        curl` :


```
root@localhost:~$ curl -f -H 'Content-Type: application/json' -XPOST \        -d '{"host_config_key": "redhat", "extra_vars": "{\"foo\": \"bar\"}"}' \        https://&lt;CONTROLLER_SERVER_NAME&gt;/api/v2/job_templates/7/callback
```





For more information, see [Launching Jobs with Curl](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/configuring_automation_execution/controller-tips-and-tricks#ref-controller-launch-jobs-with-curl) in _Configuring automation execution_ .

