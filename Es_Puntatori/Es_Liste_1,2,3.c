#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>



struct El
{
    int valore;
    struct El* next;
};

void stampaLista(struct El *listaDiElementi);
void lunghezzaLista(struct El* listaDiElementi, int i);

int main(){
    int n;
    struct El* lista; // puntatore al primo el. della lista
    struct El* l;
    lista=NULL; // il puntatore della lista successiva e inizializzata a null
    int i;

    do
    {
        printf("Inserisci un naturale o -1 per terminare");
        scanf("%d",&n);
        if (n>=0){
            if(lista==NULL){ // verifico se il puntatore è uguale a NULL
                lista=(struct EL*) malloc(sizeof(struct El)); // alloca in memoria per una struttura
                l=lista;
            }else{
                l->next=(struct EL*) malloc(sizeof(struct El)); // assegno al puntatore l dell'elemento corrente un puntatore che punta all'elemento successivo  
                l=l->next;
            }
            l->valore=n; // assegno n al campo valore dell'elemento corrente
            l->next=NULL;// assegno NULL al campo next dell'elemento corrente
        }
    } while (n>=0);

    l=lista; // assegno ad l il puntatore al primo elemento della lista
    printf("Numeri inseriti \n");
    stampaLista(l);
    lunghezzaLista(l,i);
    /*
    while (1!=NULL){
        printf("%d - %p \n",l->valore,l->next);
        l=l->next; // il puntatore corrente è assegnato al puntatore dell'elemento successivo della lista
    }
    printf("\n");
    return 0;
    */
}
void stampaLista(struct El* listaDiElementi){
    if(listaDiElementi!=NULL){
        printf("%d - %p\n",listaDiElementi->valore,listaDiElementi->next);
        listaDiElementi= listaDiElementi->next;
        stampaLista(listaDiElementi);
    }else{
        return;
    }
}

void lunghezzaLista(struct El* listaDiElementi, int i){
    if(listaDiElementi!=NULL){
        i++;
        listaDiElementi= listaDiElementi->next;
        lunghezzaLista(listaDiElementi,i);
    }else{
        printf("\n%d\n",i);
        return;
    }
}
