#include<stdlib.h>
#include<stdio.h>
#include<string.h>
#define DIM 50

int main(){
    char * s;
    int i;
    int n = 0;
    s = (char *)malloc(DIM * sizeof(char));
    
    printf("Inserire cucchietti ");

    gets(s);

    while (*s != '\0')
    {
        n++;
        s++;
    }

    printf("%d",n);
    

    fflush(stdin);
}