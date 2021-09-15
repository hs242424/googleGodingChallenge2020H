import math

def isboring(number):
    count = []
    for i in range(1, (int(math.log10(number))+1)+1):
        # print(str(number)[i])
        if int(i % 2) == (int(str(number)[i-1]) % 2):
            count.append(1)
    if len(count) == int(math.log10(number))+1:
        return True

def isboringrange(startnum, endnum):
    boringlist = []
    for number in range(startnum, endnum+1):
        if isboring(number) == True:
            boringlist.append(number)
    return boringlist


t = int(input())
for i in range(1, t+1):
    start, end = map(int, input().split())
    print(f"Case #{t}: {len(isboringrange(start, end))}")