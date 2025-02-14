#include <stdio.h>
#include <string.h>

char *s = "l_alcotsft{_tihne__ifnlfaign_igtoyt}";

int main()
{
    int len = strlen(s);
    char target[len];
    int target_index = 0;

    // Extract characters at even indices from s and store them in target
    for (int i = 0; i < len/2; i++)
    {
        target[target_index] = s[2*i];
        target[target_index+len/2] = s[2*i+1];
        target_index++;
    }

    // Null-terminate the target string
    target[len] = '\0';

    printf("Paradoxified: %s\n", target);
    return 0;
}