from cipher_options import monoalphabetic_option, polyalphabetic_option

def display_menu():
    print("1. Monoalphabetic Cipher")
    print("2. Polyalphabetic Cipher (Vigenère)")
    print("3. Exit")

while True:
    display_menu()
    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        monoalphabetic_option()
    elif choice == '2':
        polyalphabetic_option()
    elif choice == '3':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")