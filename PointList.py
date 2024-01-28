#!/usr/bin/python3


##
# ph. freimann
# 2024-01-27 List of points including fitting function
# todo: separate fitness into own class
#

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

	def __str__(self):
		dotsStrings = ""
		for point in self.pointArray:
			dotsStrings = dotsStrings + " " + point.__str__()
		return dotsStrings
		
## module test
if "__main__" == __name__:
	pointList = PointList()
	pointList.addPoint(pt.Point(3, 4))
	pointList.addPoint(pt.Point(4, 9))

	print("Points: " , pointList)
