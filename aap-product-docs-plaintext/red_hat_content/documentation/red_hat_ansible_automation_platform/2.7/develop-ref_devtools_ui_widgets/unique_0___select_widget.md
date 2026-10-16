# Standard UI widgets
## Standard UI widgets
### Select widget

The `select` widget displays a dropdown menu that enables users to choose a single value from a predefined list of options.

```
properties:
environment:
type: string
title: Environment
enum: ['dev', 'staging', 'prod']
ui:widget: select
default: 'dev'
```

