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
		if 3 == len(args):
			self.a = args[0]
			self.b = args[1]
			self.c = args[2]
		if 0 == len(args):
			self.a = rd.random()
			self.b = rd.random()
			self.c = rd.random()

	def cross(x1, x2):
		if (rd.random() < 0.5) :
			if (rd.random() < 0.5):
				return x1
			else:
				return x2
		return (x1 + x2) / 2

	## A value is in 50% NOT mutated.
  ## The other 50% are split into
  ##  a) random
  ##  b) average of v and random
	def mutateValue(v):
		if(rd.random() < 0.5):
			return v
		if(rd.random() < 0.2):
			return rd.random()
		return (rd.random() + 3*v) / 4

	def mutate(self):
		self.a = Gen.mutateValue(self.a)
		self.b = Gen.mutateValue(self.b)
		self.c = Gen.mutateValue(self.c)
	
	def crossover(self, other):
		a = Gen.cross(self.a, other.a)
		b = Gen.cross(self.b, other.b)
		c = Gen.cross(self.c, other.c)
		return Gen(a, b, c)

	def __str__(self):
		return "(a={0}, b={1}, c={2})".format(self.a, self.b, self.c)

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
