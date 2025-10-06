# 3. Configuring access to external applications with token-based authentication
## 3.2. Adding tokens
### 3.2.3. Personal Access Token migration




After upgrading to Ansible Automation Platform 2.6, Personal Access Tokens (PATs) from a 2.4 automation controller remain functional. They are visible in the platform gateway UI and you can use them with both automation controller and platform gateway APIs.

**Managing automation controller tokens**

After the upgrade, you can perform the following actions with your automation controller tokens:

-  **Platform gateway UI** : You can edit or delete the tokens, but you cannot create or refresh them.
-  **Automation controller** API: You can create, edit, delete, or refresh the tokens.


Tokens are labeled in the UI to indicate if they are automation controller only or platform gateway. Platform gateway tokens are unaffected by these requirements, other than being rendered in the UI with a **platform** type.

