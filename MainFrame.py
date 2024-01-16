#!/usr/bin/python3

import tkinter as tk
import Model
import Point

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
		self.setLabelText("saturation = " + str(self.model.getBestGen().getSaturation()))

	def paintAllPoints(self):
		for p in self.model.getPointList().getPointsArray():
			coord = p.x-3, p.y-3, p.x+3, p.y+3
			self.canvas.create_oval(coord, fill='yellow', width=1)

	def drawAllFunctions(self):
		self.canvas.delete("all")
		for g in self.model.getGeneArray():
			self.drawFunction(g, '#3f3')
		self.drawFunction(self.model.getBestGen(), '#0A6', 3)	

	def drawFunction(self, g, colcol, widthi=1):
		for x in range(FRAME_WIDTH):
			y1 = self.model.getPointList().f(g.a, g.b, g.c, x)
			y2 = self.model.getPointList().f(g.a, g.b, g.c, x+1)
			self.canvas.create_line(x, y1, x+1, y2, fill=colcol, width=widthi)

	def setLabelText(self, newText):
		self.label.config(text=newText)

	def __init__(self):
		self.model = Model.Model()

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
		self.setLabelText("saturaton =")

		root.mainloop()


## start MainFrame
if "__main__" == __name__:
	MainFrame()
