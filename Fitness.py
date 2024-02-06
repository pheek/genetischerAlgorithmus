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

class Fitness:

	def __init__(self):
		return

	# all gene values are between 0.0 and 1.0, so
  # they are stretched between min and max.
#	def stretch(v, min, max):
#		a= max-min
#		return a*v+min



	def fitnessFunctionCircle(self, pl, gen):
		## TODO Fitness for cicle
		return Circle.Circle.fitness(pl, gen)
	
	def fitnessFunctionSaturation(self, pl, gen):
		return Saturation.Saturation.fitness(pl, gen)
		
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
