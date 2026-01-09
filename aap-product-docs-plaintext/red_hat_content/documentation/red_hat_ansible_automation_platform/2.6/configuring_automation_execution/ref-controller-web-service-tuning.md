# 3. Performance tuning for automation controller
## 3.7. Automation controller tuning
### 3.7.7. Web server tuning




The Control and Hybrid nodes each serve the UI and API of automation controller. WSGI traffic is served by the uwsgi web server on a local socket. ASGI traffic is served by Daphne. NGINX listens on port 443 and proxies traffic as needed.

To scale automation controller’s web service, follow these best practices:

- Deploy multiple control nodes and use a load balancer to spread web requests over multiple servers.
- Set max connections per automation controller to 100.


To optimize automation controller’s web service on the client side, follow these guidelines:

- Direct user to use dynamic inventory sources instead of individually creating inventory hosts by using the API.
- Use webhook notifications instead of polling for job status.
- Use the bulk APIs for host creation and job launching to batch requests.
- Use token authentication. For automation clients that must make many requests very quickly, using tokens is a best practice, because depending on the type of user, there might be additional overhead when using Basic authentication.


**Additional resources**

-  [Scaling Automation Controller for API Driven Workloads](https://www.ansible.com/blog/scaling-automation-controller-for-api-driven-workloads)
-  [Bulk API in Automation Controller](https://www.ansible.com/blog/bulk-api-in-automation-controller)
-  [Configuring access to external applications with token-based authentication](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/access_management_and_authentication/gw-token-based-authentication)


