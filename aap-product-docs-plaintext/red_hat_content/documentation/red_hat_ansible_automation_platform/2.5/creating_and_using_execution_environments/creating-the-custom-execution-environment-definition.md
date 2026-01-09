# 3. Using Ansible Builder
## 3.5. Creating the custom execution environment definition




When you have installed Ansible Builder, use the following steps to create your custom execution environment.

**Procedure**

1. Create a directory to store your custom execution environment build artifacts. Any new files created with the following steps are created under this directory.


```
$ mkdir $HOME/custom-ee $HOME/custom-ee/files    $ cd $HOME/custom-ee/
```


1. Create an `    execution-environment.yml` file that defines the requirements for your custom execution environment.

Note
Version 3 of the execution environment definition format is required, so ensure the `    execution-environment.yml` file contains `    version: 3` explicitly before continuing.




1. Override the base image to point to the minimal execution environment available in your private automation hub.
1. Define the additional build files needed to point to any disconnected content sources that will be used in the build process. Your custom `        execution-environment.yml` file should look similar to the following example:


```
version: 3                images:          base_image:            name: private-hub.example.com/ee-minimal-rhel8:latest                dependencies:          python: requirements.txt          galaxy: requirements.yml                additional_build_files:          - src: files/ansible.cfg            dest: configs          - src: files/pip.conf            dest: configs          - src: files/hub-ca.crt            dest: configs          # uncomment if custom RPM repositories are required          #- src: files/custom.repo          #  dest: configs                additional_build_steps:          prepend_base:            # copy a custom pip.conf to override the location of the PyPI content            - ADD _build/configs/pip.conf /etc/pip.conf            # remove the default UBI repository definition            - RUN rm -f /etc/yum.repos.d/ubi.repo            # copy the hub CA certificate and update the trust store            - ADD _build/configs/hub-ca.crt /etc/pki/ca-trust/source/anchors            - RUN update-ca-trust            # if needed, uncomment to add a custom RPM repository configuration            #- ADD _build/configs/custom.repo /etc/yum.repos.d/custom.repo                  prepend_galaxy:            - ADD _build/configs/ansible.cfg ~/.ansible.cfg                ...
```



1. Create an `    ansible.cfg` file under the `    files/` subdirectory that points to your private automation hub.


```
$ cat files/ansible.cfg    [galaxy]    server_list = private_hub        [galaxy_server.private_hub]    url = /https://private-hub.example.com/api/galaxy/
```


1. Create a `    pip.conf` file under the `    files/` subdirectory which points to the internal PyPI mirror (a web server or something like Nexus):


```
$ cat files/pip.conf    [global]    index-url = https://&lt;pypi_mirror_fqdn&gt;/    trusted-host = &lt;pypi_mirror_fqdn&gt;
```


1. Optional: If you use a `    bindep.txt` file to add RPMs the custom execution environment, create a `    custom.repo` file under the `    files/` subdirectory that points to your disconnected Satellite or other location hosting the RPM repositories. If this step is necessary, uncomment the steps in the example `    execution-environment.yml` file that correspond with the `    custom.repo` file.

The following example is for the UBI repositories. Other local repositories can be added to this file as well. The URL path might need to change depending on where the mirror content is located on the web server.


```
$ cat files/custom.repo    [ubi-8-baseos]    name = Red Hat Universal Base Image 8 (RPMs) - BaseOS    baseurl = http://&lt;ubi_mirror_fqdn&gt;/repos/ubi-8-baseos    enabled = 1    gpgkey = file:///etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release    gpgcheck = 1        [ubi-8-appstream]    name = Red Hat Universal Base Image 8 (RPMs) - AppStream    baseurl = http://&lt;ubi_mirror_fqdn&gt;/repos/ubi-8-appstream    enabled = 1    gpgkey = file:///etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release    gpgcheck = 1
```


1. Add the CA certificate used to sign the private automation hub web server certificate. If the private automation hub uses self-signed certificates provided by the installer:


1. Copy the file `        /etc/pulp/certs/pulp_webserver.crt` from your private automation hub and name it `        hub-ca.crt` .
1. Add the `        hub-ca.crt` file to the `        files/` subdirectory.

1. If the private automation hub uses user-provided certificates signed by a certificate authority:


1. Make a copy of that CA certificate and name it `        hub-ca.crt` .
1. Add the `        hub-ca.crt` file to the `        files/`` subdirectory.

1. When you have completed the preceding steps, create your python `    requirements.txt` and ansible collection `    requirements.yml` files, with the content needed for your custom execution environment image.

Note
Any required collections must already be uploaded into your private automation hub.



The following files should exist under the `    custom-ee/` directory, with `    bindep.txt` and `    files/custom.repo` being optional:


```
$ cd $HOME/custom-ee    $ tree .    .    ├── bindep.txt    ├── execution-environment.yml    ├── files    │   ├── ansible.cfg    │   ├── custom.repo    │   ├── hub-ca.crt    │   └── pip.conf    ├── requirements.txt    └── requirements.yml        1 directory, 8 files
```




**Additional resources**

-  [Execution Environment Definition: Version 3 Format](https://ansible-builder.readthedocs.io/en/stable/definition/)


