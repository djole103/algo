#include<stdio.h>
#include<math.h>

void inttostr(int num){
	int strMap[10] = {'0','1','2','3','4','5','6','7','8','9'};
	int digit;
	int lengthString = ceil(log(num));
	char result[lengthString];
	int i =0;
	while(num){
		digit = num % 10;
		num = floor(num/10);
		result[i] = strMap[digit];
		i++;
	}
	for(i;i>0;i--) printf("%c",result[i-1]);
}

int main(){
	int test = 123;
	inttostr(test);
	return 1;
}
