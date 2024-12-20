#include <iostream>
#include <string.h>
using namespace std;

int main() {
  string user_Input;

  int randomNum = rand() % 21;
  
  srand(time(0));

  cout << "Welcome to 8Ball!\nPlease write your question here: ";
  cin >> user_Input;

  return 0;
} 