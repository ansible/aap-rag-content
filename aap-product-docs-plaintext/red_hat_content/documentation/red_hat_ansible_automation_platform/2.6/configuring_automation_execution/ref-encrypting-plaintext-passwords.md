# 3. Performance tuning for automation controller
## 3.6. PostgreSQL database configuration and maintenance for automation controller
### 3.6.1. Encrypting plain text passwords in automation controller configuration files




Plain text passwords in automation controller configuration files pose a potential security risk.

Configuration files are kept in the /etc/tower/conf.d/ folder. Files used to reach the database, for example, save passwords without encryption. This means that anyone who can read this folder can see the passwords clearly.

While permissions protect these folders, some security reports say this protection is good inadequate. The fix is to encrypt each of these passwords separately.

#### 3.6.1.1. Creating PostgreSQL password hashes




Learn how to supply the hash values that replace the plain text passwords within the automation controller configuration files.

**Procedure**

1. On your automation controller node, run the following:


```
# awx-manage shell_plus
```


1. Then run the following from the python prompt:


```
&gt;&gt;&gt; from awx.main.utils import encrypt_value, get_encryption_key \    &gt;&gt;&gt; postgres_secret = encrypt_value('$POSTGRES_PASS') \    &gt;&gt;&gt; print(postgres_secret)
```

Note
Replace the `    $POSTGRES_PASS` variable with the actual plain text password you want to encrypt.



The output should resemble the following:


```
$encrypted$UTF8$AESCBC$Z0FBQUFBQmtLdGNRWXFjZGtkV1ZBR3hkNGVVbFFIU3hhY21UT081eXFkR09aUWZLcG9TSmpndmZYQXFyRHVFQ3ZYSE15OUFuM1RHZHBqTFU3S0MyNEo2Y2JWUURSYktsdmc9PQ==
```


1. Copy the full values of these hashes and save them.


- The hash value begins with `        $encrypted$` , and is not just the string of characters, as shown in the following example:


```
$encrypted$AESCBC$Z0FBQUFBQmNONU9BbGQ1VjJyNDJRVTRKaFRIR09Ib2U5TGdaYVRfcXFXRjlmdmpZNjdoZVpEZ21QRWViMmNDOGJaM0dPeHN2b194NUxvQ1M5X3dSc1gxQ29TdDBKRkljWHc9PQ==
```

Note that the `        $*_PASS` values are already in plain text in your inventory file.





#### 3.6.1.2. Encrypting the Postgres password




Learn how to encrypt the PostgreSQL password used by automation controller for database connections.

Perform the following steps on each node in the cluster:

**Procedure**

1. Edit `    /etc/tower/conf.d/postgres.py` using:


```
$ vim /etc/tower/conf.d/postgres.py
```


1. Add the following line to the top of the file.


```
from awx.main.utils import decrypt_value, get_encryption_key
```


1. Remove the password value listed after 'PASSWORD': and replace it with the following line, replacing the supplied value of `    $encrytpted..` with your own hash value:


```
decrypt_value(get_encryption_key('value'),'$encrypted$AESCBC$Z0FBQUFBQmNONU9BbGQ1VjJyNDJRVTRKaFRIR09Ib2U5TGdaYVRfcXFXRjlmdmpZNjdoZVpEZ21QRWViMmNDOGJaM0dPeHN2b194NUxvQ1M5X3dSc1gxQ29TdDBKRkljWHc9PQ=='),
```

Note
The hash value in this step is the output value of `    postgres_secret` .




1. The full `    postgres.py` resembles the following:


```
# Ansible Automation platform controller database settings. from awx.main.utils import decrypt_value, get_encryption_key DATABASES = { 'default': { 'ATOMIC_REQUESTS': True, 'ENGINE': 'django.db.backends.postgresql', 'NAME': 'awx', 'USER': 'awx', 'PASSWORD': decrypt_value(get_encryption_key('value'),'$encrypted$AESCBC$Z0FBQUFBQmNONU9BbGQ1VjJyNDJRVTRKaFRIR09Ib2U5TGdaYVRfcXFXRjlmdmpZNjdoZVpEZ21QRWViMmNDOGJaM0dPeHN2b194NUxvQ1M5X3dSc1gxQ29TdDBKRkljWHc9PQ=='), 'HOST': '127.0.0.1', 'PORT': 5432, } }+
```




