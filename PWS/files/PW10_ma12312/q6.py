# -----------------------------------------#
# FUNCTION DEFINITIONS                     #
# -----------------------------------------#

def helper(n,index=1):
    pass

def caffeine(number_of_orders):
    # WRITE YOUR CODE HERE
    pass


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

    # Inputs to be entered are labelled as [ Input -> X ].

    caffeine(2)
    # [ Input -> L ]
    # [ Input -> Masala Chai ]
    # [ Input -> M ]
    # [ Input -> Iced Matcha Latte ]
    # Should print:
    # Enter drink size (L/M/S):
    # Choose from one of the following flavors:
    # --Iced Matcha Latte
    # --Boba Tea
    # --French Vanilla
    # --Peppermint
    # --Masala Chai
    # Flavor:
    # Order 1: Large Masala Chai --- 225
    #
    # Enter drink size (L/M/S):
    # Choose from one of the following flavors:
    # --Iced Matcha Latte
    # --Cappuccino
    # --Flat White
    # --Espresso
    # --Black Coffee
    # --Pumpkin Spice Latte
    # Flavor:
    # Order 2: Medium Iced Matcha Latte --- 145
    #
    #

    caffeine(1)
    # [ Input -> S ]
    # [ Input -> Vanilla Latte ]
    # Should print:
    # Enter drink size (L/M/S):
    # Choose from one of the following flavors:
    # --Iced Matcha Latte
    # --Caramel Latte
    # --Vanilla Latte
    # --Americano
    # --Frappe
    # --Ristretto
    # --Turkish Coffee
    # Flavor:
    # Order 1: Small Vanilla Latte --- 160
    #
    #

    caffeine(3)
    # [ Input -> M ]
    # [ Input -> Iced Matcha Latte ]
    # [ Input -> S ]
    # [ Input -> Iced Matcha Latte ]
    # [ Input -> L ]
    # [ Input -> Iced Matcha Latte ]
    # Should print:
    # Enter drink size (L/M/S):
    # Choose from one of the following flavors:
    # --Iced Matcha Latte
    # --Cappuccino
    # --Flat White
    # --Espresso
    # --Black Coffee
    # --Pumpkin Spice Latte
    # Flavor:
    # Order 1: Medium Iced Matcha Latte --- 145
    #
    # Enter drink size (L/M/S):
    # Choose from one of the following flavors:
    # --Iced Matcha Latte
    # --Caramel Latte
    # --Vanilla Latte
    # --Americano
    # --Frappe
    # --Ristretto
    # --Turkish Coffee
    # Flavor:
    # Order 2: Small Iced Matcha Latte --- 110
    #
    # Enter drink size (L/M/S):
    # Choose from one of the following flavors:
    # --Iced Matcha Latte
    # --Boba Tea
    # --French Vanilla
    # --Peppermint
    # --Masala Chai
    # Flavor:
    # Order 3: Large Iced Matcha Latte --- 175
    #
    #

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#


# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your functions, type one of the following commands in the terminal:
# python -m pytest tests/test_q6.py
# python3 -m pytest tests/test_q6.py