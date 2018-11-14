"""
https://cryptopals.com/sets/1/challenges/1

Convert hex to base64

The string:
49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d

Should produce:
SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

So go ahead and make that happen. You'll need to use this code for the rest of the exercises.

Cryptopals Rule
Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing.

"""

import binascii
import base64
import sys


def test_hex_to_base64():
    given_hex = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    given_b64 = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
    assert (hex_to_base64(given_hex) == given_b64)


def hex_to_base64(hex_):
    unhexlified_bytes = binascii.a2b_hex(hex_)

    # print(unhexlified_bytes.decode('ascii'))
    # I'm killing your brain like a poisonous mushroom

    b64_bytes = base64.b64encode(unhexlified_bytes)
    return b64_bytes.decode('ascii')


if __name__ == '__main__':
    test_hex_to_base64()
    print(hex_to_base64(sys.argv[1]))
