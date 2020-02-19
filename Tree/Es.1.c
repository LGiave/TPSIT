
#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

//define tree structure
struct tree_node{
    struct tree_node* left;
    struct tree_node* right;
    int key;
    int value;
}Tree_node;

//define tree structure's functions
void insert(struct tree_node **tree, struct tree_node* new){
    if(*tree == NULL){
        *tree = new;
        (*tree)->left = NULL;
        (*tree)->right = NULL;
    }else{
        if(new->key < (*tree)->key) insert(&(*tree)->left, new);
        else if (new->key>(*tree)->key) insert(&(*tree)->right, new);
        else printf("\n|CHIAVE DUPLICATA|\n");
        
    }
        
}

struct tree_node * find_by_key(struct tree_node *tree, int key){
    if (tree == NULL) return NULL;
    else{
        if(key<tree->key) return find_by_key(tree->left, key);
        else if (key>tree->key) return find_by_key(tree->right, key);
        else return tree;
    }
}

void in_order_view(struct tree_node * tree){
    if(tree != NULL){
        in_order_view(tree->left);
        printf("|%d|\t->\t%d" , tree->key, tree->value);
        in_order_view(tree->right);
    }
}

int main(){
    
    struct tree_node * cipresso = (struct tree_node*) malloc(sizeof(struct tree_node));
    struct tree_node * quercia = (struct tree_node*) malloc(sizeof(struct tree_node));

    cipresso->key=8;
    cipresso->value=1000;
    cipresso->left=NULL;
    cipresso->right=NULL;

    quercia->key=13;
    quercia->value=89;
    
    insert(&cipresso, quercia);
    in_order_view(cipresso);
}