# Chapter 4. Sorting in the API




To give you examples that are easy to follow, we use the following URL throughout this guide:

```
https://&lt;gateway server name&gt;/api/controller/v2/groups/
```


<span id="controller-api-sorting-in-api"></span>
Learn how to use the order_by query parameter in a GET request to sort the returned {{model_verbose_name_plural}} by one or more fields, including how to specify reverse order by using a leading dash (-).


**Procedure**

- To specify that {{ model_verbose_name_plural }} are returned in a particular order, use the `    order_by` query string parameter on the `    GET` request:


```
https://&lt;gateway server name&gt;/api/controller/v2/model_verbose_name_plural?order_by={{ order_field }}
```


- Prefix the field name with a dash ( `        -` ) to sort in reverse:


```
https://&lt;gateway server name&gt;/api/controller/v2/model_verbose_name_plural?order_by=-{{ order_field }}
```


- You can specify the sorting fields by separating the field names with a comma ( `        ,` ):


```
https://&lt;gateway server name&gt;/api/controller/v2/model_verbose_name_plural?order_by={{ order_field }},some_other_field
```





