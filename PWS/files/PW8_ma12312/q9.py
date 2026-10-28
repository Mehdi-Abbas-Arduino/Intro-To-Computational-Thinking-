# -----------------------------------------#
# FUNCTION DEFINITIONS                     #
# -----------------------------------------#


def generate_ids(names):
    lst = []
    names = names.split(',')
    num = 0

    for i in range(len(names)):
        name = names[i].split()

        firstname = name[0]
        lastname = name[-1]

        firstinitial = firstname[0].lower()
        lastinitial = lastname[0].lower()

        student_id = f"{num:05d}"

        lst.append(firstinitial + lastinitial + student_id + '@st.hu.edu.pk')
        num += 1

    return lst


def main():
    names = eval(input())
    print(generate_ids(names))


if __name__ == "__main__":
    main()


    
# -----------------------------------------#
# TESTING YOUR CODE                        #
# -----------------------------------------#
# The code below runs only when this file is executed directly.
if __name__ == "__main__":

    # ----------------------------------------------#
    # TESTING YOUR CODE ON VISIBLE TEST CASES       #
    # Run this file and manually check whether      #
    # your functions produce the expected output.   #
    # ----------------------------------------------#

    # Note: Inputs to be entered are labelled as [ Input -> X ] where X is the input.
    # Enter input without quotation marks.

    main()
    # [ Input -> '  Waqar.  Saleem, Umair Azfar   Khan, Shahid Hussain,      Shah Jamal Alam']
    # Should print:
    # ['ws00000@st.hu.edu.pk', 'uk00001@st.hu.edu.pk', 'sh00002@st.hu.edu.pk', 'sa00003@st.hu.edu.pk']

    print()

    main()
    # [ Input -> 'Harry Potter, Hermione Granger, Tom Marvolo Riddle']
    # Should print:
    # ['hp00000@st.hu.edu.pk', 'hg00001@st.hu.edu.pk', 'tr00002@st.hu.edu.pk']

    print()

    main()
    # [ Input -> 'Dalinar Kholin, Shallan Davar, Brandon Sanderson']
    # Should print:
    # ['dk00000@st.hu.edu.pk', 'sd00001@st.hu.edu.pk', 'bs00002@st.hu.edu.pk']

    print()

    main()
    # [ Input -> 'Harry Potter']
    # Should print: ['hp00000@st.hu.edu.pk']

    print()

    main()
    # [ Input -> 'Hari Puttar, Sattar Buksh, Maula Jutt']
    # Should print:
    # ['hp00000@st.hu.edu.pk', 'sb00001@st.hu.edu.pk', mj00002@st.hu.edu.pk']

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your functions, type one of the following commands in the terminal:
# python -m pytest tests/test_q9.py
# python3 -m pytest tests/test_q9.py