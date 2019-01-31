import time

#Brute force, slow
def run2(num):
    elves = []
    for e in range(1,num+1):
        elves.append(e)
    i = 0
    #count = 0
    while len(elves) > 1:
        #count +=1
        #if count % 100000 == 0: print(len(elves))
        j = (i + int(len(elves)/2)) % len(elves)
        #print(elves)
        #print(elves[i],i+1,j+1,len(elves))
        #elves[i][1] += elves[j][1]
        #print("del",elves[j])
        if j < i: i -= 1
        del elves[j]
        i = (i + 1) % len(elves)
    return elves[0]

#Brute force, slow
def run(num):
    elves = [1 for e in range(num)]
    i = 0
    while max(elves) != num:
        if elves[i] > 0:
            j = (i + 1) % num
            while elves[j] < 1:
                j = (j + 1) % num
            if i == j:
                break
            else:
                elves[i] += elves[j]
                elves[j] = 0
        i = (i + 1) % num
    return elves.index(num)+1

def reduction(num):
    elves = []
    if num % 2 == 0:
        for e in range(1,num+1,2):
            elves.append([e,2])
    else:
        for e in range(1,num+1):
            elves.append([e,1])
    while len(elves) > 1:
        if len(elves) % 2 == 0: #Even
            for i in reversed(range(0,len(elves),2)):
                elves[i][1] += elves[i+1][1]
                del elves[i+1]
        else: #odd
            for i in reversed(range(0,len(elves)-1,2)):
                elves[i][1] += elves[i+1][1]
                del elves[i+1]
            elves[len(elves)-1][1] += elves[0][1]
            del elves[0]
        #print(len(elves))
    return elves[0][0]

#https://www.reddit.com/r/adventofcode/comments/5j4lp1/2016_day_19_solutions/
#Alt solution using LL
class Node:
  def __init__(self,id):
    self.id  = id
    self.nxt = None
    self.prv = None

  def delete(self):
    self.prv.nxt = self.nxt
    self.nxt.prv = self.prv

def solve(n):
  l = list(map(Node, range(n)))
  for i in range(n):
    l[i].nxt = l[(i+1)%n]
    l[i].prv = l[(i-1)%n]

  start = l[0]
  mid   = l[int(n/2)]

  for i in range(n-1):
    mid.delete()
    mid = mid.nxt
    if (n-i)%2==1: mid = mid.nxt
    start = start.nxt

  return start.id+1

#print(solve(3018458))

now = time.time()
print("Part 1:", reduction(3018458)) #64 sec
print("Part 2:", run2(3018458)) #410 sec
print("Time taken: " + str(time.time() - now))