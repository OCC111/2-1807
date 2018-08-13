class Son():
	__instance = None
	flag = False
	def __init__(self,name):
		if Son.flag == False:
			self.name = name
		else:
			Son.flag = True
			
	def __new__(cls,*args,**kwargs):
		if cls.__instance == None:
			cls.__instance = super().__new__(cls)
			return cls.__instance
		else:
			return cls.__instance

D = Son("tom")
D1 = Son("jire")

print(D.name)
print(D1.name)
