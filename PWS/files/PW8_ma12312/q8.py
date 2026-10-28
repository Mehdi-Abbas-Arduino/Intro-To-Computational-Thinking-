# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#


def word_search(word, sentence):
    positions = []
    start = 0

    for letter in word.lower():
        found = False

        while start < len(sentence):
            if sentence[start].lower() == letter:
                positions.append(start)
                start += 1
                found = True
                break
            start += 1

        if not found:
            return []

    return [positions[0], positions[-1]]




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

    print(word_search(
        "Japan",
        "Aaj apa narangi laayi hain."
    ))
    # Should print: [2, 9]

    print(word_search(
        "Mozambique",
        "Aaj apa musambi laayi hain."
    ))
    # Should print: []

    print(word_search(
        "Canada",
        "Can a day of extreme self-care really reset your mood and nervous system?"
    ))
    # Should print: [0, 8]

    print(word_search(
        "Peru",
        "Give hope. Run!"
    ))
    # Should print: [7, 13]

    print(word_search(
        "China",
        "HU cafeteria may open a branch in all major food districts--God help us!"
    ))
    # Should print: [28, 35]

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q8.py
# python3 -m pytest tests/test_q8.py