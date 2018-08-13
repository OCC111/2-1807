class Dog():
	def __init__(self,name):
		self.name = name
		self.__age = 0
	def setage(self):
		self.age = None

	def getage(self):
		return self.__age


D = Dog("二哈")
D.getage()

print(D.getage())

