#include <stdio.h>
#include <pthread.h>
#include <unistd.h>

pthread_mutex_t m1,m2;

void *ping(void *arg){
    while (1){
        pthread_mutex_lock(&m1);
        sleep(0.9);
        printf("ping");
        pthread_mutex_unlock(&m2);
    }
}

void *pong(void *arg){
    while (1){
        pthread_mutex_lock(&m2);
        sleep(0.9);
        printf("pong");
        pthread_mutex_unlock(&m1);
    }
}

int main(int argc, char const *argv[])
{
    pthread_t t1, t2;

    pthread_mutex_unlock(&m1); // sblocchiamo la mutex
    pthread_mutex_lock(&m2);

    pthread_create (&t1, NULL, (void*)ping, NULL);
    pthread_create (&t2,NULL, (void*)pong, NULL );

    pthread_join(t1,NULL);
    pthread_join(t2,NULL);
    return 0;
}
