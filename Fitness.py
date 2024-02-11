#!/usr/bin/python3


##
# ph. freimann
# 2024-01-27 Fitness functions
#

import math

import Gen as gen
import Point as pt
import PointList
import Saturation
import Circle
import Parabel

class Fitness:

	def __init__(self):
		self.circle     = Circle    .Circle    ()
		self.saturation = Saturation.Saturation()
		self.parabel    = Parabel   .Parabel   ()
		return

<<<<<<< HEAD
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
	
=======
	def fitnessFunctionCircle(self, pl, gen):
		return self.circle.fitness(pl, gen)

	def fitnessFunctionParabel(self, pl, gen):
		return self.parabel.fitness(pl, gen)

>>>>>>> 04b337c67618b651844b75a999627df4f6b30613
	def fitnessFunctionSaturation(self, pl, gen):
		return self.saturation.fitness(pl, gen)

	def fitnessFunction(self, pl, gen):
		if(gen.type < 0.33):
			return self.fitnessFunctionCircle(pl, gen)
		if(gen.type >= 0.33 and gen.type < 0.67):
			return self.fitnessFunctionSaturation(pl, gen)
		return self.fitnessFunctionParabel(pl, gen)

## module test #########
def testfunction():
	g = gen.Gen(0.5, 2, 4)
	pl = PointList.PointList()
	pl.addPoint(pt.Point(3, 4))
	pl.addPoint(pt.Point(4, 9))

	f = Fitness()
	print("Fitness: " , f.fitnessFunction(pl, g))

if "__main__" == __name__:
	testfunction()
