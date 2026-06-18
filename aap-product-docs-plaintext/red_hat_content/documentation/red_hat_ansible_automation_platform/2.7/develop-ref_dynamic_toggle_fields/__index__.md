# Show or hide fields based on a toggle

Use a `boolean` toggle field to show or hide a group of additional fields.

In this example, selecting "Show advanced options" reveals one additional field. When the toggle is off, the field is hidden and not submitted.

```
parameters:
- title: Time server settings
required:
- ntpServers
properties:
ntpServers:
title: NTP servers
type: string
default: 0.rhel.pool.ntp.org, 1.rhel.pool.ntp.org
showAdvanced:
title: Show advanced options?
type: boolean
default: false
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
```
When `showAdvanced` is `true`, the form displays `maxSyncDelay`. When `showAdvanced` is `false`, the field is hidden.
