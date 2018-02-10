decrypt-windows-ec2-passwd
==========================

Amazon EC2 Windows Instances require you to paste in your SSH private key to decrypt the password to the instance. Although they do the decryption locally, in Javascript, I'd still prefer to do it locally... not trusting Amazon.

To Use:

 1. Select your Windows Instance
 2. Actions (or left click) > Instance Settings >  Get System Log
 3. Your full encrypted password will be there, copy it
 4. Run It

```
$ ./decrypt-windows-ec2-passwd.py -p "ercW1ff...9zEw==" -k ~/.ssh/ec2.pem

Password: bG7hKK1Kt;8
```

Alternatively, you can use the Go version:

```
$ go run decrypt-windows-ec2-passwd.go ~/.ssh/ec2.pem "ercW1ff...9xEw=="
Encrypted private key. Please enter passphrase:
Decrypted password: bG7hKK1Kt;8
```

For the convenience of UNIX users there's a simple shell script that wraps
OpenSSL tools to decrypt the password. It supports encrypted private keys in
several formats including PEM, and can decode the base64 password text from a
file, supplied on the command line, or from stdin.

```
decrypt-windows-ec2-passwd.sh ~/.ssh/id_rsa "ercW1ff...9zEw=="
Enter pass phrase for .ssh/id_rsa:
bG7hKK1Kt;8
```

Credits:

* [agl](https://github.com/tomrittervg/decrypt-windows-ec2-passwd/pull/2) for the Go version
* [marcin](https://github.com/tomrittervg/decrypt-windows-ec2-passwd/pull/3) for making the Python version accept passphrases
* [ringerc](https://github.com/ringerc) for the shell script
* [petemounce](https://github.com/petemounce) for the ruby version
