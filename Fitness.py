#!/usr/bin/python3


##
# ph. freimann
# 2024-01-27 Fitness function
#

import Gen as gen
import Point as pt
import math
import PointList

class Fitness:

	def __init__(self):
		return

	def saturation(self, a, b, c, x):
		return c*4000 + 8000*(b-0.5) * math.exp(x * math.log(a))

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
