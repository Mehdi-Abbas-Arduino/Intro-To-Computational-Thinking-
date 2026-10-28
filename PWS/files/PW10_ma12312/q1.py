# -----------------------------------------#
# FUNCTION DEFINITIONS                     #
# -----------------------------------------#

def verify_collatz(starting_number):
    # WRITE YOUR CODE HERE
    x = starting_number
    print(x)
    if x == 1:
        # print(1)
        return
    if x % 2 == 0:
        x = x // 2
        # print(x)
    elif x % 2 != 0:
        x = 3 * x + 1
        # print(x)

    verify_collatz(x)


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

    verify_collatz(1)
    # Should print:
    # 1

    print()

    verify_collatz(5)
    # Should print:
    # 5
    # 16
    # 8
    # 4
    # 2
    # 1

    print()

    verify_collatz(52)
    # Should print:
    # 52
    # 26
    # 13
    # 40
    # 20
    # 10
    # 5
    # 16
    # 8
    # 4
    # 2
    # 1

    print()

    verify_collatz(7)
    # Should print:
    # 7
    # 22
    # 11
    # 34
    # 17
    # 52
    # 26
    # 13
    # 40
    # 20
    # 10
    # 5
    # 16
    # 8
    # 4
    # 2
    # 1

    print()

    verify_collatz(12)
    # Should print:
    # 12
    # 6
    # 3
    # 10
    # 5
    # 16
    # 8
    # 4
    # 2
    # 1

    print()

    verify_collatz(63)
    # Should print:
    # 63
    # 190
    # 95
    # 286
    # 143
    # 430
    # 215
    # 646
    # 323
    # 970
    # 485
    # 1456
    # 728
    # 364
    # 182
    # 91
    # 274
    # 137
    # 412
    # 206
    # 103
    # 310
    # 155
    # 466
    # 233
    # 700
    # 350
    # 175
    # 526
    # 263
    # 790
    # 395
    # 1186
    # 593
    # 1780
    # 890
    # 445
    # 1336
    # 668
    # 334
    # 167
    # 502
    # 251
    # 754
    # 377
    # 1132
    # 566
    # 283
    # 850
    # 425
    # 1276
    # 638
    # 319
    # 958
    # 479
    # 1438
    # 719
    # 2158
    # 1079
    # 3238
    # 1619
    # 4858
    # 2429
    # 7288
    # 3644
    # 1822
    # 911
    # 2734
    # 1367
    # 4102
    # 2051
    # 6154
    # 3077
    # 9232
    # 4616
    # 2308
    # 1154
    # 577
    # 1732
    # 866
    # 433
    # 1300
    # 650
    # 325
    # 976
    # 488
    # 244
    # 122
    # 61
    # 184
    # 92
    # 46
    # 23
    # 70
    # 35
    # 106
    # 53
    # 160
    # 80
    # 40
    # 20
    # 10
    # 5
    # 16
    # 8
    # 4
    # 2
    # 1

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#


# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q1.py
# python3 -m pytest tests/test_q1.py
