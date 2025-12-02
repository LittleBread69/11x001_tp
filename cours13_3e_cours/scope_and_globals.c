#include <stdio.h>

int main(void){
    {
    int a = 3;
    printf("a=%d\n", a); //works
    }
    //printf("a=%d\n", a); //error, out of scope

    int n = 0;
    int s = 0;
    int m = -1;

    while(n < 10) {
        int m;
        m = 2 * n + 1;
        s = s + m;
        n++;
    }
}