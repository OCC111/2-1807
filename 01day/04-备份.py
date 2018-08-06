name = input("输入要备份的文件名称:")
f = open(name,"r")
content = f.read()


name1 = input("输入备份后的名字:")
f1 = open(name1,'w')
f1.write(content)

f.close()
f1.close()
