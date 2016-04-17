import math

def answer(x):
	minions = 0
	for i in range(x+1):
		minions += pow(7,i)
	return minions

for i in range(11):
	a = answer(i)
	print(a)