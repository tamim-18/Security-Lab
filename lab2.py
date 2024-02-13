import streamlit as st
from collections import Counter

def print_text_with_spaces(text, words_per_line):
    words = text.split()
    for i in range(0, len(words), words_per_line):
        st.write(" ".join(words[i:i+words_per_line]))

def decrypt(text, mapping):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            if char in mapping:
                decrypted_text += mapping[char]
            else:
                decrypted_text += "*"
        else:
            decrypted_text += char  # Preserve punctuation
    return decrypted_text

def analyze_frequency(ciphertext):
    # Remove spaces and punctuation
    ciphertext = ''.join(char for char in ciphertext if char.isalpha())
    # Count the frequency of each letter
    frequency = Counter(ciphertext)
    # Sort the letters by frequency
    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    return sorted_frequency

def substitution_cipher_gui(text, words_per_line):
    st.title("Substitution Cipher Decryption")

    st.write("Paste your ciphertext here:")
    ciphertext = st.text_area("Ciphertext")

    mapping = {}
    algo(text, mapping, words_per_line, ciphertext)

def algo(text, mapping, words_per_line, ciphertext):
    while True:
        st.write("Current mapping:")
        st.write(mapping)
        reverse_mapping = {}
        found_duplicate = False 
        for key, value in mapping.items():
          if value in reverse_mapping:
            st.write(f"{reverse_mapping[value]} maps to the same value as {key}: {value}")
            found_duplicate = True
            break
          else:
            reverse_mapping[value] = key 
        if found_duplicate:
          break          
        frequency_list = analyze_frequency(ciphertext)
        decrypted_text = decrypt(ciphertext, mapping)
        st.write("Decrypted text:")
        print_text_with_spaces(decrypted_text, words_per_line)
        
        st.write("Frequency list:")
        for char, freq in frequency_list:
            st.write(f"{char}: {freq}")
        
        replacement = st.text_input("Enter replacement (e.g., 'A':'E')")
        if replacement.lower() == 'q':
            break
        if len(replacement) != 5 or replacement[0] not in 'abcdefghijklmnopqrstuvwxyz' or replacement[1] != ":" or replacement[3] not in 'abcdefghijklmnopqrstuvwxyz':
            st.write("Invalid input. Please enter a valid replacement (e.g., 'A':'E').")
            continue
        if replacement[0] in mapping.values() or replacement[3] in mapping.values():
            st.write("Error: One of the replacement characters is already mapped to another character.")
            continue
        mapping[replacement[0]] = replacement[3]

        # Check if any character is mapped to the same replacement
        duplicate_mapping = [char for char, mapped_char in mapping.items() if mapped_char == replacement[3] and char != replacement[0]]
        if duplicate_mapping:
            st.write(f"Error: Character '{duplicate_mapping[0]}' is already mapped to '{replacement[3]}'.")
            del mapping[replacement[0]]  # Rollback the mapping

text = " gtd bsvgl vf fgedsugt dffml dkcymvsf gtmg gtd chjde ha \
aevdsxftvc tdycf bf gh id fgehsu aehz tmexftvcf. aevdsxf qms \
uvod bf gtd fgedsugt jd sddxjtds yvad udgf ghbut. vs \
mxxvgvhs, cdhcyd dkcedff bsvgl gtehbutyhod, amzvyl, aevdsxf, msx hgtdef ftmed \
fghevdf ha avsxvsu qhzzhsuehbsx jvgt fhzdhsd. gtded med zmsl idsdavgf \
ha fgmlvsu bsvgdx vsghbut gvzdf, mf vg tdycf gh amqd \
qtmyydsuvsu fvgbmgvhsf jvgtqhbemud. gtd vzchegmsqd ha fgmlvsu bsvgdx tmf fgebqp \
m qthex mzhsuzmsl cdhcyd gtehbuthbg tvfghel. pddcvsu zdzhevdf ha jtmg \
jd tmodmqqhzcyvftdx gtehbuthbg tvfghel qms tdyc bf fdd thj vsxvovxbmyf  \
msxqhzzbsvgvdf tmod cdefdodedx gtehbut ghbut gvzdf msx vsgh m ievutgdeabgbed. "

words_per_line = 10
substitution_cipher_gui(text, words_per_line)
