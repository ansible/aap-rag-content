# Tune the PostgreSQL database for optimal performance
## Encrypt the PostgreSQL password

Learn how to encrypt the PostgreSQL password used by automation controller for database connections.

### About this task

Perform the following steps on each node in the cluster:

### Procedure

1.  Edit `/etc/tower/conf.d/postgres.py` using:


```
$ vim /etc/tower/conf.d/postgres.py
```

2.  Add the following line to the top of the file.

```
from awx.main.utils import decrypt_value, get_encryption_key
```

3.  Remove the password value listed after 'PASSWORD': and replace it with the following line, replacing the supplied value of `$encrytpted..` with your own hash value:


```
decrypt_value(get_encryption_key('value'),'$encrypted$AESCBC$Z0FBQUFBQmNONU9BbGQ1VjJyNDJRVTRKaFRIR09Ib2U5TGdaYVRfcXFXRjlmdmpZNjdoZVpEZ21QRWViMmNDOGJaM0dPeHN2b194NUxvQ1M5X3dSc1gxQ29TdDBKRkljWHc9PQ=='),
```
Note:
The hash value in this step is the output value of `postgres_secret`.

4.  The full `postgres.py` resembles the following:


```
# Ansible Automation platform controller database settings. from awx.main.utils import decrypt_value, get_encryption_key DATABASES = { 'default': { 'ATOMIC_REQUESTS': True, 'ENGINE': 'django.db.backends.postgresql', 'NAME': 'awx', 'USER': 'awx', 'PASSWORD': decrypt_value(get_encryption_key('value'),'$encrypted$AESCBC$Z0FBQUFBQmNONU9BbGQ1VjJyNDJRVTRKaFRIR09Ib2U5TGdaYVRfcXFXRjlmdmpZNjdoZVpEZ21QRWViMmNDOGJaM0dPeHN2b194NUxvQ1M5X3dSc1gxQ29TdDBKRkljWHc9PQ=='), 'HOST': '127.0.0.1', 'PORT': 5432, } }+
```
