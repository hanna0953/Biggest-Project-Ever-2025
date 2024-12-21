user_Word = input("Write your guess here: ")
if user_Word == 5:
    print("Your guess: " + user_Word)
elif not re.match(r"^[A-Za-z]+$", user_Word):
    print("\nWrong input, please write only letters A-Z\n")
else:
    print("\nWrong input, your word should be 5 letter long!\n")
