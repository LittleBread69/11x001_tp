#include <math.h>
#include <stdio.h>


void exercice1(void) {
    printf("\n\nEXERCICE 1\n\n");
    
    /******************** Votre code ci-dessous ********************/
    int entier;
    printf("Entier: ");
    scanf("%d", &entier);

    if (entier > 0){
        printf("%d est positif", entier);
    }
    else if (entier < 0)
    {
        printf("%d est negatif", entier);
    }
    else{
        printf("%d est nul", entier);
    }
    /******************** Votre code ci-dessus *********************/

    return;
}


void exercice2(void) {
    printf("\n\nEXERCICE 2\n\n");
    
    /******************** Votre code ci-dessous ********************/
    unsigned int entier_naturel;

    printf("Entier: ");
    scanf("%u", &entier_naturel);

    unsigned long somme_du_naturel = 0;

    while (entier_naturel > 0) {
        somme_du_naturel += entier_naturel;
        --entier_naturel;
    }
    printf("Somme: %lu\n", somme_du_naturel);
    /******************** Votre code ci-dessus *********************/

    return;
}


void exercice2_bis(void) {
    printf("\n\nEXERCICE 2 BIS\n\n");
    
    /******************** Votre code ci-dessous ********************/
    unsigned int entier_naturel;

    printf("Entier: ");
    scanf("%u", &entier_naturel);

    unsigned long somme_du_naturel = 0;

    for (int i = 1; i <= entier_naturel; i++){
        somme_du_naturel += i;
    }

    printf("Somme: %lu\n", somme_du_naturel);
    /******************** Votre code ci-dessus *********************/

    return;
}


void exercice3(void) {
    printf("\n\nEXERCICE 3\n\n");
    
    /******************** Votre code ci-dessous ********************/
    int day_of_week;
    printf("Jour de la semaine: ");
    scanf("%d", &day_of_week);

    if (day_of_week == 0){
        printf("Lundi!\n");
    }
    else if (day_of_week == 1){
        printf("Mardi!\n");
    }
    else if (day_of_week == 2){
        printf("Mercredi!\n");
    }
    else if (day_of_week == 3){
        printf("Jeudi!\n");
    }
    else if (day_of_week == 4){
        printf("Vendredi!\n");
    }
    else if (day_of_week == 5){
        printf("Samedi!\n");
    }
    else if (day_of_week == 6){
        printf("Dimanche!\n");
    }
    else{
        printf("Pas un jour de la semaine.\n");
    }
    /******************** Votre code ci-dessus *********************/

    return;
}


void exercice3_bis(void) { //literally https://www.w3schools.com/c/c_switch.php
    printf("\n\nEXERCICE 3 BIS\n\n");
    
    //missing the break in the switch-case will cause it to go ham and act like a pseudo-while

    /******************** Votre code ci-dessous ********************/
    int day_of_week;
    printf("Jour de la semaine: ");
    scanf("%d", &day_of_week);

    switch (day_of_week)
    {
    case 0:
        printf("Lundi!\n");
        break;
    case 1:
        printf("Mardi!\n");
        break;
    case 2:
        printf("Mercredi!\n");
        break;
    case 3:
        printf("Jeudi!\n");
        break;
    case 4:
        printf("Vendredi!\n");
        break;
    case 5:
        printf("Samedi!\n");
        break;
    case 6:
        printf("Dimanche!\n");
        break;
    default:
        printf("Pas un jour de la semaine.\n");
    }
    /******************** Votre code ci-dessus *********************/

    return;
}


void exercice4(void) {
    printf("\n\nEXERCICE 4\n\n");
    
    /******************** Votre code ci-dessous ********************/
    int entier_1, entier_2, entier_3, entier_4, entier_5, somme = 0;

    printf("Veillez renseigner 5 entiers (_ _ _ _ _): ");
    scanf("%d %d %d %d %d", &entier_1, &entier_2, &entier_3, &entier_4, &entier_5);

    int entiers[5] = {entier_1, entier_2, entier_3, entier_4, entier_5};

    for (int i = 0; i<5; i++){
        somme += entiers[i];
    }

    printf("Somme des entiers: %d\n", somme);
    /******************** Votre code ci-dessus *********************/

    return;
}


void exercice4_bis(void) {
    printf("\n\nEXERCICE 4 BIS\n\n");

    /******************** Votre code ci-dessous ********************/
    int entier_1, entier_2, entier_3, entier_4, entier_5, somme = 0;

    printf("Veuillez renseigner 5 entiers (_ _ _ _ _): ");
    scanf("%d %d %d %d %d", &entier_1, &entier_2, &entier_3, &entier_4, &entier_5);

    int entiers[5] = {entier_1, entier_2, entier_3, entier_4, entier_5};

    int min_entier = entiers[0], max_entier = entiers[0];

    for (int i = 0; i < 5; i++){
        min_entier = (entiers[i] * (entiers[i] < min_entier)) + (min_entier * (entiers[i] >= min_entier));
    }
    for (int i = 0; i < 5; i++){
        max_entier = (entiers[i] * (entiers[i] > max_entier)) + (max_entier * (entiers[i] <= max_entier));
    }

    printf("Le plus petit des entiers: %d; le plus grand des entiers: %d\n", min_entier, max_entier);
    /******************** Votre code ci-dessus *********************/

    return;
}


void exercice5(void) {
    printf("\n\nEXERCICE 5\n\n");
    
    /******************** Votre code ci-dessous ********************/
    struct Etudiant{
        char prenom[30];
        int note;
    };

    struct Etudiant etudiant;
    printf("Veuillez renseigner le nom de l'étudiant et sa note: _nom_ _note_\n");
    scanf("%s %d", etudiant.prenom, &etudiant.note);
    
    if (etudiant.note >= 4){
        printf("L'étudiant %s a réussi IPA\n", etudiant.prenom);
    }
    else{
        printf("L'étudiant %s a raté IPA\n", etudiant.prenom);
    }
    
    /******************** Votre code ci-dessus *********************/

    return;
}


void exercice5_bis(void) {
    printf("\n\nEXERCICE 5 BIS\n\n");

    /******************** Votre code ci-dessous ********************/
    
    /******************** Votre code ci-dessus *********************/

    return;
}


void exercice5_ter(void) {
    printf("\n\nEXERCICE 5 TER\n\n");
    
    /******************** Votre code ci-dessous ********************/

    /******************** Votre code ci-dessus *********************/
}


void exercice6(void) {
    printf("\n\nEXERCICE 6\n\n");
    
    /******************** Votre code ci-dessous ********************/

    /******************** Votre code ci-dessus *********************/

    return;
}

int main(void) {   

    // Astuce : commenter tous les exercices sauf celui en cours pour gagner du temps !
    
    //exercice1();
    //exercice2();
    //exercice2_bis();
    //exercice3();
    //exercice3_bis();
    //exercice4();
    //exercice4_bis();
    exercice5();
    exercice5_bis();
    exercice5_ter();
    exercice6();

    return 0;
}
