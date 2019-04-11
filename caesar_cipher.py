##################################################
# Caesar cipher implementation in python:
#
# View the ASCII characters here: http://www.asciitable.com
# a-z = 97 - 122
# A-Z = 65 - 90
# By Doug Purcell
# http://www.purcellconsult.com
#
# Sample input: abcdefg
# Sample output: defghij
#
#
####################################################


def encrypt(input, key=3):
    """Encrypts the word file."""
    cipher, nums = '', 0
    size = len(input)
    i = 0
    while i < size:
        if input.isupper():
            cipher = cipher + chr((ord(input[i]) + key - 65) % 26 + 65)
        elif input.islower():
            cipher = cipher + chr((ord(input[i]) + key - 97) % 26 + 97)
        i += 1
    return cipher


def decrypt(input, key=3):
    """Decrypts the cipher text back to the plaintext."""
    cipher, nums = '', 0
    size = len(input)
    i = 0
    while i < size:
        if input.isupper():
            cipher = cipher + chr((ord(input[i]) - key - 65) % 26 + 65)
        elif input.islower():
            cipher = cipher + chr((ord(input[i]) - key - 97) % 26 + 97)
        i += 1
    return cipher



if __name__ == '__main__':
    print(encrypt('hello'))
    print(encrypt('hello world', key=5))
    print(encrypt('defend the east wall of the castle'))
    print(encrypt('defend the east wall of the castle', key=1))
    print(decrypt('khoor'))
