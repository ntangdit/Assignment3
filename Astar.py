#Asignment 3 by Nikolai Tangdit
import Node
#start and end are coordinates. graph is the world in a 2d list
def Astar(start, end, graph):
	open= []
	open.append(start)
	closed = []
	while open not None:
		node = 