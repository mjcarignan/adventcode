from collections import *
from re import X
import time

startTime = time.time()
#read file, get into useable format
file = open('./2021/1206/input.txt', 'r')
school = Counter([int(num) for num in file.read().split(',')])
file.close()

print(school)

for x,cnt in school.items():
    print(str(x)+": "+str(cnt))

def solve(S, n):
    X = S
    print(X)
    for day in range(n):
        Y = defaultdict(int)
        for x,cnt in X.items():
            if x==0:
                Y[6] += cnt
                Y[8] += cnt
            else:
                Y[x-1] += cnt
        X = Y
        print(X)
    return sum(X.values())

print(solve(school, 80))
print(solve(school, 256))

print("Total time: %s milliseconds" % round((time.time() - startTime)*1000, 3))