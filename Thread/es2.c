#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>

int cnt=1;

void stampa(void *arg){
    int tID = pthread_self();
    //int dato = *((int*)arg);
    int *dato_din = (int*)malloc(sizeof(int));
    dato_din=arg;
    //printf("Sono il thread %u. parametro passato %d  \n", tID,dato);
    printf("Sono il thread %u. Parametro passato %d \n", tID, *dato_din);
    cnt++;
    pthread_exit(&dato_din);
}

int main(int argc, char const *argv[]){
    
    pthread_t t[10];
    int i;
    int *ret;

    for(i=0;i<10;i++){
        pthread_create(&t[i],NULL,(void *) &stampa, (void *) &i);
        sleep(1);
    }
    printf("Padre: attende termine dei thread\n");
    for(i=0;i<10;i++){
        pthread_join(t[i],(void**)&ret);
        printf("Restituzione exit: %d\n",*ret);
    }
    printf("Tutti i thread sono terminati\n");
}
