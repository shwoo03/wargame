// Name: chall.c
// Compile Option: gcc chall.c -o chall -fno-stack-protector

#include <stdio.h>
#include <signal.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <time.h>

#define FLAG_SIZE 0x45

void alarm_handler() {
    puts("TIME OUT");
    exit(1);
}

void initialize() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);

    signal(SIGALRM, alarm_handler);
}

int main(void) {
    int fd;
    char *flag;

    initialize();
    srand(time(NULL)); 

    flag = (char *)malloc(FLAG_SIZE);
    fd = open("./flag", O_RDONLY);
    read(fd, flag, FLAG_SIZE);
    close(fd);

    int num1 = 0;
    int num2 = 0;
    int inpt = 0; 

    for (int i = 0; i < 50; i++){
        alarm(1);
        num1 = rand() % 10000;
        num2 = rand() % 10000;
        printf("%d+%d=?\n", num1, num2);
        scanf("%d", &inpt);

        if(inpt != num1 + num2){
            printf("Wrong...\n");
            return 0;
        }
    } 
    
    puts("Nice!");
    puts(flag);

    return 0;
}