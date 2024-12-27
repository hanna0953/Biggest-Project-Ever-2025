# Data for the five letter words has been aquired from previous WORDLE games
# (real) WORDLE available at https://www.nytimes.com/games/wordle/index.html
# Dataset taken from https://www.rockpapershotgun.com/wordle-past-answers
import random
import re
from pathlib import Path

from colorama import Fore, Style


def check_User_Input():
    while True:
        try:
            user_Word = input("Write your guess here: ")
            if len(user_Word) != 5:
                raise ValueError
            elif not re.match(r"^[A-Za-z]+$", user_Word):
                raise Exception
            user_Word_Characters = list(user_Word.upper())
            return user_Word_Characters
        except ValueError:
            print("\nWrong input, your word should be 5 letters long!\n")
        except Exception:
            print("\nWrong input, please write only letters A-Z\n")


# Random word generation and converts it to a list of characters
path_To_Words = Path(__file__).with_name("fiveletterwords.txt")
with path_To_Words.open("r") as words:
    content = words.readlines()
    total_Word_Count = len(content)
    words.close()
random_Number = random.randint(0, total_Word_Count - 1)
game_Word = content[random_Number]
game_Word_Characters = list(game_Word[:-1])
print(game_Word_Characters)

print("\nWelcome to WORDLE!\nYour word: _ _ _ _ _\n\n")
user_Guess_Count = 1
user_Word_Characters = check_User_Input()
wrongly_Guessed_Characters = []
while True:
    correct_Guessed_Characters = 0
    for i in range(5):
        if game_Word_Characters[i] == user_Word_Characters[i]:
            print(Fore.GREEN + game_Word_Characters[i] + Style.RESET_ALL, end=" ")
            correct_Guessed_Characters += 1
        elif user_Word_Characters[i] in game_Word_Characters:
            print(Fore.YELLOW + user_Word_Characters[i] + Style.RESET_ALL, end=" ")
        else:
            print(Fore.RED + "_" + Style.RESET_ALL, end=" ")
            if user_Word_Characters[i] not in wrongly_Guessed_Characters:
                wrongly_Guessed_Characters.extend(user_Word_Characters[i])
    if correct_Guessed_Characters != 5:
        print("WRONG GUESS")
        if len(wrongly_Guessed_Characters) > 0 and user_Guess_Count < 7:
            print("Word doesn't contain these letters: ", wrongly_Guessed_Characters)
            user_Guess_Count += 1
            user_Word_Characters = check_User_Input()
        else:
            print("You lost!")
            break
    elif correct_Guessed_Characters == 5:
        print("\nYou won!")
        break

# TODO
# remove showing letter when its already guessed and doesnt appear a second time
# Loop game
# Count rounds
# Check if word exists in database, dont take words that dont exist
