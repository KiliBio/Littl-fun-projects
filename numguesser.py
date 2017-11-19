""" numguesser.py, by KiliBio """
""" This programm lets the user guess a number between 1 and 100"""

import random

def main(): # main function
    print("Welcome to the number guesser game")
    lower_range_cut, upper_range_cut, random_number = range_func()
    total_guesses = max_guess_number(lower_range_cut, upper_range_cut)
    evaluation(random_number, total_guesses, lower_range_cut, upper_range_cut)

    # replay option, after the game has finished
    replay = input("Do you want to play again (y/n)? ")
    if replay == "y":
        print("Let's do this!")
        main()
    else:
        print("Ok, Thanks for playing!")

def range_func():   # allows user to select a range for the number guess
    print("Please select a range\n"
          "in which you would like to guess.")
    while True:
        while True:
            try:
                lower_range_cut = int(input("Lower boundary limit: "))
                break
            except ValueError:
                print ("Your limit must be numbers.")
        while True:
            try:
                upper_range_cut = int(input("Upper boundary limit: "))
                break
            except ValueError:
                print ("Your limit must be numbers.")
        if lower_range_cut > upper_range_cut:
            print ("Sorry, your upper limit has to be bigger than \n"
                   "your lower limit. Try it again.")
            pass
        else:
            break

    random_number = random.randint(lower_range_cut,upper_range_cut)
    return lower_range_cut, upper_range_cut, random_number

def max_guess_number(low,high): # returns the total number of guesses
    total_numbers = (high - low) + 1
    total_guesses = 0
    while (2**total_guesses) < total_numbers:
        total_guesses += 1
    print ("You have a total of %d guesses\n"
           "for your range between %d to %d"
           % (total_guesses, low, high))
    return total_guesses

def evaluation(random_number, total_guesses, lower_range_cut, upper_range_cut): # evaluates the users input
    guess_count = 0
    # I wanted to integrate the strings first, second...in the guess
    # prompt like "Your third guess: "
    # numbers_of_guess = [first, second, third, fourth, fifth,
    #                    sixth, seventh, eighth, ninth, tenth,
    #                    eleventh, twelfth, thirteenth,
    #                    fourteenth, fifteenth, sixteenth,
    #                    seventeenth, eighteenth, nineteenth,
    #                    twentieth, twenty-first, twenty-second,
    #                    twenty-third, twenty-fourth, twenty-fifth,
    #                    twenty-sixth, twenty-seventh, twenty-eighth,
    #                    twenty-ninth, thirdieth]
    while guess_count < total_guesses:
        print ("------------------------------")
        if guess_count == 0:
            user_guess = int(input("Your first guess: "))
        else:
            user_guess = int(input("Your %d. guess: " % (guess_count+1)))
        print("Your guess is: %d" % (user_guess))
        if (user_guess < lower_range_cut or user_guess > upper_range_cut):
            print("You number is outside of your defined range \n"
                  "between %d and %d. Try again!" % (lower_range_cut, upper_range_cut))
            print("You have still %d guesses left." % (total_guesses - guess_count))
        elif (random_number == user_guess):
            print("Congratulation! You got it! ")
            break
        elif user_guess > random_number:
            print("Guess lower!")
            guess_count += 1
            print("You have %d guesses left." % (total_guesses - guess_count))
        else:
            print("Guess higher!")
            guess_count += 1
            print("You have %d guesses left." % (total_guesses - guess_count))
    else:
        print ("Sorry, you didn't guess the number\n"
               "within the given number of guesses.\n"
               "The number was %d." % (random_number))



if __name__ == "__main__":
    main()