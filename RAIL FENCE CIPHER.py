def encrypt_rail_fence(text, rails):
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1

    for char in text:
        fence[rail].append(char)
        rail += direction

        if rail == rails - 1 or rail == 0:
            direction *= -1

    encrypted_text = ''.join([''.join(rail) for rail in fence])
    return encrypted_text

def decrypt_rail_fence(text, rails):
    fence = [['' for _ in range(len(text))] for _ in range(rails)]
    rail = 0
    direction = 1

    for i in range(len(text)):
        fence[rail][i] = '*'
        rail += direction

        if rail == rails - 1 or rail == 0:
            direction *= -1

    index = 0
    for i in range(rails):
        for j in range(len(text)):
            if fence[i][j] == '*' and index < len(text):
                fence[i][j] = text[index]
                index += 1

    rail = 0
    direction = 1
    decrypted_text = ''

    for i in range(len(text)):
        decrypted_text += fence[rail][i]
        rail += direction

        if rail == rails - 1 or rail == 0:
            direction *= -1

    return decrypted_text

plaintext = "Hello, Rail Fence Cipher!"
rails = 3

encrypted_text = encrypt_rail_fence(plaintext, rails)
print("Encrypted:", encrypted_text)

decrypted_text = decrypt_rail_fence(encrypted_text, rails)
print("Decrypted:", decrypted_text)
