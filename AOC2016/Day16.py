import time
def checksum(data):
    chk = ""
    for i in range(0,len(data),2):
        if data[i] == data[i+1]: chk += "1"
        else: chk += "0"
    return chk

def run(data,length):
    while len(data) < length:
        nextData = data + "0"
        for i in reversed(data):
            if i == "0": nextData += "1"
            else: nextData += "0"
        data = nextData
    data = data[0:length]
    chk = checksum(data)
    while len(chk) % 2 == 0:
        chk = checksum(chk)
    return chk

now = time.time()
print("Part 1:", run("11101000110010100",272))
print("Part 2:", run("11101000110010100",35651584))
print("Time taken: " + str(time.time() - now))