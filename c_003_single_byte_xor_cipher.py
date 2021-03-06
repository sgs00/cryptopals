"""
https://cryptopals.com/sets/1/challenges/3

Single-byte XOR cipher

The hex encoded string:
1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736

... has been XOR'd against a single character. Find the key, decrypt the message.

You can do this by hand. But don't: write code to do it for you.

How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric.
Evaluate each output and choose the one with the best score.

Achievement Unlocked
You now have our permission to make "ETAOIN SHRDLU" jokes on Twitter.
"""

import binascii
from collections import Counter

from c_002_fixed_xor import string_xor

# Credits:
# http://www.data-compression.com/english.html
# for the Statistical Distributions of English Text (space included)
# https://crypto.stackexchange.com/a/56477
# for allowing me to discover the Bhattacharyya coefficient
# further interesting reading: http://norvig.com/mayzner.html

frequencies = {
    'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442,
    'f': 0.0197881, 'g': 0.0158610, 'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033,
    'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513, 'o': 0.0596302,
    'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357,
    'u': 0.0225134, 'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984,
    'z': 0.0007836, ' ': 0.1918182, }


def brute_force(encrypted):
    """
    >>> encoded = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    >>> decoded = brute_force(encoded)[0]['decoded']
    >>> assert(decoded == "Cooking MC's like a pound of bacon")
    """

    length = int(len(encrypted) / 2)
    scores = list()

    for k in keys_generator(length):
        maybe_decrypted = string_xor(encrypted, k)
        scores.append({'key_hex': k[:2],
                       'score': englishness(maybe_decrypted),
                       'decoded': bytearray.fromhex(maybe_decrypted).decode()})

    return sorted(scores, key=lambda k: k['score'], reverse=True)


def keys_generator(length,
                   first_ascii=ord(' '), # decimal 32
                   last_ascii=ord('~')): # decimal 126
    for i in range(first_ascii, last_ascii+1):
        # hex(16) == '0x10'
        yield hex(i)[2:] * length


def englishness(hex_str):
    length = len(hex_str) / 2
    txt = bytearray.fromhex(hex_str).decode()
    cnt = Counter(txt)
    bhatta = 0
    for c, n_observed in cnt.items():
        p = n_observed / length
        q = frequencies.get(c, 0)
        bhatta += (p * q) ** 0.5
    return bhatta


if __name__ == '__main__':
    import doctest
    doctest.testmod()
