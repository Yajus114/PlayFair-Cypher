# Made By- Yajus Gakhar of The NorthCap University, Gurugram. For any queries, contact at:
# yajus19csu349@ncuindia.edu
import numpy as np
import random as randy


def key_matrix(key):
    ran_char = ''
    b = []
    count = 0
    sen = "abcdefghijklmnopqrstuvwxyz"

    for i in range(len(key)):  # this loop 
        for char in key[i]:
            if char not in b:
                if char == 'i' or char == 'j':
                    if count == 0:
                        b.append('ij')
                        count += 1
                else:
                    b.append(char.lower())

    # print(b)

    for char in sen:
        if char == 'i' or char == 'j':
            if 'ij' in b:
                pass
            else:
                b.append('ij')
        elif char not in b:
            b.append(char)

    b = np.array(b).reshape(5, 5)

    return b


def Plain_To_Cypher(pt, key):
    ran_char = ''
    mat = key_matrix(key)
    # print(mat)
    ct = ''
    a, c = [], []
    if len(pt) % 2 != 0:
        ran_char = chr(randy.randint(ord('a'), (ord('z') + 1)))
        pt += ran_char

    for z in range(0, len(pt), 2):
        a.append(pt[z] + pt[z + 1])

    for char in a:
        for i in range(1):
            c.append(char[i])
            c.append(char[i + 1])
        for f in range(1):
            z = c[f]
            j = c[f + 1]
            if z == 'i' or z == 'j':
                z = 'ij'
            if j == 'i' or j == 'j':
                j = 'ij'
            for rowi in range(5):

                for rowj in range(5):

                    for coli in range(5):

                        for colj in range(5):

                            if mat[rowi, coli] == z and mat[rowj, colj] == j:

                                if rowi != rowj and colj != coli:

                                    if mat[rowi, colj] == 'ij':
                                        ct += chr(randy.randint(105, 107)) + mat[rowj, coli] + ' '

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
        c = []
    print('The Cypher is:', ct)


def Cypher_To_Plain(ct, key):
    mat = key_matrix(key)
    # print(mat)
    pt = ''
    a, c = [], []
    for z in range(0, len(ct), 2):
        a.append(ct[z] + ct[z + 1])

    for char in a:
        for i in range(1):
            c.append(char[i])
            c.append(char[i + 1])
        for f in range(1):
            z = c[f]
            j = c[f + 1]
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

        c = []
    print('The message is:', pt)


while 1:
    q = int(input("Enter your choice:\n1. Plain Text to Cypher Text\n2. Cypher Text to Plain Text\n3. Display key "
                  "matrices\n4. Exit.\n-->"))
    if q == 1:
        Plain_To_Cypher(str(input("Enter the Plain Text(length of text > 1):\n")).replace(' ', '').lower(),
                        list(map(str, input("Enter the key:\n").lower().split(' '))))

    elif q == 2:
        Cypher_To_Plain(str(input("Enter the Cypher Text(length of text > 1):\n")).replace(' ', '').lower(),
                        list(map(str, input("Enter the key:\n").lower().split(' '))))
    elif q == 3:
        print(key_matrix(list(map(str, input("Enter the key:\n").lower().split(' ')))))
    elif q == 4:
        exit()
    else:
        print('Please enter a valid number(1 or 2) and try again.')
# se hn rq mr hn ri rm en rm sn al pn qk yg cy ld zm ch tn eo cr lf nb ru hk nh sf bw kv dc fg; playfair cypher
