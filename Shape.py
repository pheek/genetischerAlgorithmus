#!/usr/bin/python3
#
## Helper Function to
## transform a 'gen' to a min/max-Value

class Shape(object):

	def __init__(self):
		pass
	
	def stretch(self, v, min, max):
		a = max - min
		return a*v+min


###########################################################
def testfunction():
	s = Shape()
	res = s.stretch(0.3, 5, 10)
	print("stretch 30% between 5 and 10 gives: ", res)
	
if "__main__" == __name__:
	testfunction()
