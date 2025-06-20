'''
Caesar cipher is an antique cryptographic method making some information hidden to whom doesn't have the key to decrypt it.

Think of the alphabet as an ordered list of letters:

Each letter has a position in this list. a is 1, b is 2, j is 10, etc...

Caesar cypher hide information by using a key which is a positive number to add to the position of the original letter, the result being the position of the encrypted letter.

a with key == 2 gives c

If the key brings you to the end of the alphabet, you continue to count from the begining, such as:

a with key == 28 gives c

To decypher, or decrypt, the message, you apply the same procedure moving backward on the alphabet.

You must provide the functions caesar_cypher_encrypt(s, key) and caesar_cypher_decrypt(s, key) where:

s is a string (letter, word, sentence, etc).
key is a positive integer, the key of the caesar cypher.
Your implementation should only transform uppercase and lowercase ASCII letters. Special characters, numbers and letters with accents should not be transformed.

Your function shall not print but return the encoded/decoded string.

https://genepy.org/exercises/caesar-cypher
'''

import string

alphabet_upper = list(string.ascii_uppercase)
alphabet_lower = list(string.ascii_lowercase)

def caesar_cypher_encrypt(s, key):
    encrypted = []
    for char in s:
        if char.isupper():
            position = (alphabet_upper.index(char) + key) % 26
            encrypted.append(alphabet_upper[position])
        else:
            if char in alphabet_lower:
                position = (alphabet_lower.index(char) + key) % 26
                encrypted.append(alphabet_lower[position])
            else:
                encrypted.append(char)
    return ''.join(encrypted)

def caesar_cypher_decrypt(s, key):
    decrypted = []
    for char in s:
        if char.isupper():
            position = (alphabet_upper.index(char) - key) % 26
            decrypted.append(alphabet_upper[position])
        else:
            if char in alphabet_lower:
                position = (alphabet_lower.index(char) - key) % 26
                decrypted.append(alphabet_lower[position])
            else:
                decrypted.append(char)
    return ''.join(decrypted)


'''
Clean version:

def shift_char(char, key):
    if char.isupper():
        position = (alphabet_upper.index(char) + key) % 26
        return alphabet_upper[position]
    else:
        if char in alphabet_lower:
            position = (alphabet_lower.index(char) + key) % 26
            return alphabet_lower[position]
        else:
            return char

def caesar_cypher_encrypt(s, key):
    decrypted = []
    for char in s:
        decrypted.append(shift_char(char,key))
    return ''.join(decrypted)

def caesar_cypher_decrypt2(s, key):
    decrypted = []
    for char in s:
        decrypted.append(shift_char(char, -key))
    return ''.join(decrypted)
'''