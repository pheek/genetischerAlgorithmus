#!/usr/bin/python3

import random as rd
import numpy as np
import math

import Gen
import PointList

NR_OF_GENES             = 100
F_BEHALTEN              = 0.30
F_CROSSOVER             = 0.30
F_MUTATE                = 0.20
F_GENERATIONS_PER_CLICK = 1
# der rest wird neu erschaffen

class Model:

	def __init__(self):
		self.pointList  = PointList.PointList()
		self.generation = 0
		self.genes      = []

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
			randomPosition = rd.randint(0, anzahl-1)
			gen = self.genes[randomPosition]
			gencopy = Gen.Gen(gen.a, gen.b, gen.c)
			gencopy.mutate()
			self.genes.append(gencopy)

	def sortGenesByFitness(self):
		fitness = []
		for g in self.genes:
			fitness.append(self.pointList.fitnessFunction(g))
		#print("all fitness berechnent", fitness)
#		for i in range(len(self.genes)):
#			print("Fitness for gen: ", self.genes[i], " is " , fitness[i])

		combined_lists          = list(zip(fitness, self.genes))
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
