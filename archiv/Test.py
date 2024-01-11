#!/usr/bin/python3

import tkinter as tk
import random as rd
import numpy as np
import math


NR_OF_GENES      = 100
F_BEHALTEN       = 0.45
F_CROSSOVER      = 0.45
F_MUTATE         = 0.50
# der rest wird neu erschaffen


root = tk.Tk()

pointList = []

generation = 0
genes = []

def initGenes(pointList):
	global genes
	for i in range(NR_OF_GENES):
		#print("i=" , i);
		a = rd.random()
		b = rd.random() * 1000 - 500
		c = rd.random() * 1000 - 500
		genes.append((a, b, c))

def fitnessFunction(gene, pointList):
	a = gene[0]
	b = gene[1]
	c = gene[2]
	diff = 0
	for pt in pointList:
		x=pt[0]
		ySoll=pt[1]
		yIst = f(a, b, c, x)
		diff = diff + abs(ySoll - yIst)
	fitness = 1.0/diff
#	print("fitness = ", fitness)
	return fitness


def crossOverTwo(g1, g2):
	gNeu = []
	gNeu.append(rd.uniform(g1[0], g2[0]))
	stdev = abs(g1[1] - g2[1]) / 2.0;
	gNeu.append(np.random.normal((g1[1]+g2[1]) / 2, stdev))
	stdev = abs(g1[2] - g2[2]) / 2.0;
	gNeu.append(np.random.normal( (g1[2] - g2[2]) / 2, stdev))
	return (gNeu[0], gNeu[1], gNeu[2])

def crossoverSome(genes, anzahl):
	print("in crossover: Erzeuge ", anzahl, ' neue Gene durch crossover.')
	neueGene = []
	for i in range(anzahl):
		elt1, elt2 = rd.sample(genes, 2)
		neueGene.append(crossOverTwo(elt1, elt2))
	return neueGene

def mutiereSingle(gen):
	ggg = [gen[0], gen[1], gen[2]]
	idx = rd.randint(0,2)
	if idx == 0:
		ggg[idx] = rd.random()
	if idx > 0:
		ggg[idx] = rd.randint(-5000, 5000) / 10.0
	return (ggg[0], ggg[1], ggg[2])

def mutateSome(gene, anzahl):
	print("Mutiere " , anzahl , " Gene")
	nextMutation = -1
	for i in range(anzahl):
		mutiert = mutiereSingle(gene[nextMutation])
		gene[nextMutation] = mutiert
	return gene

def nextGeneration(pointList):
	global genes
	global F_BEHALTEN
	global F_CROSSOVER
	global F_MUTATE

	fitness = []
	for g in genes:
		fitness.append(fitnessFunction(g, pointList))
		#print("fitheit von gen " , g, " ist " , fitness[-1])

	## sortiere gene nach der fitness in "fitness"
	allinone = sorted(zip(fitness, genes), reverse=True)
	genes = []
	for line in allinone:
		genes.append(line[1])

	#print(genes)

	## behalte 50%
	anzGene = len(genes)
	behalten = round(anzGene * F_BEHALTEN + 0.5)

	genescopy = genes
	genes = []
	for index in range(0, behalten-1):
		genes.append(genescopy[index])

	print("vor crossover")
	#print(genes)

	neueGene = crossoverSome(genes, round(anzGene*F_CROSSOVER + 0.5))
	genes = genes + neueGene
	print("nach crossover")

	#print(genes)

	genes = mutateSome(genes, round(anzGene*F_MUTATE*F_CROSSOVER + 0.5))

	while len(genes) < NR_OF_GENES:
		a = rd.random()
		b = rd.random() * 2000 - 1000
		c = rd.random() * 2000 - 1000
		genes.append((a, b, c))

	# erzeuge neue Elemente

def f(a, b, c, x):
	return c + b * math.exp(x * math.log(a))

def drawFunction(g, colcol, widthi=1):
	global canvas
	a= g[0]
	b= g[1]
	c= g[2]
	#print("a=", a," b=",b, "   c=", c)

	for x in range(800):
		y1 = f(a, b, c, x)
		y2 = f(a, b, c, x+1)
		canvas.create_line(x, y1, x+1, y2, fill=colcol, width=widthi)

def drawAllFunctions():
	global genes
	for g in genes:
		drawFunction(g, 'blue')
	drawFunction(genes[0], 'red', 3)

# do buddon start hit
def doButtonStartHit(event):
	global canvas
	global generation
	global genes
	global pointList

	canvas.delete("all")

	print("Button Start hit")
	for point in pointList:
		print("Point (" , point[0], "|" , point[1] , ")")
	generation = generation + 1
	if 1==generation:
		initGenes(pointList)
	else:
		print("Next generation ", generation)
		for i in range(0, 100):
			nextGeneration(pointList)
	drawAllFunctions()
	print("Generation " , generation*100 , " erreicht.")
	# show do original dots
	for p in pointList:
		coord = p[0]-2, p[1]-2, p[0]+2, p[1]+2
		canvas.create_oval(coord, fill='yellow')


def dotHitInCanvas(event):
	print("I am hit at ", event.x, ", ", event.y)
	point = [event.x, event.y]
	pointList.append(point)
	coord = event.x-1, event.y+1, event.x+1, event.y-1
	canvas.create_oval(coord, fill='blue')


#frame = tk.Frame(root, width=800, height=800, bg='blue')
#frame.place(relwidth=1, relheight=1)

canvas = tk.Canvas(root, bg='#ccccff', )
canvas.pack()
canvas.bind('<Button>', dotHitInCanvas)

buttonStart = tk.Button(root, text="Start")
buttonStart.pack()
buttonStart.bind('<Button>', doButtonStartHit)


root.mainloop()
