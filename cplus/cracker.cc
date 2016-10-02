#include <iostream>
#include <string>
#include <vector>
using namespace std;

const int CHARS = 92;
const int ASCII_OFFSET = 32;
const int MAX_LENGTH = 5;
string PASSWORD; 

bool check_correct(char pw_guess[]){
  if(string(pw_guess) == PASSWORD){
    cout << "hahah we kno ur password its " << string(pw_guess) << endl;
    return true;
  }
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
  return false; //really shouldn't reach here
}

int main(){
  char password[MAX_LENGTH];
  std::cout << "Enter password of max length:" << MAX_LENGTH <<endl;  
  std::cin >> password;
  PASSWORD = string(password);
  if(crack_max_length(MAX_LENGTH)){
    cout << "holy shit we cracked it we're such hackerz hahah hdkfhsj" << endl; 
  } else {
    cout << ":( sade day in hacker town" << endl;
  }
  return 1;
}
