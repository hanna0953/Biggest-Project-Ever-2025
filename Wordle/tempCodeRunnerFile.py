while True:
    check = all(e in user_Word_Characters for e in game_Word_Characters)
    correct_Guessed_Characters = 0
    for i in range(5):
        if game_Word_Characters[i] == user_Word_Characters[i]:
            print(Fore.GREEN + game_Word_Characters[i] + Style.RESET_ALL, end=" ")
            correct_Guessed_Characters += 1
        elif check == True:
            print(Fore.YELLOW + user_Word_Characters[i] + Style.RESET_ALL, end=" ")
        else:
            print(Fore.RED + "_" + Style.RESET_ALL, end=" ")
    if correct_Guessed_Characters != 5:
        print("WRONG GUESS\n")
        user_Word_Characters = check_User_Input()
    elif correct_Guessed_Characters == 5:
        break