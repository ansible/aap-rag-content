# 10. Patch releases
## 10.4. Ansible Automation Platform patch release June 9, 2025
### 10.4.3. Automation controller




#### 10.4.3.1. Enhancements




- Updated license mechanism to allow users to provide username and password when fetching subscriptions via the API and Ansible Automation Platform user interface.(AAP-46797)


#### 10.4.3.2. Bug Fixes




- Fixed an issue where the idle dispatch workers were not recycled based upon age, or after completing the last task. Default maximum age is 4 hours, controlled by `    WORKER_MAX_LIFETIME_SECONDS` setting. Set to None to disable worker recycling.(AAP-45947)
- Fixed an analytics collector failure to clean up temporary files after failed upload to Hybrid Cloud console.(AAP-45574)
- Fixed an issue where inventory variables pulled in by update from a source with the option **Overwrite Variables** checked, were not deleted on subsequent updates from the same source when the source no longer contained the variable.(AAP-45571)


