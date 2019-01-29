from hashlib import md5
import time, math

key = "ihaygndm"
#key = "abc"

def testMD5(index):
    bool = False
    md = md5((key+str(index)).encode()).hexdigest()
    triple = ""
    for c in range(len(md)-2):
        if md[c:c+3].count(md[c]) == 3:
            triple = md[c]
            break
    for i in range(index+1,index+1+1000):
        md = md5((key+str(i)).encode()).hexdigest()
        for c in range(len(md)-4):
            #print(md[c:c+5])
            if md[c:c+5].count(triple) == 5:
                bool = True
                break
    if bool: print("Valid",index)
    else: print("Invalid",index, md5((key+str(index)).encode()).hexdigest())

def runMD(P2):
    now = time.time()
    i = 0
    dict = {}
    keyIndexes = []
    while len(keyIndexes) < 64:
        md = md5((key+str(i)).encode()).hexdigest()
        if P2:
            for _ in range(2016):
                md = md5((md).encode()).hexdigest()
        #print(md)
        for c in range(len(md)-2):
            #print(md[c:c+3])
            if md[c:c+3].count(md[c]) == 3:
                if md[c] not in dict:
                    dict[md[c]] = [i]
                else:
                    dict[md[c]].append(i)
                break
        for c in range(len(md)-4):
            #print(md[c:c+5])
            if md[c:c+5].count(md[c]) == 5:
                if md[c] in dict:
                    for v in dict[md[c]]:
                        if i - int(v) <= 1001 and v not in keyIndexes and i != v:
                            keyIndexes.append(v)
        i+=1
    keyIndexes.sort()
    #print(keyIndexes,len(keyIndexes))
    #for f in keyIndexes:
    #    testMD5(f)
    if P2:
        print("Part 2:",keyIndexes[63])
    else:
        print("Part 1:",keyIndexes[63])
    print("Time taken: " + str(time.time() - now))

runMD(False)
runMD(True)