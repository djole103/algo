#include <stdio.h>
#include <string.h>

struct Dog {
	char name[20];
	char breed[20];
	int id;
};

struct Dog dog_factory(char[20] name, char[20] breed,int id){
	struct Dog newDog;
	strcpy(newDog.name,name);
	strcpy(newDog.breed,breed);
	newDog.id = id;
	return newDog;
} 

/*void dog_kill(struct* Dog){
free memory	
}*/

int main(){
	struct Dog rex;
	strcpy( rex.name, "Rex");
	strcpy( rex.breed, "Pitbull");
	printf("%s\n", rex.name);
	
	struct Dog zeus;
	zeus = dog_factory("Zeus", "Shiba Inu",1);
	printf("%s\n",zeus.name);
	return 1;
}
