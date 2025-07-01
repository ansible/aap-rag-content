# 4. Search
## 4.1. Rules for searching
### 4.1.3. Other search considerations




Be aware of the following issues when searching in automation controller:

- There is currently no supported syntax for **OR** queries. All search terms are **AND** ed in the query parameters.
- The left part of a search parameter can be wrapped in quotes to support searching for strings with spaces. For more information, see [Rules for searching](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#ref-controller-search-tips) .
- Currently, the values in the Fields are direct attributes expected to be returned in a **GET** request. Whenever you search against one of the values, automation controller carries out an `    __icontains` search. So, for example, `    name:localhost` sends back `    ?name__icontains=localhost` . Automation controller currently performs this search for every Field value, even `    id` .


