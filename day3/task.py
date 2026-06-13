f= open("test.txt" ,"w")
f.write("name  , rolll number , brach")
f.close()
print("file created")


f= open("test.txt" ,"a")
f.write("\n aaryan , 06 , cs")
f.close
print("file added")

with open("test.txt" , "w") as f
    f.write("\n rahul , 05, cs")
    f.write("\n rahul , 05, cs")
    f.write("\n rahul , 05, cs")
    
f = open("test.txt","r")
conter= f.read()
print(conter)
f.close()


student ={
    "name" :"aaryan ", "rollnuber": 6, "branch": "cs"

}

print (student)