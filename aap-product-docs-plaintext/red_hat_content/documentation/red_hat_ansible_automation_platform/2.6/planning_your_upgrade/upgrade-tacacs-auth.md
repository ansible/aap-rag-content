# 6. Authentication movement
## 6.7. Authentication type: TACACS+




**General settings**

| Automation controller 2.4 | Platform gateway 2.6 |
| --- | --- |
| ```
TACACSPLUS_HOST: "tacacs.example.com"
TACACSPLUS_PORT: 49
TACACSPLUS_SECRET: "shared-secret"
TACACSPLUS_SESSION_TIMEOUT: 5
TACACSPLUS_AUTH_PROTOCOL: "ascii"
TACACSPLUS_REM_ADDR: false
``` | ```
"configuration": {
"HOST": "tacacs.example.com",
"PORT": 49,
"SECRET": "shared-secret",
"SESSION_TIMEOUT": 5,
"AUTH_PROTOCOL": "ascii",
"REM_ADDR": false
}
``` |


**Mappings**

TACACS+ authentication does not support user mappings in either automation controller 2.4 or Platform gateway 2.6.

