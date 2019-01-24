import os
from string import ascii_lowercase
fileDir = os.path.dirname(os.path.abspath(__file__))   # Directory of the Module
input = open(fileDir+"\Inputs\AOC06_1.txt", "r").read().splitlines()

msg = []
for i in range(len(input[0])): msg.append([])

for j in input:
    for i in range(len(j)):
        msg[i].append(j[i])

def Part12():
    message = ""
    message2 = ""
    for i in msg:
        counts = []
        for lt in ascii_lowercase:
            counts.append([i.count(lt),lt])
        counts.sort(key=lambda x: (-x[0], x[1]))
        message += counts[0][1]
        message2 += counts[25][1]
    print("Part 1:", message)
    print("Part 2:", message2)

Part12()