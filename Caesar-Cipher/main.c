#include <stdio.h>
#include <string.h>

void encrypt(char* text, int key);

int main(){
    int key = 1;
    char text[100];

    printf("Enter Message (write without whitespaces): ");
    scanf("%99s", text);

    printf("Enter Key: ");
    scanf("%d", &key);

    encrypt(text, key);

    printf("Res: %s\n", text);

    return 0;
}

void encrypt(char* text, int key){
    for(int i = 0; i < strlen(text); i++){
        if(text[i] >= 'a' && text[i] <= 'z')
            text[i] = (text[i] - 'a' + key) % 26 + 'a';
    }
}