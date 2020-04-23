#include <stdio.h>
#include <pthread.h>

void *uno (void *arg){
    printf("Sono il thread che esegue la funz. uno\n");
    pthread_exit(0);
}

void due (void *arg){
    printf("SOno il thread che esegue la funz. due\n");
    pthread_exit(0);
}

int main(){

    pthread_t t1, t2;

    printf("Padre: creo 2 thread \n");

    pthread_create(&t1, NULL, (void *)uno, NULL );
    pthread_create(&t2,NULL, (void *)&due , NULL);
    printf("Padre: attendo la terminazione dei thread creati\n");

    pthread_join(t1,NULL);
    pthread_join(t2,NULL);

    printf("Padre: i thread sono terminati\n");
    
    return 0;
}
