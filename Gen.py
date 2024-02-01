#!/usr/bin/python3

##
# ph. freimann
# 2024-01-27 Gen for genetic algorithm
# a in 0..1 is the base of the exopnetial saturation function
# b,c are saturation and starting saturation-difference

import random as rd
#import math

class Gen:

	def __init__(self, *args):
		self.type = rd.random()
		if 3 == len(args):
			self.a = args[0]
			self.b = args[1]
			self.c = args[2]
		if 0 == len(args):
			self.a = rd.random()
			self.b = rd.random()
			self.c = rd.random()
 
	def cross(x1, x2):
		if rd.random() < 0.4:
			return x1
		if rd.random() < 0.24:
		  return x2
		return (x1 + rd.random()*(x2-x1))

	## 40 % are not mutated
  ##  6 % (10 % of the remaining 60%) are completly random
  ## the rest is near the old value, but mutated
	def mutateValue(v):
		if(rd.random() < 0.4):
			return v
		if(rd.random() < 0.1):
			return rd.random()
		return (rd.random() + 8*v) / 9

	def mutate(self):
		self.type = Gen.mutateValue(self.type)
		self.a    = Gen.mutateValue(self.a)
		self.b    = Gen.mutateValue(self.b)
		self.c    = Gen.mutateValue(self.c)
		
	def crossover(self, other):
		newGen = Gen()
		newGen.type = Gen.cross(self.type, other.type)
		newGen.a    = Gen.cross(self.a   , other.a)
		newGen.b    = Gen.cross(self.b   , other.b)
		newGen.c    = Gen.cross(self.c   , other.c)
		return newGen
		

	def __str__(self):
		if(self.type < 0.5):
			tName = "Circle"
		else:
			tName = "Saturation"
		return "(type={0} a={1}, b={2}, c={3})".format(tName, self.a, self.b, self.c)

##  Modultest
def module_test():
	g1 = Gen()
	g2 = Gen(0.5, 0.4, 0.9)

	g3 = g1.crossover(g2)
	print("Gen1", g1)
	print("Gen2", g2)
	print("Gen3", g3)
	g2.mutate()
	print("Mutiertes g2:", g2)

## test the Gen Class
if "__main__" == __name__:
	module_test()
