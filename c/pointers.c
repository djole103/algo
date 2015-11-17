#include <stdio.h>
#include <stdlib.h>

typedef struct Ok{
	int* d;
} Ok;

int main(){
	int* a = malloc(sizeof(int));
	//int* a;
	*a = 5;
	/*printf("%d",*a);
	int b = 6;
	int* c = &b; 
	printf("%d",*c);*/
	Ok *ok;
	ok->d = a;
	printf("%d",*(ok->d));
	return 1;
}
