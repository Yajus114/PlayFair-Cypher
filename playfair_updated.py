import numpy as np
import random as randy

"""
Same column => right shift each letter
Same row => down shift each letter
Neither => Opposite corner letters based on a box around them
"""
ALPHAS = 'abcdefghijklmnopqrstuvwxyz'


def matrix_gen(key: str) -> ([[]], int, int):
    global ALPHAS
    """
    :param key: str
    :return key_matrix: 5x5 numpy.ndarray, lowercase, without space, non-repeating letters of the key + rest of the
                        alphabets with i and j combined (on the first occurrence of either i or j)
    """
    # Generate key string; no spaces, lowercase, + remaining alphabets in order, no repeating letters
    key = ''.join(dict.fromkeys(key.replace(' ', '').lower() + ALPHAS))
    i, j = key.find('i'), key.find('j')
    key_matrix = [_ for _ in key]
    key_matrix.pop(max(i, j))
    ij = min(i, j)
    key_matrix[ij] = 'ij'
    return np.array(key_matrix).reshape(5, 5), ij // 5, ij % 5


def encrypt(text: str, key: str) -> str:
    """
    :param text: the plaintext
    :param key: the custom key
    :return cipher_text: encrypted text with same spaces, punctuations and capitalisation
    """
    global ALPHAS
    key_matrix, quot, rem = matrix_gen(key)  # Generate key matrix
    cipher_text = ''
    text = text.replace(' ', '').lower()
    len_text = len(text)
    if len_text % 2 != 0:  # Pad plain text with a random letter if len(plain text) is not even
        text += ALPHAS[randy.randint(0, 25)]
    div_text = [text[i:i + 2] for i in range(0, len_text, 2)]  # Dividing plain text in groups of two
    for chars in div_text:
        if 'i' not in chars and 'j' not in chars:
            one, two = np.argwhere(key_matrix == chars[0])[0], np.argwhere(key_matrix == chars[1])[0]  # Find coords of each char in the key matrix
            comparison = one == two
            if comparison.all():  # letter pair
                cipher_text += chars + ' '
            elif one[0] == two[0]:  # when the chars are in the same row
                cipher_text += key_matrix[(one[0] + 1) % 5][one[1]] + key_matrix[(two[0] + 1) % 5][two[1]] + ' '
            elif one[1] == two[1]:  # when the chars are in the same column
                cipher_text += key_matrix[one[0]][(one[1] + 1) % 5] + key_matrix[two[0]][(two[1] + 1) % 5] + ' '
            else:  # when the chars are opposite
                cipher_text += key_matrix[two[0]][one[1]] + key_matrix[one[0]][two[1]] + ' '  # row of the other and col their own
        elif chars == 'ij':
            cipher_text += 'ij' + ' '
        elif chars == 'ji':
            cipher_text += 'ji' + ' '
        elif chars == 'jj' or chars == 'ii':
            cipher_text += chars + ' '
        else:
            try:  # see which of the two is i or j and set its coords manually, while finding the coords of the other
                one, two = np.argwhere(key_matrix == chars[0])[0], [quot, rem]
            except IndexError:
                one, two = [quot, rem], np.argwhere(key_matrix == chars[1])[0]
            if one[0] == two[0]:  # when the chars are in the same row
                cipher_text += key_matrix[(one[0] + 1) % 5][one[1]] + key_matrix[(two[0] + 1) % 5][two[1]] + ' '
            elif one[1] == two[1]:  # when the chars are in the same column
                cipher_text += key_matrix[one[0]][(one[1] + 1) % 5] + key_matrix[two[0]][(two[1] + 1) % 5] + ' '
            else:  # when the chars are opposite
                cipher_text += key_matrix[two[0]][one[1]] + key_matrix[one[0]][two[1]] + ' '  # row of the other and col their own

    return cipher_text


def decrypt(text, key):
    plain_text = ''
    key_matrix = matrix_gen(key)
    return plain_text


if __name__ == '__main__':
    print(f"The output is: {encrypt('Yajus Gakhar is the best programmer in the world', 'greatness')}")
