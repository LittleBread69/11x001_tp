#include <math.h>
#include <stdio.h>


void exercice1(void){
    printf("\n\nEXERCICE 1\n\n");
    
    char ma_chaine[] = "J'aime les pizzas"; // déclaration et affectation
    
    /******************** Votre code ci-dessous ********************/
    printf("%c", ma_chaine[0]);
    for (int i = 1; ma_chaine[i] != '\0'; i++){
        printf("-%c", ma_chaine[i]);
    }
    printf("\n");
    /******************** Votre code ci-dessus *********************/
    
    return;
}


void exercice2(void){
    printf("\n\nEXERCICE 2\n\n");
    
    char ma_chaine[] = "On est à Genève";
    
    /******************** Votre code ci-dessous ********************/ /*
    printf("Char[20] = %c, Char[1000000] = %c", ma_chaine[20], ma_chaine[1000000]); // THis crashes the code
    */
    /******************** Votre code ci-dessus *********************/
    
    return;
}


void exercice3(void) {
    printf("\n\nEXERCICE 3\n\n");

    int height = 7;
    
    /******************** Votre code ci-dessous ********************/
    for (int i = 1; i <= height; i++){
        for (int j = 0; j < i; j++){
            printf("*");
        }
    printf("\n");
    }
    printf("\n");
    /******************** Votre code ci-dessus *********************/

    return;
}

void exercice4(void) {
    printf("\n\nEXERCICE 4\n\n");

    int x = 42;
    printf("++x: %d\n", ++x);
    printf("x après %d\n\n", x);

    x = 42;
    printf("x++: %d\n", x++);
    printf("x après %d\n\n", x);

    x = 42;
    printf("x+=1: %d\n", x += 1);
    printf("x après %d\n\n", x);

    /******************** Votre code ci-dessous ********************/
    x = 42;
    printf("--x: %d\n", --x);
    printf("x après %d\n\n", x);

    x = 42;
    printf("x--: %d\n", x--);
    printf("x après %d\n\n", x);

    x = 42;
    printf("x-=1: %d\n", x -= 1);
    printf("x après %d\n\n", x);
    /******************** Votre code ci-dessus *********************/
    
    return;
}

/******************** Votre fonction ci-dessous ********************/
int square(int x){
    return x * x;
}
/******************** Votre fonction ci-dessus *********************/

void exercice5(void) {
    printf("\n\nEXERCICE 5\n\n");
    /******************** Votre code ci-dessous ********************/
        printf("%d", square(5));
    /******************** Votre code ci-dessus *********************/

    return;
}


void exercice6(void) {
    printf("\n\nEXERCICE 6\n\n");
    
    /******************** Votre code ci-dessous ********************/
    //printf("3.0: %d, 3.14: %d, hello: %d", square(3.0), square(3.14), square("hello")); //square("hello") doesn't compile
    printf("3.0: %d, 3.14: %d", square(3.0), square(3.14)); // returns 3 ^ 2 both times
    /******************** Votre code ci-dessus *********************/

    return;
}

void exercice7(void) {
    printf("\n\nEXERCICE 7\n\n");
    /*
    print(f"ouch = {3 < 4 < 2}") #prints out False
    */

    int ouch = 3 < 4 < 2; // returns 1 or true
    printf("%d\n", ouch);

    return;
}

void exercice8(void) {
    printf("\n\nEXERCICE 8\n\n");
    
    /**************************************************************/
    /********* Exemple d'overflow du type 'unsigned char' *********/
    /**************************************************************/

    unsigned char a, b, c;

    // Vérifions qu'un 'unsigned char' occupe bien 8 bits
    int size_of_unsigned_char = sizeof(a);
    printf("Le type 'unsigned char' utilise %d octets, c'est-à-dire %d bits.\n", size_of_unsigned_char, 8 * size_of_unsigned_char);

    // Exemple d'overflow
    a = 61;
    b = 213;
    c = a + b;  // Overflow : c ne vaut pas 61 + 213 = 274 mais 274 % 256 = 18
    printf("%d + %d = %d\n", a, b, c);
    
    /*************************************/
    /********* Fin de l'exemple *********/
    /*************************************/


    /******************** Votre code ci-dessous ********************/
    int d, e, f, size_of_int;

    size_of_int = sizeof(d);
    printf("Le type 'int' utilise %d octets, c'est-à-dire %d bits.\n", size_of_int, 8 * size_of_int);

    // Exemple d'overflow
    d = 2147483647;
    e = 2;
    f = d + e;
    
    printf("%d + %d = %d\n", d, e, f);
    /******************** Votre code ci-dessus *********************/

    return;
}


int main(void) {   

    // Astuce : commenter tous les exercices sauf celui en cours pour gagner du temps !

    exercice1();
    exercice2();
    exercice3();
    exercice4();
    exercice5();    
    exercice6();
    exercice7();
    exercice8();

    return 0;
}
