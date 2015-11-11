#include <stdio.h>


int fib(int n){
	if (n<1) return 0;
	if (n==1) return 1;
	int minustwo = 0;
	int minusone = 1;
	int curr;
	for(int i=3; i<=n; i++){
		curr = minusone + minustwo;
		minustwo = minusone;
		minusone = curr; 
	}
	return curr;
}


int main(){
	int n;
	printf("Enter which fib number you wnat:\n");
	scanf("%d",&n);
	int result = fib(n);
	printf("%d\n",result);
}
