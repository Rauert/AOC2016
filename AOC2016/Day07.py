import os
from string import ascii_lowercase
fileDir = os.path.dirname(os.path.abspath(__file__))   # Directory of the Module
input = open(fileDir+"\Inputs\AOC07_1.txt", "r").read().splitlines()
#input = ["abba[mnop]qrst","abcd[bddb]xyyx","aaaa[qwer]tyui","ioxxoj[asdfgh]zxcvbn"]

IPs = []
for i in input:
    t = i.replace("["," ")
    t = t.replace("]"," ")
    t = t.split()
    outside = []
    inside = []
    for j in range(len(t)):
        if j % 2 == 0:
            outside.append(t[j])
        else:
            inside.append(t[j])
    IPs.append([outside, inside])

def hasABBA(data):
    #print(data)
    for i in data:
        if len(i) > 3:
            for c in range(len(i)-3):
                d = i[c:c+4]
                #print(d)
                if d == d[::-1] and d[0] != d[1]:
                    #print(d, d[::-1])
                    return True
    return False

def findSSL(data):
    rtn = []
    for i in data:
        if len(i) > 2:
            for c in range(len(i)-2):
                d = i[c:c+3]
                if d[0] == d[2] and d[0] != d[1]:
                    rtn.append(d)
    return rtn

def Part1():
    count = 0
    for i in IPs:
        if hasABBA(i[0]) == True and hasABBA(i[1]) == False:
            count +=1
    print("Part 1:", count)

def Part2():
    count = 0
    for i in IPs:
        oSSL = findSSL(i[0])
        iSSL = findSSL(i[1])
        if len(oSSL) > 0 and len(iSSL) > 0:
            ssl = False
            for a in oSSL:
                for b in iSSL:
                    if a[0] == b[1] and a[1] == b[0]: ssl = True
            if ssl: count +=1
    print("Part 2:", count)

Part1()
Part2()