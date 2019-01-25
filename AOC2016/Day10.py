import os, re
from string import ascii_lowercase
fileDir = os.path.dirname(os.path.abspath(__file__))   # Directory of the Module
input = open(fileDir+"\Inputs\AOC10_1.txt", "r").read().splitlines()

ins = [] #Format: [value,bot#]
bots = {} #Format: [[List of What its holding],[instructions]]
outs = {} #Format: [List of outputs]

for i in input:
    s = i.split()
    if len(s) == 6:
        print
        ins.append([int(s[1]),s[5]])
    else:
        bots[s[1]] = [[],[s[5],s[6],s[10],s[11]]]
        for o in [[s[5],s[6]],[s[10],s[11]]]:
            if o[0] == "output":
                outs[o[1]] = []

for i in ins:
    bots[i[1]][0].append(i[0])

def Part12():
    procQ = []
    for k,v in bots.items():
        if len(v[0]) == 2:
            procQ.append(k)

    while len(procQ) > 0:
        bot = procQ.pop()
        instr = bots[bot][1]
        if 61 in bots[bot][0] and 17 in bots[bot][0]:
            print("Part 1:", bot)
        bots[bot][0].sort()
        large = bots[bot][0].pop()
        small = bots[bot][0].pop()
        for o in [[instr[2],instr[3],large],[instr[0],instr[1],small]]:
            if o[0] == "bot":
                bots[o[1]][0].append(o[2])
                if len(bots[o[1]][0]) == 2: procQ.append(o[1])
            else:
                outs[o[1]].append(o[2])
    print("Part 2:", outs["0"][0] * outs["1"][0] * outs["2"][0])

Part12()