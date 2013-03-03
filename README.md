decrypt-windows-ec2-passwd
==========================

Amazon EC2 Windows Instances require you to paste in your SSH private key to decrypt the password to the instance. Although they do the decryption locally, in Javascript, I'd still prevent to do it locally... not trusting Amazon.

To Use:

 1. Select your Windows Instance
 2. Actions -> Get System Log
 3. Your full encrypted password will be there, copy it
 4. Run It

```
$ ./decrypt-windows-ec2-passwd.py -p "ercW1ff...9zEw==" -k ~/.ssh/ec2.pem
                                                                             
Password: bG7hKK1Kt;8
```
