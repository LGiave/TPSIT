#include<stdlib.h>
#include<stdio.h>

int main(){
    float * p;
    float max;
    int i = 0;
    int n = 10;
    p = (float *)malloc(n* sizeof(float));
    for (i = 0; i < n; i++)
    {
        printf("[%d]->" , i);
        scanf("%f",p+i);
    }

    max= * p;
    for ( i = 1; i < n; i++){
        if(*(p+i)> max){
            max= *(p+i);
        }
    }
    printf("\n %f",max);
}