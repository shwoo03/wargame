#include <stdio.h>
#include <string.h>

int main(){
    char answer[4] = {0x00, 0x12, 0x32, 0x41};
    char input[4] = {0x00};

    if(!strncmp(answer, input, 4)){
        printf("PASS!!!\n");
    } else {
        printf("Fail\n");
    }
}