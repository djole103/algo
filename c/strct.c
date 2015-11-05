#include <stdio.h>
#include <string.h>

struct Dog {
	char name[20];
	char breed[20];
};

int main(){
	struct Dog rex;
	strcpy( rex.name, "Rex");
	strcpy( rex.breed, "Pitbull");
	printf("%s", rex.name);
	return 1;
}
