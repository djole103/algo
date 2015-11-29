#include <math.h>
#include <stdio.h>

void split(int x,int numDigitsInX, int* result){
	result= result + (numDigitsInX-1); //this puts it at the index of last digit
	int digit;
	while(x>0){
		digit = x%10;
		*result = digit; //set value to the digit
		x = floor(x/10); //floor function from math.h
		result--; //go back to front of array so we order digits properly
	}
}

void split2(int x,int numDigitsInX,char* result){
	//basically u tell it where to do store a sprintf, the size its gunna write
	//and then provide a char array of that size so it has somewhere to put it
	//keep in mind this gives u an array of chars in "result", still have to
	//cast to int if u want to use it
	snprintf(result,sizeof(int)*numDigitsInX, "%d",x);	
}

int main(){
	int test = 123;
	int numDigits = 3;
	int result[numDigits];

	//test method 1
	split(test,numDigits,result);
	for(int i=0;i<numDigits;i++){
		printf("%d",result[i]);
	}
	//test method 2
	char result2[numDigits];
	split2(test,numDigits,result2);
	for(int i=0;i<numDigits;i++){
		printf("%c",result2[i]);
	}
}
