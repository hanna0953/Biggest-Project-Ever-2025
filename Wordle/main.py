from pathlib import Path
# Data for the five letter words has been aquired from previous WORDLE games
user_Player_Count = 0
path_To_Words = Path(__file__).with_name('fiveletterwords.txt')
with path_To_Words.open('r') as words:
    total_Word_Count = len(words.readlines())
    print(total_Word_Count)
# while 1:
# print(total_Word_Count)

