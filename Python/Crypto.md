# Crypto Issues

    This stems from the dependency problems you must overcome to install Crypto (pycrypto)
    
    In my testing I had enabled some things in Visual Studio and modified some dependencies outlined in this link:
    https://www.programmersought.com/article/92901509220/
    
## Installation Commands (order does matter):

    pip3 uninstall pycryptodome
    pip3 uninstall pycrypto
    pip3 install pycrypto==2.6.1
    pip3 install pycryptodome==3.6.1
    
## You know the above will work for you if you see an error like:

    ImportError: cannot import name 'byte_string' from 'Crypto.Util.py3compat'