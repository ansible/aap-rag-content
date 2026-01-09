# Chapter 5. Using the search query string parameter




The search query string parameter provides a simple yet powerful way to filter and find specific resources within your Ansible Automation Platform API. Use a non-case-sensitive search to locate relevant data across designated text fields in a model and extend your search across related fields to find exactly what you need.


<span id="proc-controller-api-search"></span>
Learn how to use the search query parameter to perform a general, non-case-sensitive search across all text fields of an API model and how to use the `related__search` parameter to search across related fields.


**Procedure**

- Use the search query string parameter to perform a non-case-sensitive search within all designated text fields of a model:


```
https://&lt;gateway server name&gt;/api/controller/v2/model_verbose_name?search=findme
```


- To search across related fields, use the following:


```
https://&lt;gateway_server_name&gt;/api/controller/v2/model_verbose_name?related__search=findme
```




