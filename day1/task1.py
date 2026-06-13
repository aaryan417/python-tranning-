class person:
    def walk(self):
        print("wallk with ")

    def talk(self):
        print("talk with")

class student(person):
    def studdy(self):
        print("person tect student")


    def attend(self):
        print("student sttend classs") 

s=student()
s.walk()
s.talk()
s.studdy()
s.attend()           
