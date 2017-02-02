#include <fstream>
#include <stdio.h>
#include <string>
#include <iostream>

//namespace test {

class PrintFile {
public:
  //PrintFile();
  std::ifstream file;

  // Opens the file at *filepath*
  //
  // Returns TRUE if file is successfully opened for reading, and FALSE otherwise. 
  bool open(const char *filepath){
    file.open(filepath);
    if (file.is_open()) return true;
    else return false;
  }
  

  // Prints the contents of the open file to *stream*
  void print(std::ostream &stream){
    std::string line;
    while(std::getline(file, line)){
      //std::istringstream iss(line);
      stream << line;
    } 
  } 

};

//} // namespace test

int main(){
  PrintFile pf; //= PrintFile();
  char filename[] = "txt.txt";
  pf.open(filename);

  std::ostream stream(nullptr); // useless ostream (badbit set)
  stream.rdbuf(std::cout.rdbuf()); // uses cout's buffer

  pf.print(stream);
}
