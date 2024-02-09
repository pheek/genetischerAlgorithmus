# (c) ph. freimann 2024
# Detect and draw an saturation function
#

import MainFrame
import Shape as sh
import math

FA_MIN =  0.00001
FA_MAX =  500
XS_MIN = 0
XS_MAX = 2000
YS_MIN = 0
YS_MAX = 1200

STEPWIDTH = 7

class Parabel(sh.Shape):

	def __init__(self):
		super().__init__()

	def parabelValue(self, gen, x):
		FA = 1.0 / self.stretch(gen.a,      FA_MIN, FA_MAX)
		if(gen.a < 0.5):
			FA= -FA
#		print ("GEN: a = " , gen.a, ' --> a = ', FA)
		XS = self.stretch(gen.b, XS_MIN, XS_MAX)
		YS = self.stretch(gen.c, YS_MIN, YS_MAX)
		return FA * (XS - x)*(XS-x) + YS

#	@staticmethod
	def draw(self, fwidth, canvas, gen, colcol, widthi=1):
		y1 = self.parabelValue(gen, 0)
		for step in range((int)((fwidth + STEPWIDTH-1)/ STEPWIDTH)):
			x = (int)(step * STEPWIDTH)
			y2 = self.parabelValue(gen, x+ STEPWIDTH)
			canvas.create_line(x, y1, x + STEPWIDTH, y2, fill=colcol, width=widthi)
			y1 = y2

	def diff(self, point, gen):
		yIst = self.parabelValue(gen, point.x)
		return abs(point.y - yIst)

	## sum of all differences (kehrwert)
	def fitness(self, pointList, gen):
		diffS = 0
		for pt in pointList.getPointsArray():
			diffS = diffS + self.diff(pt, gen)
		diff = 1.0 / diffS
		return diff
