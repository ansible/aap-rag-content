+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_controller_api_browsing_api"
template = "docs/aem-title.html"
title = "Browse the REST API - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_controller_api_tools/", "Use the REST API to browse, query, filter, and authenticate"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-assembly_controller_api_browsing_api/aem-page/develop-assembly_controller_api_browsing_api.html"
last_crumb = "Browse the REST API"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Browse the REST API"
oversized = "false"
page_slug = "develop-assembly_controller_api_browsing_api"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-assembly_controller_api_browsing_api"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-assembly_controller_api_browsing_api/toc/toc.json"
type = "aem-page"
+++

# Browse the REST API

Access and use the platform gateway REST API through a web browser. You can find the recommended current version (v2), view documentation for endpoints, and use GET, PUT, and POST methods with JSON formatting.

## Procedure

1.  Go to the REST API in a web browser at:
      `https://<gateway server name>/api/controller/v2`

2.  Click the **v2** link next to **current versions** or **available versions**.
      The API supports version 2.

3.  Perform a `GET` with the `/api/` endpoint to get the `current_version`, which is the recommended version.
4.  Click the question mark icon on the navigation menu for documentation on the access methods for that particular API endpoint and what data is returned when using those methods.
5.  Use the `PUT` and `POST` verbs on the specific API pages by formatting JSON in the various text fields.
  
  Note:
      You can also view changed settings from factory defaults at the `/api/gateway/v1/settings/` endpoint. It reflects changes you made in the API browser, not changed settings that come from static settings files.

## Find resources with the search query string parameter

The API is versioned for compatibility reasons. You can see what API versions are available by querying `/api/`.

You might have to specify the content or type on `POST` or `PUT` requests:

- `PUT`: Update a specific resource (by an identifier) or a collection of resources. You can also use `PUT` to create a specific resource if you know the resource identifier before-hand.
- `POST`: Create a new resource. Also acts as a catch-all verb for operations that do not fit into the other categories.


All URIs not ending with "/" receive a 301 redirect.

Note:

The formatting of `extra_vars` attached to Job Template records is preserved. YAML is returned as YAML with formatting and comments preserved, and JSON is returned as JSON.

## Sort the API

Learn about managing ordering and sorting in the API.

To give you examples that are easy to follow, we use the following URL throughout this section:

```
https://<gateway server name>/api/controller/v2/groups/
```

## Filter resources through the API

The system recognizes a collection as a "queryset". You can filter this by using various operators.

## Advanced queries in the API

You can use additional query string parameters used to filter the list of results returned to those matching a given value. You can only use fields and relations that exist in the database for filtering.

Ensure that any special characters in the specified value are URL-encoded. For example:

```
?field=value%20xyz
```
Fields can also span relations, only for fields and relationships defined in the database:

```
?other__field=value
```
To exclude results matching certain criteria, prefix the field parameter with `not__`:

```
?not__field=value
```
By default, all query string filters are AND’ed together, so only the results matching all filters are returned. To combine results matching any one of multiple criteria, prefix each query string parameter with `or__`:

```
?or__field=value&or__field=othervalue
?or__not__field=value&or__field=othervalue
```
The default AND filtering applies all filters simultaneously to each related object being filtered across database relationships. The chain filter instead applies filters separately for each related object. To use this, prefix the query string parameter with `chain__`:

```
?chain__related__field=value&chain__related__field2=othervalue
?chain__not__related__field=value&chain__related__field2=othervalue
```
If you write the first query as `?relatedfield=value&relatedfield2=othervalue`, it returns only the primary objects where the same related object satisfied both conditions. As written by using the chain filter, it would return the intersection of primary objects matching each condition.

## Field lookups

Field lookups allow you to filter API results based on specific criteria. You can use field lookups for more advanced queries, by appending the lookup to the field name:

```
?field__lookup=value
```
The following field lookups are supported:

- exact: Exact match (default lookup if not specified, see the following note for more information).
- iexact: Case-insensitive version of exact.
- contains: Field contains value.
- icontains: Case-insensitive version of contains.
- startswith: Field starts with value.
- istartswith: Case-insensitive version of startswith.
- endswith: Field ends with value.
- iendswith: Case-insensitive version of endswith.
- regex: Field matches the given regular expression.
- iregex: Case-insensitive version of regular expression.
- gt: Greater than comparison.
- gte: Greater than or equal to comparison.
- lt: Less than comparison.
- lte: Less than or equal to comparison.
- isnull: Check whether the given field or related object is null; expects a boolean value.
- in: Check whether the given field’s value is present in the list provided; expects a list of items.
- You can specify boolean values as `True` or `1` for true, `False` or `0` for false (both case-insensitive).


