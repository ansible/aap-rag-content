# 10. Authenticating in the API
## 10.2. Basic authentication




Basic authentication is stateless, therefore, you must send the base64-encoded username and password along with each request through the Authorization header. You can use this for API calls from curl requests, python scripts, or individual requests to the API. We recommend OAuth 2 Token Authentication for accessing the API when at all possible.

The following is an example of Basic authentication with curl:

```
# the --user flag adds this Authorization header for us
curl -X GET --user 'user:password' https://&lt;controller-host&gt;/api/gateway/v1/tokens/ -k -L
```

**Additional resources**

For more information about Basic authentication, see [The 'Basic' HTTP Authentication Scheme](https://datatracker.ietf.org/doc/html/rfc7617) .



<span id="disabling_basic_authentication"></span>
#### Disabling Basic authentication


You can disable Basic authentication for security purposes.

**Procedure**

1. From the navigation panel, selectSettings→Platform gateway.
1. ClickEdit platform gateway settings.
1. Disable the option **Gateway basic auth enabled** .
1. ClickSave platform gateway settings.


