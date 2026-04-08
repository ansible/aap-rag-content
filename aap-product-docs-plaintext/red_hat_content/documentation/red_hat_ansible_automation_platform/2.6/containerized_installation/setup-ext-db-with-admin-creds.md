# 5. Advanced containerized deployment
## 5.6. Configuring an external (customer provided) PostgreSQL database
### 5.6.1. Setting up an external database with PostgreSQL admin credentials




If you have PostgreSQL admin credentials, you can supply them in the inventory file and the installation program creates the PostgreSQL users and databases for each component for you. The PostgreSQL admin account must have `SUPERUSER` privileges.

**Procedure**

- To configure the PostgreSQL admin credentials, add the following variables to the inventory file under the `    [all:vars]` group:


```
postgresql_admin_username=&lt;set your own&gt;    postgresql_admin_password=&lt;set your own&gt;
```




