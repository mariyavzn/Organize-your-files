def decrypt__text(plaintext, shift):
    decrypted_text = ""

    for char in plaintext:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    
    return decrypted_text

plaintext = "Khoor zruog"
shift = 3
decrypted_text = decrypt__text(plaintext, shift)
print("Decrypted text:", decrypted_text)