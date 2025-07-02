# 3. Installing the Red Hat Edge Manager on Ansible Automation Platform
## 3.3. Integrating with Ansible Automation Platform




To integrate the Red Hat Edge Manager with your Ansible Automation Platform instance, follow these additional steps.

**Procedure**

1. Configure the integration settings by editing the configuration file:


```
sudo vi /etc/flightctl/service-config.yaml
```


1. Update the configuration file to integrate with Ansible Automation Platform:


```
global:      baseDomain: &lt;your-edge-manager-ip-or-domain&gt;<span id="CO1-1"><!--Empty--></span><span class="callout">1</span>auth:        type: aap<span id="CO1-2"><!--Empty--></span><span class="callout">2</span>insecureSkipTlsVerify: false<span id="CO1-3"><!--Empty--></span><span class="callout">3</span>aap:          apiUrl: https://your-aap-instance.example.com<span id="CO1-4"><!--Empty--></span><span class="callout">4</span>externalApiUrl: https://your-aap-instance.example.com<span id="CO1-5"><!--Empty--></span><span class="callout">5</span>oAuthApplicationClientId: &lt;client-id-from-oauth-app&gt;<span id="CO1-6"><!--Empty--></span><span class="callout">6</span>oAuthToken: &lt;your-oauth-token&gt;<span id="CO1-7"><!--Empty--></span><span class="callout">7</span>
```


1. Start the services:


```
sudo systemctl start flightctl.target
```




