#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/****************************/
/* Vos fonctions ci-dessous */ 
/****************************/

// EXERCICE 2

struct Cell;
struct Cell {
    int val;
    struct Cell *suivante;
};
typedef struct Cell cell;
typedef struct {
    cell *premiere;
} liste;

liste *cree_liste() {
    liste *l = (liste*)malloc(sizeof(liste));
    l->premiere = 0;
    return l;
}

void ajoute_valeur(liste *l, int x) {
    cell *c;
    c = (cell*)malloc(sizeof(cell));
    c->val = x;
    c->suivante = l->premiere;
    l->premiere = c;
}

void detruit_cell(cell* c)
{
	if (c->suivante != 0)
		detruit_cell(c->suivante);
	free(c);
}

void detruit_liste(liste* l)
{
	if (l != 0)
		detruit_cell(l->premiere);
	free(l);
}

// EXERCICE 3

typedef struct {
    int num_lignes, num_colonnes;
    float **index_lignes;
} matrice;

matrice *cree_matrice(int num_lignes, int num_colonnes) {
    matrice *m;
    m = (matrice*)malloc(sizeof(matrice));
    m->num_lignes = num_lignes;
    m->num_colonnes = num_colonnes;
    m->index_lignes = (float**)malloc(num_lignes * sizeof(*(m->index_lignes)));
    for (int i = 0; i < num_lignes; i++) {
        (m->index_lignes)[i] = (float*)malloc(num_colonnes * sizeof(float));
    }
    return m;
}

void detruit_matrice(matrice *m) {
    for (int i = 0; i < m->num_lignes; i++) {
      free(m->index_lignes[i]);
    }
    free(m->index_lignes);
    free(m);
}

void randomize_matrice(matrice *m) {
    for (int i = 0; i < m->num_lignes; i++) {
      for (int j = 0; j < m->num_colonnes; j++) {
        m->index_lignes[i][j] = 2 * (float) rand() / (float) RAND_MAX - 1;
      }
    }
}

void affiche_matrice(matrice *m) {
    for (int i = 0; i < m->num_lignes; i++) {
      for (int j = 0; j < m->num_colonnes; j++) {
        printf("%.2f ", m->index_lignes[i][j]);
      }
      printf("\n");
    }
}

void insere_valeur_matrice(matrice *m, float valeur, int i, int j) {
    m->index_lignes[i][j] = valeur;
}

void norme_l2_matrice(matrice *m) {
    float s = 0;
    for (int i = 0; i < m->num_lignes; i++) {
      for (int j = 0; j < m->num_colonnes; j++) {
        s += m->index_lignes[i][j] * m->index_lignes[i][j];
      } 
    }
    printf("Norme L_2 matrice : %.2f", sqrt(s)); // add "-lm" in the command line to compile
}

int min(int a, int b)
{
	return a < b ? a : b;
}

void redimensionne_matrice(matrice *m, int nouveau_num_lignes, int nouveau_num_colonnes) {
    float **index_lignes = (float**)malloc(nouveau_num_lignes * sizeof(*m->index_lignes));
    for (int i = 0; i < nouveau_num_lignes; i++) {
      index_lignes[i] = (float*)malloc(nouveau_num_colonnes * sizeof(float));
    }

	//Pour la copie, on calcule le minimum entre l'ancienne et la nouvelle taille
	//Car on ne sait pas si on rend la matrice plus grande ou plus petite
	int min_lignes = min(m->num_lignes, nouveau_num_lignes);
	int min_colonnes = min(m->num_colonnes, nouveau_num_colonnes);
	for (int i = 0; i < min_lignes; i++){
		for (int j = 0; j < min_colonnes; j++)
			index_lignes[i][j] = m->index_lignes[i][j];
	}

    for (int i = 0; i < m->num_lignes; i++) {
      free(m->index_lignes[i]);
    }
    free(m->index_lignes);
    m->index_lignes = index_lignes;
    m->num_lignes = nouveau_num_lignes;
    m->num_colonnes = nouveau_num_colonnes;
}

/****************************/
/* Vos fonctions ci-dessus **/
/****************************/

void exercice1(void) {
    printf("\n\nEXERCICE 1\n\n");

    /******************** Votre code ci-dessous ********************/
    int n; // pile
    printf("Entrer le nombre de carrés à afficher : ");
    scanf("%d", &n);

    // allocation dynamique (= sur le tas)
    // retourne un pointeur (sur la pile) contenant 
    // l'adresse du debut de la zone alouée sur le tas.
    int* carres = (int*)malloc(n * sizeof(int));
    
    for (int i = 0; i < n; i++) {
        *(carres + i) = i * i;
    }

    for (int i = 0; i < n; i++) {
        printf("%d: %d\n", i, carres[i]);
    }

    free(carres); // on libère l'espace aloué sur le tas
    /******************** Votre code ci-dessus *********************/

    return;
}

void exercice2(void) {
    printf("\n\nEXERCICE 2\n\n");

    /******************** Votre code ci-dessous ********************/
    liste *l = cree_liste();

    int arr[] = {9, 19, 8, 3, 7, 11, 0, 22, 14, 3};

    for (int i=0; i < sizeof(arr) / sizeof(int); i++) {
      ajoute_valeur(l, arr[i]);
    }

    float sum = 0;
    int nb_elem = 0;
    for(cell *c = l->premiere; c; c = c->suivante) {
      sum += c->val;
      nb_elem++;
    }
    float moyenne = sum / nb_elem;

    printf("Moyenne: %.2f\n", moyenne);
    detruit_liste(l);
    /******************** Votre code ci-dessus *********************/

    return;
}

void exercice3(void) {
    printf("\n\nEXERCICE 3\n\n");

    /******************** Votre code ci-dessous ********************/
    matrice *m = cree_matrice(5, 7);
    randomize_matrice(m);
    //redimensionne_matrice(m, 10, 9);
    affiche_matrice(m);
    norme_l2_matrice(m);
    detruit_matrice(m);
    /******************** Votre code ci-dessus *********************/

    return;
}

int main(void) { 
  // Pour l'exercice 3, pour utiliser sqrt, il faut compiler avec cette commande : clang main_corrige.c -o main -lm
    exercice1();
    exercice2();
    exercice3();
    return 0;
}

