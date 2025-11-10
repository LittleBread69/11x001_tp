#include <stdio.h>

// Syntax printf: printf ( const char * format, arg1, arg2, ...)

// format specifier have the form: %[]specifier
// Example specifiers:
// %d or %i Integer
// %f Floating Point Number
// %c Character
// %s String (of characters)

int main()
{
    printf("Hello World\n");

    //int: Integer
    int a;
    a = 2;

    printf("My integer 'a' has the value %d\n", 3);

    // float: floating point number
    float b = 2.33;
    printf("f=%f\n", b);

    // more than one variable in printf
    printf("f=%f, a=%d\n", b, a);

    // char: Character
    char c = 'c';
    printf("c=%c\n", c);

    // in C there are no predifined Strings
    // char s = 'sbs' will be equal to 's'

    // To use a string, you may use an arry of characters
    // (arrays are similar to a list of characters in Python)

    char str[] = "Julia";

    printf("The string is: %s\n", str);

    return 0;
}