#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

void *func (void *vargp)
{
    printf("start %d\n", *(int*) vargp);
    sleep(2);
    printf("End %d\n", *(int*) vargp);
    return NULL;
}

int main()
{
    int n = 0;
    pthread_t thread_id;
    pthread_create(&thread_id, NULL, func, &n);
    pthread_join(thread_id,NULL);
    exit(0);
}
