"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    You can refactor a bit, you should refactor a bit! Don't put the code all
    inside this function, think about reusable chunks of code that you can call
    in several places.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """      
    
    print("Welcome to the guessing game!")
    print("A number between _ and _ ?")
    try:
      lowerBound = int (input ("Enter a Lowerbound: "))
      upperBound = int (input ("Enter a upperbound: "))
    except ValueError:
      return ("Please enter the valid number for the bound.")
    print(f"OK then , a number between {lowerBound} and {upperBound}")
    try:
      lowerBound = int(lowerBound)
      upperBound = int(upperBound)
    except ValueError:
      print("Please enter valid numbers.")
    actualnumber =random.randint(lowerBound,upperBound)
    guessed= False
    while not guessed:
      try:
        guessnumber=int(input("Guess a number: "))
      except ValueError:
        print ("Please enter a valid number.")
      if guessnumber == actualnumber:
            print(f"Yeah! You got it {actualnumber}")
            guessed = True
      elif guessnumber < actualnumber:
            print(f"Too small, try again")
      else:
          print(f"Too big, try again")
    return "You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())
