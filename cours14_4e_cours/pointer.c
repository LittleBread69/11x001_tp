#include <stdio.h>

int main(void){
    int *p1;
    char *p2;
    int n;
    p1 = &n;

    // pointers are printed with %p, it's hexadeciaml
    printf("p1= %p\n", p1);
    printf("&n= %p\n", &n);
    
    char c;
    p2 = &c;

    // the size of a pointer (in memory) is 8 bytes
    printf("Size of pointer adress (p1): %d octets\n", sizeof(p1));

    // To access the value at an adress, you need to use * again

    *p1 = 13;
    printf("*p1=%d\n", *p1);
    printf("n=%d\n", n);

    //examples de syntax
    //1.
    int *x, y, *z;

    //2.
    int m;

    //3.
    int *p3;
    p3 = &m;
    //~==
    int *p4 = &m;

    //Pointers and arrays
    int a[10];
    printf("a=%p\n", a);

    int *p5;
    p5 = a;

    printf("p5= %p\n", p5);
    printf("&a[0] = %p\n", &a[0]);

    return 0;
}