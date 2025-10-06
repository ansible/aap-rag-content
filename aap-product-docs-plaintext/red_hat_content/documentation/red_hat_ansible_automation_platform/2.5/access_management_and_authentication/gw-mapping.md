# 2. Configuring authentication in the Ansible Automation Platform
## 2.6. Mapping




To control which users are allowed into the Ansible Automation Platform server, and placed into Ansible Automation Platform organizations or teams based on their attributes (like username and email address) or what groups they belong to, you can configure authenticator maps.

Authenticator maps allow you to add conditions that must be met before a user is given or denied access to a resource type. Authenticator maps are associated with an authenticator and are given an order. The maps are processed in order when the user logs in. These can be thought of like firewall rules or mail filters.

