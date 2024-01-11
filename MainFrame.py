#!/usr/bin/python3

import tkinter as tk
import Model
import Point

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
		self.setLabelText("saturation = " + str(self.model.getBestGen().getSaturation()))

	def paintAllPoints(self):
		for p in self.model.getPointList().getPointsArray():
			coord = p.x-2, p.y-2, p.x+2, p.y+2
			self.canvas.create_oval(coord, fill='yellow')

	def drawAllFunctions(self):
		self.canvas.delete("all")
		for g in self.model.getGeneArray():
			self.drawFunction(g, '#ccc')
			self.drawFunction(self.model.getBestGen(), '#0A6', 3)	

	def drawFunction(self, g, colcol, widthi=1):
		for x in range(800):
			y1 = self.model.getPointList().f(g.a, g.b, g.c, x)
			y2 = self.model.getPointList().f(g.a, g.b, g.c, x+1)
			self.canvas.create_line(x, y1, x+1, y2, fill=colcol, width=widthi)

	def setLabelText(self, newText):
		self.label.config(text=newText)

	def __init__(self):
		self.model = Model.Model()

		root = tk.Tk()

		self.canvas = tk.Canvas(root, bg='#ccccff', )
		self.canvas.pack()
		self.canvas.bind('<Button>', self.dotHitInCanvas)

		frame = tk.Frame(root)
		frame.pack()

		buttonStart = tk.Button(frame, text="Next")
		buttonStart.pack()
		buttonStart.bind('<Button>', self.doButtonNextGenHit)

		self.label = tk.Label(frame)
		self.label.pack()
		self.setLabelText("saturaton =")

		root.mainloop()


## start MainFrame
MainFrame()
