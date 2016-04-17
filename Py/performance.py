from timeit import default_timer as timer
import solution_zombits
import sandbox
from random import randint

def buildPopulation(x, y, sMax):
    population = [[randint(0,sMax) for j in range(y)] for i in range(x)]
    return population

def printArr(array):
    for i in range(len(array)):
        print(array[i])

n = 10000
size = 50
sMax = 9

p = []
p1 = []

for i in xrange(n):
	a = buildPopulation(size, size, sMax)
	b = randint(0, size-1)
	c = randint(0, size-1)
	d = randint(0, sMax)
	p.append([a, b, c, d])
	p1.append([a, b, c, d])

print('Ready... Go!')

start = timer()
while p:
    i = p.pop()
    a = 1 # solution_zombits.answer(i[0],i[1],i[2],i[3])
end = timer()
#print(start, end)
print(end-start)

start = timer()
while p1:
    i = p1.pop()
    a = 1 # sandbox.answer(i[0],i[1],i[2],i[3])
end = timer()
#print(start, end)
print(end-start)
#printArr(b)
