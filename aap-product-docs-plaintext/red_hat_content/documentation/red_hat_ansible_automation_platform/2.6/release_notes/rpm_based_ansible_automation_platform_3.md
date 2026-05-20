# 9. Patch releases
## 9.9. Ansible Automation Platform patch release October 28, 2025
### 9.9.8. RPM-based Ansible Automation Platform

#### 9.9.8.1. Bug Fixes

- Fixed an issue where setting `automationgateway_disable_https=false` resulted in install failure.(AAP-55466)
- Fixed an issue where `RESOURCE_KEY SECRET_KEY` was not updated when restoring from a different environment.(AAP-54942)
- Fixed an issue where Event-Driven Ansible DE credentials failed to populate on initial installation.(AAP-54519)

Fixed an issue where the `envoy.log` for automation gateway did not receive logs after it was rotated.(AAP-51779)

Fixed an issue where `REDHAT_CANDLEPIN_VERIFY` was not being used for the correct CA permissions so that the controller could not make requests to **subscription.rhsm.redhat.com**.(AAP-55183)

