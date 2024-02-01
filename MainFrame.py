#!/usr/bin/python3

##
# ph. freimann
# 2024-01-27 GUI
#

import tkinter as tk
import Model
import Point
import Fitness as fitnClass

FRAME_WIDTH =1600
FRAME_HEIGHT= 850

class MainFrame:

	def dotHitInCanvas(self, event):
		self.canvas.delete("all")
		p = Point.Point(event.x, event.y)
		self.model.appendPoint(p)
		self.paintAllPoints()

	def doButtonNextGenHit(self, event):
		self.model.nextGenerations()
		self.drawAllFunctions()
		self.paintAllPoints()
		actBestGen = self.model.getBestGen()
		pointListT = self.model.pointList
		fitnessValue = self.fitness.fitnessFunction(pointListT, actBestGen)
		self.setLabelText("fitness = " + str(fitnessValue))

	def paintAllPoints(self):
		for p in self.model.getPointList().getPointsArray():
			coord = p.x-3, p.y-3, p.x+3, p.y+3
			self.canvas.create_oval(coord, fill='yellow', width=1)

	def drawFunctionSaturation(self, g, colcol, widthi=1):
		for x in range(FRAME_WIDTH):
			y1 = self.fitness.saturationValue(g.a, g.b, g.c, x)
			y2 = self.fitness.saturationValue(g.a, g.b, g.c, x+1)
			self.canvas.create_line(x, y1, x+1, y2, fill=colcol, width=widthi)

	def drawFunctionCircle(self, g, colcol, widthi=1):
		## TODO: Draw Circle
		self.drawFunctionSaturation(g, colcol, widthi)


	def drawAllFunctions(self):
		self.canvas.delete("all")
		for g in self.model.getGeneArray():
			if g.type < 0.5:
				self.drawFunctionCircle(g, '#3f3')
			else:
				self.drawFunctionSaturation(g, '#3f3')
		if g.type < 0.5:
			self.drawFunctionCircle(self.model.getBestGen(), '#0A6', 3)
		else:
			self.drawFunctionSaturation(self.model.getBestGen(), '#0A6', 3)


	def setLabelText(self, newText):
		self.label.config(text=newText)

	def __init__(self):
		self.model = Model.Model()
		self.fitness = fitnClass.Fitness()

		root = tk.Tk()

		self.canvas = tk.Canvas(root, bg='#eeeeee', width=FRAME_WIDTH, height=FRAME_HEIGHT)
		self.canvas.pack()
		self.canvas.bind('<Button>', self.dotHitInCanvas)

		frame = tk.Frame(root)
		frame.pack()

		buttonStart = tk.Button(frame, text="Next")
		buttonStart.pack()
		buttonStart.bind('<Button>', self.doButtonNextGenHit)

		self.label = tk.Label(frame)
		self.label.pack()
		self.setLabelText("fitness =")

		root.mainloop()


## start MainFrame
if "__main__" == __name__:
	MainFrame()
