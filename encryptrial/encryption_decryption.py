def monoalphabetic_encrypt(plaintext):
    substitution_map = {
        'a': 'q', 'b': 'w', 'c': 'e', 'd': 'r', 'e': 't', 'f': 'y', 'g': 'u', 'h': 'i', 'i': 'o', 'j': 'p',
        'k': 'a', 'l': 's', 'm': 'd', 'n': 'f', 'o': 'g', 'p': 'h', 'q': 'j', 'r': 'k', 's': 'l', 't': 'z',
        'u': 'x', 'v': 'c', 'w': 'v', 'x': 'b', 'y': 'n', 'z': 'm'
    }
    encrypted_text = ""
    for char in plaintext.lower():
        if char in substitution_map:
            encrypted_text += substitution_map[char]
        else:
            encrypted_text += char
    return encrypted_text

def monoalphabetic_decrypt(ciphertext):
    substitution_map = {
        'q': 'a', 'w': 'b', 'e': 'c', 'r': 'd', 't': 'e', 'y': 'f', 'u': 'g', 'i': 'h', 'o': 'i', 'p': 'j',
        'a': 'k', 's': 'l', 'd': 'm', 'f': 'n', 'g': 'o', 'h': 'p', 'j': 'q', 'k': 'r', 'l': 's', 'z': 't',
        'x': 'u', 'c': 'v', 'v': 'w', 'b': 'x', 'n': 'y', 'm': 'z'
    }
    decrypted_text = ""
    for char in ciphertext.lower():
        if char in substitution_map:
            decrypted_text += substitution_map[char]
        else:
            decrypted_text += char
    return decrypted_text

def polyalphabetic_encrypt(plaintext, keyword):
    encrypted_text = ""
    keyword = keyword.lower()
    keyword_length = len(keyword)
    for i, char in enumerate(plaintext.lower()):
        if char.isalpha():
            shift = ord(keyword[i % keyword_length]) - ord('a')
            encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def vigenere_decrypt(ciphertext, keyword):
    decrypted_text = ""
    keyword = keyword.lower()
    keyword_length = len(keyword)
    for i, char in enumerate(ciphertext.lower()):
        if char.isalpha():
            shift = ord(keyword[i % keyword_length]) - ord('a')
            decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text