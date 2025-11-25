#include <stdio.h>

float square_root(float q){
    const double epsilon = 1e-6;
    float a, b, x;
    a = 0;
    b = 1 + q;

    while (b - a >= epsilon)
    {
        x = (a + b) / 2;
        if (x * x >= q){
            b = x;
        }
        else{
            a = x;
        }
    }
    return x;
}

int main(void){
    printf("Square Root of 5 = %f\n", square_root(5));
    return 0;
}