#include <vector>
#include <iostream>
#include <thread>

void sort(std::vector<int>* v){
  std::sort(v -> begin(), v -> end()); //, std::greater<int>());
}

void vec_sort(std::vector<int>* v1, std::vector<int>* v2, std::vector<int>* v3){
  std::thread t1(&sort, v1);
  std::thread t2(&sort, v2);
  std::thread t3(&sort, v3);

  t1.join();
  t2.join();
  t3.join();
}

int main(){
  std::vector<int> v1 = {2,1,3};
  std::vector<int> v2 = {2,5,3};
  std::vector<int> v3 = {1,2,3};

  vec_sort(&v1, &v2, &v3);


 for(std::vector<int>::iterator iter = v1.begin(); iter != v1.end(); ++iter){
   std::cout << *iter;
 }

}
