#!/usr/bin/python3

##
# ph. freimann
# 2024-01-27 Gen-Pool Modell
#

import random as rd
import numpy as np
import math
import Fitness as fitnClass

import Gen
import PointList


NR_OF_GENES             = 300
F_BEHALTEN              = 0.45   # 10 % keep
F_CROSSOVER             = 0.40   # 20 % crossover
F_MUTATE                = 0.10   # 50 % mutation, the rest are random new genes

F_GENERATIONS_PER_CLICK = 1
# der rest wird neu erschaffen

class Model:

	def __init__(self):
		self.pointList  = PointList.PointList()
		self.generation = 0
		self.genes      = []
		self.fitness    = fitnClass.Fitness()

	def getPointList(self):
		return self.pointList

	def appendPoint(self, p):
		self.pointList.addPoint(p)

	def getGeneArray(self):
		return self.genes

	def initGenes(self):
		for i in range(NR_OF_GENES):
			self.genes.append(Gen.Gen())

	def getBestGen(self):
		return self.genes[0]

	def crossoverSome(self, anzahl):
		print("in crossover: Erzeuge ", anzahl, ' neue Gene durch crossover.')
		neueGene = []
		for i in range(anzahl):
			elt1, elt2 = rd.sample(self.genes, 2)
			neueGene.append(elt1.crossover(elt2))
		self.genes = self.genes + neueGene


	def mutateSome(self, anzahl):
		print("Mutiere " , anzahl , " Gene")
		for i in range(anzahl):
			randomPosition = rd.randint(1, anzahl*(anzahl+1)/2)
			## enforce lower indices to be mutated more the higer positions
			modifiedPosition = round(math.sqrt(1+8*(randomPosition-1))/2)-1
			modifiedPosition = anzahl - modifiedPosition
			if modifiedPosition < 0:
				modifiedPosition = 0
			if modifiedPosition >= len(self.genes):
				modifiedPosition = len(self.genes)-1
			gen = self.genes[modifiedPosition]
			gencopy = Gen.Gen(gen.a, gen.b, gen.c)
			gencopy.mutate()
			self.genes.append(gencopy)

	def sortGenesByFitness(self):
		tempFitnessArray = []
		for g in self.genes:
			fitnessValue = self.fitness.fitnessFunction(self.pointList, g)
			tempFitnessArray.append(fitnessValue)
		combined_lists          = list(zip(tempFitnessArray, self.genes))
		sorted_combined_lists   = sorted(combined_lists, reverse=True, key=lambda x : x[0])
		sorted_corresponding_values = [value for _, value in sorted_combined_lists]

		self.genes = sorted_corresponding_values


		
	def nextGeneration(self):
		self.sortGenesByFitness()

		## die besten behalten
		behalten = round(NR_OF_GENES * F_BEHALTEN + 0.5)
		genescopy = self.genes
		self.genes = []
		for index in range(0, behalten-1):
			self.genes.append(genescopy[index])

		self.crossoverSome(round(NR_OF_GENES*F_CROSSOVER + 0.5))

		self.mutateSome(round(NR_OF_GENES*F_MUTATE + 0.5))

		## create new genes
		while len(self.genes) < NR_OF_GENES:
			self.genes.append(Gen.Gen())

			# do buddon start hit
	def nextGenerations(self):
		if self.generation < 2:
			self.generation = self.generation + 1
			self.initGenes()
		else:
			print("Next generation ", self.generation)
			for i in range(0, F_GENERATIONS_PER_CLICK):
				self.generation = self.generation + 1
				self.nextGeneration()
