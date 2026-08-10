# Authenticate the Windows user

You must decide whether the connecting automation user is a domain or a local user and an administrator user account or not.

There are four main questions:

1. Which user to use to connect.
2. If, or where, credential delegation is required.
3. Is using SSH acceptable given the support-related limitations?
4. When using WinRM, is a central certificate management already established and used in the organization?

**Domain or Local User**

Ensure reliable automation access by configuring appropriate local or domain users. Prevent connection failures by verifying domain user accessibility, and streamline cross-domain management by using a consistent user account.

**Administrator or Less Privileged User**

To establish initial connectivity and validate critical playbooks, configure your setup using an administrator account if permitted by your security policies. Since features like default NTLM access are strictly restricted to the true Administrator user, first verifying your automation with full privileges ensures reliable baseline functionality before you transition to a less privileged account.

