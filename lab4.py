import streamlit as st
import numpy as np

# Define function to generate key matrix from key string
def generate_key_matrix(key):
    key = key.replace(" ", "").upper()
    key_length = len(key)
    key_size = int(key_length ** 0.5)
    square_size = key_size * key_size
    
    if key_length < square_size:
        # Pad the key string with 'X' to make its length a perfect square
        key += 'X' * (square_size - key_length)
    elif key_length > square_size:
        # Truncate the key string to make its length a perfect square
        key = key[:square_size]
    
    key_matrix = np.array([ord(char) - ord('A') for char in key]).reshape((key_size, key_size))
    return key_matrix

# Define function to perform matrix multiplication
def matrix_multiply(matrix1, matrix2):
    return np.dot(matrix1, matrix2) % 26

# Define function to perform encryption using Hill Cipher
def encrypt(plaintext, key_matrix):
    plaintext = plaintext.replace(" ", "").upper()
    plaintext_size = len(plaintext)
    key_size = key_matrix.shape[0]

    # Pad plaintext if its length is not divisible by key size
    if plaintext_size % key_size != 0:
        padding_size = key_size - (plaintext_size % key_size)
        plaintext += 'X' * padding_size

    # Split plaintext into blocks
    plaintext_blocks = [plaintext[i:i + key_size] for i in range(0, len(plaintext), key_size)]

    # Perform encryption
    ciphertext = ''
    explanation = []
    for block in plaintext_blocks:
        block_vector = np.array([ord(char) - ord('A') for char in block]).reshape((-1, 1))
        encrypted_block = matrix_multiply(key_matrix, block_vector)
        ciphertext_block = ''.join([chr(char + ord('A')) for char in encrypted_block.flatten()])  # Add space after each word
        ciphertext += ciphertext_block + ' '
        explanation.append((block, np.squeeze(block_vector), np.squeeze(encrypted_block)))

    return ciphertext.strip(), explanation  # Remove trailing space

# Define function to perform decryption using Hill Cipher
def decrypt(ciphertext, key_matrix):
    key_matrix_inverse = np.linalg.inv(key_matrix)
    key_matrix_inverse = np.round(key_matrix_inverse * np.linalg.det(key_matrix)).astype(int) % 26
    return encrypt(ciphertext, key_matrix_inverse)

def main():
    st.title("Hill Cipher Encryption/Decryption")

    # Get key from user input
    key = st.text_input("Enter key:", "").upper()
    key_matrix = generate_key_matrix(key)

    operation = st.radio("Choose operation:", ("Encryption", "Decryption"))

    if operation == "Encryption":
        plaintext = st.text_input("Enter plaintext:", "").upper()
        if st.button("Encrypt"):
            ciphertext, explanation = encrypt(plaintext, key_matrix)
            st.success(f"Encrypted ciphertext: {ciphertext}")

            st.subheader("Encryption Steps:")
            for step in explanation:
                st.write(f"Plaintext Block: {step[0]}")
                st.write(f"Plaintext Vector: {step[1]}")
                st.write(f"Encrypted Vector: {step[2]}")
                st.write("---")

    elif operation == "Decryption":
        ciphertext = st.text_input("Enter ciphertext:", "").upper()
        if st.button("Decrypt"):
            plaintext, explanation = decrypt(ciphertext, key_matrix)
            st.success(f"Decrypted plaintext: {plaintext}")

            st.subheader("Decryption Steps:")
            for step in explanation:
                st.write(f"Ciphertext Block: {step[0]}")
                st.write(f"Ciphertext Vector: {step[1]}")
                st.write(f"Decrypted Vector: {step[2]}")
                st.write("---")

if __name__ == "__main__":
    main()
