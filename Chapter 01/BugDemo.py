class Bug(object):
	legs = 0
	distance = 0
	
	def __init__(self, name = "Bug", legs = 6):
		self.name = name
		self.legs = legs
		
	def Walk(self, distance = 1):
		self.distance += distance
	
	def GetDistance(self):
		return distance
		
	def SetDiatance(self, value):
		distance = value
		
	def ToString(self):
		return self.name + " has " + str(self.legs) + " legs " + "and taken " + str(self.distance) + " steps. "

# 1
ant = Bug()
for n in range(0, 5):
	ant.Walk()
print(ant.ToString())

# 2
beetle = Bug("beetle")
beetle.legs = 8
for n in range(0, 6):
	beetle.Walk()
print(beetle.ToString())

# 3
spider = Bug("Spider", 8)
for n in range(0, 6):
	spider.Walk(2)
print(spider.ToString())
