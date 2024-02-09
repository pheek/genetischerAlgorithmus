#!/usr/bin/python3


##
# ph. freimann
# 2024-01-27 Fitness function
#

import Gen as gen
import Point as pt
import math
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

	# all gene values are between 0.0 and 1.0, so
  # they are stretched between min and max.
#	def stretch(v, min, max):
#		a= max-min
#		return a*v+min


	def fitnessFunctionCircle(self, pl, gen):
		return self.circle.fitness(pl, gen)
	
	def fitnessFunctionParabel(self, pl, gen):
		return self.parabel.fitness(pl, gen)
	
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
