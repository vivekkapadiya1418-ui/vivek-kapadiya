"""1.
src=open("one.txt","r")
data=src.read()
src.close()

dst=open("one.txt","w")
dst.write(data)
dst.close()
print("file copied successfully.")"""

#2.merge()
with open("one.txt","r") as f1,open("merge.txt","r") as f2,
open("one.txt")as f3:
    f3.write(f1.read())
    f3.write("\n")
    f3.write(f2.read())
    
print("file merge successfully") 
