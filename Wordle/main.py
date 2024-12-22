# Data for the five letter words has been aquired from previous WORDLE games
from pathlib import Path
import re
import random

user_Player_Count = 0

path_To_Words = Path(__file__).with_name('fiveletterwords.txt')
with path_To_Words.open('r') as words:
    content = words.readlines()
    total_Word_Count = len(content)
    random_Number = random.randint(0, total_Word_Count - 1)
    game_Word = content[random_Number]
    print(game_Word)
    words.close()

print("\nWelcome to WORDLE!\nYour word: _ _ _ _ _\n\n")

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

#list(user_Word)