#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define R 17000
#define C 11

typedef struct giochi{
    int Rank;
    char *Name;
    char *Platform;
    int Year;
    char *Genre;
    char *Publisher;
    float NA_Sales;
    float EU_Sales;
    float JP_Sales;
    float Other_Sales;
    float Global_Sales;
}game;

void insList(game tab[]);

int main(){

    game lista[R];
    insList(lista);
    int i=2;
}
void insList(game tab[]){
    FILE *fp;
    fp=fopen("vgsales.csv","r");
    if(fp==NULL){
        printf("Impossibile aprire il file \n");
    }else{
        printf("file aperto \n");
    }
    int i=0;
    char buffer[600];
    while(fgets(buffer,600,fp)!=NULL){
        tab[i].Rank=atoi(strtok(buffer,","));
        tab[i].Name=strtok(NULL,",");
        tab[i].Platform=strtok(NULL,",");
        tab[i].Year=atoi(strtok(NULL,","));
        tab[i].Genre=strtok(NULL,",");
        tab[i].Publisher=strtok(NULL,",");
        tab[i].NA_Sales=atoi(strtok(NULL,","));
        tab[i].EU_Sales=atoi(strtok(NULL,","));
        tab[i].JP_Sales=atoi(strtok(NULL,","));
        tab[i].Other_Sales=atoi(strtok(NULL,","));
        tab[i].Global_Sales=atoi(strtok(NULL,","));
        i++;
    }
        i=0;
        printf("%d %s %s %d %s %s %f %f %f %f %f",tab[i].Rank,tab[i].Name,tab[i].Platform,tab[i].Year,tab[i].Genre, tab[i].Publisher,tab[i].NA_Sales,tab[i].EU_Sales,tab[i].JP_Sales,tab[i].Other_Sales,tab[i].Global_Sales);
}
