# Configure the appliance at first boot
## Configure after deployment

If you deployed the appliance without providing configuration, portal services do not start. You can configure the appliance after deployment by editing the configuration files directly.

1. SSH into the appliance using the key you provided through cloud-init or another method.
2. Edit the application configuration file:

```terminal
$ sudo vi /etc/portal/configs/app-config/app-config.production.yaml
```

3. Restart the portal service:

```terminal
$ sudo systemctl restart portal
```

