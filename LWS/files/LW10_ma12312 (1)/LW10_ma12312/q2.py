# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def guess_midterm_score(midterm_score, attempts_left):
    # WRITE YOUR CODE HERE

    print(f"Attempts remaining: {attempts_left}")

    user = int(input())
    if user == midterm_score:
        print("You won with", attempts_left - 1, "attempts remaining.")
        return
    
    elif attempts_left == 1:
        print("You lost!")
        return
    
    elif midterm_score > user:
        print("Too low!")

    elif midterm_score < user:
        print("Too high!")

    guess_midterm_score(midterm_score, attempts_left-1)

   
# -----------------------------------------#
# TESTING YOUR CODE                        #
# -----------------------------------------#
# The code below runs only when this file is executed directly.
if __name__ == "__main__":

    # ----------------------------------------------#
    # TESTING YOUR CODE ON VISIBLE TEST CASES       #
    # Enter the guesses shown in the comments.      #
    # Check that the printed messages match.        #
    # ----------------------------------------------#

    # guess_midterm_score(72, 5)
    # Should print:
    # Attempts remaining: 5
    # [ Input -> 50 ]
    # Too low!
    # Attempts remaining: 4
    # [ Input -> 75 ]
    # Too high!
    # Attempts remaining: 3
    # [ Input -> 60 ]
    # Too low!
    # Attempts remaining: 2
    # [ Input -> 70 ]
    # Too low!
    # Attempts remaining: 1
    # [ Input -> 65 ]
    # You lost!

    print()

    guess_midterm_score(85, 10)
    # Should print:
    # Attempts remaining: 10
    # [ Input -> 50 ]
    # Too low!
    # Attempts remaining: 9
    # [ Input -> 75 ]
    # Too low!
    # Attempts remaining: 8
    # [ Input -> 85 ]
    # You won with 7 attempts remaining.

    print()

    guess_midterm_score(100, 1)
    # Should print:
    # Attempts remaining: 1
    # [ Input -> 100 ]
    # You won with 0 attempts remaining.

    print()

    guess_midterm_score(0, 1)
    # Should print:
    # Attempts remaining: 1
    # [ Input -> 1 ]
    # You lost!

    print()

    guess_midterm_score(43, 4)
    # Should print:
    # Attempts remaining: 4
    # [ Input -> 43 ]
    # You won with 3 attempts remaining.

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#


# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q2.py
# python3 -m pytest tests/test_q2.py
