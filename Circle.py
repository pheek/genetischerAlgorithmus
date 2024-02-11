# (c) ph. freimann 2024
# Detect and draw a circle

## 2024-02 github.com/pheek

import MainFrame
import Shape as sh
import math

# gen a:
X_MIN =    0
X_MAX = 2000

# gen b:
Y_MIN =    0
Y_MAX = 1200

# gen c: 
R_MIN =   8
R_MAX = 600

class Circle(sh.Shape):

	def __init__(self):
		super().__init__()

##		https://stackoverflow.com/questions/17985216/simpler-way-to-draw-a-circle-with-tkinter
	def paint_circle(self, x, y, r, canvas, colcol, widthi): #center coordinates, radius
		x0 = x - r
		y0 = y - r
		x1 = x + r
		y1 = y + r
		canvas.create_oval(x0, y0, x1, y1, outline=colcol, width=widthi)

	def draw(self, canvas, gen, colcol, widthi=1):
		r = self.stretch(gen.a, R_MIN, R_MAX)
		x = self.stretch(gen.b, X_MIN, X_MAX)
		y = self.stretch(gen.c, Y_MIN, Y_MAX)
		self.paint_circle(x, y, r, canvas, colcol, widthi)

  # difference to a single point
	def diff(self, point, gen):
		gr = self.stretch(gen.a, R_MIN, R_MAX)
		gx = self.stretch(gen.b, Y_MIN, X_MAX)
		gy = self.stretch(gen.c, X_MIN, Y_MAX)
		px = point.x
		py = point.y
		len = math.sqrt((px-gx)*(px-gx) + (py-gy)*(py-gy))
		return abs(len - gr)

	## sum of all differences (kehrwert)
	def fitness(self, pointList, gen):
		diffS = 0
		for pt in pointList.getPointsArray():
			diffS = diffS + self.diff(pt, gen)
		diff = 1.0 / diffS
		return diff
