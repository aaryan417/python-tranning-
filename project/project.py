import openpyxl
import pandas as pd
import matplotlib.pyplot as plt
wb = openpyxl.Workbook()
ws =wb.active
ws.title="student"


ws.append(["name","math","science","english","computer"])
ws.append(["aaryan",24,57, 89,36,])
ws.append(["aaditya", 70,88,49,81])
ws.append(["rahul", 60,49,99,67])           
ws.append(["amit", 100,79,49,89]) 
ws.append(["ankit", 4,10,20,27]) 
ws.append(["puja", 99,100,100,100]) 
print(ws)
wb.save("students.xlsx")
wb.save("students.csv")
for row in ws.iter_rows(values_only=True):
    print(row)
df = pd.read_excel("students.xlsx")
print("data lodeed")
print(df)    
df["avrage"] =df [["math","science","english","computer"]].mean(axis=1)
print(df[["name", "avrage"]])
df["result"] = df ["avrage"].apply(lambda x:"pass" if x>=60 else "fails")
print(df[["name", "avrage", "result"]])
lowest =df .loc[df["avrage"].idxmin()]


plt.bar(df["name"], df["avrage"])

plt.title("Student Average Marks")
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.axhline(y=60, color ="red", linestyle ="--", label="pass")
plt.legend()

plt.show()

