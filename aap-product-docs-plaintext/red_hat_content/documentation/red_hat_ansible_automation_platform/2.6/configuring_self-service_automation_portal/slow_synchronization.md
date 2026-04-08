# 5. Troubleshooting Ansible Automation Platform synchronization
## 5.3. Slow synchronization




**Issue:** Synchronization takes too long to complete or times out.

**Symptoms:**

- Timeouts during synchronization.
- Timeout errors appear in the logs.


**Solutions:**

- Increase the `    timeout` value in the synchronization schedule.
- Reduce the synchronization `    frequency` (sync less often).
- Add more specific filters to the Job Templates configuration to reduce the overall count of entities processed.
- For large organizations, increase the `    timeout` specifically for the identity sync ( `    orgsUsersTeams` ).


