#include <iostream>
#include <cstdio>

namespace variales{
    void const funct();
}

void const variales:: funct() {
    printf("we are going");
}
   
   using namespace variales;
main(){
    funct();
}