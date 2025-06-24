def shift_letter(letter, shift):
    if letter == " ":
        return " "
    elif letter.isupper():
        return chr(((ord(letter) - ord('A') + shift) % 26) + ord('A'))
    elif letter.islower():
        return chr(((ord(letter) - ord('a') + shift) % 26) + ord('a'))
    else:
        return letter

def caesar_cipher(message, shift):
    result = ""
    for char in message:
        result += shift_letter(char, shift)
    return result

def shift_by_letter(letter, letter_shift):
    if letter == " ":
        return " "
    shift_value = ord(letter_shift) - ord('A')
    return shift_letter(letter, shift_value)

def vigenere_cipher(message, key):
    result = ""
    key_extended = ""
    key_index = 0

    for char in message:
        if char == " ":
            key_extended += " "
        else:
            key_extended += key[key_index % len(key)]
            key_index += 1

    for i in range(len(message)):
        if message[i] == " ":
            result += " "
        else:
            shift = ord(key_extended[i]) - ord('A')
            result += shift_letter(message[i], shift)

    return result

def scytale_cipher(message, shift):
    while len(message) % shift != 0:
        message += "_"

    columns = len(message) // shift
    result = ""
    for i in range(len(message)):
        row = i // shift
        col = i % shift
        index = row + columns * col
        result += message[index]

    return result

def scytale_decipher(message, shift):
    columns = len(message) // shift
    result = [""] * len(message)
    
    for i in range(len(message)):
        row = i // columns
        col = i % columns
        index = row + col * shift
        result[index] = message[i]

    return ''.join(result)
