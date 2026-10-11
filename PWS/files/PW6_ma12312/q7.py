# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def replace_not_bad(text):
    # WRITE YOUR CODE HERE
    n = text.split()

    nots = -1
    bad = -1

    for index, i in enumerate(n):
        string = ''

        for j in i:
            string += j

            if string.lower() == 'not':
                nots = index
            elif string.lower() == 'bad':
                bad = index

    if nots == -1 or bad == -1:
        return text

    word = n[bad]

    if len(word) == 3:
        new_word = "good"
    else:
        remaining = word[3:]
        new_word = "good" + remaining

    if word[0].isupper(): # checks is the word in the old list is capital 
        new_word = new_word.capitalize()

    n[nots:bad+1] = [new_word]

    string = ''

    for i in range(len(n)):
        if i == 0:
            string += n[i]
        else:
            string += ' ' + n[i]

    return string
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

    print(replace_not_bad('This dinner is not that bad!'))
    # Should print: This dinner is good!

    print(replace_not_bad('Maula Jatt is awesome.'))
    # Should print: Maula Jatt is awesome.

    print(replace_not_bad('Cheating is not my cup of tea.'))
    # Should print: Cheating is not my cup of tea.

    print(replace_not_bad('Babar was not a badminton player growing up in Islamabad.'))
    # Should print: Babar was goodminton player growing up in Islamabad.

    print(replace_not_bad('Not every Badshah is a Maharaja.'))
    # Should print: Goodshah is a Maharaja.

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q7.py
