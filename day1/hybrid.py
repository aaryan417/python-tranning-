class dept:
    def click(self):
        print("clicking pic")



class student(dept):
    def study(self):
        print("studying")



class techer(student,):
    def teach(self):
        print ("teacing students")

s = techer()
s.study()
s.click()
s.teach()