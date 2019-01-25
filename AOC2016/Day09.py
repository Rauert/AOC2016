import os, re
from string import ascii_lowercase
fileDir = os.path.dirname(os.path.abspath(__file__))   # Directory of the Module
input = open(fileDir+"\Inputs\AOC09_1.txt", "r").read()
#input = "(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"

def Part1():
    out = ""
    i = 0
    while i < len(input):
        if input[i] == "(":
            j = i+1
            while input[j] != ")": j+=1 #Find closing
            marker = input[i+1:j].split("x")
            chars = int(marker[0])
            repeat = int(marker[1])
            #print(marker,chars,repeat,i)
            #print(len(input[j+1:j+1+chars]), input[j+1:j+1+chars])
            for _ in range(repeat):
                out += input[j+1:j+1+chars]
            i = j+1 + chars
        else:
            out += input[i]
            i += 1
    print("Part 1:", len(out))

#Memory error
def recurseRun(data):
    out = ""
    i = 0
    while i < len(data):
        if data[i] == "(":
            j = i+1
            while data[j] != ")": j+=1 #Find closing
            marker = data[i+1:j].split("x")
            chars = int(marker[0])
            repeat = int(marker[1])
            #print(marker,chars,repeat,i)
            #print(len(data[j+1:j+1+chars]), data[j+1:j+1+chars])
            temp = ""
            for _ in range(repeat):
                temp += data[j+1:j+1+chars]
            out += recurseRun(temp)
            i = j+1 + chars
        else:
            out += data[i]
            i += 1
    return out

#Super slow
def Part2(data):
    out = ""
    i = 0
    while data.count("(") > 0:
        print("(:",data.count("("))
        while i < len(data):
            if data[i] == "(":
                j = i+1
                while data[j] != ")": j+=1 #Find closing
                marker = data[i+1:j].split("x")
                chars = int(marker[0])
                repeat = int(marker[1])
                #print(marker,chars,repeat,i)
                #print(len(data[j+1:j+1+chars]), data[j+1:j+1+chars])
                for _ in range(repeat):
                    out += data[j+1:j+1+chars]
                i = j+1 + chars
            else:
                out += data[i]
                i += 1
        data = out
        print(len(data))
    print("Part 2:", len(data))

#Alternative 
def recursiveCount(data):
    count = 0
    i = 0
    while i < len(data):
        if data[i] == "(":
            j = i+1
            while data[j] != ")": j+=1 #Find closing
            marker = data[i+1:j].split("x")
            chars = int(marker[0])
            repeat = int(marker[1])
            #print(marker,chars,repeat,i)
            #print(len(input[j+1:j+1+chars]), input[j+1:j+1+chars])
            count += repeat * recursiveCount(data[j+1:j+1+chars])
            i = j+1 + chars
        else:
            count += 1
            i += 1
    return count

Part1()
#print("Part 2:", len(recurseRun(input)),recurseRun(input))
#Part2(input)
print("Part 2:", recursiveCount(input))