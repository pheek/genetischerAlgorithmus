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
B_MIN = -2000
B_MAX = 4000
C_MIN = 0
C_MAX = 2000

class Fitness:

	def __init__(self):
		return

	def stretch(v, min, max):
		a= max-min
		return a*v+min
	
	def saturation(self, a, b, c, x):
		AA = Fitness.stretch(a, A_MIN, A_MAX)
		BB = Fitness.stretch(b, B_MIN, B_MAX)
		CC = Fitness.stretch(c, C_MIN, C_MAX)
		
		return CC + BB * math.exp(x * math.log(AA))

	def fitnessFunction(self, pl, gen):
		diffSum = 0
		for pt in pl.getPointsArray():
			yIst = self.saturation(gen.a, gen.b, gen.c, pt.x)
			diffSum = diffSum + abs(pt.y - yIst)
		diff = 1.0/diffSum
		return diff

## module test
if "__main__" == __name__:
	g = gen.Gen(0.5, 2, 4)
	pl = PointList.PointList()
	pl.addPoint(pt.Point(3, 4))
	pl.addPoint(pt.Point(4, 9))

	f = Fitness()
	print("Fitness: " , f.fitnessFunction(pl, g))
