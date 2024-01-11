#!/usr/bin/python3

class Point:

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return "({0}, {1})".format(self.x, self.y)

## module Test ##
def moduleTest():
	## test Point
	p = Point(7, 9)
	print(p)

if "__main__" == __name__:
	moduleTest()
