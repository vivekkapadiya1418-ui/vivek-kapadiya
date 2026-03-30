"""#1.read()
f=open("one.txt","r")
data=f.read()#read whole file
print("file content:",data)
f.close()"""

"""#2. readline()
f=open("one.txt","r")
line1=f.readline()
line2=f.readline()
line3=f.readline()
print("line 1:",line1)
print("line 2:",line2)
print("line 3:",line3)
f.close()"""

"""#3.readlines()
f=open("one.txt","r")
lines=f.readlines()
printf("list of lines:",liens)
print("numebr of lines: ",len(lines))
f.close()"""

"""#4.strip()
#reads specific line file
f=open("one.txt","r")
lines=f.readlines()
print(lines[1].strip())
f.close()"""

#5.char(10)
f=open("one.txt","r")
data=f.read(10) #first 10 characters
print("first part:",data)
f.close