# Configure platform gateway route timeouts
## Container image uploads

Container images for execution environments can exceed 4 GB. These uploads use chunked transfer encoding, so they are primarily affected by gateway route timeout settings rather than body size limits.

