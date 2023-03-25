import os
import json
from cryptography.fernet import Fernet


def encrypt(text, key):
    """
    This function encrypts a string using AES encryption.
    """
    f = Fernet(key)
    encoded_text = text.encode()
    encrypted_text = f.encrypt(encoded_text)
    return encrypted_text


def decrypt(ciphertext, key):
    """
    This function decrypts an AES encrypted string.
    """
    f = Fernet(key)
    decrypted_text = f.decrypt(ciphertext)
    return decrypted_text.decode()


def save_data(data):
    """
    This function saves data to a JSON file.
    """
    with open("data2.json", "w") as f:
        json.dump(data, f)


def load_data():
    """
    This function loads data from a JSON file.
    """
    if os.path.exists("data.json"):
        with open("data.json", "r") as f:
            data = json.load(f)
    else:
        data = {}
    return data


# Load existing data from file
data = load_data()

# Example usage
while True:
    print('Welcome to the StringEncryptor 3000!')
    mode = input("Would you like to encrypt or decrypt a string today (type 'e' or 'd', or 'q' to quit)? ")
    if mode == "q":
        print('Awwww sorry to see you go, cya next time!')
        break

    if mode == "e":
        plaintext = input("Enter a string to encrypt: ")
        key = Fernet.generate_key()
        ciphertext = encrypt(plaintext, key)
        print("Encrypted string:", ciphertext)
        print("Encryption key:", key.decode())
        # Store encrypted string and key in data
        data[ciphertext.decode()] = key.decode()
        save_data(data)

    elif mode == "d":
        decrypt_input = input("Enter the encrypted string to decrypt: ")
        # Check if encrypted string is already stored
        if decrypt_input in data:
            key = data[decrypt_input].encode()
            decrypted_text = decrypt(decrypt_input.encode(), key)
            print("Decrypted string:", decrypted_text)
        else:
            key = input("Enter the encryption key to decrypt: ")
            decrypted_text = decrypt(decrypt_input.encode(), key.encode())
            print("Decrypted string:", decrypted_text)
            # Store decrypted plaintext string and key in data
            data[decrypt_input] = key
            save_data(data)

