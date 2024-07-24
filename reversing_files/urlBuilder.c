#include <stdio.h>
#include <string.h>

int flag = 0;
char cipherkey[256] = "abcdefghijklmnopqrstuvwxyz:,.'/;!`~";
static const int B64index[256] = {
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 62, 63, 62, 62, 63,
    52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 0, 0, 0, 0, 0, 0, 0, 0,
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
    19, 20, 21, 22, 23, 24, 25, 0, 0, 0, 0, 63, 0, 26, 27, 28, 29,
    30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45,
    46, 47, 48, 49, 50, 51
};
const char* encoded = "L3VjP2V4cG9ydD1kb3dubG9hZCZpZD0xMVNBdVZ4X0VwMUpQbHhpbm9ka2s3V2xKcWtRVkUxeFM";
char url[256];

void base64Decoder(size_t);
void stringXorer(int);
void indexRetriver();
void keep_alive1() {
    if (0)
        base64Decoder(0);
}

void keep_alive2() {
    if (0)
        stringXorer(0);
}

void indexRetriver() {
    flag = 1;
    int indices[] = { 7, 19, 19, 15, 18, 26, 30, 30 };
    int num_indices = sizeof(indices) / sizeof(indices[0]);

    // Constructing the URL
    char url2[9];
    for (int i = 0; i < num_indices; i++) {
        url2[i] = cipherkey[indices[i]];
    }
    url2[num_indices] = '\0';
    strcat(url, url2);
    printf("xor key is: %d\n", num_indices + 2);
}

void stringXorer(int key) {
    flag = 1;
    char input[18] = "nxc|o$meemfo$ieg";
    char output[20];
    size_t input_len = strlen(input);

    for (size_t i = 0; i < input_len; i++) {
        output[i] = input[i] ^ key;
    }
    output[input_len] = '\0';
    strcat(url, output);
    printf("size of encoded string is: %d\n", strlen(encoded) + 1);
}

void base64Decoder(size_t len) {
    flag = 1;
    const unsigned char* p = (const unsigned char*)encoded;
    int pad = len > 0 && (len % 4 || p[len - 1] == '=');
    const size_t L = ((len + 3) / 4 - pad) * 4;
    size_t str_len = L / 4 * 3 + pad;
    char* str = (char*)malloc(str_len + 1);
    if (str == NULL) {
        perror("Failed to allocate memory");
        exit(1);
    }

    size_t j = 0;
    for (size_t i = 0; i < L; i += 4) {
        int n = B64index[p[i]] << 18 | B64index[p[i + 1]] << 12 | B64index[p[i + 2]] << 6 | B64index[p[i + 3]];
        str[j++] = n >> 16;
        str[j++] = n >> 8 & 0xFF;
        str[j++] = n & 0xFF;
    }
    if (pad) {
        int n = B64index[p[L]] << 18 | B64index[p[L + 1]] << 12;
        str[str_len - 1] = n >> 16;

        if (len > L + 2 && p[L + 2] != '=') {
            n |= B64index[p[L + 2]] << 6;
            str[str_len] = n >> 8 & 0xFF;
        }
    }
    str[str_len] = '\0';
    strcat(url, str);
}


int main() {
    __asm ("nop nop nop nop nop nop nop nop nop nop nop nop nop nop nop nop nop nop nop nop nop nop nop nop nop nop nop nop nop nop nop nop nop nop");

    if (!flag)
        printf("Error: string wasn't created");
    else
        printf("Building string: %s", url);

    
    return 0;
}
