# Manage Windows targets with Active Directory

Manage secure Active Directory authentication and identity delegation.

**Dynamic Active Directory LDAP Inventories**

The `microsoft.ad.ldap` inventory plugin queries Active Directory domain hierarchies dynamically. This eliminates static file maintenance across vast Windows server footprints.

- **Capabilities**: Built-in support for Jinja2 group assignment templates, runtime *Local Administrator Password Solution* (LAPS) password decryption, and native *Simple and Protected GSSAPI Negotiation Mechanism* (SPNEGO) authentication compliance.

**Group managed service accounts (gMSA)**

Group Managed Service Accounts (gMSAs) provide automatic password rotation but cannot serve as the initial interactive connection identity for WinRM, PSRP, or OpenSSH endpoints. However, automation playbooks can programmatically deploy, rotate, and map gMSA targets to Windows tasks, schedules, and application pools using the `microsoft.ad.service_account` and `microsoft.ad.kds_root_key` modules.
