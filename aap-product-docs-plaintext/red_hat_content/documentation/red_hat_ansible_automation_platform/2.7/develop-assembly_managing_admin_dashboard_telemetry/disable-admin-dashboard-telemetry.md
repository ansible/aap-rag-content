# View and manage Admin dashboard telemetry
## Disable the Admin dashboard telemetry

Red Hat Ansible Lightspeed collects Admin dashboard telemetry by default to gain insight into how your organization uses the service. You can disable this telemetry to stop collecting analytics data.

### Before you begin

- You have organization administrator privileges to a Red Hat Customer Portal organization with a valid Red Hat Ansible Automation Platform subscription.

### About this task

After you disable the Admin dashboard telemetry, the Ansible Lightspeed service no longer collects the analytics telemetry data for your organization. The earlier telemetry data is still available on the Admin dashboard, but no latest data is displayed. If you re-enable the Admin dashboard telemetry, the Ansible Lightspeed service starts collecting data for your organization, and the metrics are displayed on the Admin dashboard after 24 hours.

### Procedure

1.  Log in to the [Ansible Lightspeed portal](https://c.ai.ansible.redhat.com/) as an organization administrator.
2.  From the login screen, click **Admin Portal**.
3.  Under Admin Portal, click **Telemetry**.
4.  To disable the Admin dashboard telemetry, select **Operational telemetry data only**. Note:
To re-enable the Admin dashboard telemetry, select **Admin dashboard telemetry data**.

5.  Click **Save**.
