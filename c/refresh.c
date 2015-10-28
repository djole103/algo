#include <stdio.h>
void writer(char** arr){
	/*int length = sizeof(arr)/(10*sizeof(char));
	for(int i=0;i<length;i++){
		printf("func: %i\n",arr[i]);
	}*/
	while(*arr){
		while(*arr[0]){
			putchar(*arr[0]++);
			putchar('\n');
		}
		*arr++;
	}
}

int main(int argc, char *argv[]){
	for (int i=1;i<argc;i++){
		printf("arg %d: %s\n", i, argv[i]);
	}
	writer(argv);
	return 1;
}
