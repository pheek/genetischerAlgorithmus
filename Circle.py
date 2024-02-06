# (c) ph. freimann 2024
# Detect and draw a circel

import MainFrame
import Form
import math

X_MIN = 0
X_MAX = 2000
Y_MIN = 0
Y_MAX = 1200
R_MIN = 10
R_MAX = 500

class Circle:

##		https://stackoverflow.com/questions/17985216/simpler-way-to-draw-a-circle-with-tkinter
	def create_circle(x, y, r, canvas, colcol, widthi): #center coordinates, radius
		x0 = x - r
		y0 = y - r
		x1 = x + r
		y1 = y + r
		return canvas.create_oval(x0, y0, x1, y1, outline=colcol, width=widthi)

	def drawCircle(mainFrame, gen, colcol, widthi=1):
		x = Form.Form.stretch(gen.a, X_MIN, X_MAX)
		y = Form.Form.stretch(gen.b, Y_MIN, Y_MAX)
		r = Form.Form.stretch(gen.c, R_MIN, R_MAX)
		Circle.create_circle(x, y, r, mainFrame.canvas, colcol, widthi)

	def diff(point, gen):
		gx = Form.Form.stretch(gen.a, X_MIN, X_MAX)
		gy = Form.Form.stretch(gen.b, Y_MIN, Y_MAX)
		gr = Form.Form.stretch(gen.c, R_MIN, R_MAX)
		px = point.x
		py = point.y
		len = math.sqrt((px-gx)*(px-gx) + (py-gy)*(py-gy))
		return abs(len - gr)

	## sum of all differences (kehrwert)
	def fitness(pointList, gen):
		diffS = 0
		for pt in pointList.getPointsArray():
			diffS = diffS + Circle.diff(pt, gen)
		diff = 1.0 / diffS
		return diff
