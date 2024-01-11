#!/usr/bin/python3

import random as rd
import numpy as np
import math

class Gen:

	def __init__(self, *args):
		if 3 == len(args):
			self.a = args[0]
			self.b = args[1]
			self.c = args[2]
		if 0 == len(args):
			self.a = rd.random()
			self.b = rd.random() * 1000 - 500
			self.c = rd.random() * 1000 - 500

	def getSaturation(self):
		return self.c

	def cross(x1, x2):
		if (rd.random() < 0.5) :
			if (rd.random() < 0.5):
				return x1
			else:
				return x2
		return (x1 + x2) / 2

	def mutate(self):
		if (rd.random() < 0.5):
			self.a = self.a + rd.random()*0.01-0.005
			if self.a < 0 :
				self.a = rd.random()
			if self.a > 1 :
				self.a = rd.random()
		if (rd.random() < 0.5):
			self.b = self.b + rd.random()* 4 - 2
		if (rd.random() < 0.5):
			self.c = self.c + rd.random()*4 -2

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
	g2 = Gen(0.5, 4, 5)

	g3 = g1.crossover(g2)
	print("Gen1", g1)
	print("Gen2", g2)
	print("Gen3", g3)
	g2.mutate()
	print("Mutiertes g2:", g2)

## test the Gen Class
if "__main__" == __name__:
	module_test()
