def generate_playfair_key(key):
    key_set = set(key)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  
    remaining_chars = [char for char in alphabet if char not in key_set]

    playfair_key = list(key) + remaining_chars
    playfair_matrix = [playfair_key[i:i+5] for i in range(0, 25, 5)]

    return playfair_matrix

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)

def encrypt_playfair(plaintext, key):
    plaintext = plaintext.upper().replace("J", "I").replace(" ", "")
    
    playfair_matrix = generate_playfair_key(key)

    digraphs = [plaintext[i:i+2] for i in range(0, len(plaintext), 2)]
    if len(digraphs[-1]) == 1:  
        digraphs[-1] += 'X'

    ciphertext = ""
    for digraph in digraphs:
        row1, col1 = find_position(playfair_matrix, digraph[0])
        row2, col2 = find_position(playfair_matrix, digraph[1])

        if row1 == row2:
            ciphertext += playfair_matrix[row1][(col1 + 1) % 5] + playfair_matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  
            ciphertext += playfair_matrix[(row1 + 1) % 5][col1] + playfair_matrix[(row2 + 1) % 5][col2]
        else:  
            ciphertext += playfair_matrix[row1][col2] + playfair_matrix[row2][col1]
    return ciphertext
key = "NETWORK"
plaintext = "MOSQUE"
ciphertext = encrypt_playfair(plaintext, key)
print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
PLAY FAIR CIPHER
