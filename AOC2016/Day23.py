import os, math
fileDir = os.path.dirname(os.path.abspath(__file__))   # Directory of the Module
input = open(fileDir+"\Inputs\AOC23_1.txt", "r").read().splitlines()

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

def Part1():
    reg = {"a":7,"b":0,"c":0,"d":0}
    ip = 0
    while ip < len(program):
        instr = program[ip]
        #if ip in [20]:
        #    print(instr)
        #    print(reg)
        if instr[0] == "cpy":
            a = instr[1]
            if instr[1] in reg: a = reg[instr[1]]
            if isinstance(instr[2],str): reg[instr[2]] = a
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
            b = instr[2]
            if instr[2] in reg: b = reg[instr[2]]
            if a != 0: #and isinstance(instr[2],int):
                ip += b
            else:
                ip += 1
        elif instr[0] == "tgl":
            if ip+reg[instr[1]] < len(program):
                modInstr = program[ip+reg[instr[1]]]
                if len(modInstr) == 2:
                    if modInstr[0] == "inc": program[ip+reg[instr[1]]] = ["dec", modInstr[1]]
                    else: program[ip+reg[instr[1]]] = ["inc", modInstr[1]]
                else:
                    if modInstr[0] == "jnz": program[ip+reg[instr[1]]] = ["cpy", modInstr[1], modInstr[2]]
                    else: program[ip+reg[instr[1]]] = ["jnz", modInstr[1], modInstr[2]]
            ip += 1
    print("Part 1:", reg["a"])

#Analysis shows that program is calculating factorial and then adding a constant
def Part2(num):
    return math.factorial(num) + (95*73)

Part1()
print("Part 2:", Part2(12))