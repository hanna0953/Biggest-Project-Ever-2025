# Data for the five letter words has been aquired from previous WORDLE games
from pathlib import Path
import random

user_Player_Count = 0
path_To_Words = Path(__file__).with_name('fiveletterwords.txt')
with path_To_Words.open('r') as words:
    content = words.readlines()
    total_Word_Count = len(content)
    random_Number = random.randint(0, total_Word_Count - 1)
    print (content[random_Number])
    words.close()  



