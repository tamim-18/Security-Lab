import streamlit as st

def caesar_encrypt(plaintext, shift):
    encrypted_text = "" 
    explanation = []
    for char in plaintext: 
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a') 
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            explanation.append([char, encrypted_char])
            encrypted_text += encrypted_char
        else:
            explanation.append([char, char])
            encrypted_text += char
    return encrypted_text, explanation

def caesar_decrypt(ciphertext, shift):
    decrypted_text = "" 
    explanation = []
    for char in ciphertext: 
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a') 
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset) 
            explanation.append([char, decrypted_char])
            decrypted_text += decrypted_char
        else:
            explanation.append([char, char])
            decrypted_text += char
    return decrypted_text, explanation

def main():
    st.title("Caesar Cipher")

    option = st.radio("Choose operation:", ["Encryption", "Decryption"])
    text = st.text_area("Enter text:")

    if option == "Encryption":
        shift = st.slider("Select shift value:", 0, 25)
        if st.button("Encrypt"):
            encrypted_text, explanation = caesar_encrypt(text, shift)
            st.success(f"Encrypted text: {encrypted_text}")
            st.header("Encryption Simulation")
            st.table([["Original", "Encrypted"]] + explanation)
    elif option == "Decryption":
        shift = st.slider("Select shift value:", 0, 25)
        if st.button("Decrypt"):
            decrypted_text, explanation = caesar_decrypt(text, shift)
            st.success(f"Decrypted text: {decrypted_text}")
            st.header("Decryption Simulation")
            st.table([["Original", "Decrypted"]] + explanation)

if __name__ == "__main__":
    main()
