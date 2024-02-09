#!/usr/bin/python3

##
# ph. freimann
# 2024-01-27 GUI
#

import tkinter as tk
import Model
import Point
import Fitness as fitnClass
import Saturation
import Circle
import Parabel

class MainFrame:
	
	FRAME_WIDTH  = 1600
	FRAME_HEIGHT =  850
  
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

	## dont paint each single pixel
	STEPWIDTH = 12

	def drawFunctionSaturation(self, g, colcol, widthi=1):
		self.saturation.draw(MainFrame.FRAME_WIDTH, self.canvas, g, colcol, widthi)

	def drawFunctionParabel(self, g, colcol, widthi=1):
		self.parabel.draw(MainFrame.FRAME_WIDTH, self.canvas, g, colcol, widthi)

	def drawFunctionCircle(self, g, colcol, widthi=1):
		## TODO: Draw Circle
		self.circle.draw(self.canvas, g, colcol, widthi)
		##		self.drawFunctionSaturation(g, colcol, widthi)


	def drawAllFunctions(self):
		self.canvas.delete("all")
		for g in self.model.getGeneArray():
			if g.type < 0.33:
				self.drawFunctionCircle(g, '#aaf')
			elif g.type >= 0.33 and g.type < 0.67:
				self.drawFunctionSaturation(g, '#afa')
			else :
				self.drawFunctionParabel(g, '#ffa')
				
				
		if self.model.getBestGen().type < 0.33:
			self.drawFunctionCircle(self.model.getBestGen(), '#F55', 3)
			return
		if self.model.getBestGen().type >= 0.33 and self.model.getBestGen().type < 0.67:
			self.drawFunctionSaturation(self.model.getBestGen(), '#F55', 3)
			return
		self.drawFunctionParabel(self.model.getBestGen(), '#F55', 3)
		
	def setLabelText(self, newText):
		self.label.config(text=newText)

	def __init__(self):
		self.model = Model.Model()
		self.fitness = fitnClass.Fitness()

		root = tk.Tk()

		self.canvas = tk.Canvas(root, bg='#eeeeee', width=self.FRAME_WIDTH, height=self.FRAME_HEIGHT)
		self.canvas.pack()
		self.canvas.bind('<Button>', self.dotHitInCanvas)

		self.circle     = Circle    .Circle    ()
		self.saturation = Saturation.Saturation()
		self.parabel    = Parabel   .Parabel   ()
		
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
