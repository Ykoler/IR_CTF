from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

# Function to generate a random AES key
def generate_key():
    return os.urandom(32)  # AES-256 key

# Function to save the key to a file
def save_key(key, filename='key.txt'):
    with open(filename, 'wb') as key_file:
        key_file.write(key)

# Function to encrypt a file
def encrypt_file(file_name, key, output_file):
    iv = os.urandom(16)  # Generate a random IV
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(algorithms.AES.block_size).padder()

    with open(file_name, 'rb') as file:
        data = file.read()
        padded_data = padder.update(data) + padder.finalize()

    encrypted_data = iv + encryptor.update(padded_data) + encryptor.finalize()

    with open(output_file, 'wb') as file:
        file.write(encrypted_data)

# Main function
def main():
    # Generate and save the key
    key = generate_key()
    save_key(key)
    
    # Encrypt the success.txt file
    encrypt_file('success.txt', key, 'successenc.txt')
    
if __name__ == "__main__":
    main()
