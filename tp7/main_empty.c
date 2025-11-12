#include <math.h>
#include <stdio.h>


void exercice1(void){
    printf("\n\nEXERCICE 1\n\n");
    
    printf("Bonjour monde !\n");

    printf("Nom     : Michel LAMBDA\n");
    printf("Né le   : 31.10.2001\n");
    printf("Contact : michel.lambda@unige.ch\n\n");

    return;
    // Python ajoutait par défaut \n à la fin et arrivait à print "é"
}


void exercice2(void){
    printf("\n\nEXERCICE 2\n\n");
    
    /******************** Votre code ci-dessous ********************/
    const char U = 'U';
    const char N = 'N';
    const char I = 'I';
    const char G = 'G';
    const char E = 'E';

    printf("%c%c%c%c%c\n", U, N, I, G, E);
    printf("%c%c%c%c%c\n", E, G, I, N, U);
    /******************** Votre code ci-dessus *********************/
    return;
}


void exercice3(void) {
    printf("\n\nEXERCICE 3\n\n");

    const float PI = 3.1415926535;

    // Lecture du rayon
    float radius = 10;
    float height = 5; 
    
    /******************** Votre code ci-dessous ********************/
    float surface = 2 * PI * radius * (radius + height);
    float volume =  PI * radius * radius * height;

    printf("Surface du Cylindre: %.3f\n", surface);
    printf("Volume du Cylindre: %.3f\n", volume);
    /******************** Votre code ci-dessus *********************/

    return;
}

void exercice4(void) {
    printf("\n\nEXERCICE 4\n\n");

    // Affectation de la date de naissance
    int birth_year = 2005;
    int birth_month = 06;
    int birth_day = 02;  // Déclaration et affectation des variables

    // Affectation de la date du jour
    int today_year = 2025;
    int today_month = 11;
    int today_day = 11;  // Déclaration et affectation des variables

    // Affiche les dates entrées par l'utilisateur
    printf("Je suis né.e le %d/%d/%d.\n", birth_day, birth_month, birth_year);
    printf("Aujourd'hui, nous sommes le %d/%d/%d.\n\n", today_day, today_month, today_year);    

    int age_in_day = 0;

    /******************** Votre code ci-dessous ********************/
    age_in_day = (today_year - birth_year) * 360;
    if (today_month < birth_month){
        today_month += 12;
        age_in_day -= 360;
    }
    age_in_day += (today_month - birth_month) * 30;
    if (today_day < birth_day){
        today_day += 30;
        age_in_day -= 30;
    }
    age_in_day += (today_day - today_month);
    /******************** Votre code ci-dessus *********************/

    printf("==> Mon âge est (approximativement) de %d jours.\n", age_in_day);
    
    return;
}


void exercice5(void) {
    printf("\n\nEXERCICE 5\n\n");

    // Lecture du nombre de jours
    int nb_of_days = 2153; // could've been a constant
    /******************** Votre code ci-dessous ********************/
    /*Python
    nb_of_days = int(input("Entrez un nombre de jours à convertir : "))
    # ******************** Votre code ci-dessous ********************
    years = nb_of_days // 365
    weeks = (nb_of_days % 365) // 7
    days = (nb_of_days - 365 * years - 7 * weeks)

    print(f"{nb_of_days} font {years} année(s), {weeks} semaine(s) et {days} jour(s).")
    */

    int years, weeks, days = 0;
    years = nb_of_days / 365;
    weeks = (nb_of_days % 365) / 7;
    days = (nb_of_days - 365 * years - 7 * weeks);

    printf("%d jours font %d année(s), %d semaines(s) et %d jours(s).\n", nb_of_days, years, weeks, days);

    /******************** Votre code ci-dessus *********************/

    return;
}


void exercice6(void) {
    printf("\n\nEXERCICE 6\n\n");

    int a = 7, b = 2;
    float c;  
    
    /******************** Votre code ci-dessous ********************/
    c = (float) a / b;
    /******************** Votre code ci-dessus *********************/
    
    printf("%d / %d = %f \n", a, b, c);

    return;
}

void exercice7(void) {
    printf("\n\nEXERCICE 7\n\n");
    
    /******************** Votre code ci-dessous ********************/
    int nombre = 42;

    if (nombre < 0 || nombre > 9){
        printf("%d n'est pas un nombre valide. Les nombre valide sont entre 0 (incl) et 9 (incl).\n", nombre);
    }
    else{
        printf("%d est un nombre valide.\n", nombre);
    }
    /******************** Votre code ci-dessus *********************/

    return;
}

void exercice8(void) {
    printf("\n\nEXERCICE 8\n\n");
    
    /******************** Votre code ci-dessous ********************/
    int x = 42;
    do {
        printf("J'affiche même si x vaut 42\n");
    } while (x != 42);  // attention à ce dernier point-virgule
    /******************** Votre code ci-dessus *********************/

    return;
}

void exercice9(void) {
    printf("\n\nEXERCICE 9\n\n");
    
    /******************** Votre code ci-dessous ********************/
    for (int i=0; i < 10; i++) {
        printf("%d\n", i);
    }
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
    exercice9();
    return 0;
}
