# Chapter 4. Projects




Projects are a logical collection of rulebooks. They must be a git repository and located in the path defined for Event-Driven Ansible content in Ansible collections: `/extensions/eda/rulebooks` at the root of the project.

Important
To meet high availability demands, Event-Driven Ansible controller shares centralized [Redis (REmote DIctionary Server)](https://redis.io/) with the Ansible Automation Platform UI. When Redis is unavailable, you will not be able to create or sync projects.



