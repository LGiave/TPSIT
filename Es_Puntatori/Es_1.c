#include<stdlib.h>
#include<stdio.h>

int main(){
    float * p;
    int i;
    int n = 10;
    p = (float *)malloc(n* sizeof(float));
    for (i = 0; i < n; i++)
    {
        printf("%d",i);
        scanf("%f",(p+i));
    }
    
    for (i=0;i<n;i++)
    {
        printf("%f",*(p+i));
    }

    
    fflush(stdin);
}