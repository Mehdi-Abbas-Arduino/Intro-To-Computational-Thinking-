# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def sum_odd(first_number, second_number):

    
    total = 0
    if type(first_number) == int and type(second_number) == int:
        if first_number <= second_number:
            
            for i in range(first_number,second_number+1):
                if i % 2 != 0:
                    total += i
                    
            return total
        
        elif first_number > second_number:
                for i in range(second_number,first_number+1):
                            if i % 2 != 0:
                                total += i
                                
                return total
                    
    
    else:
        return ('Error: bad argument. sum_odd is defined for integers only.')



    
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
    
    print(sum_odd(1, 1))
    # Should print: 1
    
    print(sum_odd(2, 2))
    # Should print: 0
     
    print(sum_odd(1, 2))
    # Should print: 1
     
    print(sum_odd(2, 3))
    # Should print: 3
     
    print(sum_odd(13, 2))
    # Should print: 48
     
    print(sum_odd(6.7, 10))
    # Should print: Error: bad argument. sum_odd is defined for integers only.

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#


# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q1.py