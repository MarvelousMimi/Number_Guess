# Number guessing game
# Store an number
# Ask the user to make a guess
# Check if the guess is the same as the number
# If true, the player wins, game over!
# Else, give the user some hints

our_fav_number = 23

user_guess = input("Enter your guess: ")

user_guess = float(user_guess)
print((user_guess))

if user_guess == our_fav_number:
     print("Success, You guessed the numnber! Our favorite number is: " + str(our_fav_number))
if user_guess < our_fav_number:
    print('Your guess is too low, Try a little higher') 
if user_guess > our_fav_number:
    print('Your guess is too high, Try a little lower')  
