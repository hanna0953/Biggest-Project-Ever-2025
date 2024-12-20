#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main() {
  srand(time(0));
<<<<<<< HEAD
  int randomNum = rand() % 20 + 1;
  string user_Input;
  
=======

  ifstream file("answers.txt"); // Open the file 
  if (!file) 
  { 
    cerr << "Unable to open file answers.txt\n"; 
    return 1; // Exit if the file cannot be opened 
  } 

  string line;
  int current_Line = 0;
>>>>>>> refs/remotes/origin/main
  cout << "\nWelcome to 8Ball!\n\nPlease write your question here: ";
  cin >> user_Input;

 // Read the file line by line 
  while (getline(file, line)) {
      current_Line++; 
      if (current_Line == randomNum) 
      {
          cout << "Answer: " << line << endl; 
          break; // Exit the loop once the desired line is found 
      } 
   } 
  return 0;
  //test123
} 