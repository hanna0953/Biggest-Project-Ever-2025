# Data for the five letter words has been aquired from previous WORDLE games 
# available at https://www.nytimes.com/games/wordle/index.html
from colorama import Fore, Style
from pathlib import Path
import re
import random

user_Round_Count = 0

# Random word generation and converts it to a list of characters
path_To_Words = Path(__file__).with_name('fiveletterwords.txt')
with path_To_Words.open('r') as words:
    content = words.readlines()
    total_Word_Count = len(content)
    words.close()  
random_Number = random.randint(0, total_Word_Count - 1)
game_Word = content[random_Number]
game_Word_Characters = list(game_Word[:-1])
print(game_Word_Characters)

print("\nWelcome to WORDLE!\nYour word: _ _ _ _ _\n\n")

# Makes user add his word and checks if it's 5 letters
while True:
    try:
        user_Word = input('Write your guess here: ')
        if len(user_Word) != 5:
            raise ValueError
        elif not re.match(r"^[A-Za-z]+$", user_Word):
            raise Exception
        break 
    except ValueError:
        print("\nWrong input, your word should be 5 letters long!\n")
    except Exception:
        print("\nWrong input, please write only letters A-Z\n")

# Converts user input to Uppercase 
user_Word_Characters = list(user_Word.upper())
# print(user_Word_Characters)

# Check for similarities between Game Word and User Word
matches = [i for i in game_Word_Characters if i in user_Word_Characters]
for i in range(5):
    try:
        if i < 4:
            print(matches[i], end=" ")
        else:
            print(matches[i])
    except IndexError:
        if i < 4:
            print("_ ", end=" ")
        else:
            print("_ ")

# Colors for letters (for future)
print(Fore.YELLOW + 'Color for good letters on wrong spot')
print(Fore.GREEN + 'Color for good letters on good spot')
print(Style.RESET_ALL)

# TO DO 
# Add an array for wrong letters
# For example if user guessed "A" and it was wrong do:
# B C D E F G H I J K L M N O P Q R S T U V W X Y Z 