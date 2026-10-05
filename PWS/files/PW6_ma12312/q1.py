# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def mirror_message(message):
    # WRITE YOUR CODE HERE
    string = ''
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    total = 26

    for i in range(len(message)):

        if message[i].isalpha():

            if message[i] in lower:
                count = 0

                for j in range(len(lower)):
                    if message[i] == lower[j]:
                        break
                    else:
                        count += 1

                x = total - 1 - count
                z = lower[x]
                string += z

            elif message[i] in upper:
                count = 0

                for j in range(len(upper)):
                    if message[i] == upper[j]:
                        break
                    else:
                        count += 1

                x = total - 1 - count
                z = upper[x]
                string += z

        else:
            string += message[i]

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

    print(mirror_message('ABC'))
    # Should print: ZYX

    print(mirror_message('abc'))
    # Should print: zyx

    print(mirror_message('Habib'))
    # Should print: Szyry

    print(mirror_message('CS101!'))
    # Should print: XH101!

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q1.py
