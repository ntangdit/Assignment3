import Node
#import Astar
#from sys import argv
#script =argv

print "Please choose which maze to travel World1.txt or World2.txt"
#filename = raw_input("> ")
filename= 'World1.txt'
txt= open(filename)
print txt.read()
#Now I have the map. I want to put it in a graph of nodes
with open(filename) as f:
	data= f.read().splitlines()
	
#print data[0].split()
for i in range(0,len(data)-1):
	data[i]=data[i].split(' ')
	print data[i]

for k in range(0, len(data)-1):
	for j in range(0, len(data[k]-1)):
		