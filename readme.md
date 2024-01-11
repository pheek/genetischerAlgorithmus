Genetic Algorithm
=================
(genetischer Algorithmus)

This algorithm tries to approximate some measured points with a saturation func
tion.

The algorithm uses the following concepts

Fitness
-------
The function having the least sum of differences to the given points has the best fitness (= 1/sum)

Crossover
---------
Two genes are "crossed-overed" having each gene of the first parent, the second parent or the average.

Mutate
------
A mutation is about 10% or less of the given value. The base of the exponential function must be between 0 and 1. Otherwise it is no saturation function. This is the only "mathematical" concept

New genes
---------
After each generation, there are some places left in the array, so they are fillde with complete new gens.

Classes:
Point (.py)     : A (x|y)-coordinate pair
Gen   (.py)     : A "gene" providing random-init, crossover and mutation
PointList (.py) : Mostly an array of points, but also the fitness-function
Model (.py)     : The genetic algorihtm
MainFrame (.py) : A grapical UI





