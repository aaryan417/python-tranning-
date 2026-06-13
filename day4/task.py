a=["apple", "banana", "mango", 
 "orange", "grapes"]
for i in range(0,3):
    print(a[i])

a.remove("banana")
a.append("pineapple")  
print(a)  




stu=["Rahul", "Priya", "Rahul",
 "Rohan", "Priya", "Sneha"]
stu.remove("Priya")
stu.append("amit")
print(stu)






dist={
    "Rahul" :85,
    "Priya" :90,
    "Rohan" :65,
}

for name, marks in dist.items():
    if marks > 80:
        print(f"{name} pass  {marks}")
    else:
        print(f"{name} fail {marks}")    





student = ("Rahul", 20, "Pune", "Python")

name, age, city, course = student

print("Name  :", name)
print("Age   :", age)
print("City  :", city)
print("Course:", course)


