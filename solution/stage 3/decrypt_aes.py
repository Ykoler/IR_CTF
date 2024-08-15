from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

# Function to load the key from a file
def load_key(filename='key.txt'):
    with open(filename, 'rb') as key_file:
        return key_file.read()

# Function to decrypt a file
def decrypt_file(file_name, key, output_file):
    with open(file_name, 'rb') as file:
        encrypted_data = file.read()

    iv = encrypted_data[:16]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()

    try:
        decrypted_data = decryptor.update(encrypted_data[16:]) + decryptor.finalize()
        unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()
    except ValueError as e:
        print(f"Decryption error: {e}")
        return

    print(file_name, ":   ", unpadded_data)

# Main function
def main():
    # Decrypt all files in the current directory
    for filename in os.listdir('.'):
        if filename.endswith('.txt') and filename != 'success.txt':
            print(f"Decrypting {filename}")
            decrypt_file(filename, load_key(), f'dec_{filename}')

if __name__ == "__main__":
    main()
