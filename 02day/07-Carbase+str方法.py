class Car():
	def __init__(self,color,num): #实例化方法 默认被调用
		self.color = color
		self.num = num

	def __str__(self):
		msg = "颜色:%s,型号:%s"%(self.color,self.num)
		return msg
		
	def Run(self):
		print("日行千里")

	def listen(self):
		print("听音乐")

	
benchi = Car("香槟金","BC G500") #创建一个对象或一个实例
benchi.Run()
benchi.listen()
print(benchi)




bmw = Car("绿色","BMW X5")
bmw.Run()
bmw.listen()
print(bmw)
		
