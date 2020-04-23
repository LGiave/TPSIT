#include<stdio.h>
#include<stdlib.h>
#include<pthread.h>
#include<unistd.h>
#include<stdbool.h>

int biglietti_c = 30;


pthread_mutex_t m1 = PTHREAD_MUTEX_INITIALIZER;
pthread_mutex_t m2 = PTHREAD_MUTEX_INITIALIZER;


void *casse(void* argv){
    int biglietti; 
    if(pthread_mutex_lock(&m1) == 0){
        printf("CASSA 1:\n");
        biglietti = 1 + rand() %3;
        printf("\tSono il cliente %u, e voglio acquistare %d biglietti.\n" , pthread_self(), biglietti);
        if(biglietti_c == 0){
            printf("\tBiglietti acquistati 0\n");
        }else if(biglietti > 0 && biglietti<= biglietti_c){
            printf("\tBiglietti acquistati %d\n", biglietti);
            biglietti_c -= biglietti;
        }else if(biglietti > 0 && biglietti > biglietti_c){
            printf("\tBiglietti acquistati %d\n" , biglietti_c);
            biglietti_c = 0;
        }
        printf("\t%d biglietti rimanenti.\n" , biglietti_c);
        pthread_mutex_unlock(&m1);
    }
    if(pthread_mutex_lock(&m2) == 0){ 
        printf("CASSA 2:");
        biglietti = 1 + rand() %3;
        printf("\tSono il cliente %u, e voglio acquistare %d biglietti.\n" , pthread_self(), biglietti);
        if(biglietti_c == 0){
            printf("\tBiglietti acquistati 0\n");
        }else if(biglietti > 0 && biglietti<= biglietti_c){
            printf("\tBiglietti acquistati %d\n", biglietti);
            biglietti_c -= biglietti;
        }else if(biglietti > 0 && biglietti > biglietti_c){
            printf("\tBiglietti acquistati %d\n" , biglietti_c);
            biglietti_c = 0;
        }
        printf("\t%d biglietti rimanenti.\n" , biglietti_c);
        pthread_mutex_unlock(&m2);
    }
    pthread_exit(NULL);
}

int main(int argv, char **argc){
    pthread_t c[20];
    int i; 
    for(i=3; i>0; i--){
        printf("Il cinema apre tra %d...\n" , i);
        sleep(1);
    }
    printf("\n\tCINEMA APERTO\n\n");

    for(i=0; i<20; i++){
        pthread_create(&c[i], NULL, (void *)casse, NULL);
    }
    for(i=0; i<20; i++){
        pthread_join(c[i], NULL);
    }
    printf("\n\tCINEMA CHIUSO\n\n");
    return 0;
}
