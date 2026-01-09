# 10. Authenticating in the API
## 10.2. Basic authentication




Basic authentication is stateless, therefore, you must send the base64-encoded username and password along with each request through the Authorization header. You can use this for API calls from curl requests, python scripts, or individual requests to the API.

We recommend OAuth 2 Token Authentication for accessing the API when at all possible.

The following is an example of Basic authentication with curl:

```
# the --user flag adds this Authorization header for us
curl -X GET --user 'user:password' https://&lt;controller-host&gt;/api/gateway/v1/tokens/ -k -L
```

**Additional resources**

-  [The 'Basic' HTTP Authentication Scheme](https://datatracker.ietf.org/doc/html/rfc7617)


