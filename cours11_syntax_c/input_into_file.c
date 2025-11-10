#include <stdio.h>

int main(int args, char* argv[]){

    // print the count of the of arguments
    printf("The value args is %d\n", args);

    for (int i=0; i < args; i++){
        printf("%s \n", argv[i]);
    }

    return 0;
}