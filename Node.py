#Node designed to be a block in my maze
class Node(object):
	#Thinking location will be an x and y coordinate
	def __init__ (self,x,y):
		self.location= [x,y]
		self.parent= None
		#don't know value yet but should initialize
		self.h=0
		self.f=0
		self.dis2Start= 0
		self.adjacent=0
	
	#Can make functionality within class
