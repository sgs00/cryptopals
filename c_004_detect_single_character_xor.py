# encoding: utf-8

"""
https://cryptopals.com/sets/1/challenges/4

Detect single-character XOR

One of the 60-character strings in this file has been encrypted by single-character XOR.
Find it.
(Your code from #3 should help.)

"""

import os

from c_003_single_byte_xor_cipher import score_plain_english, brute_force


def run():
    here = os.path.realpath(os.path.dirname(__file__))

    candidate_key = candidate_decrypted = score = None

    with open(os.path.join(here, 'c_004_4.txt')) as f:
        for line in f:
            line = line.strip()
            for maybe_key, maybe_decrypted in brute_force(line):
                _score = score_plain_english(maybe_decrypted)
                if not score or _score < score:
                    score = _score
                    candidate_key = maybe_key
                    candidate_decrypted = maybe_decrypted

    print(candidate_decrypted)
    print('Key was: ' + str(candidate_key))


if __name__ == '__main__':
    run()

