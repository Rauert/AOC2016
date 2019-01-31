import os
from string import ascii_lowercase
fileDir = os.path.dirname(os.path.abspath(__file__))   # Directory of the Module
input = open(fileDir+"\Inputs\AOC21_1.txt", "r").read().splitlines()

inst = []

for i in input:
    s = i.split()
    if s[0] == "swap":
        if s[1] == "position": inst.append([s[0] + s[1][0], int(s[2]), int(s[5])])
        else: inst.append([s[0] + s[1][0], s[2], s[5]])
    elif s[0] == "rotate":
        if s[1] == "based": inst.append([s[0], s[6]])
        else: inst.append([s[0] + s[1][0], int(s[2])])
    elif s[0] == "reverse": inst.append([s[0], int(s[2]), int(s[4])])
    elif s[0] == "move": inst.append([s[0], int(s[2]), int(s[5])])


#for i in ips:
    #print(i)

def Part12():
    pw = "abcdefgh"
    for i in inst:
        if i[0] == "swapp":
            pw[i[1]], pw[i[2]] = pw[i[2]], pw[i[1]]
        elif i[0] == "swapl":
            pw[pw.index(i[1])], pw[pw.index(i[2])] = pw[pw.index(i[2])], pw[pw.index(i[1])]
        elif i[0] == "rotatel":
        elif i[0] == "rotater":
        elif i[0] == "rotate":
        elif i[0] == "reverse":
            pw[i[1]:i[2]+1] = pw[i[1]:i[2]+1][::-1]
        elif i[0] == "move":

    print("Part 2:")
Part12()