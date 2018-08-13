class Dog(object):
	__instance = None #类属性
	def __new__(cls):
		if cls.__instance == None:
			cls.__instance = object.__new__(cls)
			return cls.__instance
		else:
			return cls.__instance

D = Dog()
D1 = Dog()
