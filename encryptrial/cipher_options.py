from encryption_decryption import monoalphabetic_encrypt, monoalphabetic_decrypt, polyalphabetic_encrypt, vigenere_decrypt

def monoalphabetic_option():
    action = input("Choose action (1. Encrypt, 2. Decrypt): ")
    if action == '1':
        plaintext = input("Enter text to encrypt: ")
        encrypted_text = monoalphabetic_encrypt(plaintext)
        print(f"Encrypted text: {encrypted_text}")
    elif action == '2':
        ciphertext = input("Enter text to decrypt: ")
        decrypted_text = monoalphabetic_decrypt(ciphertext)
        print(f"Decrypted text: {decrypted_text}")
    else:
        print("Invalid action. Please choose 1 or 2.")

def polyalphabetic_option():
    action = input("Choose action (1. Encrypt, 2. Decrypt): ")
    if action == '1':
        plaintext = input("Enter text to encrypt: ")
        keyword = input("Enter a keyword: ")
        encrypted_text = polyalphabetic_encrypt(plaintext, keyword)
        print(f"Encrypted text: {encrypted_text}")
    elif action == '2':
        ciphertext = input("Enter text to decrypt: ")
        keyword = input("Enter the keyword: ")
        decrypted_text = vigenere_decrypt(ciphertext, keyword)
        print(f"Decrypted text: {decrypted_text}")
    else:
        print("Invalid action. Please choose 1 or 2.")