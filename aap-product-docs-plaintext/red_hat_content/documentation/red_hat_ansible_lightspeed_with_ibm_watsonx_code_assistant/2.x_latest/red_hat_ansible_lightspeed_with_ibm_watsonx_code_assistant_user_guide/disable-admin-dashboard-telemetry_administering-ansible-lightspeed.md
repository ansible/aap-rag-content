# 6. Administering the Ansible Lightspeed Service
## 6.2. Viewing and managing the Admin dashboard telemetry
### 6.2.4. Disabling the Admin dashboard telemetry




Red Hat Ansible Lightspeed collects the Admin dashboard telemetry data by default. The data provides insight into how your organization users are using the Ansible Lightspeed service. If you no longer want to collect analytics telemetry data for your organization, you can disable the Admin dashboard telemetry.

After you disable the Admin dashboard telemetry, the Ansible Lightspeed service no longer collects the analytics telemetry data for your organization. The earlier telemetry data is still available on the Admin dashboard, but no latest data is displayed. If you re-enable the Admin dashboard telemetry, the Ansible Lightspeed service starts collecting data for your organization, and the metrics are displayed on the Admin dashboard after 24 hours.

**Prerequisites**

- You have organization administrator privileges to a Red Hat Customer Portal organization with a valid Red Hat Ansible Automation Platform subscription.


**Procedure**

1. Log in to the [Ansible Lightspeed portal](https://c.ai.ansible.redhat.com/) as an organization administrator.
1. From the login screen, click **Admin Portal** .
1. Under Admin Portal, click **Telemetry** .
1. To disable the Admin dashboard telemetry, select **Operational telemetry data only** .

Note
To re-enable the Admin dashboard telemetry, select **Admin dashboard telemetry data** .




1. Click **Save** .


