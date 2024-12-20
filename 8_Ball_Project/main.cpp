#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main() {
  string user_Input;  
  int randomNum = rand() % 21;
  
  srand(time(0));

  ifstream inFile;
  inFile.open("answers.txt");

  cout << "\nWelcome to 8Ball!\n\nPlease write your question here: ";
  cin >> user_Input;
  
  

  return 0;
} 