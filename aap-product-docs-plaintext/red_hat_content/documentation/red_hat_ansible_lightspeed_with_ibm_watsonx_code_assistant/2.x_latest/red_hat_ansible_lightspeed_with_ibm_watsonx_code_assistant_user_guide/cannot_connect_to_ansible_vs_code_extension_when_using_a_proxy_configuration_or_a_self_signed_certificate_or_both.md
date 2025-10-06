# 7. Troubleshooting
## 7.3. Troubleshooting Ansible Visual Studio Code extension errors
### 7.3.3. Cannot connect to Ansible VS code extension when using a proxy configuration or a self-signed certificate or both




You might encounter errors when connecting with to the Ansible VS code extension through a proxy. Connections to the outbound domain `https://c.ai.ansible.redhat.com` fail and a network error message is displayed.

To resolve this issue, you must add the URL `https://c.ai.ansible.redhat.com/` in VS Code proxy settings. If you are using Red Hat Single Sign-On (RH-SSO) to authenticate users, then you must also grant access to `https://sso.redhat.com` in VS code proxy settings.

To modify the proxy settings in VS code, perform the following tasks:

1. Open Visual Studio Code.
1. Navigate to **File > Preferences > Settings** .
1. SelectApplication→Proxyin the sidebar.
1. In the **Http: Proxy** field, add the following URLs to the proxy:


-  `        https://c.ai.ansible.redhat.com/`
-  `        https://sso.redhat.com` , if you are using RH-SSO to authenticate users.

1. In the **http: Proxy Support** drop down list, select **Override** .
1. Search for and select the following configuration keys:


-  **Electron Fetch**
-  **System Certificates V2** if you are using your own Certificate Authority (CA).



For information about how to set up proxy support in VS Code, see [Proxy server support](https://code.visualstudio.com/docs/setup/network#_proxy-server-support) in VS Code documentation and [Proxy settings and fallback](https://www.chromium.org/developers/design-documents/network-stack/proxy-settings-fallback/) in The Chromium Project documentation.

