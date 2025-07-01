# Chapter 2. Browsing with the API




REST APIs give access to resources (data entities) through URI paths.


<span id="controller-api-browsing"></span>
**Procedure**

1. Go to the automation controller REST API in a web browser at:

https://<gateway server name>/api/controller/v2


1. Click the **"v2"** link next to **"current versions"** or **"available versions"** . Automation controller supports version 2 of the API.
1. Perform a `    GET` with just the `    /api/` endpoint to get the `    current_version` , which is the recommended version.
1. Click the![Copy](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Automation_execution_API_overview-en-US/images/0504de6cf08a84c593fa9c06dd7ef5e1/api-questionmark.png)
icon on the navigation menu, for documentation on the access methods for that particular API endpoint and what data is returned when using those methods.
1. Use the `    PUT` and `    POST` verbs on the specific API pages by formatting JSON in the various text fields.



You can also view changed settings from factory defaults at `/api/v2/settings/changed/` endpoint. It reflects changes you made in the API browser, not changed settings that come from static settings files.

