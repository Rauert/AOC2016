import os
from copy import deepcopy
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

def Part1():
    pw = "abcdefgh"
    for i in inst:
        #print(pw)
        #print(i)
        if i[0] == "swapp":
            a, b = i[1], i[2]
            if a > b: a, b = i[2], i[1]
            pw = pw[0:a] + pw[b] + pw[a+1:b] + pw[a] + pw[b+1:]
        elif i[0] == "swapl":
            a, b = pw.index(i[1]), pw.index(i[2])
            if a > b: a, b = pw.index(i[2]), pw.index(i[1])
            pw = pw[0:a] + pw[b] + pw[a+1:b] + pw[a] + pw[b+1:]
        elif i[0] == "rotatel":
            for j in range(i[1]): pw = pw[1:] + pw[0]
        elif i[0] == "rotater":
            for j in range(i[1]): pw = pw[len(pw)-1] + pw[0:len(pw)-1]
        elif i[0] == "rotate":
            count = pw.index(i[1])
            if count >= 4: count += 1
            count += 1
            for j in range(count): pw = pw[len(pw)-1] + pw[0:len(pw)-1]
        elif i[0] == "reverse":
            pw = pw[0:i[1]] + pw[i[1]:i[2]+1][::-1] + pw[i[2]+1:]
        elif i[0] == "move":
            tmp = pw[i[1]]
            pw = pw[0:i[1]] + pw[i[1]+1:]
            pw = pw[0:i[2]] + tmp + pw[i[2]:]
        #print(pw)
    print("Part 1:", pw)

def Part2():
    pw = "fbgdceah"
    for i in reversed(inst):
        #print(pw)
        #print(i)
        if i[0] == "swapp":
            a, b = i[1], i[2]
            if a > b: a, b = i[2], i[1]
            pw = pw[0:a] + pw[b] + pw[a+1:b] + pw[a] + pw[b+1:]
        elif i[0] == "swapl":
            a, b = pw.index(i[1]), pw.index(i[2])
            if a > b: a, b = pw.index(i[2]), pw.index(i[1])
            pw = pw[0:a] + pw[b] + pw[a+1:b] + pw[a] + pw[b+1:]
        elif i[0] == "rotatel":
            for j in range(i[1]): pw = pw[len(pw)-1] + pw[0:len(pw)-1]
        elif i[0] == "rotater":
            for j in range(i[1]): pw = pw[1:] + pw[0]
        #Need to condider location of char after rotation.
        elif i[0] == "rotate":
            indx = pw.index(i[1])
            if indx in [0,1]:
                for j in range(1): pw = pw[1:] + pw[0]
            elif indx == 2:
                for j in range(2): pw = pw[len(pw)-1] + pw[0:len(pw)-1]
            elif indx == 3:
                for j in range(2): pw = pw[1:] + pw[0]
            elif indx == 4:
                for j in range(1): pw = pw[len(pw)-1] + pw[0:len(pw)-1]
            elif indx == 5:
                for j in range(3): pw = pw[1:] + pw[0]
            elif indx == 7:
                for j in range(4): pw = pw[len(pw)-1] + pw[0:len(pw)-1]
        elif i[0] == "reverse":
            pw = pw[0:i[1]] + pw[i[1]:i[2]+1][::-1] + pw[i[2]+1:]
        elif i[0] == "move":
            tmp = pw[i[2]]
            pw = pw[0:i[2]] + pw[i[2]+1:]
            pw = pw[0:i[1]] + tmp + pw[i[1]:]
        #print(pw)
    print("Part 2:", pw)

Part1()
Part2()