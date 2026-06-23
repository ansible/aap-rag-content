# Standard UI widgets
## Hidden widget

The `hidden` widget holds a fixed or prefilled value that is not visible to the user but is included in the submitted data. Use this widget for passing non-user-editable data, such as authentication tokens.

```
kind: Template
metadata:
name: my-AAP-template
title: Example AAP Template
spec:
parameters:
- title: Authentication
properties:
token:
title: AAP Authentication Token
type: string
description: Oauth2 token
ui:field: AAPTokenField
ui:widget: hidden
ui:backstage:
review:
show: false
steps:
- id: launch-job
name: Launch AAP Job Template
action: rhaap:launch-job-templat
input:
token: ${{ parameters.token }}
...
```

