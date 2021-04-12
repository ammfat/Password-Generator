#!/usr/bin/env python

from random import choice, randint
from string import ascii_letters, digits, punctuation


def generate(n):
    alphanumpunc = ascii_letters + digits + punctuation

    return ''.join([choice(alphanumpunc) for i in range(n)])

def main():
    n = randint(8, 64)

    passwd = generate(n)
    print(passwd, len(passwd))

if __name__ == "__main__":
    main()
