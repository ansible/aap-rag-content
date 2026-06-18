# Reference step output in output

After the `rhaap:launch-job-template` action runs, the step output includes job execution data. Reference this data using the `${{ steps['<step-id>'].output.data.<field> }}` syntax.

The `rhaap:launch-job-template` action returns the following output fields:

| Reference                                       | Type   | Description                                                                               |
| ----------------------------------------------- | ------ | ----------------------------------------------------------------------------------------- |
| `${{ steps['launch-job'].output.data.id }}`     | number | Ansible Automation Platform Job ID.                                                       |
| `${{ steps['launch-job'].output.data.status }}` | string | Ansible Automation Platform Job status (for example, `pending`, `running`, `successful`). |
| `${{ steps['launch-job'].output.data.url }}`    | string | Direct URL to the job in Ansible Automation Platform.                                     |

## Displaying job execution data in the output

```
output:
text:
- title: Job launched
content: |
**Job ID:** ${{ steps['launch-job'].output.data.id }}
**Status:** ${{ steps['launch-job'].output.data.status }}
links:
- title: View job in Ansible Automation Platform
url: ${{ steps['launch-job'].output.data.url }}
```
