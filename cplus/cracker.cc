#include <iostream>
#include <string>
#include <fstream>
#include <chrono>
#include <ctime>
using namespace std;

const int CHARS = 92;
const int ASCII_OFFSET = 32;
const int MAX_LENGTH = 5;
string PASSWORD; 

bool check_correct(string pw_guess){
  if(pw_guess == PASSWORD){
    cout << "hahah we kno ur password its " << string(pw_guess) << endl;
    return true;
  }
  return false;
}

bool crack_w_dict(int max_length){
  ifstream common_pws;
  string pw_guess;
  common_pws.open("/Users/djole/code/algo/cplus/pw_dictionary");
  while(getline(common_pws, pw_guess)){
    if(check_correct(string(pw_guess))){
      cout << "hahah ur pw 2 basic bro its " << string(pw_guess) << endl;
      common_pws.close();
      return true;  
    }
  }
  common_pws.close();
  return false;
}

bool crack(char passw[], int position, int length){
  if (position > length){
    return check_correct(passw); 
  } else {
    for(int i=0;i< CHARS;i++){
      passw[position] = ASCII_OFFSET + i; 
      passw[position+1] = '\0';
      if (crack(passw, position+1, length)){
        return true; 
      } 
    }
    return false;
  }
}

bool crack_max_length(int length){
  char pw[length];
  for(int i=0;i<length;i++){
    cout << "Trying to crack with length:" << i << endl;
    if(crack(pw, 0, i)){
      return true; 
    } 
  }
  return false; //really shouldn't reach here ever
}

int main(){
  char password[MAX_LENGTH];
  std::cout << "Enter password of max length:" << MAX_LENGTH <<endl;  
  std::cin >> password;
  PASSWORD = string(password);

  clock_t start;
  start = clock();
  if(crack_max_length(MAX_LENGTH)){
    cout << "holy shit we cracked it we're such hackerz hahah hdkfhsj" << endl; 

    clock_t total_time = 1000 * (finish - start) / CLOCKS_PER_SEC;
    cout << "Cracked in: " << total_time << " ms" << endl;
  } else {
    cout << ":( sade day in hacker town" << endl;
  }
  clock_t finish;
  finish = clock();
  return 1;
}
