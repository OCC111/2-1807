class Dog():
	def __init__(self,name):
		self.name = name

	def __str__(self):
		msg = "我是str方法"
		return msg

	def __del__(self):
		print("哈哈")

D = Dog("二哈")

D1 = D

del D

del D1
