#include <stdio.h>
#include <string.h>

int main() {
    char flag[] = "t`qcxo0s0o2.kd\\.k\\o0s0o20z";
    char input[100];  
    int index = strlen(flag) - 1;

    for (int i = 0; i < strlen(flag); i++) {
        input[i] = flag[i] + 3;
    }
    input[strlen(flag)] = '\0'; // Null-terminate the modified string

    for (int j = 0; j < index; j += 2) {
        char tmp = input[j];
        input[j] = input[index - j - 1];
        input[index - j - 1] = tmp;
    }

    printf("Mixed Flag: %s\n", input);
    return 0;
}