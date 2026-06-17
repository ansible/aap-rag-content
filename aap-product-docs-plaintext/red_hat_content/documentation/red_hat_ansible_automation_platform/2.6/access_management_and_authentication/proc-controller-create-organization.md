# 4. Managing access with role-based access control
## 4.1. Organizations
### 4.1.2. Creating an organization

Ansible Automation Platform automatically creates a default organization. If you have a self-support level license, you have only the default organization available and cannot delete it.

**Procedure**

1. From the navigation panel, select Access Management → Organizations.

2. Click Create organization.

3. Enter the **Name** and give a **Description** for your organization.


Note
If automation controller is enabled on the platform, continue with Step 4. Otherwise, proceed to Step 6.

4. Select the name of the **Execution environment** or search for one that members of this organization can use to run automation.

5. Enter the name of the **Instance Groups** on which to run this organization.

6. Optional: Enter the **Galaxy credentials** or search from a list of existing ones.

7. Select the **Max hosts** for this organization. The default is 0. When this value is 0, it signifies no limit. If you try to add a host to an organization that has reached or exceeded its cap on hosts, an error message displays:

You have already reached the maximum number of 1 hosts allowed for your organization. Contact your System Administrator for assistance.

8. Click Next.

9. If you selected more than 1 instance group, you can manage the order by dragging and dropping the instance group up or down in the list and clicking Confirm.


Note
The execution precedence is determined by the order in which the instance groups are listed.

10. Click Next and verify the organization settings.

11. Click Finish.

