# (c) ph. freimann 2024
# Detect and draw an saturation function
#

import MainFrame
import Form
import math

A_MIN = 0.0000001
A_MAX = 0.9999999
B_MIN = -4000
B_MAX = 6000
C_MIN = 0
C_MAX = 1200

class Saturation:

#	@staticmethod
	def drawSaturation(mainFrame, gen, colcol, widthi=1):
		for step in range((int)((mainFrame.FRAME_WIDTH + mainFrame.STEPWIDTH-1)/mainFrame.STEPWIDTH)):
			x = (int)(step * mainFrame.STEPWIDTH)
			y1 = Saturation.saturationValue(gen, x)
			y2 = Saturation.saturationValue(gen, x+ mainFrame.STEPWIDTH)
			mainFrame.canvas.create_line(x, y1, x + mainFrame.STEPWIDTH, y2, fill=colcol, width=widthi)


	def saturationValue(gen, x):
		AA = Form.Form.stretch(gen.a, A_MIN, A_MAX)
		BB = Form.Form.stretch(gen.b, B_MIN, B_MAX)
		CC = Form.Form.stretch(gen.c, C_MIN, C_MAX)
		return CC + BB * math.exp(x * math.log(AA))

	def diff(point, gen):
		yIst = Saturation.saturationValue(gen, point.x)
		return abs(point.y - yIst)

	## sum of all differences (kehrwert)
	def fitness(pointList, gen):
		diffS = 0
		for pt in pointList.getPointsArray():
			diffS = diffS + Saturation.diff(pt, gen)
		diff = 1.0 / diffS
		return diff
