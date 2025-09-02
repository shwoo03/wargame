// Compile: gcc -o shell_basic shell_basic.c -lseccomp
// apt install seccomp libseccomp-dev

#include <fcntl.h>
#include <seccomp.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/prctl.h>
#include <unistd.h>
#include <sys/mman.h>
#include <signal.h>

// TIME OUT 함수 
void alarm_handler() {
    puts("TIME OUT");
    exit(-1);
}

// 버퍼 지정 후 알람 설정 
void init() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    signal(SIGALRM, alarm_handler);
    alarm(10);
}

void banned_execve() {
  scmp_filter_ctx ctx;
  ctx = seccomp_init(SCMP_ACT_ALLOW);
  if (ctx == NULL) {
    exit(0);
  }
  seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(execve), 0);
  seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(execveat), 0);
  seccomp_load(ctx);
}

int main(int argc, char *argv[]) {
  char *shellcode = mmap(NULL, 0x1000, PROT_READ | PROT_WRITE | PROT_EXEC, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);   // 4KB 메모리 할당 rwx 권한을 가짐 
  void (*sc)();
  
  init();
  
  // execve, execveat 시스템 호출을 금지함 
  banned_execve();

  printf("shellcode: ");
  read(0, shellcode, 0x1000); // 0x1000 바이트 만큼 데이터의 셸코드를 읽음 

  sc = (void *)shellcode;
  sc(); // 셸 코드 실행 

  return 0;
}
