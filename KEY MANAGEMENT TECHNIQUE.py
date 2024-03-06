#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
void generateKeyStream(int keyStream[], int length) {
    srand(time(0));
    for (int i = 0; i < length; i++) {
        keyStream[i] = rand() % 27; 
    }
}
void encrypt(char plaintext[], int keyStream[], char ciphertext[]) {
    int plaintextLen = strlen(plaintext);
    for (int i = 0; i < plaintextLen; i++) {
        if (plaintext[i] >= 'A' && plaintext[i] <= 'Z') {
            int shift = keyStream[i];
            ciphertext[i] = (plaintext[i] - 'A' + shift) % 26 + 'A';
        } else {
            ciphertext[i] = plaintext[i];
        }
    }
    ciphertext[plaintextLen] = '\0';
}
void decrypt(char ciphertext[], int keyStream[], char plaintext[]) {
    int ciphertextLen = strlen(ciphertext);
    for (int i = 0; i < ciphertextLen; i++) {
        if (ciphertext[i] >= 'A' && ciphertext[i] <= 'Z') {
            int shift = keyStream[i];
            plaintext[i] = (ciphertext[i] - 'A' - shift + 26) % 26 + 'A';
        } else {
            plaintext[i] = ciphertext[i];
        }
    }
    plaintext[ciphertextLen] = '\0';
}

int main() {
    char plaintext[100];
    char ciphertext[100];
    char decryptedText[100];
    int keyStream[100];
    int length;

    printf("Enter the plaintext: ");
    fgets(plaintext, sizeof(plaintext), stdin);
    plaintext[strcspn(plaintext, "\n")] = '\0';

    length = strlen(plaintext);

    generateKeyStream(keyStream, length);

    printf("\nKey Stream: ");
    for (int i = 0; i < length; i++) {
        printf("%d ", keyStream[i]);
    }

    encrypt(plaintext, keyStream, ciphertext);
    printf("\n\nCiphertext: %s", ciphertext);

    decrypt(ciphertext, keyStream, decryptedText);
    printf("\nDecrypted Text: %s", decryptedText);

    return 0;
}
