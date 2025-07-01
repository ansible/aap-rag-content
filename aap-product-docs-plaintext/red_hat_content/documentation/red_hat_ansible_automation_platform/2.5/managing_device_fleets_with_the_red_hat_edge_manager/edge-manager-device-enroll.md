# 2. Red Hat Edge Manager architecture
## 2.3. Device enrollment




You must enroll devices to a Red Hat Edge Manager service before you can start managing them. The Red Hat Edge Manager agent that runs on a device handles the device enrollment.

When the agent starts on a device, the agent searches for the configuration in the `/etc/flightctl/config.yaml` file. The file defines the following configurations:

- The enrollment endpoint, which is the Red Hat Edge Manager service that the agent connects to for enrollment.
- The enrollment certificate, which is the X.509 client certificate and key that the agent only uses to securely request enrollment from the Red Hat Edge Manager service.
-  **Optional** : Any additional agent configuration.


The agent starts the enrollment process by searching for the enrollment endpoint, the Red Hat Edge Manager service, that is defined in the configuration file. After establishing a secure, mTLS-protected network connection with the service, the agent submits an enrollment request to the service.

The request includes a description of hardware and operating system of the device, a X.509 certificate signing request, and the cryptographic identity of the device. The enrollment request must be approved by an authorized user. After the request is approved, the device becomes trusted and managed by the Red Hat Edge Manager service.

