from hashlib import md5
import time, math

key = "uqwqemis"

def Part1():
    now = time.time()
    i = 0
    pw = ""
    while True:
        md = md5((key+str(i)).encode()).hexdigest()
        if md[0:5] == "00000":
            print(md)
            pw += md[5:6]
            if len(pw) == 8:
                break
        i+=1
    print("Part 1:", pw)
    print("Time taken: " + str(time.time() - now))

def Part2():
    now = time.time()
    i = 0
    pw = ["","","","","","","",""]
    while True:
        md = md5((key+str(i)).encode()).hexdigest()
        if md[0:5] == "00000":
            print(md)
            if md[5:6].isdigit():
                loc = int(md[5:6])
                if loc < 8:
                    if pw[loc] == "":
                        pw[loc] = md[6:7]
                        if len("".join(pw)) == 8:
                            break
        i+=1
    print("Part 2:", "".join(pw))
    print("Time taken: " + str(time.time() - now))

#Part1()
Part2()