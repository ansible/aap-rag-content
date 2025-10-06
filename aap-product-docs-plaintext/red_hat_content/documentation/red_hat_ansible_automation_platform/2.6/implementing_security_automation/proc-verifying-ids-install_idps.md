# 2. Automating Network Intrusion Detection and Prevention Systems (IDPS) with Ansible Automation Platform
## 2.1. Requirements and prerequisites
### 2.1.1. Verifying your IDPS installation




Use the following procedure to verify that Snort has been configured successfully:

**Procedure**

1. Call snort using `    sudo` and ask for the version:


```
$ sudo snort --version           ,,_     -*&gt; Snort! &lt;*-      o"  )~   Version 2.9.13 GRE (Build 15013)      ""    By Martin Roesch &amp; The Snort Team: http://www.snort.org/contact#team            Copyright (C) 2014-2019 Cisco and/or its affiliates. All rights reserved.            Copyright (C) 1998-2013 Sourcefire, Inc., et al.            Using libpcap version 1.5.3            Using PCRE version: 8.32 2012-11-30            Using ZLIB version: 1.2.7
```


1. Verify that the service is actively running using the following command:

`    sudo systemctl` :


```
$ sudo systemctl status snort    ● snort.service - Snort service       Loaded: loaded (/etc/systemd/system/snort.service; enabled; vendor preset: disabled)       Active: active (running) since Mon 2019-08-26 17:06:10 UTC; 1s ago      Main PID: 17217 (snort)       CGroup: /system.slice/snort.service               └─17217 /usr/sbin/snort -u root -g root -c /etc/snort/snort.conf -i eth0 -p -R 1 --pid-path=/var/run/snort --no-interface-pidfile --nolock-pidfile    [...]
```


1. If the Snort service is not actively running, restart it with `    systemctl restart snort` and recheck the status.
1. When you confirm that the service is actively running, exit the Snort server by simultaneously pressing `    CTRL` and `    D` , or by typing `    exit` on the command line. All further interaction will be done through Ansible Automation Platform from the Ansible control host.


