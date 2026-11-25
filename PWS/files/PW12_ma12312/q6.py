def decrypt_cryptogram(cryptogram, frequency_order):
    # WRITE YOUR CODE HERE
    m = {}
    for i in cryptogram:
        x = i
        for j in range(len(x)):
            if x[j] not in m :
                if x[j].isalpha():
                    m[x[j]] = 1
            else:
                if x[j].isalpha():
                    m[x[j]] += 1
    
    sorted_m = dict(sorted(m.items(), key=lambda item: item[1],reverse=True))
    mapp = {}
    i = 0
    for k in sorted_m.keys():
        mapp[k] = frequency_order[i]
        i += 1
    lis2 = []
    for i in cryptogram:
        x = i
        word = ''
        for j in range(len(x)):
            if x[j] in mapp:
                word += mapp[x[j]]
            else:
                word += x[j]

        lis2.append(word)

    return [m, lis2]

def main():
    x = int(input())
    lis = []
    for i in range(x):
        lis.append(input())
    x = input()
    z = decrypt_cryptogram(lis,x)
    print(z)


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
    main()
    # Enter these lines when prompted:
    # 2
    # ABBA!
    # CAB?
    # eto
    # Should print:
    # [{'A': 3, 'B': 3, 'C': 1}, ['ette!', 'oet?']]

    print()

    main()
    # Enter these lines when prompted:
    # 2
    # ZZY Z!
    # QY?
    # eta
    # Should print:
    # [{'Z': 3, 'Y': 2, 'Q': 1}, ['eet e!', 'at?']]

    # ----------------------------------------------#
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW       #
    # ----------------------------------------------#

    # In order to test your function, run:
    # pytest tests/test_q6.py