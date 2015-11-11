#include <stdio.h>

struct Person {
	int age;
	char name[20];
};

struct Person factoryPerson(int age,char* name){
	struct Person p;
	p.age = age;
	strcpy(p.name,name);
	return p;
}

struct Parent {
	struct Person super;
	struct Child* child;	
};

struct Child {
	struct Person super;
	struct Parent* parent;	
};


int main(){
	int* a;
	int* b;
	struct Person tony = factoryPerson(35,"Tony");
	struct Person abby = {21,"Abby"};
	printf("%s\n", abby.name);

	struct Parent ttony = {tony};
	struct Child aabby = {abby,&ttony};
	ttony.child = &aabby;
	printf("%s\n",ttony.child->super.name);
	return 1;
}
