from copy import deepcopy
from sys import argv, stdin
from random import seed, shuffle
from itertools import permutations

## FUNCTIONS
def readblock(filename):
    fp = open(filename, 'r')
    block = fp.read().rstrip().split("\n")
    for i in range(0,len(block)):
        block[i] = block[i].replace(" ", ";")
    fp.close()
    return block

def computedim(blocks):
    count = 0
    a = ''.join(blocks[0])
    b = ''.join(blocks[1])
    c = ''.join(blocks[2])
    d = ''.join(blocks[3])
    e = ''.join(blocks[4])
    f = ''.join(blocks[5])
    g = ''.join(blocks[6])
    t = ""
    t += a
    t += b
    t += c
    t += d
    t += e
    t += f
    t += g
    count = len(t.replace(";",""))
    return count

def place(block, mat, l, i, j):
    for r in range(0,len(block)):
        for c in range(0,len(block[r])):
            if i+r >= l or j+c >= l:
                return False
            elif mat[i+r][j+c] != '-' and block[r][c] != ';':
                return False

    for r in range(0,len(block)):
        for c in range(0,len(block[r])):
            if mat[i+r][j+c] != '-' and block[r][c] == ';':
                pass
            else:
                mat[i+r][j+c] = block[r][c]

    return True

## MAIN
blocks = [[] for j in range(0,7)]

# Blocks import
for j in range(0,7):
    blocks[j] = readblock(argv[j+1])

# Matrix creation
count = computedim(blocks)
l = int(count**(1.0/2))
mat = [['-' for i in range(0,l)] for j in range(0,l)]

# for it in permutations(blocks):
#     print(it)
#
# exit()

# Main loop
seed(None)
for t in range(0,100000):
    shuffle(blocks)
    matcopy = deepcopy(mat)

    stopb = False
    for b in range(0,7):
        # print(matcopy)
        stopi = False
        for i in range(0,l):
            for j in range(0,l):
                if place(blocks[b], matcopy, l, i, j) == True:
                    # print("Placed " + str(b) + "! " + "Pos:[" + str(i) + "," + str(j) + "]")
                    stopi = True
                    break
                else:
                    # print("NOT placed " + str(b) + "! " + "Pos:[" + str(i) + "," + str(j) + "]")
                    if i == l-1 and j == l-1:
                        stopb = True
                        break
            if stopi == True or stopb == True:
                break
        if stopb == True:
            break

    if stopb == False:
        # if checkmat(matcopy) == True:
        #     finalprint(matcopy)
        print("WIN")
        break

if stopb == True:
    print("LOSE")

print(matcopy)
