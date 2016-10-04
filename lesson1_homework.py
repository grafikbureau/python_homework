# First "hard-code" some number in the program (write the number into a variable). You can call this variable secret.
# Then the user has to find out what this number is (using raw_input). Store user's guess in a variable called guess.
# Check if your secret is equal to user's guess.
# If the user's guess is wrong, let him/her know that (use print and if/else).
# If the user's guess is correct, congratulate him/her.

secret = 5

guess = int(raw_input("Guess: "))

if guess == secret:
    res = "Congratulation"

else: res = "Sorry, wrong guess. Try again!"

print res