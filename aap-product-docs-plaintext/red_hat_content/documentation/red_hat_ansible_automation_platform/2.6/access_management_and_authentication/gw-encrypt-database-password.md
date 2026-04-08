# 6. Configuring Ansible Automation Platform
## 6.2. Platform gateway
### 6.2.4. Encrypting the platform gateway database password




System administrators can encrypt the database password used by platform gateway and apply it directly to the configuration file, resolving issues related to the `SECRET_KEY` loading order.

Note
Platform gateway uses the Django framework, which requires the `SECRET_KEY` to be fully loaded into memory before the decryption function ( `ansible_encryption.decrypt_string()` ) is called. If the decryption call runs before the key is loaded, the process fails, preventing platform gateway from accessing the database.



**Procedure**

1. Access the command line on the platform gateway node.
1. Use the `    aap-gateway-manage shell_plus` command to open an interactive Django shell:


```
aap-gateway-manage shell_plus
```


1. Inside the shell, run the following commands to import the encryption library, set your password, and generate the encrypted string:


```
&gt;&gt;&gt; from ansible_base.lib.utils.encryption import ansible_encryption    &gt;&gt;&gt; value = 'your-database-password' # REPLACE with your actual password    &gt;&gt;&gt; encrypted_value = ansible_encryption.encrypt_string(value)    &gt;&gt;&gt; print(encrypted_value)
```


1. Copy the entire output string starting with `    $encrypted$` . This is your encrypted password.
1. Exit the shell using `    quit()` .
1. Open the platform gateway configuration file for editing:


```
vi /etc/ansible-automation-platform/gateway/settings.py
```


1. Locate the section defining the `    DATABASES` variable. You must insert the code to load the `    SECRET_KEY` before the `    DATABASES` dictionary is defined.
1. Update the file to include the highlighted code, replacing only the placeholder text for the `    PASSWORD` key with your copied encrypted string:


```
from ansible_base.lib.utils.encryption import ansible_encryption    from django.conf import settings        # ... other configuration settings ...        # The GATEWAY_SECRET_KEY_FILE is typically defined earlier in settings.    # The SECRET_KEY must be loaded before the decryption function is called.    with open(GATEWAY_SECRET_KEY_FILE, 'rb') as f:        settings.SECRET_KEY = f.read().strip()        DATABASES = {        'default': {            'ENGINE': 'django.db.backends.postgresql',            'HOST': '10.0.108.77', # Example host, use your value            # ... other database settings ...            'PASSWORD':            ansible_encryption.decrypt_string('$encrypted$UTF8$AESCBC$Z0FBQUFBQnBBNU...            &lt;YOUR_ENCRYPTED_STRING&gt;...QWdPUHM9'),            # ... other database settings ...            'PORT': '5432', # Example port, use your value        }    }
```


1. Save and close the file.
1. Restart platform gateway to load the new encrypted configuration:


```
sudo systemctl restart aap-gateway
```




**Verification**

Confirm that platform gateway starts without errors and that you can access the platform UI, which indicates a successful database connection.


