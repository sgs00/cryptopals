"""
https://cryptopals.com/sets/1/challenges/2

Fixed XOR

Write a function that takes two equal-length buffers and produces their XOR combination.

If your function works properly, then when you feed it the string:
1c0111001f010100061a024b53535009181c

... after hex decoding, and when XOR'd against:
686974207468652062756c6c277320657965

... should produce:
746865206b696420646f6e277420706c6179

"""

import binascii
import sys


def test_string_xor():
    op1 = '1c0111001f010100061a024b53535009181c'
    # print(binascii.a2b_hex(op1))
    # b'\x1c\x01\x11\x00\x1f\x01\x01\x00\x06\x1a\x02KSSP\t\x18\x1c'

    op2 = '686974207468652062756c6c277320657965'
    # print(binascii.a2b_hex(op2))
    # b"hit the bull's eye"

    res = '746865206b696420646f6e277420706c6179'
    # print(binascii.a2b_hex(res))
    # b"the kid don't play"

    assert string_xor(op1, op2) == res


def string_xor(op1, op2):

    if len(op1) != len(op2):
        raise ValueError("Operands must have the same length.")

    op1 = binascii.a2b_hex(op1)
    op2 = binascii.a2b_hex(op2)

    bytes_xor = bytes(a ^ b for a, b in zip(op1, op2))

    return bytes_xor.hex()


if __name__ == '__main__':
    test_string_xor()
    print(string_xor(sys.argv[1], sys.argv[2]))
