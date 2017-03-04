#!/bin/sh
#
# Quick EC2 password decrypt by Craig Ringer, based on work by "hedgehog" on
# Stack Overflow (http://stackoverflow.com/a/4982867/398670). Only requires
# tools preinstalled on most Linux systems, supports encrypted private keys.
#
# See also:
# * http://serverfault.com/q/603984/102814

set -e -u

if [ $# -ne 2 ]; then
    echo "Usage: $0 /path/to/key [ \"base64 password text\" | /path/to/password/file | - ]"
    exit 1
fi

set -o pipefail

if [ -e "$2" -o "$2" = "-" ]; then
    # file exists, or user specified stdin
    cat "$2" | base64 --decode | openssl rsautl -decrypt -inkey "$1"
else
    # No such file and isn't stdin, assume it's base64
    echo "$2" | base64 --decode | openssl rsautl -decrypt -inkey "$1"
fi
echo
