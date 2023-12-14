import random

password_length_int = False
password = []
password_string = ""

guess_int = False
guess = []
guess_string = ""

tries = 0

while password_length_int == False:
    try:
        password_length = input("How long should the password be? ")
        password_length = int(password_length)
    except:
        print("Please enter an integer")
    else:
        password_length_int = True

password_len = 0
for length in range(password_length):
    password_len+=1
    password.insert(password_len, int(random.randint(0,9)))

for digit in password:
    password_string+=str(digit)

while password_string != guess_string:
    tries+=1

    guess_int = False
    guess = []
    guess_string = ""
    while guess_int == False:
        try:
            guess_input = input("Guess the password ")
            guess_input = int(guess_input)
            if len(str(guess_input)) != len(password_string):
                print("It has to be the correct length of " + str(password_length) + " digits long")
                continue
        except:
            print("It has to be an integer")
        else:
            guess_int = True
    
    guess_length = 0
    for digit in str(guess_input):
        guess_length+=1
        guess.insert(guess_length, int(digit))

    for digit in guess:
        guess_string+=str(digit)

    correct_digit = 0
    correct_place = 0

    for digit in range(len(guess)):
        guess_digit = guess[digit]
        password_digit = password[digit]

        if guess_digit == password_digit:
            correct_place+=1

        if guess_digit in password:
            correct_digit+=1

    print("You have " + str(correct_digit) + " correct digit(s), " + str(correct_place) + " of which are in the correct place")
    
else:
    print("Well done you guessed the word in " + str(tries) + " tries")
    
