// Name: chall.c
// Compile Option: gcc chall.c -o chall -fno-stack-protector

#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>
#include <string.h>
#include <fcntl.h>

#define FLAG_SIZE 0x45

void alarm_handler() {
    puts("TIME OUT");
    exit(-1);
}

void initialize() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);

    signal(SIGALRM, alarm_handler);
    alarm(30);
}


int main(int argc, char *argv[]) {
    int fd;
    char *flag;

    initialize();

    // read flag
    flag = (char *)malloc(FLAG_SIZE);
    fd = open("./flag", O_RDONLY);
    read(fd, flag, FLAG_SIZE);
    close(fd);

    printf("Input: ");

    unsigned char arr[9];
    scanf("%8s", arr);
    printf("arr  | 0x%x  0x%x  0x%x  0x%x  0x%x  0x%x  0x%x  0x%x |\n", arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7]);

    unsigned int * int_arr = (unsigned int *)arr;

    printf("arr  | 0x%x  0x%x |\n", int_arr[0], int_arr[1]);

    if(int_arr[0] == 0x64726d68 && int_arr[1] == 0x636b3a29){
        puts("Nice!");
        puts(flag);
    }
    else{
        puts("No...");
    }

    return 0;
}