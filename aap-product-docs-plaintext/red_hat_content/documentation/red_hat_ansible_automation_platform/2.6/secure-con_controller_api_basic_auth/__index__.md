# Basic authentication

Basic authentication is stateless. You must send the base64-encoded username and password along with each request through the Authorization header. You can use this method for API calls from curl requests, Python scripts, or individual requests to the API.

OAuth 2 token authentication through platform gateway is the recommended method for accessing the API.

The following is an example of basic authentication with curl:

```
# the --user flag adds this Authorization header for us
curl -X GET --user 'user:password' https://<gateway server name>/api/gateway/v1/tokens/ -k -L
```

## Disable basic authentication

In Ansible Automation Platform 2.6 and earlier, you could disable basic authentication for security purposes.

Basic authentication is automatically disabled in Ansible Automation Platform 2.7 and cannot be re-enabled. All authentication must use OAuth 2 tokens created through platform gateway.

For authentication in Ansible Automation Platform 2.7, see:
