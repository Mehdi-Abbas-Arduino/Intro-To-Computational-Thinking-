def find_ing_words(words):
    # WRITE YOUR CODE HERE
    if not words:
        return []
    # if len(words[0]) > 2:
    if words[0][-3:] == "ing":
        return [words[0]] + find_ing_words(words[1:])
    else:
        return find_ing_words(words[1:])
    # else:
    return find_ing_words(words[1:])
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

    sentence = ['how', 'is', 'it', 'going', 'this', 'morning', 'mr', 'browning']
    print(find_ing_words(sentence))
    # Should print: ['going', 'morning', 'browning']

    print(find_ing_words(['ing', 'in', 'king']))
    # Should print: ['ing', 'king']

    print(find_ing_words(['is', 'it', 'in']))
    # Should print: []

    print(find_ing_words([]))
    # Should print: []

    print(find_ing_words(['going', 'doing', 'going']))
    # Should print: ['going', 'doing', 'going']

    print(find_ing_words(['singing', 'morning', 'singer', 'ings']))
    # Should print: ['singing', 'morning']

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#


# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q3.py
# python3 -m pytest tests/test_q3.py
