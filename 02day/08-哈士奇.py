class Dog():
	def __init__(self,name):
		self.name = name

	def wark(self,call):
		print("狗%s"%call)
	def eat(self,food):
		print("吃%s"%food)


hashiqi = Dog("哈士奇")
print(hashiqi)
hashiqi.wark("汪汪叫")
hashiqi.eat("狗粮")


xiaotian = Dog("哮天犬")
print(xiaotian)
xiaotian.wark("狂叫")
xiaotian.eat("二氧化碳")
