# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def print_four_letter_codes(letters):
    n = len(letters)
    for i in range(n):
        for j in range(n):
            # if j == i:
            #     continue
            for k in range(n):
                # if k==i or k==j:
                #     continue
                for z in range(n):
                    if z!=i and z!=j and  z!=k and i != j and i != j and i != k and j!=k and j!=k and k!=i and k!=j:
                        code = letters[i] + letters[j] + letters[k] + letters[z]
                        print(code,end=' ')
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

    print_four_letter_codes("code")
    ''' Should print:
    code coed cdoe cdeo ceod cedo ocde oced odce odec oecd oedc dcoe dceo doce doec deco deoc ecod ecdo eocd eodc edco edoc
    '''

    print()
    print()

    print_four_letter_codes("music")
    ''' Should print:
    musi musc muis muic mucs muci msui msuc msiu msic mscu msci mius miuc misu misc micu mics mcus mcui mcsu mcsi mciu mcis umsi umsc umis umic umcs umci usmi usmc usim usic uscm usci uims uimc uism uisc uicm uics ucms ucmi ucsm ucsi ucim ucis smui smuc smiu smic smcu smci sumi sumc suim suic sucm suci simu simc sium siuc sicm sicu scmu scmi scum scui scim sciu imus imuc imsu imsc imcu imcs iums iumc iusm iusc iucm iucs ismu ismc isum isuc iscm iscu icmu icms icum icus icsm icsu cmus cmui cmsu cmsi cmiu cmis cums cumi cusm cusi cuim cuis csmu csmi csum csui csim csiu cimu cims cium cius cism cisu
    '''

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q6.py