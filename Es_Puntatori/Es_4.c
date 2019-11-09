#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define DIM 50

typedef struct struttura
{
    char nome[DIM];
    int numero;
}Struttura;


int main(){
    Struttura* list;
    int dim = 0;
    printf("Inserire dimensione della lista\n");
    scanf("%d" , &dim);

    list = (Struttura*) malloc(dim*sizeof(Struttura));

    printf("Dimensione struttura = %d\n" , sizeof(Struttura));

    for (int i = 0; i < dim; i++)
    {
        char temp[DIM];
        printf("%d = " , i);

        fflush(stdin);
        gets(temp);

        printf("\n");

        strcpy((i+list)->nome, temp);

        (i+list)->numero = i;
    }
    

    for (int k = 0; k < dim; k++){
        printf("pointer list [%d] = %p\n" , k , (list+k));
    }

    for (int i = 0; i < dim; i++)
    {
        printf("Struttura %d\n " , i);
        printf("Nome: %s \t Numero: %d" ,(list+i)->nome , (list+i)->numero );
        printf("\n");
    }
    

    
    free(list);

    getch();
    fflush(stdin);
    return 1;
}