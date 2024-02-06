## Helper Function to
## transform a 'gen' to a min/max-Value

class Form:
	
	def stretch(v, min, max):
		a= max-min
		return a*v+min
