#include <iostream>
using namespace std;

int main(){

  int number;
  cout << "Enter an integer: ";
  cin >> number;
bool valid = cin.good();
char next = cin.get();
bool endOfInt = ((next == ' ') || (next == '\n'));


  if (valid && endOfInt) { 
cout << "The integer you have entered is " << number;
  } else {
    cerr << "Error: Invalid input.";
  }

  return 0;
}

	
