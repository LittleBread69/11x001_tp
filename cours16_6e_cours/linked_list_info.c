/* Linked lists: an laternative to arrays where adding an item (node) is efficient

In particular: items (nodes) are stored at individual memory addresses instead of octets after octets.
*/

#include <stdio.h>
#include <stdlib.h>

//recursive definition of a node

struct Node
{
    float val;
    struct Node *next;
};

typedef struct Node node;

typedef struct {
    node *head;
} list;

// create an empty list
list *create_list(){
    list *l = (list *)malloc(sizeof(list));
    l->head = NULL;
    return l;
}

//delete one node and those following it (recusive function)
void delete_nodes(node *n){
    if (n){
        node *nxt = n->next;
        free(n);
        delete_nodes(nxt);
    }
}

//delete list
void delete_list(list *l){
    delete_nodes(l->head);
    free(l);
}

//addinf a value
void add_value(list *l, float x){
    node *n;
    n = (node *)malloc(sizeof(node));
    n->val = x;
    n->next = l->head;

    l->head = n;
}


//length of linked list
int length_nodes(node *n){
    if (n) {
        return 1 + length_nodes(n->next);
    }
    else {
        return 0;
}
}

int length_recursive(list *l){
    return length_nodes(l->head);
}

int length_iterative(list *l){
    int len = 0;
    for (node *n = l->head; n; n = n->next){
        len++;
    }
    return len;
}

//merging lists
list *merge_lists(list *l, list *m){
    //1. find the last element/node of the list l
    node *d = l->head;
    if (d){ //not NULL
        while (d->next) d = d-> next;

        //2. update the pointer of the last element to head of 2nd list
        d->next = m->head;
        return l;
    }
    
}

/***** MAIN *****/
int main(void){

    list *l = create_list();

    add_value(l, 0.0);

    for (int k=0; k<10; k++) add_value(l, k);

    for (node *n = l->head; n; n = n->next){
        printf("%f\n", n->val);
    }

    //free space when no longer needed !
    //delete_list(l);

    //length of a list
    //version 1: recusrive claculation
    int len_rec = length_recursive(l);
    printf("len_rec=%d\n", len_rec);
    int len_iter = length_iterative(l);
    printf("len_iter=%d\n", len_iter);

    list *second_list = create_list();
    for (int k = 10; k < 20; k++) add_value(second_list, k);

    second_list = merge_lists(second_list, l);

    for (node *n = second_list->head; n; n = n->next){
        printf("%f\n", n->val);
    }

    return 0;
}