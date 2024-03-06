#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define BLOCK_SIZE 8

void encrypt_CBC_3DES(const unsigned char *plaintext, int plaintext_len, const unsigned char *key, const unsigned char *iv, unsigned char *ciphertext) {
    int i, numBlocks;
    const unsigned char *currentBlock = plaintext;
    unsigned char *currentCiphertext = ciphertext;

    numBlocks = plaintext_len / BLOCK_SIZE;

    for (i = 0; i < numBlocks; i++) {
        currentBlock += BLOCK_SIZE;
        currentCiphertext += BLOCK_SIZE;
    }
}

int main() {
    const unsigned char *plaintext = (unsigned char *)"Hello, world!";
    const unsigned char *key = (unsigned char *)"0123456789ABCDEF";
    const unsigned char *iv = (unsigned char *)"ABCDEFGH";
    unsigned char ciphertext[BLOCK_SIZE * 2];

    encrypt_CBC_3DES(plaintext, strlen((char *)plaintext), key, iv, ciphertext);

    printf("Ciphertext: ");
    for (int i = 0; i < BLOCK_SIZE * 2; i++) {
        printf("%02X ", ciphertext[i]);
    }
    printf("\n");

    return 0;
}
