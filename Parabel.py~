# (c) ph. freimann 2024
# Detect and draw an saturation function
#

import MainFrame
import Shape as sh
import math

A_MIN = 0.0000001
A_MAX = 0.9999999
B_MIN = -4000
B_MAX = 6000
C_MIN = 0
C_MAX = 1200

STEPWIDTH = 7

class Saturation(sh.Shape):

	def __init__(self):
		super().__init__()

	def saturationValue(self, gen, x):
		AA = self.stretch(gen.a, A_MIN, A_MAX)
		BB = self.stretch(gen.b, B_MIN, B_MAX)
		CC = self.stretch(gen.c, C_MIN, C_MAX)
		return CC + BB * math.exp(x * math.log(AA))

#	@staticmethod
	def draw(self, fwidth, canvas, gen, colcol, widthi=1):
		for step in range((int)((fwidth + STEPWIDTH-1)/ STEPWIDTH)):
			x = (int)(step * STEPWIDTH)
			y1 = self.saturationValue(gen, x)
			y2 = self.saturationValue(gen, x+ STEPWIDTH)
			canvas.create_line(x, y1, x + STEPWIDTH, y2, fill=colcol, width=widthi)


	def diff(self, point, gen):
		yIst = self.saturationValue(gen, point.x)
		return abs(point.y - yIst)

	## sum of all differences (kehrwert)
	def fitness(self, pointList, gen):
		diffS = 0
		for pt in pointList.getPointsArray():
			diffS = diffS + self.diff(pt, gen)
		diff = 1.0 / diffS
		return diff
