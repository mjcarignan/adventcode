#20201212

import time

STARTTIME = time.time()

#read file, get in to useable format
file = open('20201212_data', 'r')
navigation = [direction.strip() for direction in file.readlines()]


class waypoint:
	
	__x_position = 0
	__y_position = 0



	def __init__(self,x,y):
		self.__x_position = x
		self.__y_position = y


	def move(self,direction,distance):
		if direction == 'N':
			self.__y_position = self.__y_position + distance
		if direction == 'E':
			self.__x_position = self.__x_position + distance
		if direction == 'S':
			self.__y_position = self.__y_position - distance
		if direction == 'W':
			self.__x_position = self.__x_position - distance
		if direction == 'F':
			if self.__cardinal_direction == 'N':
				self.__y_position = self.__y_position + distance
			if self.__cardinal_direction == 'E':
				self.__x_position = self.__x_position + distance
			if self.__cardinal_direction == 'S':
				self.__y_position = self.__y_position - distance
			if self.__cardinal_direction == 'W':
				self.__x_position = self.__x_position - distance	
		return

	def getXPostion(self):
		return self.__x_position

	def getYPostion(self):
		return self.__y_position

class boat:
	
	__x_position = 0
	__y_position = 0
	__heading = 0
	__cardinal_direction = 'N'
	__boat_waypoint = ''

	def setCardinaldirection(self):
		if self.__heading == 0: self.__cardinal_direction = 'N'
		if self.__heading == 90: self.__cardinal_direction = 'E'
		if self.__heading == 180: self.__cardinal_direction = 'S'
		if self.__heading == 270: self.__cardinal_direction = 'W'
		return

	def __init__(self,x,y,h,wx,wy):
		self.__x_position = x
		self.__y_position = y
		self.__heading = h
		self.setCardinaldirection()
		self.__boat_waypoint = waypoint(wx,wy)

	def move(self,direction,distance):
		if direction == 'N':
			self.__y_position = self.__y_position + distance
		if direction == 'E':
			self.__x_position = self.__x_position + distance
		if direction == 'S':
			self.__y_position = self.__y_position - distance
		if direction == 'W':
			self.__x_position = self.__x_position - distance
		if direction == 'F':
			if self.__cardinal_direction == 'N':
				self.__y_position = self.__y_position + distance
			if self.__cardinal_direction == 'E':
				self.__x_position = self.__x_position + distance
			if self.__cardinal_direction == 'S':
				self.__y_position = self.__y_position - distance
			if self.__cardinal_direction == 'W':
				self.__x_position = self.__x_position - distance	
		return

	def newHeading(self,direction,degrees):
		if direction == 'R':
			self.__heading = self.__heading + degrees
		
		if direction == 'L':
			self.__heading = self.__heading - degrees

		if self.__heading < 0:
			self.__heading = 360 + self.__heading

		if self.__heading > 360:
			self.__heading = self.__heading - 360

		if self.__heading == 360:
			self.__heading = 0

		self.setCardinaldirection()

	def getHeading(self):
		return self.__heading

	def getCHeading(self):
		return self.__cardinal_direction

	def getXPostion(self):
		return self.__x_position

	def getYPostion(self):
		return self.__y_position

	def getWaypoint(self):
		return self.__boat_waypoint

#Part 1
myBoat = boat(0,0,90,0,0)  #start facing east
#print(str(myBoat.getCHeading()) + str(myBoat.getHeading()))
#print(str(myBoat.getXPostion()) + ',' +  str(myBoat.getYPostion()) + "\n")

for instruction in navigation:
	if instruction[0] in list("NESWF"):
		myBoat.move(instruction[0],int(instruction[1:]))
	if instruction[0] in list("RL"):
		myBoat.newHeading(instruction[0],int(instruction[1:]))
	#print(str(myBoat.getCHeading()) + str(myBoat.getHeading()))
	#print(str(myBoat.getXPostion()) + ',' +  str(myBoat.getYPostion()))

print("Part 1: distance from origin: " + str(abs(myBoat.getXPostion()) + abs(myBoat.getYPostion())))
#print(str(myBoat.getCHeading()) + str(myBoat.getHeading()))
#print(str(myBoat.getXPostion()) + str(myBoat.getYPostion()))


