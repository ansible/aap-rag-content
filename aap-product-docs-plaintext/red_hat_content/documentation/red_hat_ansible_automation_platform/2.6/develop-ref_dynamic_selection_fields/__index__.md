# Show different fields based on a selection

Use an `enum` field with `dependencies` and `allOf` to display different configuration fields for each option.

In this example, selecting a database type reveals a version dropdown specific to that engine:

```
properties:
dbType:
title: Database type
type: string
enum:
- PostgreSQL
- MySQL
dependencies:
dbType:
allOf:
- if:
properties:
dbType:
const: PostgreSQL
then:
properties:
version:
type: number
enum: [13, 14, 15]
title: PostgreSQL version
default: 15
- if:
properties:
dbType:
const: MySQL
then:
properties:
version:
type: string
enum: ['5.7', '8.0']
title: MySQL version
default: '8.0'
```
Each `if`/`then` block in the `allOf` array matches one `enum` value. Selecting "PostgreSQL" shows the PostgreSQL version list; selecting "MySQL" replaces it with the MySQL version list.
