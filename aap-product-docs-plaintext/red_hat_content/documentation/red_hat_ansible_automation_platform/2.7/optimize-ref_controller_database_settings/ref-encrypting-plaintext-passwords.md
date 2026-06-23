# Tune the PostgreSQL database for optimal performance
## Encrypt plain text passwords in automation controller configuration files

Plain text passwords in automation controller configuration files pose a potential security risk.

Configuration files are kept in the /etc/tower/conf.d/ folder. Files used to reach the database, for example, save passwords without encryption. This means that anyone who can read this folder can see the passwords clearly.

While permissions protect these folders, some security reports say this protection is good inadequate. The fix is to encrypt each of these passwords separately.

