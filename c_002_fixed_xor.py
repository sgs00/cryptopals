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


def string_xor(op1, op2):
    """
    >>> assert(string_xor('00', '0102'))
    Traceback (most recent call last):
    ValueError: Operands' lenghts do not match

    >>> a = "1c0111001f010100061a024b53535009181c"
    >>> b = "686974207468652062756c6c277320657965"
    >>> result = "746865206b696420646f6e277420706c6179"

    >>> assert(string_xor(a, b) == result)
    
    # easter egg
    >>> import binascii
    >>> assert(binascii.a2b_hex(b) == b"hit the bull's eye")
    >>> assert(binascii.a2b_hex(result) == b"the kid don't play")    
    """

    if len(op1) != len(op2):
        raise ValueError("Operand's lenghts do not match")

    return format(int(op1, base=16) ^ int(op2, base=16), 'x')


if __name__ == '__main__':
    import doctest
    doctest.testmod()
