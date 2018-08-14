class showError(Exception):
	def __init__(self,name):
		self.name = name

class Name():
	def myname(self):
		self.name = input("输入名字:")
		try:
			if self.name == "laowang":
				raise showError(self.name)
		except showError as ret:
			print("您输入的是:%s，不符合本程序要求!"%self.name)

s = showError(Exception)
N = Name()
N.myname()
