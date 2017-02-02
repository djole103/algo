#include <iostream>
#include <vector>

void inc_vector(std::vector<int>* vec){
 for(std::vector<int>::iterator iter = vec -> begin(); iter != vec -> end(); ++iter){
    *iter += 1;
 } 
}

int main(){
  std::vector<int> vec = {1,2,3};
  inc_vector(&vec);

 for(std::vector<int>::iterator iter = vec.begin(); iter != vec.end(); ++iter){
   std::cout << *iter;
 }
}
