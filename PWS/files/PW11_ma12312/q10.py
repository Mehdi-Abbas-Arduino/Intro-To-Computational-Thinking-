def helperequal(first_word, second_word,diff=0):
    if first_word == '' and second_word == '' :
        return diff
    else:
        first_word = first_word.lower()
        second_word = second_word.lower()
        first = first_word[0]
        second = second_word[0]
        if first != second:
            diff += 1
        return helperequal(first_word[1:],second_word[1:],diff)

def helper(first_word, second_word):
    if len(first_word) > len(second_word):
        longer = first_word.lower()
        shorter = second_word.lower()
    else:
        longer = second_word.lower()
        shorter = first_word.lower()
    min_diff = len(shorter)
    for i in range(len(longer) - len(shorter) + 1):
        current_diff = 0
        for j in range(len(shorter)):
            if shorter[j] != longer[i + j]:
                current_diff += 1
        if current_diff < min_diff:
            min_diff = current_diff
    return min_diff + len(longer) - len(shorter)

def word_distance(first_word, second_word):
    # WRITE YOUR CODE HERE
    if len(first_word) == len(second_word):
        return helperequal(first_word,second_word)
    else:
        return helper(first_word,second_word)


# -----------------------------------------#
# TESTING YOUR CODE                        #
# -----------------------------------------#
# The code below runs only when this file is executed directly.
if __name__ == "__main__":

    # ----------------------------------------------#
    # TESTING YOUR CODE ON SAMPLE TEST CASES        #
    # Run this file and manually check whether      #
    # your function produces the expected output.   #
    # ----------------------------------------------#

    print(word_distance('kitten', 'KittEN'))
    # Should print: 0

    print(word_distance('spa ces', 'a ces'))
    # Should print: 2

    print(word_distance('kitten', 'sitting'))
    # Should print: 3

    print(word_distance('xyz', 'abc'))
    # Should print: 3

    print(word_distance('sTaLl', 'StaBle'))
    # Should print: 2

    print(word_distance('abc', 'axbcy'))
    # Should print: 3

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#


# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q10.py
# python3 -m pytest tests/test_q10.py
