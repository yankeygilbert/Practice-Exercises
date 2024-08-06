#include<stdio.h>
int main(){
    int x=17,*ptr=&x;
    int *y[2]={ptr};
    printf("%d",*y[0]);

}