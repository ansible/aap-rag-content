# Chapter 7. Using pagination in the API




The API paginates responses for collections. This means that while a collection might contain tens or hundreds of thousands of objects, in each web request, only a limited number of results are returned for API performance reasons.


<span id="controller-api-using-pagination"></span>
When you receive the result for a collection, something similar to the following is displayed:


```
{'count': 25, 'next': 'http://testserver/api/controller/v2/some_resource?page=2', 'previous': None, 'results': [ ... ] }
```

**Procedure**

1. Request the page given by the "next" sequential URL, to get to the next page.
1. Use the `    page_size=XX` query string parameter to change the number of results returned for each request.


- The `        page_size` has a default maximum limit of 200, which is enforced when a user tries a value beyond it, for example, `        ?page_size=1000` . However, you can change this limit by setting the value in `        /etc/tower/conf.d/&lt;some file&gt;.py` to something higher. For example, `        MAX_PAGE_SIZE=1000` .

1. Use the page query string parameter to retrieve a particular page of results:


```
http://&lt;gateway server name&gt;/api/controller/v2/model_verbose_name?page_size=100&amp;page=2
```

Note
The preceding and following links returned with the results set these query string parameters automatically.

Do not request page sizes greater than 200.

The user interface uses smaller values to avoid scrolling.






