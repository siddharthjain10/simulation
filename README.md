#**********************************************************************************#
This is simulation project for criminal intelligence and police search.
Map is a square grid with equal distances between the edges.
Criminal with 2 priorities: escaping the vicinity circle and escaping the city.
There are 4 police vehicles which can be generated randomly, which works on
probability model based on initial location of crime.
#**********************************************************************************#
Criminal Inteligence:
The map has been divided in 4 quadrants, and 4 corners are the exit points.
The criminal will try to exit from the nearest possible exit point.
When there is no police vehicle in vicinity circle of the criminal,
he will use the roulette wheel concept, since the distances are same. We can
inculcate the cost matrix for varying distances. When there is atleast one police
vehicle in vicinity circle he will try to escape from police using the cost matrix
on the map.
#**********************************************************************************#
Police Inteligence:
Assuming the initial location is known to the police the will create a probability 
model where the criminal might be. Police will try to reach the nearest location 
with highest probability. If the criminal comes in the vicinity circle of any 
vehicle the probability at that point becomes one, rest places zero, hence all 
the vehicles will try to reach this new point and further probability model will 
again start.
#**********************************************************************************#
