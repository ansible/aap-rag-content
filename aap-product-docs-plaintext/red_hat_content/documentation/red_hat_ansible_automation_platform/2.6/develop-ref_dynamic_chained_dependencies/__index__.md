# Chain multiple dynamic dependencies

You can define multiple `dependencies` in the same parameter step. Each dependency operates independently.

In this example, selecting "Yes" for the restart confirmation reveals a reason field, while enabling advanced options reveals additional technical fields:

```
dependencies:
showAdvanced:
allOf:
- if:
properties:
showAdvanced:
const: true
then:
properties:
maxSyncDelay:
type: number
title: Max sync delay (ms)
default: 500
serviceRestart:
allOf:
- if:
properties:
serviceRestart:
const: 'Yes'
then:
properties:
restartReason:
type: string
title: Reason for restart
description: Provide a reason for restarting the service.
default: Applying new configuration.
minLength: 10
errorMessage:
minLength: 'Provide a more detailed reason (at least 10 characters).'
```
Each key under `dependencies` corresponds to a property name in the same parameter step. When the user changes a field value, only the matching `if`/`then` branch is displayed.
