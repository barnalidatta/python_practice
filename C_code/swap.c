#include <stdio.h>

int main(){
    int a = 5, b =10, temp;
    temp = a;
    a = b;
    b = temp;

    printf("value of a is %d\n", a);
    printf("value of b is %d", b);
}
