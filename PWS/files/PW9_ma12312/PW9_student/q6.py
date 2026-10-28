# -----------------------------------------#
# FUNCTION DEFINITIONS                     #
# -----------------------------------------#

def seniority(names, ages):
    # WRITE YOUR CODE HERE
    if len(names) != len(ages):
        return -1
    new = []
    for i in range(len(names)):
        new.append([names[i],ages[i]])
    def sort_key(x):
            return (x[1])
    
    new.sort(key=sort_key)
    new2 = []
    new3 = []
    for i in range(len(new)):
        new2.append(new[i][0])

    return new2
def main():
    names = input().split(",")
    ages = input().split(",")

    for i in range(len(names)):
        names[i] = names[i].strip()
        ages[i] = int(ages[i].strip())

    x = seniority(names, ages)
    print(x)

# -----------------------------------------#
# TESTING YOUR CODE                        #
# -----------------------------------------#
# The code below runs only when this file is executed directly.
if __name__ == "__main__":

    # ----------------------------------------------#
    # TESTING YOUR CODE ON VISIBLE TEST CASES       #
    # Run this file and manually check whether      #
    # your function produces the expected output.   #
    # ----------------------------------------------#

    # Note: Inputs to be entered are labelled as [ Input -> X ] where X is the input.

    main()
    # [ Input -> waqar, jamal, umair, shahid ]
    # [ Input -> 20, 22, 19, 18 ]
    # Should print: ['shahid', 'umair', 'waqar', 'jamal']

    main()
    # [ Input -> Ayesha, Bilal, Sara, Hamza, Zoya, Omar ]
    # [ Input -> 22, 25, 21, 20, 22, 21 ]
    # Should print: ['Hamza', 'Sara', 'Omar', 'Ayesha', 'Zoya', 'Bilal']

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your functions, type one of the following commands in the terminal:
# python -m pytest tests/test_q6.py
# python3 -m pytest tests/test_q6.py