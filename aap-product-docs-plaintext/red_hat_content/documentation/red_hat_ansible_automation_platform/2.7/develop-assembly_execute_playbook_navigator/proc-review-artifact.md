# Run playbooks locally with automation content navigator
## Review playbook results

Automation content navigator saves playbook runs as JSON artifact files. You can use these files to share, review, or troubleshoot results without requiring access to the original playbook or inventory.

### Before you begin

- A automation content navigator artifact JSON file from a playbook run.

### Procedure

Start automation content navigator with the artifact file.

```
$ ansible-navigator replay simple_playbook_artifact.json
```

1.  Review the playbook results that match when the playbook ran.
![Playbook results](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/navigator-artifact-replay.png)

### Results

You can now type the number next to the plays and tasks to step into each to review the results, as you would after executing the playbook.

