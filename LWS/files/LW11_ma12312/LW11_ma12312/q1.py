def remove_vowels(text):
    # WRITE YOUR CODE HERE
    # remove_vowels(text[:-1])
    vowels = "aeiou"
    if (text) == '':
        return ''
    if text[0].lower() in vowels:
        return ("") +  remove_vowels(text[1:])
    else:
        return (text[0]) + remove_vowels(text[1:])
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

    print(remove_vowels('recursion'))
    # Should print: 'rcrsn'

    print(remove_vowels('Defenestrate'))
    # Should print: 'Dfnstrt'

    print(remove_vowels('Orange'))
    # Should print: 'rng'

    print(remove_vowels('The quick brown fox jumps over the lazy dog.'))
    # Should print: 'Th qck brwn fx jmps vr th lzy dg.'

    print(remove_vowels(''))
    # Should print: ''

    print(remove_vowels('AI in 2026!'))
    # Should print: ' n 2026!'

    print(remove_vowels('AEIOUaeiou'))
    # Should print: ''

    print(remove_vowels('Python Programming'))
    # Should print: 'Pythn Prgrmmng'

    print(remove_vowels('Why so serious?'))
    # Should print: 'Why s srs?'

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#


# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q1.py
# python3 -m pytest tests/test_q1.py
