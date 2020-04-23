#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

#define DESTRA (i+1)%N
#define SINISTRA (i-1+N)%N

#define N 5
#define PENSA 0
#define ATTESA 1
#define MANGIA 2

pthread_mutex_t mutex, mutex_f[N];
int stato[N];

void pensa(int i){
    printf("\n FILOSOFO %d: STO PENSANDO",i);
    sleep(rand()%N);
}

void mangia(int i){
    printf("\n FILOSOFO %d: STO MANGIANDO",i);
    sleep(rand()%N);
}

void controllaPosate(int i){
    if(stato[i]==ATTESA && stato[DESTRA] != MANGIA && stato[SINISTRA]!= MANGIA){
        stato[i]=MANGIA;
        printf("\n FILOSOFO %d: PRENDO LE FORCHETTE",i);
    }else{
        printf("\n FILOSOFO %d: FORCHETTE OCCUPATE, ATTENDO PER MANGIARE",i);
    }
}

void prendi(int i){
    pthread_mutex_lock(&mutex);
    printf("\n FILOSOFO %d: HO FAME ASPETTO LE FORCHETTE",i);
    stato[i]= ATTESA;
    controllaPosate(i);

    pthread_mutex_lock(&mutex_f[i]);
    pthread_mutex_unlock(&mutex);
}

void posa(int i){
    pthread_mutex_lock(&mutex);
    stato[i]=PENSA;
    pthread_mutex_unlock(&mutex_f[i]);
    pthread_mutex_unlock(&mutex);
}


void * filosofo(void *arg){
    int i=(*(int *)arg);
    while (1)
    {
        pensa(i);

        prendi(i);

        mangia(i);

        posa(i);
    }
}

int main(int argc, char const *argv[])
{
    pthread_t filo[N];
    int i;

    pthread_mutex_init(&mutex,NULL);
    for (i = 0; i < N; i++)
    {
        pthread_mutex_init(&mutex_f[i],NULL);
    }

    for (i=0;i<N;i++){
        pthread_create(&filo[i],NULL, (void*)filosofo,(void*)&i);
    }
    
    
    return 0;
}