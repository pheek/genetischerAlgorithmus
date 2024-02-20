# (c) ph. freimann 2024
# Detect and draw an saturation function
#

## 2024-02 github.com/pheek


import MainFrame
import Shape as sh
import math

#FA_MIN =  0
FA_MAX = 1.2
XS_MIN = 0
XS_MAX = 2000
YS_MIN = 0
YS_MAX = 1200

STEPWIDTH = 7

class Parabel(sh.Shape):

	def __init__(self):
		super().__init__()

	def parabelValue(self, gen, x):
		FA = (gen.a - 0.5) * (gen.a - 0.5) * 2 * FA_MAX
		if gen.a < 0.5:
			FA = -FA
		XS = self.stretch(gen.b, XS_MIN, XS_MAX)
		YS = self.stretch(gen.c, YS_MIN, YS_MAX)
		return FA * (XS - x)*(XS-x) + YS

	def distance(self, xp, yp, a, b, c):
		zaehler = abs(yp-(a*xp*xp+b*yp+c))
		klammer = 2*a*xp + b
		nenner  = math.sqrt(1+klammer*klammer)
		return zaehler/nenner

	def abstandParabelPunkt(self, point, gen):
		xp = point.x
		yp = point.y
		a  = (gen.a - 0.5) * (gen.a - 0.5) * 2 * FA_MAX
		if gen.a < 0.5:
			a=-a
		xs = self.stretch(gen.b, XS_MIN, XS_MAX)
		ys = self.stretch(gen.c, YS_MIN, YS_MAX)
		b = 2 * xs * a
		c = a * xs*xs + ys
		abst = self.distance(xp,yp, a, b, c)
		print("Abst Parabel y=" , a , " x^2 , " , b , " x , " , c , " zu P(" ,xp , ", " , yp , ") ist gleich " , abst)
		return abst


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
#			diffS = diffS + self.diff(pt, gen)
		diff = 1.0 / diffS
		return diff
