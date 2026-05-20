# 6. Authentication movement
## 6.6. Authentication type: RADIUS

Review the general settings and mappings for RADIUS authentication. Compare how configurations transform from automation controller 2.4 to the platform gateway 2.6.

**General settings**

| Automation controller 2.4 | Platform gateway 2.6 |
| --- | --- |
| RADIUS_SERVER: "radius.example.com"     RADIUS_PORT: 1812     RADIUS_SECRET: "shared-secret" | "configuration": {       "SERVER": "radius.example.com",       "PORT": 1812,       "SECRET": "shared-secret"     } |

**Mappings**

RADIUS authentication does not support user mappings in either automation controller 2.4 or Platform gateway 2.6.

