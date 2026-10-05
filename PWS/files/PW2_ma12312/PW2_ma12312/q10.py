# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +----------------+------------+
# |     Input      |   Output   |
# |  ra   wa   ca  |            |
# |  rb   wb   cb  |            |
# +----------------+------------+
# |  34    5    6  |    A        |
# |  23    5    6  |            |
# +----------------+------------+
# |  123  14    5  |            |
# |  323   1    6  |     B       |
# +----------------+------------+
# |  199  14   16  |  TIE          |
# |  199  13   17  |            |
# +----------------+------------+


# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variables here.
ra,wa,ca = input("Enter values = ").split()
rb,wb,cb = input("Enter values = ").split()
ra = int(ra)
wa = int(wa)
ca = int(ca)
rb = int(rb)
wb = int(wb)
cb = int(cb)

# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement below.

acount = 0
bcount = 0
if ra > rb:
    acount += 1
elif ra < rb:
    bcount += 1
    
if wa > wb:
    acount += 1
elif wa < wb:
    bcount += 1

if ca > cb:
    acount += 1
if ca < cb:
    bcount += 1
    
    
if acount > bcount:
    print("A")
elif bcount > acount:
    print("B")
elif bcount == acount:
    print("TIE")
# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.
