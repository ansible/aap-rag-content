# Troubleshoot failed event-driven automation triggers
## Resolve rulebook activations stuck in pending state

Diagnose and resolve issues preventing a rulebook activation from transitioning from Pending to a running, operational state.

### Procedure

Confirm whether there are other running activations and if you have reached the limits (for example, memory or CPU limits). 1.  If there are other activations running, terminate one or more of them, if possible.
2.  If not, verify that the `dispatcherd` service and the PostgreSQL database are running and reachable.

- Use the `dispatcherctl alive` command to verify the health and availability of background task workers.
- Check the status of the **PostgreSQL** service to ensure it can accept connections, as a database failure will prevent activations from transitioning out of the Pending state.

3.  If all systems are working as expected, check your eda-server internal logs in the worker, scheduler, API, and nginx containers and services to see if the problem can be determined. These logs reveal the source of the issue, such as an exception thrown by the code, a runtime error with network issues, or an error with the rulebook code. If your internal logs do not provide information that leads to resolution, report the issue to Red Hat support.

