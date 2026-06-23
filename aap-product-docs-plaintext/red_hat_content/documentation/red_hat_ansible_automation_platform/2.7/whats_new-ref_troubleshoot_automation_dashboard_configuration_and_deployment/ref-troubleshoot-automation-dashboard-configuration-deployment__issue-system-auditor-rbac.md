# Troubleshoot automation dashboard configuration and deployment
## Issue 2: System Auditor cannot access dashboard (RBAC broken)

**Symptom**

- System Auditor role users cannot see dashboard navigation item in Ansible Automation Platform UI
- Attempting to access dashboard URL directly shows access denied or 404
- Only Administrator role users can access dashboard


**Expected behavior:** System Auditor should have read-only access to dashboard

**Actual behavior:** Dashboard completely unavailable to System Auditor role

**Root cause**

Dashboard RBAC permissions not correctly registered for System Auditor role. The dashboard permission model assumes both Administrator (read/write) and System Auditor (read-only) access, but implementation only grants access to Administrators.

**Diagnostic commands**

1.      Verify user role:



```
# Check user's role assignments in AAP
# Navigate to: Access → Users → [username] → Roles
```
Confirm user has System Auditor role.

2.      Check dashboard visibility in UI:

Log in as System Auditor user and check if "Automation dashboard" appears in navigation menu.

**Solution**

**Technology Preview Limitation:**

If System Auditor access is not working in your Ansible Automation Platform 2.7 build:

1.      **Grant Administrator role temporarily:**

For users who need dashboard access during Technology Preview period:

- Navigate to Access> (and then)Users> (and then)[username]
- Add Administrator role

Warning:
This grants full admin access, not just dashboard read-only

2.      **Use dedicated dashboard admin account:**

Create a separate admin account specifically for dashboard access:

- Username: `dashboard-viewer`
- Role: Administrator
- Purpose: Dashboard viewing only

**Verification after fix**

- **Log in as System Auditor:** Use account with only System Auditor role (no Administrator role)

- **Verify dashboard visible:** "Automation dashboard" navigation item appears in Ansible Automation Platform UI

-      **Verify read-only access:**

* Can view all dashboard data
* Cannot modify cost settings
* Cannot create/modify/delete saved reports (filter sets)

Important:

**Automation dashboard access (Technology Preview):**

- **Administrator:** Full read/write access
- **System Auditor:** Not available in Technology Preview. Workaround: Grant Administrator role to users requiring dashboard access.

