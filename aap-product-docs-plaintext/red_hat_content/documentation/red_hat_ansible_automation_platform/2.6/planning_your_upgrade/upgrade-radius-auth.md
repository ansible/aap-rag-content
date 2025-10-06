# 6. Authentication movement
## 6.6. Authentication type: RADIUS




**General settings**

| Automation controller 2.4 | Platform gateway 2.6 |
| --- | --- |
| ```
RADIUS_SERVER: "radius.example.com"
RADIUS_PORT: 1812
RADIUS_SECRET: "shared-secret"
``` | ```
"configuration": {
"SERVER": "radius.example.com",
"PORT": 1812,
"SECRET": "shared-secret"
}
``` |


**Mappings**

RADIUS authentication does not support user mappings in either automation controller 2.4 or Platform gateway 2.6.

