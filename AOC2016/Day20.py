import os
from string import ascii_lowercase
fileDir = os.path.dirname(os.path.abspath(__file__))   # Directory of the Module
input = open(fileDir+"\Inputs\AOC20_1.txt", "r").read().splitlines()

ips = []

for i in input:
    s = i.split("-")
    ips.append([int(s[0]),int(s[1])])
ips.sort(key=lambda x: x[0])

#for i in ips:
    #print(i)

def Part12():
    ranges = [ips[0]]
    for i in range(1,len(ips)):
        if ips[i][0] <= ranges[len(ranges)-1][1]+1: #Ranges overlap
            if ips[i][1] > ranges[len(ranges)-1][1]: #Make sure range isnt inside, ignore if is
                 ranges[len(ranges)-1][1] = ips[i][1] #Extend range
        else:
            ranges.append(ips[i])

    print("Part 1:", ranges[0][1]+1)
    #for i in ranges: print(i)
    count = 0
    min, max = 0, 4294967295
    if ranges[0][0] > min: count += ranges[0][0]
    if ranges[len(ranges)-1][1] < max: count += (max - ranges[len(ranges)-1][1])
    for i in range(len(ranges)-1):
        count += (ranges[i+1][0] - ranges[i][1] - 1)
    print("Part 2:", count)
Part12()