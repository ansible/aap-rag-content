# Chapter 5. Using the search query string parameter




**Procedure**

- Use the search query string parameter to perform a non-case-sensitive search within all designated text fields of a model:


```
https://&lt;controller server name&gt;/api/v2/model_verbose_name?search=findme
```

- To search across related fields, use the following:


```
https://&lt;controller server name&gt;/api/v2/model_verbose_name?related__search=findme
```

