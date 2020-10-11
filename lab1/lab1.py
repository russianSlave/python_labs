def func (n):
    return 9/(n**2+7*n+12)

countForSumm = 160

sN = 0

for i in range(0,countForSumm+1):
    sN +=func(i)

print(sN)

i = 1
e = 0.00001
lastSN = 0
curSN = func(0)

while abs(lastSN-curSN) > e:
    lastSN = curSN
    curSN += func(i)
    i+=1

print("L = " + str(curSN))	
