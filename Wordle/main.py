# Data for the five letter words has been aquired from previous WORDLE games
# (real) WORDLE available at https://www.nytimes.com/games/wordle/index.html
# Dataset taken from https://www.rockpapershotgun.com/wordle-past-answers

import random
from pathlib import Path

from colorama import Fore, Style  # type: ignore

path_To_Words = Path(__file__).with_name("fiveletterwords.txt")

game_Counter = 0


# Searches database for a word matching user input
def search_Word_Func(user_Word):
    try:
        with path_To_Words.open("r") as database:
            content = {line.strip().upper() for line in database}
            return user_Word.upper() in content
    except FileNotFoundError:
        print("Error: Word database file not found!")
        return False


# Accepts user input and checks it's validity
def check_User_Input():
    while True:
        try:
            user_Word = input("Write your guess here: ").strip()
            if len(user_Word) != 5:
                raise ValueError("Word must be exactly 5 letters long.")
            if not user_Word.isalpha():
                raise ValueError("Word must contain only letters A-Z.")
            if not search_Word_Func(user_Word):
                raise TypeError("Word doesn't exist in the database.")
            return list(user_Word.upper())
        except ValueError as e:
            print(f"\nWrong input: {e}\n")
        except TypeError as e:
            print(f"\nWrong input: {e}\n")


# Logic of the game
def play_Round():
    global game_Counter
    game_Counter += 1
    print("Game Counter: ", game_Counter)

    with path_To_Words.open("r") as words:
        content = words.readlines()
        total_Word_Count = len(content)
        words.close()
    random_Number = random.randint(0, total_Word_Count - 1)
    game_Word = content[random_Number]
    game_Word_Characters = list(game_Word[:-1])
    print(game_Word_Characters)
    print(
        "\nWelcome to WORDLE!\nYour word: _ _ _ _ _\n\nGuess 1 / 7",
    )
    user_Guess_Count = 1
    user_Word_Characters = check_User_Input()
    wrongly_Guessed_Characters = []
    while True:
        correct_Guessed_Characters = 0
        duplicate_Characters = []
        already_Guessed_Characters = []
        for i in range(5):
            if game_Word_Characters[i] == user_Word_Characters[i]:
                print(Fore.GREEN + game_Word_Characters[i] + Style.RESET_ALL, end=" ")
                correct_Guessed_Characters += 1
                already_Guessed_Characters.append(user_Word_Characters[i])
                print("green", already_Guessed_Characters)
            elif (
                user_Word_Characters[i] in game_Word_Characters
                and user_Word_Characters[i] not in already_Guessed_Characters
            ):
                print(Fore.YELLOW + user_Word_Characters[i] + Style.RESET_ALL, end=" ")
                already_Guessed_Characters.append(user_Word_Characters[i])
                print("yellow", already_Guessed_Characters)
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
                        "Word doesn't contain these letters: ",
                        wrongly_Guessed_Characters,
                    )
                print("Round:", user_Guess_Count, "/ 7")
                user_Word_Characters = check_User_Input()
            else:
                print("Error! Restarting game")
                break
        elif correct_Guessed_Characters == 5:
            print("\nYou won!")
            break


# main function which calls the play_Round function
def main():
    play_Round()
    while True:
        resp = input("Would you like to play another round? (y/n)\n")
        if resp.lower() == "y" or len(resp) == 0:
            play_Round()
        elif resp.lower() == "n":
            print("Thanks for playing")
            print(f"Total rounds played: {game_Counter}")
            break
        else:
            print("Please input Y/n")


if __name__ == "__main__":
    main()

# TODO
# Remove showing letter when its already guessed and doesnt appear a second time