For example, `?created__gte=2023-01-01` provides a list of items created after 1/1/2023.

You can specify null values as `None` or `Null` (both case-insensitive), though we recommend using the `isnull` lookup to explicitly check for null values.

You can specify lists (for the `in` lookup) as a comma-separated list of values. Filtering based on the requesting user’s level of access by query string parameter:

- `role_level`: Level of role to filter on, such as `admin_role`


Note:

Earlier releases of Ansible Automation Platform returned queries with **_exact** results by default. As a workaround, set the `limit` to `?limit_exact` for the default filter. For example, `/api/controller/v2/jobs/?limit_exact=example.domain.com` results in:

```
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
...
```

## View collection responses that are not shown by default

The API paginates responses for collections. This means that while a collection might contain tens or hundreds of thousands of objects, in each web request, only a limited number of results are returned for API performance reasons.

## Access resource objects through API identifiers

The platform gateway API uses a primary key to access individual resource objects. You can access resources by using resource-specific, human-readable identifiers through the named URL feature.

The following example shows the named URL path where you can access a resource object without an auxiliary query string:

```
/api/controller/v2/hosts/host_name++inv_name++org_name/
```

## API configuration values

There are two named-URL-related configuration settings available under `/api/controller/v2/settings/named-url/: NAMED_URL_FORMATS` and `NAMED_URL_GRAPH_NODES`.

`NAMED_URL_FORMATS` is a read only key-value pair list of all available named URL identifier formats. The following shows an example `NAMED_URL_FORMATS`:

```
"NAMED_URL_FORMATS": {
"organizations": "<name>",
"teams": "<name>++<organization.name>",
"credential_types": "<name>+<kind>",
"credentials": "<name>++<credential_type.name>+<credential_type.kind>++<organization.name>",
"notification_templates": "<name>++<organization.name>",
"job_templates": "<name>++<organization.name>",
"projects": "<name>++<organization.name>",
"inventories": "<name>++<organization.name>",
"hosts": "<name>++<inventory.name>++<organization.name>",
"groups": "<name>++<inventory.name>++<organization.name>",
"inventory_sources": "<name>++<inventory.name>++<organization.name>",
"inventory_scripts": "<name>++<organization.name>",
"instance_groups": "<name>",
"labels": "<name>++<organization.name>",
"workflow_job_templates": "<name>++<organization.name>",
"workflow_job_template_nodes": "<identifier>++<workflow_job_template.name>++<organization.name>",
"applications": "<name>++<organization.name>",
"users": "<username>",
"instances": "<hostname>"
}
```
For each item in `NAMED_URL_FORMATS`, the key is the API name of the resource to have named URL. The value is a string indicating how to form a human-readable unique identifier for that resource. `NAMED_URL_FORMATS` only lists the resources that can have named URL, any resource not listed there has no named URL. If a resource can have named URL, its objects must have a `named_url` field that represents the object-specific named URL. That field is only visible under detail view, not list view. You can access specified resource objects by using accurately generated named URL. This the object and its related URLs. For example, if `/api/controller/v2/res_name/obj_slug/` is valid, `/api/controller/v2/res_name/obj_slug/related_res_name/` is also valid.

`NAMED_URL_FORMATS` are instructive enough to compose human-readable unique identifiers and named URLs themselves. For ease-of-use, every object of a resource that can have named URL has a related field `named_url` that displays that object’s named URL. You can copy and paste that field for your own custom use. For more information, see the help text of the API browser if a resource object has named URL.

You can manually decide the named URL label, for example with ID 5. To compose a named URL for this specific resource object by using `NAMED_URL_FORMATS`, first look up the labels field of `NAMED_URL_FORMATS` to get the identifier format `<name>++<organization.name>`:

- The first part of the URL format is `<name>`, which indicates that you can find the label resource detail in `/api/controller/v2/labels/5/`, and look for `name` field in returned JSON. If you have the `name` field with value `Foo`, then the first part of the unique identifier is `Foo`.

- The second part of the format is double plus sign ++. That is the delimiter that separates different parts of a unique identifier. Append them to the unique identifier to get `Foo++`.

- The third part of the format is `<organization.name>`, which indicates that the field is not in the current label object under investigation, but in an organization that the label object points to. As the format indicates, look up the organization in the related field of the current returned JSON. That field might not exist. If it exists, follow the URL given in that field, for example, `/api/gateway/v1/organizations/3/`, to get the details of the specific organization, extract its name field, for example, "Default", and append it to the current unique identifier. Since `<organizations.name>` is the last part of the format, it generates the following named URL: `/api/controller/v2/labels/Foo++Default/`. In the case where an organization does not exist in the related field of the label object detail, append an empty string instead. This does not alter the current identifier. Therefore, `Foo++` becomes the final unique identifier and the resulting generated named URL becomes `/api/controller/v2/labels/Foo++/`.

