#include <stdio.h>

int twosum(int* nums,int length, int goal){
	if (nums[0] == NULL) return 0;
	int start = 0;
	int end = length;
	while(start < end){
		//printf("START: %i END: %i",start,end);
		if (nums[start] + nums[end] > goal) end--;
		else if (nums[start] + nums[end] < goal) start++;
		else{
			//printf("%i %i",start,end);
			return 1;
		}
	}
	return 0;
	
}

int main(){
	int result;
	int goal = 10;
	int test[5] = {2,4,6,7,9};
	int length =  sizeof(test)/sizeof(test[0]) -1;
	result = twosum(test,length,goal);
	if(result) printf("YES");
	else printf("NO");

	return 1;
}
