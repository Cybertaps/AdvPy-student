#!/bin/usr/env python

import string
import base64
from Crypto.Cipher import AES

def main():
    a = ""
    with open("ex4_1_data.txt") as fin:
        a = fin.read().strip()
        # for i in xrange(len(string.ascii_lowercase)):
        # print("{}: {}".format(i, ceasarDecode(a, i)))
    afterRot6 = ceasarDecode(a, 6)

    ceasar_decrypteda = afterRot6[:158]
    ceasar_decryptedb = afterRot6[158:]
    # print ceasar_decrypteda
    # print ""
    # print ceasar_decryptedb


def ceasarEncode(data, shift):
    result = ""

    for letter in data:
        if letter.isupper():
            base_position = string.ascii_uppercase.find(letter)
            encoded_position = (base_position + shift) % 26
            result += string.ascii_uppercase[encoded_position]

        elif letter.islower():
            base_position = string.ascii_lowercase.find(letter)
            encoded_position = (base_position + shift) % 26
            result += string.ascii_lowercase[encoded_position]

        else:
            result += letter
    return result


def ceasarDecode(data, shift):
    return ceaserDecode(data, shift * -1)


def atbash_encode(data):
    result = ""

    for letter in data[::-1]:
        if letter.isupper():
            base_position = string.ascii_uppercase.find(letter)
            encoded_position = (base_position + shift) % 26
            result += string.ascii_uppercase[encoded_position]

        elif letter.islower():
            base_position = string.ascii_lowercase.find(letter)
            encoded_position = (base_position + shift) % 26
            result += string.ascii_lowercase[encoded_position]

        else:
            result += letter

    return result


# def atbashDecode (data, shift):
# return ceasarEncode (data, shift * -1)

if __name__ == "__main__":
    main()
