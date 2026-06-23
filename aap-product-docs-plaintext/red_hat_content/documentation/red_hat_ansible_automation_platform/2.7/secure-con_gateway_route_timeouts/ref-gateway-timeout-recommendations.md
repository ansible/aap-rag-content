# Configure platform gateway route timeouts
## Gateway timeout recommendations

Platform gateway route timeout values determine how long the gateway waits for requests to complete before terminating the connection.

### Recommended timeout values by upload size

| Expected upload size | Recommended timeout       | Use case                          |
| -------------------- | ------------------------- | --------------------------------- |
| Up to 1 GB           | 600 seconds (10 minutes)  | Small execution environments      |
| 1-4 GB               | 1800 seconds (30 minutes) | Medium execution environments     |
| 4-10 GB              | 3600 seconds (1 hour)     | Large execution environments      |
| Over 10 GB           | 7200 seconds (2 hours)    | Enterprise execution environments |

### Calculating timeout values

If your environment requires specific settings, use the following formula to calculate a timeout value:

1. Measure your upload bandwidth by timing a test file upload.
2. Calculate the base timeout: `timeout_seconds = (file_size_in_GB x 1024) / (bandwidth_in_MB_per_second)`
3. Add a 25% buffer to the result: `recommended_timeout = timeout_seconds x 1.25`
4. Round the result up to the nearest multiple of 300 seconds (5 minutes).

### Performance considerations

Increasing timeout values might lead to the following issues:

- **Increased memory usage:** The gateway maintains connection state for all active uploads.
- **Connection pool exhaustion:** Many concurrent long-running uploads can consume all available connections.
- **Delayed error detection:** Network issues might take longer to surface.

### Best practices

- Set timeouts based on the largest file size you expect to upload.
- Monitor gateway resource usage during large uploads to automation hub.
- Schedule large uploads during off-peak hours.
- Use multiple smaller images instead of a single large image when possible.
