#!/usr/bin/env python

import argparse
import os
from random import choice, randint
from string import ascii_letters, digits, punctuation

def generate(n):
    """
    Return a tuple contains the generated password and it length
    """

    alphanumpunc = ascii_letters + digits + punctuation

    passwd = ''.join([choice(alphanumpunc) for i in range(n)])
    passwd_len = len(passwd)

    return passwd, passwd_len

def main():
    parser = argparse.ArgumentParser(
        prog="pynerate.py",
        description="Lite tools to generate alphanumeric+punctuation password.",
        allow_abbrev=False
    )

    parser.add_argument("-n", "--length",
                        type=int,
                        help="set password length. Default is 8")

    parser.add_argument("-v", "--verbose",
                        action="store_true",
                        help="print output verbosely")

    args = parser.parse_args()

    if args.length:
        passwd, passwd_len = generate(args.length)
    else:
        passwd, passwd_len = generate(8)

    if args.verbose:
        print("Password\t: {}\nLength\t\t: {}".format(passwd, passwd_len))
    else:
        print(passwd)

if __name__ == "__main__":
    main()
