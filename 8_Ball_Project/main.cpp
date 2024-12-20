#include <iostream>
#include <string.h>
using namespace std;

int main() {
  string user_Input;
  srand(time(0));
  int randomNum = rand() % 20 + 1;

  cout << "Welcome to 8Ball!\nPlease write your question here: ";
  cin >> user_Input;

  return 0;
} 