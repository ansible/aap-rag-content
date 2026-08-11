# Search field values

You can determine the available search fields and related search fields for any resource by sending an `OPTIONS` request to the API endpoint.

## Procedure

1.  Send a `GET` request to the resource endpoint to identify the available field names.
Field names come from the keys returned in the `GET` response. The `url`, `related`, and `summary_fields` keys are excluded.

To search for jobs by type, enter `type:run` on the Jobs page. To discover valid values for the `type` field, send an `OPTIONS` request to `/api/v2/jobs` and locate the `"type"` entry.

2.  Send an `OPTIONS` request to the same endpoint to find related search fields.
Related search fields are listed in the `related_search_fields` attribute of the `OPTIONS` response. Strip the `__search` suffix to get the related field name you can use in the search bar.

The `/api/v2/jobs` endpoint returns:

```
"related_search_fields": [
"modified_by__search",
"project__search",
"credentials__search",
"created_by__search",
"inventory__search",
"labels__search",
"schedule__search",
"job_template__search",
"instance_group__search",
"hosts__search"
]
```

## Results

Any query that does not start with a recognized field or related field name is treated as a generic string search, equivalent to `?search=<term>`.
