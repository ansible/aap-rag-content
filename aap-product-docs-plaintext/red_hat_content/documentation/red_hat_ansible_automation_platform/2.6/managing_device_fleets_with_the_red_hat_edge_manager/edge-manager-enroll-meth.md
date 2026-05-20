# 2. Red Hat Edge Manager architecture
## 2.3. Device enrollment
### 2.3.1. Enrollment methods

You can provision the enrollment endpoint and certificate to the device in the following ways:

Early binding
You can build an operating system image that includes the enrollment endpoint and certificate. Devices that use an early binding image can automatically connect to the defined service to request enrollment, without depending on any provisioning infrastructure. The devices share the same long-lived X.509 client certificate. However, in this case, the devices are bound to a specific service and owner.

Late binding
You can define the enrollment endpoint and certificate at provisioning time instead of including them in the operating system image. Devices that use a late binding image are not bound to a single owner or service and can have device-specific, short-lived X.509 client certificates. However, late binding requires virtualization or bare-metal provisioning infrastructure that can request device-specific enrollment endpoints and certificates from the Red Hat Edge Manager service and inject them into the provisioned system by using mechanisms such as [cloud-init](https://cloud-init.io/), [Ignition](https://coreos.github.io/ignition/supported-platforms/), or [kickstart](https://anaconda-installer.readthedocs.io/en/latest/kickstart.html).

Note

The enrollment certificate is only used to secure the network connection for submitting an enrollment request. The enrollment certificate is not involved in the actual verification or approval of the enrollment request. The enrollment certificate is no longer used with enrolled devices, as the devices rely on device-specific management certificates instead.

