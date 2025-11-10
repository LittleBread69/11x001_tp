#include <stdio.h>

int main(){
    // arithmetic operators: + - * / %

    int a = 3 * (1 + 2);
    printf("%d\n", a);

    //increment and decrement operators
    
    int i = 0;
    
    /*
    Increment with
    i = i + 1;
    i += 1;
    */
    i++;

    printf("i=%d\n", i);

    /*
    Decrement with
    i = i - 1;
    i -= 1;
    */
    i--;


    printf("i=%d\n", i);


    i = 0;
    int j = 0;

    //j = i (before increment);
    j = i++;
    printf("i=%d, j=%d\n", i, j);

    i = 0;
    j = 0;

    j = ++i;
    printf("i=%d, j=%d\n", i, j);

    return 0;
}