import os.path 
#源文件地址
sourceFileAddress="文件地址"

if !os.path.isfile(sourceFileAddress) or os.path.splitext(sourceFileAddress)[1]!='.py':
	print('sorry,the file is not python file')
#目标文件地址
targetFileAddress="%s/target.py" %os.path.split(sourceFileAddress)[0]
fileIn=open(sourceFileAddress)
count=0 #用来记录需要多少tab符
for line in fileIn.readline():
	if line[0,3]='def'：
		count=count+1