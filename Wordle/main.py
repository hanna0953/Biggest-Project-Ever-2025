# Data for the five letter words has been aquired from previous WORDLE games
# (real) WORDLE available at https://www.nytimes.com/games/wordle/index.html
# Dataset taken from https://www.rockpapershotgun.com/wordle-past-answers
import random
import re
from pathlib import Path

from colorama import Fore, Style  # type: ignore

path_To_Words = Path(__file__).with_name("fiveletterwords.txt")

def search_Word_Func(user_Word):
    try:
        with path_To_Words.open("r") as database:
            content = {line.strip().upper() for line in database}
            return user_Word.upper() in content
    except FileNotFoundError:
        print("Error: Word database file not found!")
        return False

def check_User_Input():
    while True:
        try:
            user_Word = input("Write your guess here: ").strip() # strip works very nice with accident spacebar input
            if len(user_Word) != 5:
                raise ValueError("Word must be exactly 5 letters long.")
            if not user_Word.isalpha():
                raise ValueError("Word must contain only letters A-Z.") # sometimes shows instead of search_Word_Func error, for example word: REACH
            if not search_Word_Func(user_Word):
                raise TypeError("Word doesn't exist in the database.")
            return list(user_Word.upper())
        except ValueError as e:
            print(f"\nWrong input: {e}\n")
        except TypeError as e:
            print(f"\nWrong input: {e}\n")

# Random word generation and converts it to a list of characters
# path_To_Words = Path(__file__).with_name("fiveletterwords.txt") # Probably not needed cuz its above now
with path_To_Words.open("r") as words:
    content = words.readlines()
    total_Word_Count = len(content)
    words.close()
random_Number = random.randint(0, total_Word_Count - 1)
game_Word = content[random_Number]
game_Word_Characters = list(game_Word[:-1])
print(game_Word_Characters)

print("\nWelcome to WORDLE!\nYour word: _ _ _ _ _\n\nRound 1 / 7")
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
        user_Guess_Count += 1
        if user_Guess_Count > 7:
            print("You lost!")
            break
        elif user_Guess_Count <= 7:
            if len(wrongly_Guessed_Characters) > 0:
                print(
                    "Word doesn't contain these letters: ", wrongly_Guessed_Characters
                )
            print("Round:", user_Guess_Count, "/ 7")
            user_Word_Characters = check_User_Input()
        else:
            print("Error! Restarting game")
            break
    elif correct_Guessed_Characters == 5:
        print("\nYou won!")
        break

# TODO
# Remove showing letter when its already guessed and doesnt appear a second time
# Loop game
# Count rounds
# Improve search_Word_Func, especially why it shows the wrong error on word REACH or FREAK