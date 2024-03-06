def vigenere_encrypt(plaintext, key):
    encrypted_text = ""
    key = key.upper()
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            if char.isupper():
                encrypted_text += chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
            else:
                encrypted_text += chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
            key_index += 1
        else:
            encrypted_text += char

    return encrypted_text


def vigenere_decrypt(ciphertext, key):
    decrypted_text = ""
    key = key.upper()
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            if char.isupper():
                decrypted_text += chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
            else:
                decrypted_text += chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
            key_index += 1
        else:
            decrypted_text += char

    return decrypted_text


plaintext = "meet me today"
key = "best"

encrypted_text = vigenere_encrypt(plaintext, key)
print("Encrypted text:", encrypted_text)

decrypted_text = vigenere_decrypt(encrypted_text, key)
print("Decrypted text:", decrypted_text)
