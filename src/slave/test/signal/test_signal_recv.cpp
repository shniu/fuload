#include <error.h>
#include <errno.h>
#include <sys/time.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <poll.h>
#include <sys/epoll.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <fcntl.h>
#include <strings.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <signal.h>

int getsig = 0;
void ouch(int sig)
{
    getsig = 1;
}
int main(int argc, const char *argv[])
{
    signal(SIGUSR1,ouch);
    while(1)
    {
        printf("hello world\n");
        if (getsig == 1)
        {
            printf("get signal\n");
            getsig = 0;
        }
        sleep(1);
    }
    return 0;
}
