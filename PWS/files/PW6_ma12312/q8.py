# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def generate_ids(num_students):
    # WRITE YOUR CODE HERE
    num = '00000'
    for i in range(num_students):
        x = input()
        x = x.split()
        firstname = x[0]
        lastname = x[-1]
        firstintial = firstname[0].lower()
        lastintial = lastname[0].lower()
        print(firstintial + lastintial + num + '@st.habib.edu.pk')
        num = f"{int(num) + 1:05d}" #"00001"
        # turns into 1 add 4 digits behind it
        # if i == num_students -1 :
        #     return firstinitial + lastintial + str(num) + '@st.habib.edu.pk'



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

    print("Testing 1:")
    generate_ids(4)
    # [ Input -> '   Waqar.  Saleem']
    # Should print: ws00000@st.habib.edu.pk
    # [ Input -> 'Umair Azfar   Khan']
    # Should print: uk00001@st.habib.edu.pk
    # [ Input -> 'Shahid Hussain']
    # Should print: sh00002@st.habib.edu.pk
    # [ Input -> '    Shah Jamal Alam']
    # Should print: sa00003@st.habib.edu.pk

    print()

    print("Testing 2:")
    generate_ids(3)
    # [ Input -> 'Harry Potter']
    # Should print: hp00000@st.habib.edu.pk
    # [ Input -> 'Hermione Granger']
    # Should print: hg00001@st.habib.edu.pk
    # [ Input -> 'Tom Marvolo Riddle']
    # Should print: tr00002@st.habib.edu.pk

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q8.py