An important aspect of generating a unique identifier for named URL has to do with reserved characters. As the identifier is part of a URL, the following reserved characters by URL standard are encoded by percentage symbols: `;/?:@=&[]`. For example, if an organization is named `;/?:@=&[]`, its unique identifier should be `%3B%2F%3F%3A%40%3D%26%5B%5D`. Another special reserved character is `` `, which is not reserved by URL standard but used by named URL to link different parts of an identifier. It is encoded by `[] ``. For example, if an organization is named ``[]`, its unique identifier is `%5B[]%5D``, where original `[` and `]` are percent encoded and `` ` is converted to `[] ``.

Although you cannot manually change `NAMED_URL_FORMATS`, modifications do occur automatically and expand over time, reflecting underlying resource modification and expansion. Consult the `NAMED_URL_FORMATS` on the same cluster where you want to use the named URL feature.

`NAMED_URL_GRAPH_NODES` is another read-only list of key-value pairs that exposes the internal graph data structure used to manage named URLs. This is not intended to be human-readable but must be used for programmatically generating named URLs. An example script for generating named URL given the primary key of arbitrary resource objects that can have a named URL, using info provided by `NAMED_URL_GRAPH_NODES`, can be found in [GitHub](https://github.com/ansible/awx/blob/devel/tools/scripts/pk_to_named_url.py).

## Understand how to identify resources by name

The API uses a consistent protocol to generate human-readable unique identifiers for resources that can be addressed by name in the API and the web interface.

Resources are identifiable by their unique keys, which are tuples of resource fields. Every resource is guaranteed to have its primary key number alone as a unique key, but there might be many other unique keys. A resource can generate an identifier format and, therefore, have a named URL if it has at least one unique key that satisfies the following rules:

1. The key must contain only fields that are either the `name` field, or text fields with a finite number of possible choices (such as credential type resource’s `kind` field).
2. The only permitted exceptional field that breaks the preceding rule is a many-to-one related field relating to a resource other than itself, which is also allowed to have a slug.


If there are resources `Foo` and `Bar`, both `Foo` and `Bar` contain a name field and a choice field that can only have values "yes" or "no". Additionally, resource `Foo` has a many-to-one field (a foreign key) relating to `Bar`, for example `fk`. `Foo` has a unique key tuple (`name`, `choice`, `fk`) and `Bar` has a unique key tuple (`name`, `choice`). `Bar` can have named URL because it satisfies the preceding first rule. `Foo` can also have named URL, even though it breaks the first rule, the extra field breaking rule number one is the `fk` field, which is many-to-one-related to `Bar` and `Bar` can have named URL.

For resources satisfying rule number one, their human-readable unique identifiers are combinations of foreign key fields, delimited by `` `. In specific, resource `Bar` in the preceding example has slug format `<name><choice> ``.

Note that the field order matters in slug format and the `name` field always comes first if present, followed by the remaining fields arranged in lexicographic order of field name. For example, if `Bar` also has an `a_choice` field satisfying rule one and the unique key becomes (`name`, `choice`, `a_choice`), its slug format becomes `<name><a_choice><choice>`.

For resources satisfying rule number two, if traced back through the extra foreign key fields, the result is a tree of resources that identify objects of that resource. To generate the identifier format, each resource in the traceback tree generates its own part of the standalone format, using all fields but the foreign keys. Finally, all parts are combined by `++` in the following order:

- Put standalone format as the first identifier part.
- Recursively generate unique identifiers for each resource. The underlying resource is pointing to using a foreign key (a child of a traceback tree node).
- Treat generated unique identifiers as the rest of the identifier components. Sort them in lexicographic order of corresponding foreign keys.
- Combine all components together using `++` to generate the final identifier format.


When generating an identifier format for resource `Foo`, the API generates the standalone formats, ``<name><choice>` for `Foo` and `<fk.name><fk.choice>`` for `Bar`, then combines them together to be `<name><choice>+<fk.name>+<fk.choice>`.

When generating identifiers according to the given identifier format, there are cases where a foreign key might point to nowhere. In this case, the API substitutes the part of the format corresponding to the resource the foreign key should point to with an empty string. For example, if a `Foo` object has the `name ="alice"`, `choice ="yes",` but `fk field = None`, its resulting identifier is `alice+yes++`.
