# 6. Job templates
## 6.17. Provisioning callbacks
### 6.17.1. Enabling Provisioning Callbacks




Use the following procedure to enable provisioning callbacks for a job template.

**Procedure**

- To enable callbacks, check the **Provisioning callback** option in the job template. This displays **Provisioning callback details** for the job template.

Note
If you intend to use automation controller’s provisioning callback feature with a dynamic inventory, set **Update on Launch** for the inventory group used in the job template.



Callbacks also require a host config key, to ensure that foreign hosts with the URL cannot request configuration. Give a custom value for the **Host config key** . The host key can be reused across many hosts to apply this job template against multiple hosts. If you want to control what hosts are able to request configuration, you can change the key can at any time.




