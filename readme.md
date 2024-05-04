Genetic Algorithm
=================
(genetischer Algorithmus)

![Screenshot](https://github.com/pheek/genetischerAlgorithmus/blob/main/Screenshot.png)


This algorithm tries to approximate some measured points with a saturation function.

... and also can detect circles...

![ScreenshotCircle](https://github.com/pheek/genetischerAlgorithmus/blob/main/ScreenshotCircle.png)

... and parabolas.

![ScreenshotParabola](![ScreenshotParabel](https://github.com/pheek/genetischerAlgorithmus/blob/main/ScreenshotParabel.png)



The algorithm uses the following concepts

Fitness
-------
The function having the least sum of differences to the given points has the best fitness (= 1/sum)

Crossover
---------
Two genes are "crossed-overed" having each gene of either the first parent, the second parent or the average of both.
Technically the *-operator (__mul__ in python) was overloaded for this. 

Mutate
------
Not every gen is mutated. Some are untouched, some are complete new and some are bionmial distributed around the old value. All values of all genes are allways between 0.0 and 1.0

New genes
---------
After each generation, there are some places left in the array, so they are fillde with complete new gens.

Classes:

* Point (.py)     : A (x|y)-coordinate pair
* Gen   (.py)     : A "gene" providing random-init, crossover and mutation
* PointList (.py) : Mostly an array of points, but also the fitness-function
* Model (.py)     : The genetic algorihtm
* MainFrame (.py) : A grapical UI

* Fitness (.py)   : calculate fitness of a ge

* Shape(.py)      : Helper Functions for all the following shapes
* Circle (.py)    : Detect circles and draw circles
* Saturation(.py) : Detect and draw saturation functions
* Parabel(.py)    : Detect parobolas




