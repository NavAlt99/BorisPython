# Define an encrypt_message function that accepts a string.
# The input string will consist of only alphabetic characters.
# The function should return a string where all characters have been moved
# "up" two spots in the alphabet. For example, "a" will become "c".
#
# EXAMPLES
# encrypt_message("abc") => "cde"
# encrypt_message("xyz") => "zab"
# encrypt_message("")    => ""


def encrypt_message(stringx):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted = ""

    for letter in stringx:
        encrypted_letter_index = (alphabet.index(letter) + 1) % 26
        encrypted += alphabet[encrypted_letter_index]

    return encrypted

print(encrypt_message("xyz"))