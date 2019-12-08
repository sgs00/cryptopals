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

import base64
import binascii


def hex_to_base64(hex_string):
    """
    >>> given_hex = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    >>> given_b64 = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

    >>> assert(hex_to_base64(given_hex) == given_b64)
    """

    _bytes = binascii.a2b_hex(hex_string)
    return str(base64.b64encode(_bytes))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
