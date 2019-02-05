import os
fileDir = os.path.dirname(os.path.abspath(__file__))   # Directory of the Module
input = open(fileDir+"\Inputs\AOC25_1.txt", "r").read().splitlines()

program = []

for i in input:
    s = i.split()
    a = s[1]
    if s[1].isdigit() or s[1][0] == "-":
        a = int(s[1])
    if len(s) == 2:
        program.append([s[0],a])
    else:
        b = s[2]
        if s[2].isdigit() or s[2][0] == "-":
            b = int(s[2])
        program.append([s[0],a,b])

#for i in program: print(i)

def run(aVal):
    reg = {"a":aVal,"b":0,"c":0,"d":0}
    ip = 0
    series = []
    while ip < len(program):
        instr = program[ip]
        if instr[0] == "cpy":
            a = instr[1]
            if instr[1] in reg: a = reg[instr[1]]
            reg[instr[2]] = a
            ip += 1
        elif instr[0] == "inc":
            reg[instr[1]] += 1
            ip += 1
        elif instr[0] == "dec":
            reg[instr[1]] -= 1
            ip += 1
        elif instr[0] == "jnz":
            a = instr[1]
            if instr[1] in reg: a = reg[instr[1]]
            if a != 0:
                ip += instr[2]
            else:
                ip += 1
        elif instr[0] == "out":
            a = instr[1]
            if instr[1] in reg: a = reg[instr[1]]
            series.append(a)
            ip += 1
            if len(series) == 8: return series

def Part1():
    i = 0
    series = []
    while series != [0,1,0,1,0,1,0,1]:
        i = i+1
        series = run(i)
    print("Part 1:", i)

Part1()