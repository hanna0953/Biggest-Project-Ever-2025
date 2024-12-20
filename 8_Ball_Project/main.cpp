#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main() {
  srand(time(0));
  int randomNum = rand() % 20 + 1;
  string user_Input;
  


  cout << "\nWelcome to 8Ball!\n\nPlease write your question here: ";
  cin >> user_Input;
  
  

  return 0;
} 