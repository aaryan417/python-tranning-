class dept:
    def click(self):
        print("clicking pic")



class student:
    def study(self):
        print("studying")



class techer(dept ,student):
    def teach(self):
        print ("teacing students")

s = techer()
s.study()

s.click()
s.teach()