import os
from string import ascii_lowercase
fileDir = os.path.dirname(os.path.abspath(__file__))   # Directory of the Module
input = open(fileDir+"\Inputs\AOC04_1.txt", "r").read().splitlines()
#input = ["aaaaa-bbb-z-y-x-123[abxyz]","a-b-c-d-e-f-g-h-987[abcde]","not-a-real-room-404[oarel]","totally-real-room-200[decoy]"]
rooms = []
for i in input:
    r = i[0:-1].split("[")
    rooms.append([r[0][0:len(r[0])-4],int(r[0][len(r[0])-3:]),r[1]])

def Part12():
    count = 0
    for i in rooms:
        counts = []
        for lt in ascii_lowercase:
            counts.append([i[0].count(lt),lt])
        counts.sort(key=lambda x: (-x[0], x[1]))
        code = ""
        for j in range(5): code += counts[j][1]
        if code == i[2]:
            count += i[1]
            #Part 2
            decoded = ""
            for k in i[0]:
                if k == "-":
                    decoded += " "
                else:
                    decoded += ascii_lowercase[(ascii_lowercase.index(k) + i[1]) % len(ascii_lowercase)]
            if decoded == "northpole object storage":
                print("Part 2:", i[1])
        #counts = sorted(counts, key=lambda x: (x[0], sorted(x[1])),reverse=True)
    print("Part 1:", count)

Part12()