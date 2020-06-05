#include <stdlib.h>
#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>

#define MAXCICLI 100

sem_t mutex , pieno , vuoto;

char buffer[10];
int in,out;

void *produci(void *arg);
void *consuma(void *arg);

int main(int argc, char const *argv[])
{
    pthread_t prod, cons;

    sem_init(&mutex,0,1);

    sem_init(&pieno,0,0);

    sem_init(&vuoto,0,10);

    pthread_create(&prod,NULL,(void*)produci,NULL);
    pthread_create(&cons,NULL,(void*)consuma,NULL);

    pthread_join(prod,NULL);
    pthread_join(cons,NULL);
    return 0;
}

void *produci(void *arg){
    int i = 0;
    char c;

    while(i<MAXCICLI){
        i++;
        c = (char) (rand()%26)+97;

        sem_wait(&vuoto);
        sem_wait(&mutex);

        buffer[in]=c;
        printf("inserire %c\n",c);
        in=(in+1)%10;

        sem_post(&mutex);
        sem_post(&pieno);
    }
}

void *consuma(void *arg){
    int i = 0;
    char c;

    while (i<MAXCICLI){
        i++;

        sem_wait(&pieno);
        sem_wait(&mutex);

        c = buffer[out];
        printf("prelevo %c\n",c);
        out= (out+1)%10;

        sem_post(&mutex);
        sem_post(&vuoto);
    }
    
}

