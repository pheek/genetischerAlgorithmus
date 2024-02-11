#!/usr/bin/python3


##
# ph. freimann
# 2024-01-27 Fitness function
#

import Gen as gen
import Point as pt
import math
import PointList

A_MIN = 0.00001
A_MAX = 1.0
B_MIN = -4000
B_MAX = 6000
C_MIN = 0
C_MAX = 1200

class Fitness:

	def __init__(self):
		return

	# all gene values are between 0.0 and 1.0, so
  # they are stretched between min and max.
	def stretch(v, min, max):
		a= max-min
		return a*v+min

	
	def saturationValue(self, a, b, c, x):
		AA = Fitness.stretch(a, A_MIN, A_MAX)
		BB = Fitness.stretch(b, B_MIN, B_MAX)
		CC = Fitness.stretch(c, C_MIN, C_MAX)
		
		return CC + BB * math.exp(x * math.log(AA))

	def circleValue(self, a, b, c, x):
		## NOT YET
		return

	def fitnessFunctionCircle(self, pl, gen):
		return self.fitnessFunctionSaturation(pl, gen)
	
	def fitnessFunctionSaturation(self, pl, gen):
		diffSum = 0
		for pt in pl.getPointsArray():
			yIst = self.saturationValue(gen.a, gen.b, gen.c, pt.x)
			diffSum = diffSum + abs(pt.y - yIst)
		diff = 1.0/diffSum
		return diff

	def fitnessFunction(self, pl, gen):
		if(gen.type < 0.5):
			return self.fitnessFunctionCircle(pl, gen)
		else:
			return self.fitnessFunctionSaturation(pl, gen)


## module test
if "__main__" == __name__:
	g = gen.Gen(0.5, 2, 4)
	pl = PointList.PointList()
	pl.addPoint(pt.Point(3, 4))
	pl.addPoint(pt.Point(4, 9))

	f = Fitness()
	print("Fitness: " , f.fitnessFunction(pl, g))
