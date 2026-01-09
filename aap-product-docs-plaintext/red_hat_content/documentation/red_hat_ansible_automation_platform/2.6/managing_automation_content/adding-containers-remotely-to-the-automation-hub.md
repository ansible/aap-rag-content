# 3. Manage containers in private automation hub
## 3.6. Working with signed containers
### 3.6.2. Defining an image source for the signing pipeline




After configuring a container signing service, define the source of the images you want to sign. Configure a remote registry to tell private automation hub where to find upstream images so that it can retrieve them, add your signature, and then store them locally.

**Procedure**

1. Log in to Ansible Automation Platform.
1. From the navigation panel, selectAutomation Content→Remote Registries.
1. ClickCreate remote registry.


- In the **Name** field, enter the name of the registry where the container resides.
- In the **URL** field, enter the URL of the registry where the container resides.
- In the **Username** field, enter the username if necessary.
- In the **Password** field, enter the password if necessary.
- ClickCreate remote registry.



