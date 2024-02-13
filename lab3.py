import streamlit as st
import string

def vigenere_encrypt(plaintext, key):
    explanation = []
    ciphertext = ""
    index = 0
    keyLength = len(key)

    for char in plaintext.upper():
        if char not in string.ascii_uppercase:
            ciphertext += char
            explanation.append((char, "-", char))
            continue

        k_i = ord(key[index % keyLength]) - ord('A')
        p_i = ord(char) - ord('A')
        encrypted_char = chr((p_i + k_i) % 26 + ord('A'))
        ciphertext += encrypted_char
        explanation.append((char, key[index % keyLength], encrypted_char))

        index += 1

    return ciphertext, explanation

def vigenere_decrypt(ciphertext, key):
    explanation = []
    plaintext = ""
    index = 0
    keyLength = len(key)

    for char in ciphertext.upper():
        if char not in string.ascii_uppercase:
            plaintext += char
            explanation.append((char, "-", char))
            continue

        p_i = ord(key[index % keyLength]) - ord('A')
        k_i = ord(char) - ord('A')
        decrypted_char = chr((k_i - p_i) % 26 + ord('A'))
        plaintext += decrypted_char
        explanation.append((char, key[index % keyLength], decrypted_char))

        index += 1

    return plaintext, explanation

def main():
    st.title("Vigenère Cipher")

    choice = st.radio("Choose operation:", ["Encrypt", "Decrypt"])

    if choice == "Encrypt":
        plaintext = st.text_input("Enter plaintext:")
        key = st.text_input("Enter key:")
        if st.button("Encrypt"):
            ciphertext, explanation = vigenere_encrypt(plaintext, key)
            st.success(f"Encrypted ciphertext: {ciphertext}")
            st.write("Encryption Steps:")
            st.table(explanation)
    elif choice == "Decrypt":
        ciphertext = st.text_input("Enter ciphertext:")
        key = st.text_input("Enter key:")
        if st.button("Decrypt"):
            plaintext, explanation = vigenere_decrypt(ciphertext, key)
            st.success(f"Decrypted plaintext: {plaintext}")
            st.write("Decryption Steps:")
            st.table(explanation)

if __name__ == "__main__":
    main()  


