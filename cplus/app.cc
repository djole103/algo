#include <iostream>
#include <string>
#include <vector>
using std::vector;
using std::string;

/*
 *can use static string array
 *or can pass pointer
*/


//doing it with pointers and updating the actual memory
string* all_combinations(string alphabet[], string word = "", string[] results = []){
  if(alphabet.length() == 0){
    return [];
  }

  for(int i=0;i<alphabet.length();i++){
    string result = word + alphabet[i];
    results.append(result);
    all_combinations(alphabet[:i] + alphabet[i+1:], result, results);
  }

  return results;
}

int main(){
  string password;
  std::cout << "Enter password:";  
  std::cin >> password;
  return 1;
}
