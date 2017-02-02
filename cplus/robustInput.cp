#include <iostream>
using namespace std;

int main(){

  int number;
  cout << "Enter an integer: ";
  cin >> number;
  bool valid = cin.good();

  if (valid) {
    char next = cin.get();
    bool endOfInt = ((next == ' ') || (next == '\n'));
    cout << "The integer you have entered is " << number;
  } else { 
    char next = cin.get();
    bool endOfInt = (next == '.');
    cerr << "Error: Invalid input.";
  }

  return 0;
}

	
