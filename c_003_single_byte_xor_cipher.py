# encoding: utf-8

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
import os


# This dictionary is obtained running the function `get_frequencies` below
frequencies = {
    'B': 0.016047959168228293, 'D': 0.03871183735737418, 'T': 0.08938126949659495, 'X': 0.0019135048594134572,
    'F': 0.021815103969122528, 'M': 0.025263217360184446, 'Y': 0.017213606152473405, 'J': 0.002197788956104563,
    'U': 0.026815809362304373, 'H': 0.04955707280570641, 'C': 0.03164435380900101, 'K': 0.008086975227142329,
    'N': 0.07172184876283856, 'Q': 0.0010402453014323196, 'I': 0.0732511860723129, 'S': 0.06728203117491646,
    'W': 0.018253618950416498, 'G': 0.020863354250923158, 'P': 0.020661660788966266, 'E': 0.1209652247516903,
    'R': 0.0633271013284023, 'Z': 0.001137563214703838, 'A': 0.08551690673195275, 'L': 0.04206464329306453,
    'V': 0.01059346274662571, 'O': 0.07467265410810447, }


def get_frequencies():
    # http://practicalcryptography.com/cryptanalysis/letter-frequencies-various-languages/english-letter-frequencies/
    # http://practicalcryptography.com/media/cryptanalysis/files/english_monograms.txt
    here = os.path.realpath(os.path.dirname(__file__))

    d = dict()
    with open(os.path.join(here, 'c_003_english_monograms.txt')) as f:
        for line in f.readlines():
            k, v = line.split()
            d[k] = int(v)

    s = sum(d.values())
    e = {k: v/s for k, v in d.items()}

    assert abs(1 - sum(e.values())) < 0.0001
    return e


def score_plain_english(text):
    """
    Score is a tuple: (number_of_non_AZ_characters, chi_square)
    Lower is better.

    White space' s frequency  is not given, but being a very common (and valid) character, I'm not
     considering it when incrementing non_AZ_characters

    Further interesting reading:
    # https://crypto.stackexchange.com/questions/30209/developing-algorithm-for-detecting-plain-text-via-frequency-analysis
    # http://norvig.com/mayzner.html
    """

    text = text.upper()
    counter = Counter(text)

    chi_sq = skipped = 0
    for t in text:
        try:
            observed = counter[t]
            expected = frequencies[t] * len(text)
            chi_sq += (observed-expected)**2 / expected
        except KeyError:
            if t != ' ':
                skipped += 1

    return skipped, chi_sq


def brute_force(encrypted):

    assert len(encrypted) % 2 == 0
    n_bytes = int(len(encrypted) / 2)

    last_ascii = ord('ÿ')
    assert last_ascii == 255

    for i in range(last_ascii+1):
        maybe_key = bytes([i] * n_bytes)
        maybe_decrypted = [a ^ b for a, b in zip(maybe_key, binascii.a2b_hex(encrypted))]
        maybe_decrypted = bytes(maybe_decrypted)
        try:
            maybe_decrypted = maybe_decrypted.decode('ascii')
        except UnicodeDecodeError:
            # skipping, contains unprintable chars
            continue

        yield maybe_key, maybe_decrypted


def run():
    encrypted = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

    results = dict()
    for maybe_key, maybe_decripted in brute_force(encrypted):
        results[maybe_decripted] = score_plain_english(maybe_decripted)

    for k, v in sorted(results.items(), key=lambda x: x[1]):
        print(k)
        print('score: ' + str(v))
        print()


if __name__ == '__main__':
    run()

