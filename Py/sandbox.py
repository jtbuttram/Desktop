from random import randint

def buildPopulation(x,y):
	population = [[randint(0,9) for j in range(y)] for i in range(x)]
	return population

def printArr(array):
	for i in range(len(array)):
		print(array[i])

def answer(population, x, y, strength):
	vector = []
	xMax = len(population[0])-1
	yMax = len(population)-1
	if population[y][x] <= strength:
		population[y][x] = -1
		vector.append([x,y])
	while vector:
		thisRabbit = vector.pop()
		x = thisRabbit[0]
		y = thisRabbit[1]
		if x != 0:
			if population[y][x-1] != -1:
				if population[y][x-1] <= strength:
					population[y][x-1] = -1
					vector.append([x-1,y])
		if y != 0:
			if population[y-1][x] != -1:
				if population[y-1][x] <= strength:
					population[y-1][x] = -1
					vector.append([x,y-1])
		if x != xMax:
			if population[y][x+1] != -1:
				if population[y][x+1] <= strength:
					population[y][x+1] = -1
					vector.append([x+1,y])
		if y != yMax:
			if population[y+1][x] != -1:
				if population[y+1][x] <= strength:
					population[y+1][x] = -1
					vector.append([x,y+1])
	return population

def answer_1(population, x, y, strength):
	vector = []
	xMax = len(population[0])-1
	yMax = len(population)-1
	if population[y][x] <= strength:
		population[y][x] = -1
		vector.append([x,y]) # changed this to tuple instead of list
	while vector:
		thisRabbit = vector.pop()
		x = thisRabbit[0]
		y = thisRabbit[1]
		if x != 0:
			if population[y][x-1] != -1:
				if population[y][x-1] <= strength:
					population[y][x-1] = -1
					vector.append([x-1,y])
		if y != 0:
			if population[y-1][x] != -1:
				if population[y-1][x] <= strength:
					population[y-1][x] = -1
					vector.append([x,y-1])
		if x != xMax:
			if population[y][x+1] != -1:
				if population[y][x+1] <= strength:
					population[y][x+1] = -1
					vector.append([x+1,y])
		if y != yMax:
			if population[y+1][x] != -1:
				if population[y+1][x] <= strength:
					population[y+1][x] = -1
					vector.append([x,y+1])
	return population