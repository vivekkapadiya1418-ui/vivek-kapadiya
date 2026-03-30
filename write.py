"""#1. write()
f=open("one.txt","w")
f.write("hello students\n")
f.write("welcome to python file handling.\n")
f.write("learning is fun!\n")
f.close()"""

"""#2. 
f=open("one.txt","w")
f.write("new content only.\n")
f.close()"""

#3.writelines
f=("one.txt","a")
f=open("one.txt","w")
liens=[
 "python programing\n",
 "file handaling\n",
 "error handaling\n",
 "exception handaling\n"   
]
f.writelines(lines)
f.close()