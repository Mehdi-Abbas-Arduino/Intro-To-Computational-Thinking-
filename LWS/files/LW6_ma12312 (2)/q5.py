# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def expand_message(encoded_message):
    """Expand groups using their number and brackets.

    Start with an empty string and index 0.
    If a digit is found, build the complete number.
    Find the text inside the brackets.
    Repeat that text using the number and add it to the result.
    Move past the closing bracket and continue.
    If there is no digit, add the current character.
    Return the final expanded string.
    """
    
    string = ''
    i = 0

    while i < len(encoded_message):
        if encoded_message[i].isdigit():
            number = 0

            while i < len(encoded_message) and encoded_message[i].isdigit(): # want to get digits 
                number = number * 10 + int(encoded_message[i])
                i += 1

            if i < len(encoded_message) and encoded_message[i] == '[': # searching first bracket 
                first = i + 1
                second = first

                while second < len(encoded_message) and encoded_message[second] != ']': # searching second bracket 
                    second += 1

                letter = encoded_message[first:second] # 
                string += number * letter
                i = second + 1

        else:
            string += encoded_message[i]
            i += 1

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

    print(expand_message('3[ha]'))
    # Should print: hahaha

    print(expand_message('2[go] team!'))
    # Should print: gogo team!

    print(expand_message('2[abc]3[cd]ef'))
    # Should print: abcabccdcdcdef

    print(expand_message('12[!] done'))
    # Should print: !!!!!!!!!!!! done

    print(expand_message('3[ac]'))
    # Should print: acacac

    print(expand_message('3[a]2[bc]'))
    # Should print: aaabcbc

    print(expand_message('ab9[cd]2[ef]g'))
    # Should print: abcdcdcdcdcdcdcdcdcdefefg

    print(expand_message('2[a]2[b]cd'))
    # Should print: aabbcd

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q5.py