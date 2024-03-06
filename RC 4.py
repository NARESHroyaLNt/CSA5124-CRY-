def initialize_s_box(key):
    s_box = list(range(256))
    j = 0

    for i in range(256):
        j = (j + s_box[i] + key[i % len(key)]) % 256
        s_box[i], s_box[j] = s_box[j], s_box[i]

    return s_box

def rc4_encrypt(message, key):
    s_box = initialize_s_box(key)
    i = j = 0
    encrypted_message = bytearray()

    for char in message:
        i = (i + 1) % 256
        j = (j + s_box[i]) % 256
        s_box[i], s_box[j] = s_box[j], s_box[i]
        k = s_box[(s_box[i] + s_box[j]) % 256]
        encrypted_char = char ^ k
        encrypted_message.append(encrypted_char)

    return bytes(encrypted_message)

def rc4_decrypt(encrypted_message, key):
    return rc4_encrypt(encrypted_message, key)

def main():
    key = b"SecretKey"
    message = "Hello, RC4!"

    print("Original Message:", message)

    encrypted_message = rc4_encrypt(message.encode(), key)
    print("\nEncrypted Message:", encrypted_message.hex())

    decrypted_message = rc4_decrypt(encrypted_message, key)
    print("\nDecrypted Message:", decrypted_message.decode())

if _name_ == "_main_":
    main()
