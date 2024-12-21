# Data for the five letter words has been aquired from previous WORDLE games
from pathlib import Path
import re

user_Player_Count = 0

path_To_Words = Path(__file__).with_name('fiveletterwords.txt')
with path_To_Words.open('r') as words:
    total_Word_Count = len(words.readlines())
    print("Total Words Count: ", total_Word_Count)
    words.close()

test_Word = ['BREAD']
print("\nWelcome to WORDLE!\nYour word: _ _ _ _ _\n\n")

# user_Word = input("Write your guess here: ")
# if user_Word == 5:
#     print("Your guess: " + user_Word)
# elif not re.match(r"^[A-Za-z]+$", user_Word):
#     print("\nWrong input, please write only letters A-Z\n")
# else:
#     print("\nWrong input, your word should be 5 letter long!\n")

while True:
    try:
        user_word = input('Write your guess here: ')
        if len(user_word) != 5:
            raise ValueError
        break 
    except ValueError:
        print("\nWrong input, your word should be 5 letters long!\n")

#list(user_Word)