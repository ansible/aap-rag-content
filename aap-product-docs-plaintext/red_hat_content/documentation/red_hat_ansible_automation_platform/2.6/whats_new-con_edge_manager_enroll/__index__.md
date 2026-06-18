# Enroll devices

To manage your devices with the Red Hat Edge Manager, you must enroll the devices to the Red Hat Edge Manager service.

The first time the Red Hat Edge Manager agent runs on a device, the agent prepares for the enrollment process by generating a cryptographic key pair. The cryptographic key pair serves as the unique cryptographic identity of the device. The key pair consists of a public and a private key. The private key never leaves the device, so that the device cannot be duplicated or impersonated.

When the device is not yet enrolled, the agent performs service discovery to find its Red Hat Edge Manager service instance. Then, the device establishes a secure, mTLS-protected network connection to the service. The device uses its X.509 enrollment certificate that the device acquired during image building or device provisioning. The device submits an enrollment request to the service that includes the following:

- a description of the device hardware and operating system
- an X.509 Certificate Signing Request which includes the cryptographic identity of the device to obtain the initial management certificate


The device is not considered trusted and remains quarantined in a device lobby until an authorized user approves or denies the request.

For more information, see the following sections:

## Enrollment methods

You can provision the enrollment endpoint and certificate to the device in the following ways:

Early binding
You can build an operating system image that includes the enrollment endpoint and certificate. Devices that use an early binding image can automatically connect to the defined service to request enrollment, without depending on any provisioning infrastructure. The devices share the same long-lived X.509 client certificate. However, in this case, the devices are bound to a specific service and owner.

Late binding
You can define the enrollment endpoint and certificate at provisioning time instead of including them in the operating system image. Devices that use a late binding image are not bound to a single owner or service and can have device-specific, short-lived X.509 client certificates. However, late binding requires virtualization or bare-metal provisioning infrastructure that can request device-specific enrollment endpoints and certificates from the Red Hat Edge Manager service and inject them into the provisioned system by using mechanisms such as *cloud-init*, *Ignition*, or *kickstart*.

Note:

The enrollment certificate is only used to secure the network connection for submitting an enrollment request. The enrollment certificate is not involved in the actual verification or approval of the enrollment request. The enrollment certificate is no longer used with enrolled devices, as the devices rely on device-specific management certificates instead.
