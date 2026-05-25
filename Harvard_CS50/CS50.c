#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>


typedef struct{
    string name;
    string number;
}
person;

typedef struct node{
    int number;
    struct node *next;
}
node;


int calculator(int num1, int num2);
float discount(float price);
int mario(void);
int contacts(void);
int address(void);
int copy(void);
int memory(void);
void swap(int *a, int *b);
void scanning(void);
int list(void);


int main(void){
    list();
}


int calculator(int num1, int num2){
    return num1 + num2;
}

float discount(float price){
    return price * 0.85;
}

int mario(void){
    int n;

    do{
        n = get_int("Width: ");
    }
    while(n < 1);

    for (int i = 0; i < n; i++){
       printf("?");
    }
    printf("\n");
}

int contacts(void){
    person people[2];
    people[0].name = "Carter";
    people[0].number = "+1-617-495-1000";

    people[1].name = "David";
    people[1].number = "+1-949-468-2750";

    for (int i = 0; i < 2; i++){
        if (strcmp(people[i].name, "David") == 0){
            printf("Found %s\n", people[i].number);
            return 0;
        }
    }
    printf("Not found\n");
    return 1;
}

int address(void){
    int n = 50;
    int *pointer = &n;
    printf("The address is: %p\n", pointer);
    return 0;
}

int copy(void){
    char *s = get_string("s: ");
    char *t = malloc(strlen(s) + 1);
    
    if (t == NULL){
        return 1;
    }

    strcpy(t, s);

    if (strlen(t) > 0){
        t[0] = toupper(t[0]);
    }

    printf("s: %s\n", s);
    printf("s: %s\n", t);

    free(t);

    return 0;
}

int memory(void){
    int *x = malloc(3 * sizeof(int));
    
    x[0] = 72;
    x[1] = 73;
    x[2] = 74;
    
    free(x);

    return 0;
}

void swap(int *a, int *b){
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

void scanning(void){
    char *s[4];
    printf("s: ");
    scanf("%s", s);
    printf("s: %s\n", s);
}

int list(void){
    // List of size 0
    node *list = NULL;

    // Add a number to list
    node *n = malloc(sizeof(node));
    if (n == NULL){
        return 1;
    }
    n->number = 1;
    n->next = NULL;

    // Update list to point to new node
    list = n;

    // Add a number to list
    n = malloc(sizeof(node));
    if (n == NULL){
        free(list);
        return 1
    }
    n->number = 2;
    n->next = NULL;
    list->next = n;

    // Add a number to list
    n = malloc(sizeof(node));
    if (n==NULL){
        free(list->next);
        free(list);
        return 1;
    }
    n->number = 3;
    n->next = NULL;
    list->next->next = n;

    // Print numbers
    for (node *tmp = list; tmp != NULL; tmp->next){
        printf("%i\n", tmp->number);
    }

    // Free list
    while (list != NULL){
        node *tmp = list->next;
        free(list);
        list = tmp;
    }
    
    return 0;
}
