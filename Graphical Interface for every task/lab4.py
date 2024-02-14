import streamlit as st
import numpy as np
import math

st.title("Hill Cipher Encryption/Decryption")

# Function to remove spaces from a sentence
def remove_spaces(sentence):
    return sentence.replace(" ", "")

# Function to calculate the modular inverse of a number
def mod_inv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Function to calculate the modular inverse of a matrix
def modular_inverse(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = mod_inv(det, modulus)
    if det_inv is None:
        raise ValueError("Modular inverse does not exist.")
    matrix_modulus_inv = (det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus)
    return matrix_modulus_inv

# Function to generate a key matrix from the given key string
def generate_key_matrix(key):
    keylen = len(key)
    n = math.ceil(math.sqrt(keylen))
    key_matrix = np.array([], dtype=int)
    for i in range(n, keylen + n, n):
        temp = np.array([])
        string = key[(i - n):i]
        for x in string:
            temp = np.append(temp, (ord(x) - ord('A')))
        if len(key_matrix):
            key_matrix = np.vstack([key_matrix, temp])
        else:
            key_matrix = temp
    return key_matrix

# Function to generate a text matrix from the given text
def generate_text_matrix(text):
    tlen = len(text)
    text_matrix = np.array([], dtype=int)
    for i in range(tlen):
        text_matrix = np.append(text_matrix, (ord(text[i]) - ord('A')))
    text_matrix = np.resize(text_matrix, (tlen, 1))
    return text_matrix

# Function to encrypt text using the Hill Cipher
def hill_encryption(text, key):
    text_matrix = generate_text_matrix(text)
    key_matrix = generate_key_matrix(key)
    enc = np.dot(key_matrix, text_matrix) % 26
    non_space_chars = sum(1 for char in text if char != ' ')
    enc = np.resize(enc, (1, non_space_chars))
    ec_text = ''
    space_positions = []
    for i, char in enumerate(text):
        if char == ' ':
            space_positions.append(i)
    for i in enc[0]:
        ec_text += chr(ord('A') + int(i))
    return ec_text

# Function to decrypt text using the Hill Cipher
def hill_decryption(text, key):
    keylen = len(key)
    tlen = len(text)
    n = math.ceil(math.sqrt(keylen))
    text_matrix = generate_text_matrix(text)
    key_matrix = generate_key_matrix(key)
    key_matrix_inv = modular_inverse(key_matrix, 26)
    dec = np.dot(key_matrix_inv, text_matrix) % 26
    non_space_chars = sum(1 for char in text if char != ' ')
    dec = np.resize(dec, (1, non_space_chars))
    dec_text = ''
    for i in dec[0]:
        dec_text += chr(ord('A') + int(i))
    return dec_text

# Streamlit UI
option = st.radio("Choose operation:", ("Encryption", "Decryption"))

if option == "Encryption":
    plaintext = st.text_input("Enter plaintext:", "").upper()
    key = st.text_input("Enter key:", "").upper()
    if st.button("Encrypt"):
        ciphertext = hill_encryption(plaintext, key)
        st.success(f"Encrypted ciphertext: {ciphertext}")

elif option == "Decryption":
    ciphertext = st.text_input("Enter ciphertext:", "").upper()
    key = st.text_input("Enter key:", "").upper()
    if st.button("Decrypt"):
        plaintext = hill_decryption(ciphertext, key)
        st.success(f"Decrypted plaintext: {plaintext}")
