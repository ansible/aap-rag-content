# Output text

Use `output.text` to display information to the user after the template runs. Each text block has a `title` and `content` field. The `content` field supports markdown formatting.

```
output:
text:
- title: Request submitted
content: |
Your request has been submitted.
```
You can include multiple text blocks:

```
output:
text:
- title: Request submitted
content: |
Your deployment of **${{ parameters.app_name }}** has been submitted.

**Job ID:** ${{ steps['launch-job'].output.data.id }}
**Status:** ${{ steps['launch-job'].output.data.status }}

- title: Configuration summary
content: |
- Inventory: ${{ parameters.inventory }}
- Application: ${{ parameters.app_name }}
```
