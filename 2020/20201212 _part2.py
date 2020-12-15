#20201212_part2

import time

STARTTIME = time.time()

#read file, get in to useable format
file = open('20201212_data', 'r')
navigation = [direction.strip() for direction in file.readlines()]


class boat:
	
	__x_position = 0
	__y_position = 0
	__x_waypoint = 0
	__y_waypoint = 0

	def rotateWaypoint(self, direction, degrees):
		if direction+str(degrees) == "L90" or direction+str(degrees) == "R270":
			xtemp = self.__x_waypoint
			ytemp = self.__y_waypoint
			if self.__x_waypoint * self.__y_waypoint > 0: #means it is in either quad 1 or 3
				self.__x_waypoint = ytemp*-1
				self.__y_waypoint = xtemp
			elif self.__x_waypoint * self.__y_waypoint < 0: # means in quad 2 or 4
				self.__x_waypoint = ytemp
				self.__y_waypoint = xtemp*-1
			elif (self.__x_waypoint * self.__y_waypoint == 0 and self.__x_waypoint == 0): # means on y axis
				self.__x_waypoint = ytemp*-1
				self.__y_waypoint = xtemp
			elif (self.__x_waypoint * self.__y_waypoint == 0 and self.__y_waypoint == 0): # means on x axis
				self.__x_waypoint = ytemp
				self.__y_waypoint = xtemp
		
		if degrees == 180:
			self.__x_waypoint = self.__x_waypoint*-1
			self.__y_waypoint = self.__y_waypoint*-1
			
		if direction+str(degrees) == "R90" or direction+str(degrees) == "L270":
			xtemp = self.__x_waypoint
			ytemp = self.__y_waypoint
			if self.__x_waypoint * self.__y_waypoint > 0: #means it is in either quad 1 or 3
				self.__x_waypoint = ytemp
				self.__y_waypoint = xtemp*-1
			elif self.__x_waypoint * self.__y_waypoint < 0: # means in quad 2 or 4
				self.__x_waypoint = ytemp*-1
				self.__y_waypoint = xtemp
			elif (self.__x_waypoint * self.__y_waypoint == 0 and self.__x_waypoint == 0): # means on y axis
				self.__x_waypoint = ytemp
				self.__y_waypoint = xtemp
			elif (self.__x_waypoint * self.__y_waypoint == 0 and self.__y_waypoint == 0): # means on x axis
				self.__x_waypoint = ytemp
				self.__y_waypoint = xtemp
	


	def __init__(self,x,y,wx,wy):
		self.__x_position = x
		self.__y_position = y
		self.__x_waypoint = wx
		self.__y_waypoint = wy


	def moveWaypoint(self,direction,distance):
		if direction == 'N':
			self.__y_waypoint = self.__y_waypoint + distance
		if direction == 'E':
			self.__x_waypoint = self.__x_waypoint + distance
		if direction == 'S':
			self.__y_waypoint = self.__y_waypoint - distance
		if direction == 'W':
			self.__x_waypoint = self.__x_waypoint - distance

	def moveBoat(self,value):
		self.__x_position = self.__x_position + (self.__x_waypoint*value)
		self.__y_position = self.__y_position + (self.__y_waypoint*value)
		return

	def getXPostion(self):
		return self.__x_position

	def getYPostion(self):
		return self.__y_position

	def getWaypoint(self):
		return ("Waypoint: " + str(self.__x_waypoint) + ", " + str(self.__y_waypoint))


myBoat = boat(0,0,10,1)  #start facing east

for instruction in navigation:
	if instruction[0] in list("NESW"):
		myBoat.moveWaypoint(instruction[0],int(instruction[1:]))
	elif instruction[0] in list("RL"):
		myBoat.rotateWaypoint(instruction[0],int(instruction[1:]))
	elif instruction[0] in list("F"):
		myBoat.moveBoat(int(instruction[1:]))
	print(instruction)
	#print(str(myBoat.getCHeading()) + str(myBoat.getHeading()))
	#print(myBoat.getWaypoint())
	#print(str(myBoat.getXPostion()) + ', ' +  str(myBoat.getYPostion()))

#print("Part 1: distance from origin: " + str(abs(myBoat.getXPostion()) + abs(myBoat.getYPostion())))
#print(str(myBoat.getCHeading()) + str(myBoat.getHeading()))
print(abs(myBoat.getXPostion()) + abs(myBoat.getYPostion()))

