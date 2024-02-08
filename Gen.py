#!/usr/bin/python3

##
# ph. freimann
# 2024-01-27 Gen for genetic algorithm
# attributes
# type <0.5: circle
#      >0.5: saturation
# saturation: a, b, c mean     c  + b*a^x
# circle    : a, b, c mean     (a,b) as midpoint and c as radius

import random as rd
from numpy import random as nrp
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
		## je 40% for x1 or x2
		if rd.random() < 0.4:
			return x1
		if rd.random() < 0.667:
		  return x2
	  ## 20 % for between those two
		return (x1 + rd.random()*(x2-x1))

	## Muate in different ways
	def mutateValue(v):
		## 5%: complete new mutation
		if(rd.random() < 0.05):
			return rd.random()
		## 80% don't change
		if(rd.random() < 0.8):
			return v
		## binomial distribution betwenn 0.0 and 1.1 nearest to existing v
		newv = float((nrp.binomial(n=200, p=v, size=1) / 200)[0])
		if newv < 0.000001:
			return 0.000001
		if newv > 0.999999:
			return 0.999999
		return newv
		

	def mutate(self):
		self.type = Gen.mutateValue(self.type)
		self.a    = Gen.mutateValue(self.a)
		self.b    = Gen.mutateValue(self.b)
		self.c    = Gen.mutateValue(self.c)

	## crossover is applied using the multiply operator *
	## newGen = firstElder * secondElder
	def __mul__(self, other):
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

	## crossover g3 = child of g1 and g2
	g3 = g1 * g2
	print("Gen1", g1)
	print("Gen2", g2)
	print("Gen3", g3)
	g2.mutate()
	print("Mutiertes g2:", g2)

## test the Gen Class
if "__main__" == __name__:
	module_test()
