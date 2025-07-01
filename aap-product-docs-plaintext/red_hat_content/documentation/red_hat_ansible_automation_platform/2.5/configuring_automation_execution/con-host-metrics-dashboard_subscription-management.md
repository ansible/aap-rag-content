# 11. Subscription management in Ansible Automation Platform and automation controller
## 11.1. Host metrics and subscription
### 11.1.1. Host Metrics dashboard




To view your host metrics, in the navigation pane, selectAutomation Analytics→Host Metrics.

The Host Metrics dashboard provides high level automation run details per managed host, including:

- The first and last time a host was automated.
- The number of times automation has been run or attempted to be run against a host.
- The number of times a managed host has been deleted.


The ability to view the number of times automation has been run on hosts enables you to:

- View your most commonly automated hosts.
- More accurately reflect the scope of your automation landscape.


#### 11.1.1.1. Soft deletion




Soft deletion enables the removal of decommissioned hosts from the Host Metrics view and excludes them from any potential managed node counting. Additionally, the following host types can also be deleted:

- Ephemeral, uniquely provisioned hosts, such as those used for CI-CD, or testing only.
- Bench provisioning or temporary hosts.
- Older hosts that have been decommissioned and are never automated against.


Soft deletion is intended for legitimate use case scenarios only. It must not be used to violate subscription counting, for example, for the purposes of node recycling. For more information, see [How are "managed nodes" defined as part of the Red Hat Ansible Automation Platform offering](https://access.redhat.com/articles/3331481) ?

