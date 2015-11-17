#include <stdio.h>
#include <stdlib.h>

typedef struct Node
{
	int value;
	struct Node** next;
} Node;

Node* createNode(int value){
	Node *root;
	root->value = value;
	root->next = malloc(sizeof(Node));
	root->next = NULL;
	return root;
}

void insert(Node *node,int value){
	while(node->next!=NULL){
		node = node->next;
	}
	Node *new = createNode(value);
	node->next = new;
}

int main(){	
	struct Node *root = createNode(0);
	int test[5] = {1,2,3,4,5};
	for (int i=0;i<5;i++){
		insert(root,test[i]);	
	}
}
