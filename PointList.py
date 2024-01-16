#!/usr/bin/python3

import Gen as gen
import Point as pt
import math

class PointList:

	def __init__(self):
		self.pointArray  = []

	def addPoint(self, p):
		self.pointArray.append(p)

	def getPointsArray(self):
		return self.pointArray
		
	def f(self, a, b, c, x):
		return c + b * math.exp(x * math.log(a))
	
	def fitnessFunction(self, gen):
		diff = 0
		for pt in self.pointArray:
			yIst = self.f(gen.a, gen.b, gen.c, pt.x)
			diff = diff + abs(pt.y - yIst)
			fitness = 1.0/diff
		return fitness

## module test
if "__main__" == __name__:
	g = gen.Gen(0.5, 2, 4)
	pl = PointList()
	pl.addPoint(pt.Point(3, 4))
	pl.addPoint(pt.Point(4, 9))

	print("Fitness: " , pl.fitnessFunction(g))
