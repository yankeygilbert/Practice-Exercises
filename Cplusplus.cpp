#include <iostream>
// function in c++
int *functionadd (int *a, int *b)
{   
         *a += *b;
        return a ;
        

}
int func2(int num, int *p)
{
    int y =  num + *p;

}
//structures in c++
  struct home {
        char chair[5]="home" ;
        int windows;
        struct location{
         char *place[5] = {"anjai","kansa","accra"};
          }places;
    }afie;
//pointers in C++
   char func(char *arr[])
{
    
     for(char *p = (*++arr);*p != '\0';p++ )
       std::cout<<*p<<std::endl; 
}
 
main(){
    
    
}