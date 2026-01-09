# 2. Use a playbook to establish a connection to a managed node
## 2.3. Gather facts from network devices




The `gather_facts` keyword supports gathering network device facts in standardized key/value pairs. You can feed these network facts into further tasks to manage the network device.

You can also use the `gather_network_resources` parameter with the network `*_facts` modules (such as `arista.eos.eos_facts` ) to return a subset of the device configuration, as the following example shows:

```
- hosts: arista
gather_facts: True
gather_subset: interfaces
module_defaults:
arista.eos.eos_facts:
gather_network_resources: interfaces
```

The playbook returns the following interface facts:

```
"network_resources": {
"interfaces": [
{
"description": "test-interface",
"enabled": true,
"mtu": "512",
"name": "Ethernet1"
},
{
"enabled": true,
"mtu": "3000",
"name": "Ethernet2"
},
{
"enabled": true,
"name": "Ethernet3"
},
{
"enabled": true,
"name": "Ethernet4"
},
{
"enabled": true,
"name": "Ethernet5"
},
{
"enabled": true,
"name": "Ethernet6"
},
]
}
```

Note
`gather_network_resources` renders configuration data as facts for all supported resources ( `interfaces/bgp/ospf/etc`` ), whereas `gather_subset` is primarily used to fetch operational data.



