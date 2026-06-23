# Configure platform gateway route timeouts

In Ansible Automation Platform 2.7, all API access to platform components goes through platform gateway. Gateway-level timeout settings control how long platform gateway waits for backend services to respond before closing a connection.

Important:

If you experience timeout errors when uploading container images or collections to automation hub, increase gateway route timeouts to allow more time for the upload to complete.

As all traffic now routes through platform gateway, gateway-level settings for request body size limits and connection timeouts apply to uploads that previously went directly to automation hub.

Collection uploads and container image uploads have different size characteristics and are affected by different gateway settings.

