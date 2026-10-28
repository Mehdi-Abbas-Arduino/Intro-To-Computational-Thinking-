# -----------------------------------------#
# FUNCTION DEFINITIONS                     #
# -----------------------------------------#
def slow_reveal(message):
    if message == '':
        return
    slow_reveal(message[:-1])
    print(message)


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

    slow_reveal('Pizza!')
    # Should print:
    # P
    # Pi
    # Piz
    # Pizz
    # Pizza
    # Pizza!

    slow_reveal('Hi')
    # Should print:
    # H
    # Hi

    slow_reveal('A')
    # Should print:
    # A

    slow_reveal('')
    # Should print nothing.

    slow_reveal("And just like that... he's gone.")
    # Should print:
    # A
    # An
    # And
    # And 
    # And j
    # And ju
    # And jus
    # And just
    # And just 
    # And just l
    # And just li
    # And just lik
    # And just like
    # And just like 
    # And just like t
    # And just like th
    # And just like tha
    # And just like that
    # And just like that.
    # And just like that..
    # And just like that...
    # And just like that... 
    # And just like that... h
    # And just like that... he
    # And just like that... he'
    # And just like that... he's
    # And just like that... he's 
    # And just like that... he's g
    # And just like that... he's go
    # And just like that... he's gon
    # And just like that... he's gone
    # And just like that... he's gone.

    slow_reveal('0123456789')
    # Should print:
    # 0
    # 01
    # 012
    # 0123
    # 01234
    # 012345
    # 0123456
    # 01234567
    # 012345678
    # 0123456789

    slow_reveal('Hi!')
    # Should print:
    # H
    # Hi
    # Hi!

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#


# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q10.py
# python3 -m pytest tests/test_q10.py
