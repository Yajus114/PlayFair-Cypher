# Made By- Yajus Gakhar of The NorthCap University, Gurugram. For any queries, contact at:
# yajus19csu349@ncuindia.edu
import numpy as np
import random as randy


def key_matrix(key):  # function used to generate the key matrix using an inputted pass phrase or key phrase. The code
    # accepts spaces and capital letters also. 
    b = []
    count = 0
    sen = "abcdefghijklmnopqrstuvwxyz"

    for i in range(len(key)):  # this loop 
        for char in key[i]:
            if char not in b:
                if char == 'i' or char == 'j':
                    if count == 0:
                        b.append('ij')  # appending 'ij' once for i or j in key
                        count += 1
                else:
                    b.append(char.lower())

    for char in sen:  # appending the rest of the remaining alphabets to the list
        if char == 'i' or char == 'j':
            if 'ij' in b:
                pass
            else:
                b.append('ij')
        elif char not in b:
            b.append(char)

    b = np.array(b).reshape(5, 5)  # matrix formation

    return b  # returning the key matrix


def Plain_To_Cypher(pt, key):
    ran_char = ''
    mat = key_matrix(key)
    # print(mat)  # if you enable this, you may generate the key matrix simultaneously with the cypher
    ct = ''
    a = []
    if len(pt) % 2 != 0:  # adding a random character to the plain text if length of plain text is odd
        ran_char = chr(randy.randint(ord('a'), (ord('z') + 1)))
        pt += ran_char

    for z in range(0, len(pt), 2):  # appending pairs from the plaintext
        a.append(pt[z] + pt[z + 1])

    for char in a:  # generating the cypher
        for i in range(1):  # sets the pair of letters one at a time to variables z and j
            for f in range(1):
                z = char[i]
                j = char[i + 1]
                if z == 'i' or z == 'j':
                    z = 'ij'
                if j == 'i' or j == 'j':
                    j = 'ij'
                for rowi in range(5):

                    for rowj in range(5):

                        for coli in range(5):

                            for colj in range(5):  # setting up row and column variables for the key matrix

                                if mat[rowi, coli] == z and mat[rowj, colj] == j:  # if elemnt found

                                    if rowi != rowj and colj != coli:  # different cases for matched elements

                                        if mat[rowi, colj] == 'ij':
                                            ct += chr(randy.randint(105, 107)) + mat[rowj, coli] + ' '  # inserting random i or j

                                        elif mat[rowj, coli] == 'ij':
                                            ct += mat[rowi, colj] + chr(randy.randint(105, 107)) + ' '

                                        else:
                                            ct += mat[rowi, colj] + mat[rowj, coli] + ' '

                                    elif rowi == rowj and colj != coli:

                                        if mat[rowi, coli - 1] == 'ij':
                                            ct += chr(randy.randint(105, 107)) + mat[rowj, colj - 1] + ' '

                                        elif mat[rowj, colj - 1] == 'ij':
                                            print('doing')
                                            ct += mat[rowi, coli - 1] + chr(randy.randint(105, 107)) + ' '

                                        else:
                                            # print('done improper')
                                            ct += mat[rowj, coli - 1] + mat[rowi, colj - 1] + ' '

                                    elif rowj != rowi and colj == coli:

                                        if mat[rowi - 1, coli] == 'ij':
                                            ct += chr(randy.randint(105, 107)) + mat[rowj - 1, colj] + ' '

                                        elif mat[rowj - 1, colj] == 'ij':
                                            ct += mat[rowi - 1, coli] + chr(randy.randint(105, 107)) + ' '

                                        else:
                                            # print('done proper')
                                            ct += mat[rowi - 1, colj] + mat[rowj - 1, coli] + ' '

                                    else:
                                        ct += z + z + ' '
    print('The Cypher is:', ct)


def Cypher_To_Plain(ct, key):
    mat = key_matrix(key)
    # print(mat)
    pt = ''
    a = []
    for z in range(0, len(ct), 2):  # appending pairs from the cypher text 
        a.append(ct[z] + ct[z + 1])

    for char in a:
        for i in range(1):
            for f in range(1):
                z = char[i]
                j = char[i + 1]
                if z == 'j' or z == 'i':
                    z = 'ij'
                if j == 'j' or j == 'i':
                    j = 'ij'
                for rowi in range(0, 5):
                    for rowj in range(0, 5):
                        for coli in range(0, 5):
                            for colj in range(0, 5):
                                if mat[rowi, coli] == z and mat[rowj, colj] == j:
                                    if rowi != rowj and colj != coli:
                                        pt += mat[rowi, colj] + mat[rowj, coli]
                                    elif rowi == rowj and colj != coli:
                                        if colj == 4:
                                            colj = 0
                                            pt += mat[rowi, colj] + mat[rowj, coli + 1] + ' '
                                        elif coli == 4:
                                            coli = 0
                                            pt += mat[rowj, coli] + mat[rowi, colj + 1] + ' '
                                        else:
                                            pt += mat[rowi, coli + 1] + mat[rowj, colj + 1] + ' '
                                    elif rowi != rowj and colj == coli:
                                        if rowi == 4:
                                            rowi = 0
                                            pt += mat[rowi, colj] + mat[rowj + 1, coli] + ' '
                                        elif rowj == 4:
                                            rowj = 0
                                            pt += mat[rowi + 1, colj] + mat[rowj, coli] + ' '
                                        else:
                                            pt += mat[rowi + 1, coli] + mat[rowj + 1, colj] + ' '
                                    else:
                                        pt += z + z + ' '
    print('The message is:', pt)


while 1:
    q = int(input("Enter your choice:\n1. Plain Text to Cypher Text\n2. Cypher Text to Plain Text\n3. Display key "
                  "matrices\n4. Exit.\n-->"))
    if q == 1:
        Plain_To_Cypher(str(input("Enter the Plain Text(length of text > 1):\n")).strip().lower(),
                        list(map(str, input("Enter the key:\n").lower().split(' '))))

    elif q == 2:
        Cypher_To_Plain(str(input("Enter the Cypher Text(length of text > 1):\n")).strip().lower(),
                        list(map(str, input("Enter the key:\n").lower().split(' '))))
    elif q == 3:
        print(key_matrix(list(map(str, input("Enter the key:\n").lower().split(' ')))))
    elif q == 4:
        exit()
    else:
        print('Please enter a valid number(1 or 2) and try again.')
# se hn rq mr hn ri rm en rm sn al pn qk yg cy ld zm ch tn eo cr lf nb ru hk nh sf bw kv dc fg; playfair cypher
