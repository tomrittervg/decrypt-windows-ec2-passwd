#!/usr/bin/env python

import base64, binascii, getpass, optparse, sys
from Crypto.PublicKey import RSA


def pkcs1_unpad(text):
    #From http://kfalck.net/2011/03/07/decoding-pkcs1-padding-in-python
    if len(text) > 0 and text[0] == '\x02':
        # Find end of padding marked by nul
        pos = text.find('\x00')
        if pos > 0:
            return text[pos+1:]
    return None

def long_to_bytes (val, endianness='big'):
    # From http://stackoverflow.com/questions/8730927/convert-python-long-int-to-fixed-size-byte-array
    
    # one (1) hex digit per four (4) bits
    try:
        #Python < 2.7 doesn't have bit_length =(
        width = val.bit_length()
    except:
        width = len(val.__hex__()[2:-1]) * 4
    
    # unhexlify wants an even multiple of eight (8) bits, but we don't
    # want more digits than we need (hence the ternary-ish 'or')
    width += 8 - ((width % 8) or 8)
    
    # format width specifier: four (4) bits per hex digit
    fmt = '%%0%dx' % (width // 4)
    
    # prepend zero (0) to the width, to zero-pad the output
    s = binascii.unhexlify(fmt % val)
    
    if endianness == 'little':
        # see http://stackoverflow.com/a/931095/309233
        s = s[::-1]
    
    return s

def decryptPassword(rsaKey, password):
    #Undo the whatever-they-do to the ciphertext to get the integer
    encryptedData = base64.b64decode(password)
    ciphertext = int(binascii.hexlify(encryptedData), 16)

    #Decrypt it
    plaintext = rsaKey.decrypt(ciphertext)

    #This is the annoying part.  long -> byte array
    decryptedData = long_to_bytes(plaintext)
    #Now Unpad it
    unpaddedData = pkcs1_unpad(decryptedData)

    #Done
    return unpaddedData
    
if __name__ == "__main__":
    parser = optparse.OptionParser()
    parser.add_option("-k", "--key", dest="keyfile", default="~/.ssh/id_rsa", help="location of your ssh private key")
    parser.add_option("-p", "--password", dest="password", help="encrypted password")
    (options, args) = parser.parse_args()
    
    if not options.keyfile or not options.password:
        parser.print_help()
        sys.exit(-1)
    
    #Open your keyfile
    try:
        keyFile = open(options.keyfile)
    except:
        print "Could not find file", options.keyfile
        sys.exit(-1)
    #Read file
    keyLines = keyFile.readlines()
    #Import it
    try:
        key = RSA.importKey(keyLines, passphrase=getpass.getpass('Encrypted Key Password (leave blank if none): '))
    except ValueError, ex:
        print "Could not import SSH Key (Is it an RSA key? Is it password protected?): %s" % ex
        sys.exit(-1)
    #Decrypt it
    print ""
    print "Password:", decryptPassword(key, options.password)
