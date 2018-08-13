class Dog():
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def wark(self):
		print("叫")

D = Dog("二哈",10)
D.wark()

print(D.name)
print(D.age)
