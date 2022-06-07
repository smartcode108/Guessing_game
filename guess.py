secret_word = "cook"
guess = ""
guess_count = 0
guess_limit = 3
Out_of_guess = False



while guess != secret_word and not(Out_of_guess):
    if guess_count < guess_limit:
        guess = input("Enter a guess: ")
        guess_count += 1
    else:
        Out_of_guess = True

if Out_of_guess:
    print("Out of guess, you lose!")
else:
    print("You Win")

