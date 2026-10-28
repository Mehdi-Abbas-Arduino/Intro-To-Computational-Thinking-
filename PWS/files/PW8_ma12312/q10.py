# -----------------------------------------#
# FUNCTION DEFINITIONS                     #
# -----------------------------------------#


# -----------------------------------------#
# FUNCTION DEFINITIONS                     #
# -----------------------------------------#

def calculate_gpa(credits, scores):
    total_points = 0
    total_credits = 0

    for i in range(len(scores)):
        if scores[i] >= 85:
            grade = 4.0
        elif scores[i] >= 80:
            grade = 3.7
        elif scores[i] >= 75:
            grade = 3.3
        elif scores[i] >= 70:
            grade = 3.0
        elif scores[i] >= 65:
            grade = 2.7
        elif scores[i] >= 60:
            grade = 2.3
        elif scores[i] >= 55:
            grade = 2.0
        elif scores[i] >= 50:
            grade = 1.0
        else:
            grade = 0.0

        total_points += credits[i] * grade
        total_credits += credits[i]

    return round(total_points / total_credits, 2)


def main():
    credits = list(map(int, input().split()))
    scores = list(map(int, input().split()))

    print(calculate_gpa(credits, scores))


if __name__ == "__main__":
    main()



# -----------------------------------------#
# TESTING YOUR CODE                        #
# -----------------------------------------#
# The code below runs only when this file is executed directly.
if __name__ == "__main__":

    # ----------------------------------------------#
    # TESTING YOUR CODE ON VISIBLE TEST CASES       #
    # Run this file and manually check whether      #
    # your functions produce the expected output.   #
    # ----------------------------------------------#

    # Note: Inputs to be entered are labelled as [ Input -> X ] where X is the input.

    main()
    # [ Input -> 3 3 1 4 4]
    # [ Input -> 80 73 94 62 85]
    # Should print: 2.91

    print()

    main()
    # [ Input -> 2 1 1 3 1 3 4]
    # [ Input -> 71 60 97 86 68 66 95]
    # Should print: 3.1

    print()

    main()
    # [ Input -> 1 1 1 1 1 1 1 1 1 1]
    # [ Input -> 100 95 90 85 80 75 70 67 63 60]
    # Should print: 3.07

    print()

    main()
    # [ Input -> 4 3 2 1]
    # [ Input -> 95 85 75 60]
    # Should print: 3.48

    print()

    main()
    # [ Input -> 4]
    # [ Input -> 100]
    # Should print: 4.0

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your functions, type one of the following commands in the terminal:
# python -m pytest tests/test_q10.py
# python3 -m pytest tests/test_q10.py