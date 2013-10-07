decrypt-windows-ec2-passwd
==========================

Amazon EC2 Windows Instances require you to paste in your SSH private key to decrypt the password to the instance. Although they do the decryption locally, in Javascript, I'd still prefer to do it locally... not trusting Amazon.

To Use:

 1. Select your Windows Instance
 2. Actions -> Get System Log
 3. Your full encrypted password will be there, copy it
 4. Run It

```
$ ./decrypt-windows-ec2-passwd.py -p "ercW1ff...9zEw==" -k ~/.ssh/ec2.pem

Password: bG7hKK1Kt;8
```

Alternatively, if you have an encrypted private key, you'll need to use the Go version:

```
$ go run decrypt-windows-ec2-passwd.go ~/.ssh/ec2.pem "ercW1ff...9xEw=="
Encrypted private key. Please enter passphrase:
Decrypted password: bG7hKK1Kt;8
```

(Full credit to [agl](https://github.com/tomrittervg/decrypt-windows-ec2-passwd/pull/2) for the Go version)
