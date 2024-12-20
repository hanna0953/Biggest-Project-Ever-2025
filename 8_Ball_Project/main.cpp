#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main() {
  string user_Input;  
  int randomNum = rand() % 21;
  
  srand(time(0));

  ifstream file("answers.txt"); // Open the file 
  if (!file) 
  { 
    cerr << "Unable to open file answers.txt\n"; 
    return 1; // Exit if the file cannot be opened 
  } 

  string line;
  int current_Line = 0;
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
} 