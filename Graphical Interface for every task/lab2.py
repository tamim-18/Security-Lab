import streamlit as st
from collections import Counter

# Function to remove spaces and punctuation from text
def clean_text(text):
    return ''.join(char for char in text if char.isalpha())

# Function to decrypt text using the given mapping
def decrypt_text(text, mapping):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            decrypted_text += mapping.get(char, "*")  # Use '*' if no mapping found
        else:
            decrypted_text += char  # Preserve punctuation
    return decrypted_text

# Function to analyze the frequency of characters in text
def analyze_frequency(text):
    cleaned_text = clean_text(text)
    frequency = Counter(cleaned_text)
    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    return sorted_frequency

# Streamlit app
def main():
    st.title("Interactive Decryption with Hill Cipher")

    # User input for ciphertext
    ciphertext = st.text_area("Enter ciphertext:", "")

    # Analyze frequency of characters in ciphertext
    frequency_list = analyze_frequency(ciphertext)
    st.subheader("Frequency Analysis")
    for char, freq in frequency_list:
        st.write(f"{char}: {freq}")

    st.subheader("Decrypted Text")

    # Show initial decrypted text based on placeholder mapping
    decrypted_text = decrypt_text(ciphertext, {})
    st.write(decrypted_text)

    # User input for trial and error decryption
    st.subheader("Trial and Error Decryption")
    st.write("Manually map each character to its decrypted counterpart.")

    # Interactive mapping
    mapping = {}
    sorted_frequency_chars = [char for char, _ in frequency_list]
    sorted_frequency_chars.sort()  # Sort characters alphabetically
    for char in sorted_frequency_chars:
        replacement = st.text_input(f"Replace '{char}' with:", mapping.get(char, ""))
        if replacement:
            mapping[char] = replacement.upper()

    # Show decrypted text with updated mapping
    decrypted_text = decrypt_text(ciphertext, mapping)
    st.success("Final Decrypted Text:")
    st.write(decrypted_text)

    # Show the current mapping
    st.subheader("Current Mapping:")
    for char, replacement in mapping.items():
        st.write(f"'{char}' -> '{replacement}'")

if __name__ == "__main__":
    main()
