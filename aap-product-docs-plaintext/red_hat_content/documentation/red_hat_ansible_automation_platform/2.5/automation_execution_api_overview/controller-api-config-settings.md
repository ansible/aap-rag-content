# 8. Access resources
## 8.1. Configuration settings




There are two named-URL-related configuration settings available under `/api/v2/settings/named-url/: NAMED_URL_FORMATS` and `NAMED_URL_GRAPH_NODES` .

`NAMED_URL_FORMATS` is a read only key-value pair list of all available named URL identifier formats. The following shows an example `NAMED_URL_FORMATS` :

```
"NAMED_URL_FORMATS": {
"organizations": "&lt;name&gt;",
"teams": "&lt;name&gt;++&lt;organization.name&gt;",
"credential_types": "&lt;name&gt;+&lt;kind&gt;",
"credentials": "&lt;name&gt;++&lt;credential_type.name&gt;+&lt;credential_type.kind&gt;++&lt;organization.name&gt;",
"notification_templates": "&lt;name&gt;++&lt;organization.name&gt;",
"job_templates": "&lt;name&gt;++&lt;organization.name&gt;",
"projects": "&lt;name&gt;++&lt;organization.name&gt;",
"inventories": "&lt;name&gt;++&lt;organization.name&gt;",
"hosts": "&lt;name&gt;++&lt;inventory.name&gt;++&lt;organization.name&gt;",
"groups": "&lt;name&gt;++&lt;inventory.name&gt;++&lt;organization.name&gt;",
"inventory_sources": "&lt;name&gt;++&lt;inventory.name&gt;++&lt;organization.name&gt;",
"inventory_scripts": "&lt;name&gt;++&lt;organization.name&gt;",
"instance_groups": "&lt;name&gt;",
"labels": "&lt;name&gt;++&lt;organization.name&gt;",
"workflow_job_templates": "&lt;name&gt;++&lt;organization.name&gt;",
"workflow_job_template_nodes": "&lt;identifier&gt;++&lt;workflow_job_template.name&gt;++&lt;organization.name&gt;",
"applications": "&lt;name&gt;++&lt;organization.name&gt;",
"users": "&lt;username&gt;",
"instances": "&lt;hostname&gt;"
}
```

For each item in `NAMED_URL_FORMATS` , the key is the API name of the resource to have named URL. The value is a string indicating how to form a human-readable unique identifier for that resource. `NAMED_URL_FORMATS` only lists the resources that can have named URL, any resource not listed there has no named URL. If a resource can have named URL, its objects must have a `named_url` field that represents the object-specific named URL. That field is only visible under detail view, not list view. You can access specified resource objects by using accurately generated named URL. This the object and its related URLs. For example, if `/api/v2/res_name/obj_slug/` is valid, `/api/v2/res_name/obj_slug/related_res_name/` is also valid.

`NAMED_URL_FORMATS` are instructive enough to compose human-readable unique identifiers and named URLs themselves. For ease-of-use, every object of a resource that can have named URL has a related field `named_url` that displays that object’s named URL. You can copy and paste that field for your own custom use. For more information, see the help text of the API browser if a resource object has named URL.

You can manually decide the named URL label, for example with ID 5. To compose a named URL for this specific resource object by using `NAMED_URL_FORMATS` , first look up the labels field of `NAMED_URL_FORMATS` to get the identifier format `&lt;name&gt;++&lt;organization.name&gt;` :

- The first part of the URL format is `    &lt;name&gt;` , which indicates that you can find the label resource detail in `    /api/v2/labels/5/` , and look for `    name` field in returned JSON. If you have the `    name` field with value `    Foo` , then the first part of the unique identifier is `    Foo` .
- The second part of the format is double plus sign ++. That is the delimiter that separates different parts of a unique identifier. Append them to the unique identifier to get `    Foo++` .
- The third part of the format is `    &lt;organization.name&gt;` , which indicates that the field is not in the current label object under investigation, but in an organization that the label object points to. As the format indicates, look up the organization in the related field of the current returned JSON. That field might not exist. If it exists, follow the URL given in that field, for example, `    /api/v2/organizations/3/` , to get the details of the specific organization, extract its name field, for example, "Default", and append it to the current unique identifier. Since `    &lt;organizations.name&gt;` is the last part of the format, it generates the following named URL: `    /api/v2/labels/Foo++Default/` .

In the case where an organization does not exist in the related field of the label object detail, append an empty string instead. This does not alter the current identifier. Therefore, `    Foo++` becomes the final unique identifier and the resulting generated named URL becomes `    /api/v2/labels/Foo++/` .




An important aspect of generating a unique identifier for named URL has to do with reserved characters. As the identifier is part of a URL, the following reserved characters by URL standard are encoded by percentage symbols: `;/?:@=&amp;[]` . For example, if an organization is named `;/?:@=&amp;[]` , its unique identifier should be `%3B%2F%3F%3A%40%3D%26%5B%5D` . Another special reserved character is `+` , which is not reserved by URL standard but used by named URL to link different parts of an identifier. It is encoded by `[+]` . For example, if an organization is named `[+]` , its unique identifier is `%5B[+]%5D` , where original `[` and `]` are percent encoded and `+` is converted to `[+]` .

Although you cannot manually change `NAMED_URL_FORMATS` , modifications do occur automatically and expand over time, reflecting underlying resource modification and expansion. Consult the `NAMED_URL_FORMATS` on the same cluster where you want to use the named URL feature.

`NAMED_URL_GRAPH_NODES` is another read-only list of key-value pairs that exposes the internal graph data structure used to manage named URLs. This is not intended to be human-readable but must be used for programmatically generating named URLs. An example script for generating named URL given the primary key of arbitrary resource objects that can have a named URL, using info provided by `NAMED_URL_GRAPH_NODES` , can be found in [GitHub](https://github.com/ansible/awx/blob/devel/tools/scripts/pk_to_named_url.py) .

