# Optimize request timeouts
## Cascading client timeouts
### Timeout grace periods

At the uWSGI layer, the `uwsgi_timeout_grace_period` allows the application to attempt a graceful shutdown. During this period, the application displays a traceback of the current stack position at the time of the timeout. If the process does not exit within the grace period, Ansible Automation Platform maintains forcefully terminates it.

